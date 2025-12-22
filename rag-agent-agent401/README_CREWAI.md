# RAG Agent - CrewAI Edition

## Migration from Google ADK to CrewAI

This application has been migrated from Google's Agent Development Kit (ADK) to CrewAI, replacing Google's Vertex AI RAG Engine with a FAISS-based vector store and OpenAI embeddings.

## Overview

The RAG (Retrieval-Augmented Generation) Agent answers questions about your document corpus using semantic search and LLM-based synthesis. It provides:

1. **Document Retrieval** - Semantic search across your knowledge base
2. **Answer Synthesis** - Combines information from multiple sources
3. **Citation Support** - Provides accurate citations for all answers

## Architecture

### ADK vs CrewAI Comparison

| Component | Google ADK (Original) | CrewAI (Migrated) |
|-----------|----------------------|-------------------|
| **Framework** | Google ADK | CrewAI |
| **LLM** | Gemini 2.0 Flash | OpenAI GPT-4o-mini |
| **Vector Store** | Vertex AI RAG Engine | FAISS (local) |
| **Embeddings** | Vertex AI | OpenAI Embeddings |
| **Document Loading** | Vertex AI Storage | LangChain loaders |
| **Deployment** | Vertex AI Agent Engine | Standalone Python |
| **Cost** | Per-query + storage | Per-API-call only |

### CrewAI Agents

The RAG agent can be run in two modes:

#### Simple Mode (Single Agent)
- **Document Retriever** - Handles entire workflow in one agent
- Determines if retrieval is needed
- Retrieves relevant documents
- Synthesizes answer with citations

#### Multi-Agent Mode (Three Agents)
1. **Query Analyzer Agent**
   - Classifies query intent (casual vs specific vs unclear)
   - Determines if retrieval is needed
   - Suggests clarifying questions if needed

2. **Document Retriever Agent**
   - Performs vector search
   - Filters by similarity threshold (>0.6)
   - Returns top-k documents (k=10)
   - Extracts relevant passages

3. **Answer Synthesizer Agent**
   - Combines information from multiple sources
   - Creates concise, factual answers
   - Formats proper citations
   - Admits when information is unavailable

### Custom Tools

1. **VectorSearchTool**
   - Performs semantic search using FAISS
   - Configurable top-k and similarity threshold
   - Returns documents with relevance scores
   - Includes source metadata

2. **DocumentRetrieverTool**
   - Higher-level retrieval interface
   - Uses LLM to extract relevant passages
   - Provides context and citations
   - Handles edge cases (no results, etc.)

3. **CorpusIndexerTool**
   - Indexes documents into vector store
   - Supports PDF and TXT files
   - Configurable chunk size and overlap
   - Creates FAISS index

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- Document corpus (PDF or TXT files)

### Installation

1. **Clone or download this directory**

```bash
cd rag-agent-agent401
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment**

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

5. **Create vector store from your documents**

```bash
# Place your documents in a directory, e.g., ./docs
python setup_vector_store.py --corpus-dir ./docs --output-dir ./vector_store
```

This will:
- Load all PDF and TXT files from `./docs`
- Split documents into chunks
- Create embeddings using OpenAI
- Build a FAISS vector store
- Save to `./vector_store`

## Usage

### Interactive Mode

```bash
python main.py
```

This starts an interactive chat session:

```
> What are the key business segments in Alphabet's 2024 10-K?

Running simple RAG workflow...
[Retrieval and synthesis...]

ANSWER
================================================================================

According to Alphabet's 2024 10-K report, the key business segments are:

1. Google Services - Including Google Search, YouTube, Google Maps, and Play Store
2. Google Cloud - Offering cloud computing, data analytics, and AI solutions
3. Other Bets - Including Waymo for autonomous driving technology

Citations:
1) goog-10-k-2024.pdf: Business Overview Section
```

### Command Line Query

```bash
# Simple mode (single agent)
python main.py "What is retrieval-augmented generation?"

# Multi-agent mode (three agents)
python main.py --multi "Explain vector search similarity metrics"
```

### Programmatic Usage

```python
from main import run_rag_agent

# Simple mode
result = run_rag_agent("What is RAG?", mode="simple")

# Multi-agent mode
result = run_rag_agent("Explain embeddings", mode="multi")

print(result)
```

## Key Migration Changes

### 1. RAG Backend

**Before (ADK):**
```python
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

ask_vertex_retrieval = VertexAiRagRetrieval(
    rag_resources=[
        rag.RagResource(rag_corpus=os.environ["RAG_CORPUS"])
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6
)
```

**After (CrewAI):**
```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vector_store = FAISS.load_local("./vector_store", embeddings)
retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 10, "score_threshold": 0.6}
)
```

### 2. Agent Architecture

**Before (ADK):**
```python
root_agent = Agent(
    model='gemini-2.0-flash-001',
    instruction=INSTRUCTIONS,
    tools=[ask_vertex_retrieval]
)
```

**After (CrewAI):**
```python
document_retriever = Agent(
    role="Documentation Retrieval Specialist",
    goal="Answer questions using retrieved documentation",
    backstory=BACKSTORY,
    tools=[DocumentRetrieverTool(), VectorSearchTool()]
)

