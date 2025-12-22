"""
SingleStore Search Tool - Main Application

A CrewAI-powered application for querying and analyzing SingleStore databases
with multiple specialized agents working collaboratively.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from agents import (
    create_database_analyst_agent,
    create_data_interpreter_agent,
    create_results_synthesizer_agent
)
from tasks import (
    create_query_formulation_task,
    create_data_analysis_task,
    create_synthesis_task
)


def initialize_crew():
    """
    Initialize the SingleStore Search crew with all agents.

    Returns:
        tuple: (analyst_agent, interpreter_agent, synthesizer_agent)
    """
    # Load environment variables
    load_dotenv()

    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY not found in environment variables. "
            "Please set it in your .env file."
        )

    # Initialize LLM (can be customized)
    llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    # Create agents
    analyst_agent = create_database_analyst_agent(llm)
    interpreter_agent = create_data_interpreter_agent(llm)
    synthesizer_agent = create_results_synthesizer_agent(llm)

    return analyst_agent, interpreter_agent, synthesizer_agent


def run_singlestore_analysis(user_query):
    """
    Run a complete SingleStore database analysis workflow.

    Args:
        user_query: User's data request or question

    Returns:
        str: Final analysis report
    """
    # Initialize agents
    analyst, interpreter, synthesizer = initialize_crew()

    # Create tasks
    query_task = create_query_formulation_task(analyst, user_query)
    analysis_task = create_data_analysis_task(
        interpreter,
        "Results from query formulation"
    )
    synthesis_task = create_synthesis_task(
        synthesizer,
        "Results from data analysis"
    )

    # Set up task dependencies
    analysis_task.context = [query_task]
    synthesis_task.context = [query_task, analysis_task]

    # Create crew
    crew = Crew(
        agents=[analyst, interpreter, synthesizer],
        tasks=[query_task, analysis_task, synthesis_task],
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
    print("SingleStore Search Tool - CrewAI Agent System")
    print("=" * 70)
    print()
    print("This system uses three specialized AI agents to help you:")
    print("  1. Database Analyst - Formulates optimal SingleStore queries")
    print("  2. Data Interpreter - Analyzes and extracts insights")
    print("  3. Results Synthesizer - Creates comprehensive reports")
    print()
    print("=" * 70)
    print()

    # Get user query
    print("Enter your data query or question for SingleStore analysis:")
    print("(Example: 'Show me sales trends by region for the last quarter')")
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
        result = run_singlestore_analysis(user_query)

        print()
        print("=" * 70)
        print("FINAL REPORT")
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
