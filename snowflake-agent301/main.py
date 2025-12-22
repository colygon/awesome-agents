"""
Snowflake Search Tool - Main Application

A CrewAI-powered application for querying and analyzing Snowflake data warehouse
with multiple specialized agents working collaboratively.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from agents import (
    create_warehouse_analyst_agent,
    create_analytics_specialist_agent,
    create_insights_communicator_agent
)
from tasks import (
    create_query_design_task,
    create_analytics_task,
    create_communication_task
)


def initialize_crew():
    """
    Initialize the Snowflake Search crew with all agents.

    Returns:
        tuple: (analyst_agent, specialist_agent, communicator_agent)
    """
    # Load environment variables
    load_dotenv()

    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY not found in environment variables. "
            "Please set it in your .env file."
        )

    # Initialize LLM
    llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    # Create agents
    analyst_agent = create_warehouse_analyst_agent(llm)
    specialist_agent = create_analytics_specialist_agent(llm)
    communicator_agent = create_insights_communicator_agent(llm)

    return analyst_agent, specialist_agent, communicator_agent


def run_snowflake_analysis(user_query):
    """
    Run a complete Snowflake data warehouse analysis workflow.

    Args:
        user_query: User's data request or question

    Returns:
        str: Final business intelligence report
    """
    # Initialize agents
    analyst, specialist, communicator = initialize_crew()

    # Create tasks
    query_task = create_query_design_task(analyst, user_query)
    analytics_task = create_analytics_task(
        specialist,
        "Results from query design"
    )
    communication_task = create_communication_task(
        communicator,
        "Results from analytics"
    )

    # Set up task dependencies
    analytics_task.context = [query_task]
    communication_task.context = [query_task, analytics_task]

    # Create crew
    crew = Crew(
        agents=[analyst, specialist, communicator],
        tasks=[query_task, analytics_task, communication_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()

    return result


def main():
    """
    Main application entry point with interactive interface.
    """
    print("=" * 70)
    print("Snowflake Search Tool - CrewAI Agent System")
    print("=" * 70)
    print()
    print("This system uses three specialized AI agents to help you:")
    print("  1. Warehouse Analyst - Designs optimal Snowflake queries")
    print("  2. Analytics Specialist - Extracts insights from data")
    print("  3. Insights Communicator - Creates business intelligence reports")
    print()
    print("=" * 70)
    print()

    # Get user query
    print("Enter your data query or question for Snowflake analysis:")
    print("(Example: 'Analyze customer retention trends over the past year')")
    print()
    user_query = input("Query: ").strip()

    if not user_query:
        print("No query provided. Exiting.")
        return

    print()
    print("=" * 70)
    print("Processing your query with CrewAI agents...")
    print("=" * 70)
    print()

    try:
        # Run the analysis
        result = run_snowflake_analysis(user_query)

        print()
        print("=" * 70)
        print("FINAL BUSINESS INTELLIGENCE REPORT")
        print("=" * 70)
        print()
        print(result)
        print()
        print("=" * 70)
        print("Analysis complete!")
        print("=" * 70)

    except Exception as e:
        print(f"\nError during analysis: {str(e)}")
        print("\nPlease check your configuration and try again.")


if __name__ == "__main__":
    main()
