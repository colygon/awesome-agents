"""
RAG Agent CrewAI Tasks
Defines the workflow for document retrieval and answer synthesis
"""

from crewai import Task
from agents import query_analyzer, document_retriever, answer_synthesizer


def create_tasks(user_query: str):
    """
    Create tasks for RAG workflow

    Args:
        user_query: User's question or query

    Returns:
        List of Task objects
    """

    # Task 1: Analyze query intent
    analyze_intent_task = Task(
        description=f"""Analyze the user's query to determine the appropriate response strategy.

        User Query: "{user_query}"

        Determine:
        1. Is this casual conversation or a specific question requiring knowledge retrieval?
        2. Is the query clear enough to answer, or does it need clarification?
        3. What type of information is the user seeking?

        Classification:
        - CASUAL: General chat, greetings, off-topic conversation
        - SPECIFIC: Clear question requiring corpus retrieval
        - CLARIFY: Ambiguous query needing more information

        Output your classification and reasoning.""",
        agent=query_analyzer,
        expected_output="""Classification (CASUAL/SPECIFIC/CLARIFY) with brief reasoning.
        If SPECIFIC, list key topics/entities to search for.
        If CLARIFY, suggest clarifying questions to ask."""
    )

    # Task 2: Retrieve relevant documents
    retrieve_docs_task = Task(
        description=f"""Retrieve relevant documents from the knowledge base to answer the query.

        User Query: "{user_query}"

        Steps:
        1. Use vector search to find top-k most similar documents (k=10)
        2. Filter results by similarity threshold (>0.6)
        3. Extract key passages relevant to the query
        4. Organize retrieved information by relevance
        5. Note source documents for citation

        Return:
        - Retrieved document chunks with metadata
        - Relevance scores
        - Source information (titles, sections, URLs)
        - Any gaps in available information""",
        agent=document_retriever,
        expected_output="""Retrieved document chunks with:
        - Content text
        - Source document title and section
        - Relevance score
        - URL if available
        List any information gaps found.""",
        context=[analyze_intent_task]
    )

    # Task 3: Synthesize answer with citations
    synthesize_answer_task = Task(
        description=f"""Synthesize the retrieved information into a clear answer with proper citations.

        User Query: "{user_query}"

        Requirements:
        1. Create a concise, factual answer based on retrieved documents
        2. Do not include information not found in retrieved chunks
        3. Add "Citations:" section at the end with numbered sources
        4. Format: "1) Document Title: Section Name"
        5. If multiple chunks from same document, cite only once
        6. If information is insufficient, state clearly

        Citation Format Example:
        [Your answer here]

        Citations:
        1) RAG Implementation Guide: Best Practices Section
        2) Vector Search Documentation: Similarity Metrics Chapter""",
        agent=answer_synthesizer,
        expected_output="""Complete answer with:
        - Main answer text (concise and factual)
        - Citations section with numbered references
        - Note if information is incomplete or unavailable""",
        context=[analyze_intent_task, retrieve_docs_task]
    )

    return [analyze_intent_task, retrieve_docs_task, synthesize_answer_task]


def create_simple_task(user_query: str):
    """
    Create a simplified single-agent task for direct RAG queries

    Args:
        user_query: User's question

    Returns:
        Single Task object
    """

    simple_rag_task = Task(
        description=f"""Answer the user's question using document retrieval.

        User Query: "{user_query}"

        Workflow:
        1. Determine if this is a casual conversation or specific question
        2. If specific question:
           - Retrieve relevant documents (top 10, similarity > 0.6)
           - Synthesize answer from retrieved content
           - Add citations at the end
        3. If casual conversation:
           - Respond appropriately without using retrieval
        4. If unclear:
           - Ask clarifying questions

        Citation Format:
        [Answer]

        Citations:
        1) Source 1
        2) Source 2

        Remember: Only provide information from the corpus. State clearly if
        information is not available.""",
        agent=document_retriever,
        expected_output="""Complete response including:
        - Answer to the query
        - Citations section (if retrieval was used)
        - Clarifying questions (if needed)
        - Clear statement if information unavailable"""
    )

    return [simple_rag_task]
