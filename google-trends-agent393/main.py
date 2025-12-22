"""
Google Trends Agent - Main Entry Point
CrewAI implementation of Google ADK trends analysis agent
"""

import os
from typing import List
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_trends_agents
from tasks import create_trends_analysis_tasks

# Load environment variables
load_dotenv()


def run_trends_analysis(keywords: List[str],
                       regions: List[str] = ["US"],
                       timeframe: str = "today 12-m",
                       category: str = "all",
                       report_type: str = "comprehensive"):
    """
    Run the Google Trends analysis crew.

    Args:
        keywords: List of keywords to analyze
        regions: List of region codes (e.g., ["US", "GB", "JP"])
        timeframe: Time period (e.g., "today 12-m", "today 3-m")
        category: Category filter (e.g., "all", "business", "technology")
        report_type: Type of report (executive, comprehensive, detailed)

    Returns:
        Complete trend analysis report
    """

    # Create agents
    data_collector, trend_analyzer, report_writer = create_trends_agents()

    # Create tasks
    tasks = create_trends_analysis_tasks(
        keywords=keywords,
        regions=regions,
        timeframe=timeframe,
        category=category,
        report_type=report_type
    )

    # Create crew
    crew = Crew(
        agents=[data_collector, trend_analyzer, report_writer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute
    try:
        result = crew.kickoff()
        return result
    except Exception as e:
        return f"Error analyzing trends: {str(e)}"


def main():
    """
    Main function with example trend analysis.
    """
    print("=== Google Trends Analysis Agent ===\n")

    # Example analysis
    keywords = ["Artificial Intelligence", "Machine Learning", "ChatGPT"]
    regions = ["US", "GB", "JP"]
    timeframe = "today 12-m"

    print(f"Analyzing Keywords: {', '.join(keywords)}")
    print(f"Regions: {', '.join(regions)}")
    print(f"Timeframe: {timeframe}\n")
    print("Processing with Trends Analysis Crew...\n")

    result = run_trends_analysis(
        keywords=keywords,
        regions=regions,
        timeframe=timeframe,
        category="technology",
        report_type="comprehensive"
    )

    print("\n=== Trend Analysis Report ===")
    print(result)


if __name__ == "__main__":
    main()
