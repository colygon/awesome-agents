"""
SingleStore Search Tool - CrewAI Task Definitions

This module defines tasks for the SingleStore database search and analysis workflow.
"""

from crewai import Task


def create_query_formulation_task(agent, user_query):
    """
    Create a task for formulating SingleStore database queries.

    Args:
        agent: Database Analyst agent
        user_query: User's data request or question

    Returns:
        Task: Query formulation task
    """
    return Task(
        description=f"""Analyze the following user query and formulate an appropriate
        SingleStore SQL query to retrieve the requested information:

        User Query: {user_query}

        Consider:
        - SingleStore's distributed architecture and query optimization
        - Appropriate use of columnstore and rowstore tables
        - Indexing strategies for optimal performance
        - Any data filtering or aggregation requirements

        Provide a detailed SQL query plan including:
        1. The SQL query structure
        2. Expected table schemas involved
        3. Performance optimization considerations
        4. Expected result set characteristics""",
        expected_output="""A comprehensive query plan with:
        - Optimized SQL query for SingleStore
        - Explanation of query structure and optimization
        - Expected data schema and result format
        - Performance considerations and best practices""",
        agent=agent
    )


def create_data_analysis_task(agent, query_context):
    """
    Create a task for analyzing query results.

    Args:
        agent: Data Interpreter agent
        query_context: Context from the query formulation task

    Returns:
        Task: Data analysis task
    """
    return Task(
        description=f"""Based on the query plan from the Database Analyst:

        {query_context}

        Analyze the expected results and identify:
        1. Key metrics and KPIs that would be revealed
        2. Potential patterns or trends in the data
        3. Anomalies or outliers to watch for
        4. Relationships between different data points
        5. Business insights that could be derived

        Consider how the distributed nature of SingleStore affects data
        aggregation and provide insights on interpreting results from
        multiple partitions.""",
        expected_output="""A detailed analysis including:
        - Key metrics and their significance
        - Identified patterns and trends
        - Potential anomalies or areas of concern
        - Business insights and their implications
        - Recommendations for further investigation""",
        agent=agent
    )


def create_synthesis_task(agent, analysis_context):
    """
    Create a task for synthesizing results into actionable reports.

    Args:
        agent: Results Synthesizer agent
        analysis_context: Context from the data analysis task

    Returns:
        Task: Results synthesis task
    """
    return Task(
        description=f"""Create a comprehensive report based on the data analysis:

        {analysis_context}

        Synthesize the information into a clear, actionable report that includes:
        1. Executive summary of findings
        2. Detailed breakdown of key insights
        3. Visual representation recommendations (charts, graphs, dashboards)
        4. Actionable recommendations
        5. Next steps and follow-up queries

        Ensure the report is accessible to both technical and non-technical
        stakeholders, with clear explanations of SingleStore-specific
        considerations.""",
        expected_output="""A complete report with:
        - Executive summary (2-3 paragraphs)
        - Detailed findings section
        - Visualization recommendations
        - Actionable recommendations (3-5 items)
        - Suggested follow-up analyses
        - Technical appendix with SingleStore-specific notes""",
        agent=agent
    )