crew = Crew(
    agents=[document_retriever],
    tasks=[retrieval_task],
    process=Process.sequential
)
```

### 3. Document Ingestion

**Before (ADK):**
- Upload PDFs to Google Cloud Storage
- Use Vertex AI RAG API to create corpus
- Automatic chunking and indexing
- Managed service (requires GCP setup)

**After (CrewAI):**
- Local document processing
- Manual chunking with LangChain
- Local FAISS vector store
- Full control over indexing

```bash
# Setup is now a simple script
python setup_vector_store.py --corpus-dir ./documents
```

## Features Preserved

All core functionality has been preserved:

- ✓ Semantic search with configurable similarity threshold
- ✓ Top-k retrieval (default k=10)
- ✓ Citation support with source attribution
- ✓ Casual conversation detection
- ✓ Clarifying questions when needed
- ✓ Clear indication when information unavailable
- ✓ Multi-document synthesis

## Benefits of CrewAI Migration

1. **No Cloud Dependency** - Fully local operation
2. **Cost Effective** - Only pay for OpenAI API calls, no managed service fees
3. **Data Privacy** - Documents stay on your machine
4. **Flexibility** - Easy to swap vector stores (Chroma, Pinecone, etc.)
5. **Transparency** - Full visibility into indexing and retrieval
6. **Portability** - Run anywhere Python runs
7. **Customization** - Complete control over chunking, embeddings, search

## Limitations and Notes

1. **Local Storage** - FAISS index stored locally (can be large for big corpora)
2. **No Managed Updates** - Must re-index when documents change
3. **RAM Usage** - Entire vector store loaded into memory
4. **Single User** - Not designed for concurrent multi-user access

## Customization

### Change Vector Store

Replace FAISS with Chroma, Pinecone, or Weaviate:

```python
# In tools.py, replace FAISS with Chroma
from langchain_community.vectorstores import Chroma

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)
```

### Change Embedding Model

```python
# In tools.py
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"  # Higher quality, higher cost
)
```

### Adjust Chunking Strategy

```python
# In setup_vector_store.py
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,      # Larger chunks
    chunk_overlap=300,    # More overlap
    separators=["\n\n", "\n", ". ", " "]
)
```

### Add Support for More File Types

```python
# In setup_vector_store.py
from langchain_community.document_loaders import (
    UnstructuredMarkdownLoader,
    UnstructuredHTMLLoader
)

# Add markdown support
md_loader = DirectoryLoader(
    corpus_dir,
    glob="**/*.md",
    loader_cls=UnstructuredMarkdownLoader
)
md_docs = md_loader.load()
```

### Integrate with Cloud Vector Stores

For production deployments:

```python
# Pinecone example
from langchain_pinecone import PineconeVectorStore
import pinecone

pinecone.init(api_key=os.getenv("PINECONE_API_KEY"))
vector_store = PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    index_name="my-rag-index"
)
```

## Troubleshooting

### "Vector store not found"

```bash
# Create the vector store first
python setup_vector_store.py --corpus-dir ./your-documents
```

### "OPENAI_API_KEY not found"

```bash
# Set in .env file
echo "OPENAI_API_KEY=sk-..." > .env
```

### "No relevant documents found"

- Check similarity threshold (default 0.6)
- Verify documents were indexed correctly
- Try broader search queries
- Check vector store path is correct

### Memory errors with large corpora

For very large document sets:

1. Use a cloud vector store (Pinecone, Weaviate)
2. Reduce chunk size
3. Index documents in batches
4. Use memory-mapped FAISS index

```python
# In tools.py, for large indices
import faiss
index = faiss.read_index("./vector_store/index.faiss", faiss.IO_FLAG_MMAP)
```

## Performance Optimization

### Indexing Speed

```bash
# Use parallel processing
python setup_vector_store.py --corpus-dir ./docs --workers 4
```

### Query Speed

```python
# Use HNSW index for faster search (in setup_vector_store.py)
vector_store = FAISS.from_documents(
    chunks,
    embeddings,
    index_type="hnsw"
)
```

### Reduce API Costs

```python
# Use smaller embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Use gpt-3.5-turbo instead of gpt-4
llm = ChatOpenAI(model="gpt-3.5-turbo")
```

## Advanced Features

### Hybrid Search

Combine vector search with keyword search:

```python
from langchain.retrievers import BM25Retriever, EnsembleRetriever

# BM25 for keyword matching
bm25_retriever = BM25Retriever.from_documents(chunks)

# Combine with vector search
ensemble_retriever = EnsembleRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    weights=[0.7, 0.3]
)
```

### Document Metadata Filtering

```python
# Add metadata during indexing
for doc in chunks:
    doc.metadata["department"] = "engineering"
    doc.metadata["date"] = "2024-01"

# Filter during retrieval
retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 10,
        "filter": {"department": "engineering"}
    }
)
```

### Multi-Query Retrieval

```python
# Generate multiple queries for better coverage
from langchain.retrievers.multi_query import MultiQueryRetriever

multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(),
    llm=ChatOpenAI()
)
```

## Future Enhancements

Potential improvements:

1. **Real-time Indexing** - Auto-index new documents
2. **Multi-lingual Support** - Embeddings for multiple languages
3. **Graph RAG** - Add knowledge graph for relationships
4. **Conversation Memory** - Track chat history for context
5. **Source Ranking** - ML-based re-ranking of results
6. **Batch Queries** - Process multiple questions efficiently

## License

This CrewAI migration is based on the original Google ADK sample, licensed under Apache 2.0.

## Acknowledgments

- Original ADK implementation: Google LLC
- CrewAI framework: CrewAI team
- FAISS: Facebook AI Research
- LangChain: LangChain team
- Migration: Claude Code

---

**Migration Date:** December 2025
**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
**FAISS Version:** 1.7.4+
