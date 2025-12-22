"""
Custom RAG Tools for Document Retrieval
Provides vector search and document retrieval capabilities
"""

from crewai_tools import BaseTool
from typing import Type, List, Dict
from pydantic import BaseModel, Field
import os
import numpy as np
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI


class VectorSearchInput(BaseModel):
    """Input schema for VectorSearchTool"""
    query: str = Field(..., description="Search query to find relevant documents")
    top_k: int = Field(default=10, description="Number of top results to return")
    similarity_threshold: float = Field(default=0.6, description="Minimum similarity score (0-1)")


class VectorSearchTool(BaseTool):
    name: str = "Vector Search Tool"
    description: str = """Performs semantic search across the document corpus using vector
    embeddings. Returns top-k most relevant document chunks with similarity scores."""
    args_schema: Type[BaseModel] = VectorSearchInput

    def _run(self, query: str, top_k: int = 10, similarity_threshold: float = 0.6) -> str:
        """
        Perform vector similarity search

        Args:
            query: Search query
            top_k: Number of results to return
            similarity_threshold: Minimum similarity score

        Returns:
            Retrieved documents with scores
        """
        try:
            # Check if vector store exists
            vector_store_path = os.getenv("VECTOR_STORE_PATH", "./vector_store")

            if not os.path.exists(vector_store_path):
                return f"""Vector store not found at {vector_store_path}.
Please run the setup script to create the vector store first:
python setup_vector_store.py --corpus-dir /path/to/documents"""

            # Load vector store
            embeddings = OpenAIEmbeddings()
            vector_store = FAISS.load_local(
                vector_store_path,
                embeddings,
                allow_dangerous_deserialization=True
            )

            # Perform similarity search with scores
            results = vector_store.similarity_search_with_score(query, k=top_k)

            # Filter by similarity threshold
            filtered_results = [
                (doc, score) for doc, score in results
                if (1 - score) >= similarity_threshold  # FAISS returns distance, convert to similarity
            ]

            if not filtered_results:
                return f"No documents found with similarity >= {similarity_threshold}"

            # Format results
            formatted = []
            for i, (doc, score) in enumerate(filtered_results, 1):
                similarity = 1 - score  # Convert distance to similarity
                source = doc.metadata.get("source", "Unknown")
                page = doc.metadata.get("page", "N/A")

                formatted.append(f"""Result {i} (Similarity: {similarity:.3f}):
Source: {source}
Page: {page}
Content: {doc.page_content[:500]}...
---""")

            return "\n".join(formatted)

        except Exception as e:
            return f"Error performing vector search: {str(e)}"


class DocumentRetrieverInput(BaseModel):
    """Input schema for DocumentRetrieverTool"""
    query: str = Field(..., description="Query to retrieve relevant documents for")


class DocumentRetrieverTool(BaseTool):
    name: str = "Document Retriever Tool"
    description: str = """Retrieves relevant documents from the knowledge base to answer
    user questions. Uses vector search with post-processing to find the most relevant
    information."""
    args_schema: Type[BaseModel] = DocumentRetrieverInput

    def _run(self, query: str) -> str:
        """
        Retrieve and rank documents for a query

        Args:
            query: User's question or query

        Returns:
            Retrieved and ranked documents
        """
        try:
            # Check if vector store exists
            vector_store_path = os.getenv("VECTOR_STORE_PATH", "./vector_store")

            if not os.path.exists(vector_store_path):
                return f"""Vector store not found. Please set up the knowledge base first.

To create a vector store:
1. Place your documents in a directory (PDF, TXT supported)
2. Run: python setup_vector_store.py --corpus-dir /path/to/documents

Or set VECTOR_STORE_PATH environment variable to existing vector store."""

            # Load vector store
            embeddings = OpenAIEmbeddings()
            vector_store = FAISS.load_local(
                vector_store_path,
                embeddings,
                allow_dangerous_deserialization=True
            )

            # Retrieve documents
            retriever = vector_store.as_retriever(
                search_type="similarity_score_threshold",
                search_kwargs={
                    "k": 10,
                    "score_threshold": 0.6
                }
            )

            docs = retriever.get_relevant_documents(query)

            if not docs:
                return "No relevant documents found in the knowledge base for this query."

            # Use LLM to extract relevant passages
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

            # Format documents for LLM
            docs_text = "\n\n".join([
                f"[Document {i+1}]\nSource: {doc.metadata.get('source', 'Unknown')}\nContent: {doc.page_content}"
                for i, doc in enumerate(docs[:5])  # Limit to top 5
            ])

            prompt = f"""Extract the most relevant information from these documents to answer the query.

Query: {query}

Documents:
{docs_text}

For each relevant passage:
1. Quote or summarize the key information
2. Note the source document
3. Explain its relevance to the query

If no documents contain relevant information, state that clearly."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error retrieving documents: {str(e)}"


class CorpusIndexerInput(BaseModel):
    """Input schema for CorpusIndexerTool"""
    corpus_dir: str = Field(..., description="Directory containing documents to index")


class CorpusIndexerTool(BaseTool):
    name: str = "Corpus Indexer Tool"
    description: str = """Indexes a directory of documents into a vector store for retrieval.
    Supports PDF and text files."""
    args_schema: Type[BaseModel] = CorpusIndexerInput

    def _run(self, corpus_dir: str) -> str:
        """
        Index documents from a directory

        Args:
            corpus_dir: Path to directory containing documents

        Returns:
            Status message
        """
        try:
            if not os.path.exists(corpus_dir):
                return f"Error: Directory not found: {corpus_dir}"

            # Load documents
            print(f"Loading documents from {corpus_dir}...")

            # Load PDFs
            pdf_loader = DirectoryLoader(
                corpus_dir,
                glob="**/*.pdf",
                loader_cls=PyPDFLoader,
                show_progress=True
            )
            pdf_docs = pdf_loader.load()

            # Load text files
            txt_loader = DirectoryLoader(
                corpus_dir,
                glob="**/*.txt",
                loader_cls=TextLoader,
                show_progress=True
            )
            txt_docs = txt_loader.load()

            all_docs = pdf_docs + txt_docs

            if not all_docs:
                return f"No PDF or TXT files found in {corpus_dir}"

            print(f"Loaded {len(all_docs)} documents")

            # Split documents
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_documents(all_docs)
            print(f"Split into {len(chunks)} chunks")

            # Create embeddings and vector store
            print("Creating embeddings...")
            embeddings = OpenAIEmbeddings()
            vector_store = FAISS.from_documents(chunks, embeddings)

            # Save vector store
            vector_store_path = os.getenv("VECTOR_STORE_PATH", "./vector_store")
            vector_store.save_local(vector_store_path)

            return f"""Successfully indexed {len(all_docs)} documents into {len(chunks)} chunks.
Vector store saved to: {vector_store_path}

Documents processed:
- PDF files: {len(pdf_docs)}
- Text files: {len(txt_docs)}
- Total chunks: {len(chunks)}

The vector store is ready for queries."""

        except Exception as e:
            return f"Error indexing corpus: {str(e)}"
