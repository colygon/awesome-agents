#!/usr/bin/env python
"""
Vector Store Setup Script
Creates a FAISS vector store from a corpus of documents
"""

import argparse
import os
from pathlib import Path
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()


def setup_vector_store(corpus_dir: str, output_dir: str = "./vector_store"):
    """
    Create a vector store from documents in a directory

    Args:
        corpus_dir: Path to directory containing documents
        output_dir: Path to save the vector store

    Returns:
        Path to created vector store
    """

    print(f"\n{'='*80}")
    print("VECTOR STORE SETUP")
    print(f"{'='*80}\n")

    # Verify corpus directory exists
    if not os.path.exists(corpus_dir):
        raise ValueError(f"Corpus directory not found: {corpus_dir}")

    print(f"Corpus directory: {corpus_dir}")
    print(f"Output directory: {output_dir}\n")

    # Load PDF documents
    print("Loading PDF files...")
    pdf_loader = DirectoryLoader(
        corpus_dir,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
        use_multithreading=True
    )
    pdf_docs = pdf_loader.load()
    print(f"  Loaded {len(pdf_docs)} PDF documents")

    # Load text documents
    print("\nLoading text files...")
    txt_loader = DirectoryLoader(
        corpus_dir,
        glob="**/*.txt",
        loader_cls=TextLoader,
        show_progress=True,
        use_multithreading=True
    )
    txt_docs = txt_loader.load()
    print(f"  Loaded {len(txt_docs)} text documents")

    # Combine all documents
    all_docs = pdf_docs + txt_docs

    if not all_docs:
        raise ValueError(f"No PDF or TXT files found in {corpus_dir}")

    print(f"\nTotal documents loaded: {len(all_docs)}")

    # Split documents into chunks
    print("\nSplitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(all_docs)
    print(f"  Created {len(chunks)} chunks")

    # Create embeddings
    print("\nCreating embeddings (this may take a while)...")
    embeddings = OpenAIEmbeddings()

    # Create vector store
    print("Building FAISS vector store...")
    vector_store = FAISS.from_documents(chunks, embeddings)

    # Save vector store
    os.makedirs(output_dir, exist_ok=True)
    vector_store.save_local(output_dir)
    print(f"\n✓ Vector store saved to: {output_dir}")

    # Print summary
    print(f"\n{'='*80}")
    print("SETUP COMPLETE")
    print(f"{'='*80}")
    print(f"\nDocuments processed:")
    print(f"  - PDF files: {len(pdf_docs)}")
    print(f"  - Text files: {len(txt_docs)}")
    print(f"  - Total chunks: {len(chunks)}")
    print(f"\nVector store location: {output_dir}")
    print(f"\nYou can now run the RAG agent:")
    print(f"  export VECTOR_STORE_PATH={output_dir}")
    print(f"  python main.py")

    return output_dir


def main():
    """Main entry point"""

    parser = argparse.ArgumentParser(
        description="Create a vector store from a corpus of documents"
    )
    parser.add_argument(
        "--corpus-dir",
        required=True,
        help="Directory containing documents to index (PDF, TXT)"
    )
    parser.add_argument(
        "--output-dir",
        default="./vector_store",
        help="Directory to save the vector store (default: ./vector_store)"
    )

    args = parser.parse_args()

    try:
        # Check for OpenAI API key
        if not os.getenv("OPENAI_API_KEY"):
            print("\nError: OPENAI_API_KEY environment variable not set")
            print("Please set it in your .env file or environment:")
            print("  export OPENAI_API_KEY=sk-...")
            return 1

        # Create vector store
        setup_vector_store(args.corpus_dir, args.output_dir)
        return 0

    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
