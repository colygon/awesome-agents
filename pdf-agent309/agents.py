"""
PDF Search Tool - CrewAI Agent Definitions

This module defines specialized agents for PDF search and RAG-enhanced
content extraction using CrewAI framework.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_pdf_analyzer_agent(llm=None):
    """
    Create a PDF Analyzer agent for PDF structure analysis.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured PDF Analyzer agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    return Agent(
        role="PDF Document Analyst",
        goal="Analyze PDF structure and formulate effective content extraction strategies",
        backstory="""You are an expert in PDF document formats, structures, and
        content extraction techniques. You have deep knowledge of PDF specifications,
        text extraction algorithms, metadata handling, and document parsing. You excel
        at understanding PDF structures including text layers, images, tables, and
        embedded content, enabling efficient RAG-based search.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_content_extractor_agent(llm=None):
    """
    Create a Content Extractor agent for RAG-based PDF search.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Content Extractor agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    return Agent(
        role="RAG PDF Search Specialist",
        goal="Extract and search PDF content using RAG capabilities for semantic retrieval",
        backstory="""You are a specialist in applying Retrieval Augmented Generation
        to PDF documents. You excel at extracting text from PDFs, creating semantic
        embeddings, and performing intelligent search across document contents. Your
        expertise includes handling various PDF formats, OCR for scanned documents,
        and ranking search results by relevance.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_insights_synthesizer_agent(llm=None):
    """
    Create an Insights Synthesizer agent for presenting PDF search results.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Insights Synthesizer agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.4)

    return Agent(
        role="Document Insights Synthesizer",
        goal="Synthesize PDF search results into clear, actionable insights",
        backstory="""You are a document analysis expert who excels at synthesizing
        information from PDF search results. You create comprehensive summaries,
        highlight key findings, and present extracted content in a user-friendly
        format. Your reports help users quickly understand document contents and
        locate relevant information efficiently.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
