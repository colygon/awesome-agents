"""
Deep Search ADK - CrewAI Multi-Agent Deep Research System
Main execution script for sequential deep search workflow

This script orchestrates three specialized agents:
1. Query Analyst (Query optimization and strategy)
2. Deep Researcher (Multi-source research)
3. Synthesis Specialist (Insight generation)

Usage:
    python main.py

    Or import and use programmatically:
    from main import run_deep_search
    result = run_deep_search("your research query")
"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import (
    create_query_analyst,
    create_deep_researcher,
    create_synthesis_specialist
)
from tasks import (
    create_query_analysis_task,
    create_deep_research_task,
    create_synthesis_task
)


def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()

    # Verify OpenAI API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your .env file or export it:")
        print("  export OPENAI_API_KEY='your-api-key-here'")
        sys.exit(1)


def get_sample_query():
    """
    Provides a sample research query for demonstration.

    Returns:
        str: Sample query
    """
    return """
    What are the latest developments in quantum computing, and how might they
    impact cybersecurity in the next 5-10 years? Include current state of technology,
    major players, potential threats to existing encryption methods, and emerging
    post-quantum cryptography solutions.
    """


def get_custom_query():
    """
    Prompts user for a custom research query.

    Returns:
        str: User-provided query
    """
    print("\n" + "="*80)
    print("Deep Search ADK - Multi-Agent Research System")
    print("="*80 + "\n")

    print("Enter your research query or question:")
    print("(Press Enter twice to finish)\n")

    query_lines = []
    while True:
        line = input()
        if line == '' and len(query_lines) > 0 and query_lines[-1] == '':
            break
        query_lines.append(line)

    query = '\n'.join(query_lines).strip()

    if not query:
        print("No query provided. Using sample query.")
        return get_sample_query()

    return query


def run_deep_search(query: str, verbose: bool = True):
    """
    Executes the multi-agent deep search workflow.

    Args:
        query: The research query or question
        verbose: Whether to print detailed progress

    Returns:
        dict: Results containing query analysis, research findings, and synthesis
    """
    if verbose:
        print("\n" + "="*80)
        print("Initializing Deep Search Multi-Agent System")
        print("="*80 + "\n")

    # Create agents
    if verbose:
        print("Creating specialized research agents...")

    query_analyst = create_query_analyst()
    deep_researcher = create_deep_researcher()
    synthesis_specialist = create_synthesis_specialist()

    if verbose:
        print("  ✓ Query Analyst")
        print("  ✓ Deep Researcher")
        print("  ✓ Synthesis Specialist\n")

    # Create tasks
    if verbose:
        print("Configuring deep search workflow...")

    analysis_task = create_query_analysis_task(query_analyst, query)
    research_task = create_deep_research_task(deep_researcher, analysis_task)
    synthesis_task = create_synthesis_task(synthesis_specialist, query, research_task)

    if verbose:
        print("  ✓ Query Analysis Task")
        print("  ✓ Deep Research Task")
        print("  ✓ Synthesis Task\n")

    # Create and execute crew
    if verbose:
        print("Assembling research crew with sequential workflow...")
        print("="*80 + "\n")

    crew = Crew(
        agents=[query_analyst, deep_researcher, synthesis_specialist],
        tasks=[analysis_task, research_task, synthesis_task],
        process=Process.sequential,
        verbose=True
    )

    if verbose:
        print("\nExecuting deep search workflow...")
        print("This may take several minutes depending on query complexity.\n")

    # Execute the crew
    start_time = datetime.now()
    result = crew.kickoff()
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    if verbose:
        print("\n" + "="*80)
        print(f"Deep Search Complete! (Duration: {duration:.2f} seconds)")
        print("="*80 + "\n")

    return {
        'result': result,
        'duration': duration,
        'timestamp': datetime.now().isoformat(),
        'query': query
    }


def save_results(result: dict, output_file: str = None):
    """
    Saves deep search results to a file.

    Args:
        result: Results dictionary from run_deep_search
        output_file: Optional custom output filename
    """
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"deep_search_report_{timestamp}.md"

    with open(output_file, 'w') as f:
        f.write("# Deep Search Research Report\n\n")
        f.write(f"**Query**: {result['query']}\n\n")
        f.write(f"**Generated**: {result['timestamp']}\n")
        f.write(f"**Duration**: {result['duration']:.2f} seconds\n\n")
        f.write("---\n\n")
        f.write(str(result['result']))

    print(f"\nResults saved to: {output_file}")


def main():
    """Main entry point for the CLI application."""
    # Load environment variables
    load_environment()

    # Choose between sample or custom query
    print("\n" + "="*80)
    print("Deep Search ADK - Multi-Agent Research System")
    print("="*80 + "\n")
    print("Options:")
    print("  1. Use sample query (quantum computing & cybersecurity)")
    print("  2. Provide custom research query")

    choice = input("\nSelect option (1-2): ").strip()

    if choice == '1':
        query = get_sample_query()
        print("\nUsing sample query: Quantum Computing Impact on Cybersecurity")
    else:
        query = get_custom_query()

    # Run deep search
    result = run_deep_search(query, verbose=True)

    # Display results
    print("\n" + "="*80)
    print("RESEARCH RESULTS")
    print("="*80 + "\n")
    print(result['result'])

    # Ask to save results
    save_choice = input("\n\nWould you like to save these results to a file? (y/n): ").strip().lower()
    if save_choice == 'y':
        custom_filename = input("Enter filename (press Enter for auto-generated): ").strip()
        save_results(result, custom_filename if custom_filename else None)

    print("\nThank you for using Deep Search ADK!")


if __name__ == "__main__":
    main()
