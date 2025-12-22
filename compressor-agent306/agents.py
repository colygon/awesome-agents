"""
Files Compressor Tool - CrewAI Agent Definitions

This module defines specialized agents for file compression and archive management
using CrewAI framework.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_compression_strategist_agent(llm=None):
    """
    Create a Compression Strategist agent for analyzing compression needs.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Compression Strategist agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    return Agent(
        role="Compression Strategy Expert",
        goal="Analyze file structures and determine optimal compression strategies",
        backstory="""You are an expert in file compression algorithms and archive
        formats with deep knowledge of ZIP, TAR, GZIP, BZIP2, and 7Z formats. You
        excel at analyzing file types, sizes, and structures to recommend the most
        efficient compression methods. Your expertise includes understanding trade-offs
        between compression ratio, speed, and compatibility.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_archive_manager_agent(llm=None):
    """
    Create an Archive Manager agent for compression operations.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Archive Manager agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.1)

    return Agent(
        role="Archive Management Specialist",
        goal="Execute file compression and manage archive creation efficiently",
        backstory="""You are a systems expert specializing in file archival and
        compression operations. You have extensive experience with various compression
        tools and libraries, managing large-scale file operations, and ensuring data
        integrity during compression. You understand filesystem operations, directory
        traversal, and optimal archive structuring.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_optimization_analyst_agent(llm=None):
    """
    Create an Optimization Analyst agent for post-compression analysis.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Optimization Analyst agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    return Agent(
        role="Compression Optimization Analyst",
        goal="Analyze compression results and provide optimization recommendations",
        backstory="""You are a data analyst specializing in compression efficiency
        and storage optimization. You excel at analyzing compression ratios, processing
        times, and space savings to provide actionable insights. Your expertise helps
        organizations optimize their archival strategies and storage costs.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
