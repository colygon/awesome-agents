"""
Directory Search Tool - CrewAI Task Definitions

This module defines tasks for the directory search and RAG workflow.
"""

from crewai import Task


def create_analysis_task(agent, search_query):
    """
    Create a task for analyzing directory search requirements.

    Args:
        agent: Directory Analyzer agent
        search_query: User's search query

    Returns:
        Task: Directory analysis task
    """
    return Task(
        description=f"""Analyze the directory search requirements and formulate
        an effective search strategy:

        Search Query: {search_query}

        Consider:
        1. Search scope (file names, content, metadata)
        2. Directory traversal strategy (depth, breadth, selective)
        3. File type filtering and inclusion patterns
        4. Content analysis requirements
        5. RAG search parameters for semantic matching
        6. Performance optimization strategies

        Provide a comprehensive search plan including:
        - Directory traversal approach
        - File filtering criteria
        - Content search methodology
        - RAG embedding and similarity parameters
        - Expected search complexity and time""",
        expected_output="""A detailed search strategy with:
        - Directory traversal plan
        - File filtering rules (extensions, patterns, size)
        - Content search approach (keyword, semantic, hybrid)
        - RAG configuration (embedding model, chunk size, similarity threshold)
        - Performance estimates
        - Search scope boundaries""",
        agent=agent
    )


def create_search_task(agent, analysis_context):
    """
    Create a task for executing RAG-based directory search.

    Args:
        agent: Content Searcher agent
        analysis_context: Context from the analysis task

    Returns:
        Task: Search execution task
    """
    return Task(
        description=f"""Execute the directory search using RAG capabilities based
        on the search strategy:

        {analysis_context}

        Search operations:
        1. Traverse directory structure according to strategy
        2. Apply file filtering criteria
        3. Extract and embed file contents
        4. Perform semantic similarity search
        5. Rank results by relevance
        6. Extract relevant content snippets

        For each match:
        - File path and metadata
        - Relevance score
        - Content excerpts showing matches
        - Contextual information

        Use RAG to:
        - Create semantic embeddings of file contents
        - Perform vector similarity search
        - Retrieve contextually relevant files
        - Rank by semantic relevance""",
        expected_output="""Search results including:
        - List of matching files with full paths
        - Relevance scores (0-1) for each result
        - Content excerpts highlighting matches
        - File metadata (size, type, modified date)
        - Total results count
        - Search performance metrics
        - Semantic similarity explanations""",
        agent=agent
    )


def create_curation_task(agent, search_context):
    """
    Create a task for curating and presenting search results.

    Args:
        agent: Results Curator agent
        search_context: Context from the search task

    Returns:
        Task: Results curation task
    """
    return Task(
        description=f"""Organize and present the directory search results:

        {search_context}

        Curation activities:
        1. Categorize results by file type, location, or topic
        2. Rank results by relevance and usefulness
        3. Create hierarchical organization of findings
        4. Generate summary statistics
        5. Provide actionable recommendations
        6. Identify patterns in results

        Create a comprehensive report with:
        - Executive summary of findings
        - Categorized results with navigation
        - Key insights and patterns
        - Recommendations for further exploration
        - Directory organization suggestions""",
        expected_output="""A curated search report with:
        - Executive summary (2-3 paragraphs)
        - Results organized by category/relevance
        - Top 10 most relevant files with details
        - Summary statistics (total files, categories, sizes)
        - Identified patterns and insights
        - Actionable recommendations (3-5 items)
        - Suggested follow-up searches or actions""",
        agent=agent
    )
