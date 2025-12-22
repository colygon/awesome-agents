"""
Snowflake Search Tool - CrewAI Task Definitions

This module defines tasks for the Snowflake data warehouse search and analysis workflow.
"""

from crewai import Task


def create_query_design_task(agent, user_query):
    """
    Create a task for designing Snowflake warehouse queries.

    Args:
        agent: Warehouse Analyst agent
        user_query: User's data request or question

    Returns:
        Task: Query design task
    """
    return Task(
        description=f"""Design an optimal Snowflake data warehouse query based on
        the following user request:

        User Query: {user_query}

        Consider Snowflake-specific features:
        - Virtual warehouse sizing and auto-suspend settings
        - Clustering keys for performance optimization
        - Time travel capabilities for historical analysis
        - Result caching strategies
        - Zero-copy cloning for data exploration

        Provide a comprehensive query plan including:
        1. SQL query optimized for Snowflake
        2. Virtual warehouse recommendations (size, auto-suspend)
        3. Clustering and partitioning strategies
        4. Expected query performance characteristics
        5. Time travel or cloning considerations if applicable""",
        expected_output="""A detailed Snowflake query plan with:
        - Optimized SQL query leveraging Snowflake features
        - Virtual warehouse configuration recommendations
        - Performance optimization strategies
        - Expected execution time and resource usage
        - Data freshness and time travel considerations""",
        agent=agent
    )


def create_analytics_task(agent, query_context):
    """
    Create a task for analyzing Snowflake query results.

    Args:
        agent: Analytics Specialist agent
        query_context: Context from the query design task

    Returns:
        Task: Analytics task
    """
    return Task(
        description=f"""Analyze the expected results from the Snowflake query plan:

        {query_context}

        Perform comprehensive analytics including:
        1. Key performance indicators (KPIs) identification
        2. Trend analysis and pattern recognition
        3. Anomaly detection and outlier identification
        4. Correlation analysis between variables
        5. Statistical significance of findings
        6. Historical comparison using Snowflake's time travel

        Leverage Snowflake's analytical capabilities:
        - Window functions for advanced analytics
        - JSON and semi-structured data analysis
        - Geospatial functions if applicable
        - Machine learning insights from Snowpark""",
        expected_output="""Comprehensive analytics report with:
        - Identified KPIs and metrics with context
        - Detected patterns, trends, and seasonality
        - Highlighted anomalies with potential explanations
        - Correlation insights and statistical analysis
        - Recommendations for deeper investigation
        - Snowflake-specific optimization opportunities""",
        agent=agent
    )


def create_communication_task(agent, analytics_context):
    """
    Create a task for communicating insights and recommendations.

    Args:
        agent: Insights Communicator agent
        analytics_context: Context from the analytics task

    Returns:
        Task: Communication task
    """
    return Task(
        description=f"""Create a comprehensive business intelligence report from
        the analytics findings:

        {analytics_context}

        Develop a complete stakeholder report including:
        1. Executive summary with key takeaways
        2. Detailed findings organized by business impact
        3. Visualization recommendations (charts, dashboards)
        4. Actionable recommendations with priorities
        5. Implementation roadmap for recommendations
        6. ROI analysis where applicable

        Tailor communication for:
        - Executive stakeholders (strategic insights)
        - Technical teams (implementation details)
        - Business users (operational guidance)

        Highlight Snowflake advantages utilized in the analysis.""",
        expected_output="""A polished business intelligence report with:
        - Executive summary (3-4 paragraphs)
        - Detailed findings section with business context
        - Visualization strategy and dashboard mockups
        - Prioritized actionable recommendations (5-7 items)
        - Implementation timeline and resource requirements
        - Expected business impact and ROI
        - Technical appendix with Snowflake-specific details""",
        agent=agent
    )
