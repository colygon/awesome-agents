"""
Google Trends Agents - CrewAI Implementation
Migrated from Google ADK to multi-agent workflow
"""

from crewai import Agent
from tools import (
    fetch_trending_topics,
    get_interest_over_time,
    compare_regional_interest,
    get_related_queries,
    get_category_trends,
    analyze_trend_pattern,
    generate_trend_insights,
    calculate_trend_score,
    create_trend_visualization,
    export_trend_report
)


def create_data_collector() -> Agent:
    """
    Creates the Data Collector agent.
    Gathers trend data from multiple sources.
    """
    return Agent(
        role="Trends Data Specialist",
        goal="Collect comprehensive Google Trends data including current trends, historical patterns, and regional variations",
        backstory="""You are an expert data collection specialist focused on market intelligence
        and trend analysis. You have deep experience with Google Trends API and understand how to
        gather high-quality, relevant trend data. You know which metrics matter for different types
        of analysis and can efficiently collect data across multiple regions and time periods. You're
        meticulous about data quality and always verify the completeness of your datasets.""",
        verbose=True,
        allow_delegation=False,
        tools=[
            fetch_trending_topics,
            get_interest_over_time,
            compare_regional_interest,
            get_related_queries,
            get_category_trends,
            calculate_trend_score
        ]
    )


def create_trend_analyzer() -> Agent:
    """
    Creates the Trend Analyzer agent.
    Analyzes patterns and generates insights from trend data.
    """
    return Agent(
        role="Market Intelligence Analyst",
        goal="Analyze trend patterns, identify emerging opportunities, and extract actionable business insights",
        backstory="""You are a seasoned market analyst with expertise in trend forecasting and
        pattern recognition. You excel at identifying emerging trends before they become mainstream,
        understanding seasonal patterns, and comparing regional variations. You have a strong
        background in statistical analysis and can separate signal from noise in trend data. Your
        analyses have helped businesses make strategic decisions about product launches, marketing
        campaigns, and market expansion. You think critically about data and always consider
        multiple factors before drawing conclusions.""",
        verbose=True,
        allow_delegation=False,
        tools=[
            analyze_trend_pattern,
            generate_trend_insights,
            calculate_trend_score,
            compare_regional_interest
        ]
    )


def create_report_writer() -> Agent:
    """
    Creates the Report Writer agent.
    Synthesizes findings into comprehensive reports.
    """
    return Agent(
        role="Business Intelligence Reporter",
        goal="Create clear, actionable reports that communicate trend insights to stakeholders and decision-makers",
        backstory="""You are an experienced business intelligence reporter who specializes in
        translating complex data analysis into clear, actionable insights. You have a talent for
        identifying the most important findings and presenting them in a way that drives decision-making.
        Your reports are known for their clarity, visual appeal, and practical recommendations. You
        understand different audience needs - from executives wanting high-level summaries to analysts
        needing detailed data. You always include visualizations, key metrics, and specific
        recommendations. You write in a professional but accessible style that makes trend data
        understandable and compelling.""",
        verbose=True,
        allow_delegation=False,
        tools=[
            generate_trend_insights,
            create_trend_visualization,
            export_trend_report
        ]
    )


def create_trends_agents():
    """
    Creates and returns all Google Trends analysis agents.

    Returns:
        Tuple of (data_collector, trend_analyzer, report_writer)
    """
    return (
        create_data_collector(),
        create_trend_analyzer(),
        create_report_writer()
    )
