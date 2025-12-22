"""
SingleStore Search Tool - CrewAI Agent Definitions

This module defines specialized agents for querying and analyzing
SingleStore distributed SQL databases using CrewAI framework.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_database_analyst_agent(llm=None):
    """
    Create a Database Analyst agent specialized in SingleStore queries.

    This agent is responsible for understanding user queries and translating
    them into effective SingleStore database searches.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Database Analyst agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.1)

    return Agent(
        role="SingleStore Database Analyst",
        goal="Understand user data requirements and formulate effective SingleStore database queries",
        backstory="""You are an expert in SingleStore distributed SQL databases with deep
        knowledge of SQL query optimization, distributed database architectures, and
        real-time analytics. You excel at translating business questions into
        efficient database queries that leverage SingleStore's unique capabilities
        like columnstore indexes and distributed query processing.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_data_interpreter_agent(llm=None):
    """
    Create a Data Interpreter agent for analyzing query results.

    This agent processes the results from SingleStore queries and
    provides meaningful insights and interpretations.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Data Interpreter agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    return Agent(
        role="Data Insights Interpreter",
        goal="Analyze query results and extract meaningful insights and patterns",
        backstory="""You are a data analyst with extensive experience in interpreting
        database query results. You excel at identifying trends, anomalies, and
        actionable insights from structured data. Your strength lies in translating
        raw data into clear, business-relevant conclusions that drive decision-making.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_results_synthesizer_agent(llm=None):
    """
    Create a Results Synthesizer agent for presenting findings.

    This agent takes the data insights and creates comprehensive,
    user-friendly reports and visualizations.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Results Synthesizer agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.5)

    return Agent(
        role="Results Synthesizer",
        goal="Create comprehensive, actionable reports from data analysis",
        backstory="""You are a data storyteller who excels at communicating complex
        database insights to diverse audiences. You combine technical accuracy with
        clear communication, creating reports that are both detailed and accessible.
        Your visualizations and summaries help stakeholders make informed decisions
        based on SingleStore data.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
