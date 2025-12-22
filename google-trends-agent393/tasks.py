"""
Google Trends Tasks - CrewAI Implementation
Defines the workflow tasks for trend analysis
"""

from crewai import Task
from agents import create_data_collector, create_trend_analyzer, create_report_writer


def create_data_collection_task(keywords: List[str], regions: List[str] = ["US"],
                                timeframe: str = "today 12-m", category: str = "all") -> Task:
    """
    Creates a task to collect trend data.

    Args:
        keywords: List of keywords to analyze
        regions: List of regions to collect data for
        timeframe: Time period for analysis
        category: Category filter

    Returns:
        Task for collecting trend data
    """
    data_collector = create_data_collector()

    return Task(
        description=f"""Collect comprehensive Google Trends data:

Keywords: {', '.join(keywords)}
Regions: {', '.join(regions)}
Timeframe: {timeframe}
Category: {category}

Your data collection should include:
1. Current trending topics in the specified category and regions
2. Historical interest over time for the specified keywords
3. Regional comparison data to identify geographic variations
4. Related queries (both rising and top) for each keyword
5. Category-specific trends if applicable
6. Calculate trend scores for each keyword

Ensure data completeness and quality. Collect enough data points for
meaningful analysis. Note any data gaps or limitations.""",
        agent=data_collector,
        expected_output="Complete dataset including trending topics, historical data, regional comparisons, related queries, and trend scores for all keywords and regions"
    )


def create_analysis_task(keywords: List[str], regions: List[str] = ["US"],
                        timeframe: str = "today 12-m") -> Task:
    """
    Creates a task to analyze trend patterns.

    Args:
        keywords: List of keywords being analyzed
        regions: List of regions in analysis
        timeframe: Time period analyzed

    Returns:
        Task for analyzing trend data
    """
    trend_analyzer = create_trend_analyzer()

    return Task(
        description=f"""Analyze the collected trend data to identify patterns and insights:

Keywords: {', '.join(keywords)}
Regions: {', '.join(regions)}
Timeframe: {timeframe}

Your analysis should include:
1. Identify the overall trend pattern for each keyword (growing, stable, declining)
2. Determine the strength and consistency of trends
3. Identify seasonal patterns or cyclical behavior
4. Compare performance across regions and identify top markets
5. Analyze related queries to understand search intent and opportunities
6. Identify emerging trends vs mature/declining topics
7. Calculate comprehensive trend scores
8. Generate actionable insights and recommendations

Focus on finding business-relevant patterns and opportunities.
Consider both short-term fluctuations and long-term trajectories.""",
        agent=trend_analyzer,
        expected_output="Comprehensive trend analysis with pattern identification, regional insights, opportunity assessment, and business recommendations",
        context=[create_data_collection_task(keywords, regions, timeframe)]
    )


def create_report_generation_task(keywords: List[str], report_type: str = "comprehensive") -> Task:
    """
    Creates a task to generate the final report.

    Args:
        keywords: List of keywords analyzed
        report_type: Type of report (executive, comprehensive, detailed)

    Returns:
        Task for generating the report
    """
    report_writer = create_report_writer()

    return Task(
        description=f"""Create a {report_type} trend analysis report:

Keywords Analyzed: {', '.join(keywords)}
Report Type: {report_type}

Your report should include:

1. Executive Summary
   - Key findings in 3-5 bullet points
   - Top opportunities identified
   - Critical recommendations

2. Trend Overview
   - Summary of each keyword's performance
   - Trend scores and grades
   - Overall market dynamics

3. Detailed Analysis
   - Historical trend patterns with visualizations
   - Regional performance comparison
   - Related search analysis
   - Seasonal patterns identified

4. Business Insights
   - Market opportunities
   - Competitive landscape implications
   - Risk factors to consider

5. Recommendations
   - Specific, actionable recommendations
   - Priority ranking
   - Expected outcomes

6. Visualizations
   - Trend line charts for each keyword
   - Regional heatmaps or comparison charts
   - Related query analysis

7. Data Export
   - Export complete report in JSON format
   - Include all supporting data

Write in a professional, clear style. Use visualizations effectively.
Make recommendations specific and actionable. Target the report for
business decision-makers.""",
        agent=report_writer,
        expected_output=f"Complete {report_type} trend analysis report with executive summary, detailed findings, visualizations, and actionable recommendations in both formatted text and JSON export",
        context=[
            create_data_collection_task(keywords),
            create_analysis_task(keywords)
        ]
    )


def create_trends_analysis_tasks(keywords: List[str], regions: List[str] = ["US"],
                                 timeframe: str = "today 12-m", category: str = "all",
                                 report_type: str = "comprehensive"):
    """
    Creates all tasks for the trends analysis workflow.

    Args:
        keywords: List of keywords to analyze
        regions: List of regions to analyze
        timeframe: Time period for analysis
        category: Category filter
        report_type: Type of report to generate

    Returns:
        List of tasks in execution order
    """
    from typing import List  # Import at function level to avoid circular import

    return [
        create_data_collection_task(keywords, regions, timeframe, category),
        create_analysis_task(keywords, regions, timeframe),
        create_report_generation_task(keywords, report_type)
    ]
