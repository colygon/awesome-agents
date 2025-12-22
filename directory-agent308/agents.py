"""
Directory Search Tool - CrewAI Agent Definitions

This module defines specialized agents for directory search and RAG-enhanced
file system analysis using CrewAI framework.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_directory_analyzer_agent(llm=None):
    """
    Create a Directory Analyzer agent for file system exploration.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Directory Analyzer agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    return Agent(
        role="Directory Structure Analyst",
        goal="Analyze directory structures and formulate effective search strategies",
        backstory="""You are an expert in file systems, directory structures, and
        efficient search algorithms. You have deep knowledge of filesystem hierarchies,
        file organization patterns, and search optimization techniques. You excel at
        understanding how to navigate complex directory trees and locate specific files
        or content patterns efficiently using RAG-enhanced search capabilities.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_content_searcher_agent(llm=None):
    """
    Create a Content Searcher agent for RAG-based file content search.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Content Searcher agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    return Agent(
        role="RAG Content Search Specialist",
        goal="Search directory contents using RAG capabilities to find relevant information",
        backstory="""You are a specialist in Retrieval Augmented Generation (RAG)
        search techniques applied to file systems. You excel at semantic search across
        file contents, understanding context, and retrieving relevant information from
        large directory structures. Your expertise includes vector embeddings, similarity
        search, and intelligent content ranking.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_results_curator_agent(llm=None):
    """
    Create a Results Curator agent for organizing search findings.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Results Curator agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.4)

    return Agent(
        role="Search Results Curator",
        goal="Organize and present directory search results in a clear, actionable format",
        backstory="""You are an information architect specializing in organizing and
        presenting search results. You excel at categorizing files, ranking results by
        relevance, and creating clear hierarchical representations of directory contents.
        Your presentations help users quickly understand search results and take action.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
