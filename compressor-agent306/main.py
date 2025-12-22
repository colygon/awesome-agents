"""
Files Compressor Tool - Main Application

A CrewAI-powered application for intelligent file compression and archive management
with multiple specialized agents working collaboratively.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from agents import (
    create_compression_strategist_agent,
    create_archive_manager_agent,
    create_optimization_analyst_agent
)
from tasks import (
    create_strategy_task,
    create_execution_task,
    create_analysis_task
)


def initialize_crew():
    """
    Initialize the Files Compressor crew with all agents.

    Returns:
        tuple: (strategist_agent, manager_agent, analyst_agent)
    """
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY not found in environment variables. "
            "Please set it in your .env file."
        )

    llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    strategist_agent = create_compression_strategist_agent(llm)
    manager_agent = create_archive_manager_agent(llm)
    analyst_agent = create_optimization_analyst_agent(llm)

    return strategist_agent, manager_agent, analyst_agent


def run_compression_workflow(compression_request):
    """
    Run a complete file compression workflow.

    Args:
        compression_request: User's compression requirements

    Returns:
        str: Final analysis report
    """
    strategist, manager, analyst = initialize_crew()

    strategy_task = create_strategy_task(strategist, compression_request)
    execution_task = create_execution_task(manager, "Results from strategy")
    analysis_task = create_analysis_task(analyst, "Results from execution")

    execution_task.context = [strategy_task]
    analysis_task.context = [strategy_task, execution_task]

    crew = Crew(
        agents=[strategist, manager, analyst],
        tasks=[strategy_task, execution_task, analysis_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result


def main():
    """
    Main application entry point with interactive interface.
    """
    print("=" * 70)
    print("Files Compressor Tool - CrewAI Agent System")
    print("=" * 70)
    print()
    print("This system uses three specialized AI agents to help you:")
    print("  1. Compression Strategist - Analyzes and plans compression")
    print("  2. Archive Manager - Executes compression operations")
    print("  3. Optimization Analyst - Analyzes results and optimizations")
    print()
    print("=" * 70)
    print()

    print("Describe your file compression requirements:")
    print("(Example: 'Compress log files from /var/logs older than 30 days')")
    print()
    compression_request = input("Request: ").strip()

    if not compression_request:
        print("No request provided. Exiting.")
        return

    print()
    print("=" * 70)
    print("Processing your compression request with CrewAI agents...")
    print("=" * 70)
    print()

    try:
        result = run_compression_workflow(compression_request)

        print()
        print("=" * 70)
        print("FINAL COMPRESSION ANALYSIS REPORT")
        print("=" * 70)
        print()
        print(result)
        print()
        print("=" * 70)
        print("Analysis complete!")
        print("=" * 70)

    except Exception as e:
        print(f"\nError during compression workflow: {str(e)}")
        print("\nPlease check your configuration and try again.")


if __name__ == "__main__":
    main()
