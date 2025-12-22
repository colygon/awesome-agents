"""
Snowflake Search Tool - CrewAI Agent Definitions

This module defines specialized agents for querying and analyzing
Snowflake data warehouse using CrewAI framework.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_warehouse_analyst_agent(llm=None):
    """
    Create a Warehouse Analyst agent specialized in Snowflake queries.

    This agent is responsible for understanding user queries and translating
    them into effective Snowflake data warehouse searches.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Warehouse Analyst agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.1)

    return Agent(
        role="Snowflake Warehouse Analyst",
        goal="Transform user data requirements into optimized Snowflake queries",
        backstory="""You are an expert in Snowflake data warehousing with deep
        knowledge of SQL optimization, virtual warehouses, data clustering, and
        zero-copy cloning. You excel at leveraging Snowflake's unique features
        like time travel, automatic clustering, and multi-cluster warehouses to
        deliver high-performance analytics queries.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_analytics_specialist_agent(llm=None):
    """
    Create an Analytics Specialist agent for processing query results.

    This agent analyzes Snowflake query results to extract insights,
    patterns, and business intelligence.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Analytics Specialist agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    return Agent(
        role="Data Analytics Specialist",
        goal="Extract valuable insights and patterns from Snowflake data warehouse queries",
        backstory="""You are a data analytics expert specializing in cloud data
        warehouses. You have extensive experience analyzing large-scale datasets
        and identifying trends, anomalies, and opportunities. Your expertise in
        statistical analysis and business intelligence helps organizations make
        data-driven decisions based on Snowflake warehouse data.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_insights_communicator_agent(llm=None):
    """
    Create an Insights Communicator agent for presenting findings.

    This agent takes analytics insights and creates comprehensive,
    stakeholder-friendly reports and visualizations.

    Args:
        llm: Language model instance (optional, uses default if None)

    Returns:
        Agent: Configured Insights Communicator agent
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4", temperature=0.5)

    return Agent(
        role="Business Insights Communicator",
        goal="Transform data analytics into clear, actionable business intelligence reports",
        backstory="""You are a data storytelling expert who bridges the gap between
        technical analytics and business decision-making. You excel at creating
        compelling narratives from Snowflake data warehouse insights, designing
        effective visualizations, and delivering recommendations that drive action.
        Your reports are valued for their clarity and business impact.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
