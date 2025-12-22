"""
PDF Search Tool - CrewAI Task Definitions

This module defines tasks for the PDF search and RAG workflow.
"""

from crewai import Task


def create_pdf_analysis_task(agent, search_query):
    """
    Create a task for analyzing PDF search requirements.

    Args:
        agent: PDF Analyzer agent
        search_query: User's search query for PDF content

    Returns:
        Task: PDF analysis task
    """
    return Task(
        description=f"""Analyze the PDF search requirements and formulate an
        effective content extraction and search strategy:

        Search Query: {search_query}

        Consider:
        1. PDF file identification and selection criteria
        2. Content extraction approach (text layers vs OCR)
        3. Metadata utilization (title, author, creation date)
        4. Chunking strategy for large documents
        5. RAG embedding parameters for semantic search
        6. Page-level vs document-level search

        Provide a comprehensive extraction plan including:
        - PDF selection and filtering criteria
        - Text extraction methodology
        - Chunking and embedding strategy
        - Search scope (full text, specific sections, metadata)
        - Expected processing complexity""",
        expected_output="""A detailed PDF search strategy with:
        - PDF file selection criteria
        - Content extraction approach (text layer, OCR, hybrid)
        - Chunking parameters (size, overlap)
        - RAG configuration (embedding model, similarity threshold)
        - Search methodology (semantic, keyword, hybrid)
        - Performance and accuracy estimates""",
        agent=agent
    )


def create_extraction_task(agent, analysis_context):
    """
    Create a task for extracting and searching PDF content.

    Args:
        agent: Content Extractor agent
        analysis_context: Context from the analysis task

    Returns:
        Task: Content extraction and search task
    """
    return Task(
        description=f"""Extract and search PDF content using RAG capabilities
        based on the analysis strategy:

        {analysis_context}

        Extraction and search operations:
        1. Load and parse PDF files
        2. Extract text content (with OCR if needed)
        3. Chunk content for optimal embedding
        4. Create semantic embeddings
        5. Perform vector similarity search
        6. Rank results by relevance
        7. Extract relevant passages with context

        For each match provide:
        - PDF file name and page number
        - Relevance score
        - Matched content excerpt
        - Surrounding context
        - Metadata (document info, section headers)

        Use RAG to:
        - Generate embeddings of PDF content chunks
        - Perform semantic similarity search
        - Retrieve contextually relevant passages
        - Rank by semantic relevance""",
        expected_output="""PDF search results including:
        - List of matching PDFs with file names
        - Page numbers for each match
        - Relevance scores (0-1)
        - Content excerpts with highlighting
        - Contextual snippets (before/after)
        - Document metadata (title, author, date)
        - Total matches count
        - Search performance metrics""",
        agent=agent
    )


def create_synthesis_task(agent, extraction_context):
    """
    Create a task for synthesizing PDF search insights.

    Args:
        agent: Insights Synthesizer agent
        extraction_context: Context from the extraction task

    Returns:
        Task: Insights synthesis task
    """
    return Task(
        description=f"""Synthesize PDF search results into a comprehensive report:

        {extraction_context}

        Synthesis activities:
        1. Organize results by relevance and document
        2. Create document summaries highlighting key findings
        3. Identify themes and patterns across results
        4. Extract key quotes and passages
        5. Generate cross-document insights
        6. Provide navigation guidance

        Create a report with:
        - Executive summary of findings
        - Top relevant documents with summaries
        - Key passages and quotes
        - Thematic analysis
        - Recommendations for further reading
        - Quick reference guide to results""",
        expected_output="""A comprehensive synthesis report with:
        - Executive summary (2-3 paragraphs)
        - Top 5 most relevant documents with summaries
        - Key findings and quotes (5-7 items)
        - Thematic analysis across documents
        - Cross-document insights
        - Recommended reading order
        - Quick reference index with page numbers""",
        agent=agent
    )
