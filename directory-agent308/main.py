"""
Directory Search Tool - Main Application

A CrewAI-powered application for intelligent directory search with RAG capabilities
using multiple specialized agents working collaboratively.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from agents import (
    create_directory_analyzer_agent,
    create_content_searcher_agent,
    create_results_curator_agent
)
from tasks import (
    create_analysis_task,
    create_search_task,
    create_curation_task
)


def initialize_crew():
    """
    Initialize the Directory Search crew with all agents.

    Returns:
        tuple: (analyzer_agent, searcher_agent, curator_agent)
    """
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY not found in environment variables. "
            "Please set it in your .env file."
        )

    llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    analyzer_agent = create_directory_analyzer_agent(llm)
    searcher_agent = create_content_searcher_agent(llm)
    curator_agent = create_results_curator_agent(llm)

    return analyzer_agent, searcher_agent, curator_agent


def run_directory_search(search_query):
    """
    Run a complete directory search workflow with RAG capabilities.

    Args:
        search_query: User's search query

    Returns:
        str: Final curated search results
    """
    analyzer, searcher, curator = initialize_crew()

    analysis_task = create_analysis_task(analyzer, search_query)
    search_task = create_search_task(searcher, "Results from analysis")
    curation_task = create_curation_task(curator, "Results from search")

    search_task.context = [analysis_task]
    curation_task.context = [analysis_task, search_task]

    crew = Crew(
        agents=[analyzer, searcher, curator],
        tasks=[analysis_task, search_task, curation_task],
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
    print("Directory Search Tool - CrewAI Agent System with RAG")
    print("=" * 70)
    print()
    print("This system uses three specialized AI agents to help you:")
    print("  1. Directory Analyzer - Plans search strategy")
    print("  2. RAG Content Searcher - Performs semantic search")
    print("  3. Results Curator - Organizes and presents findings")
    print()
    print("=" * 70)
    print()

    print("Enter your directory search query:")
    print("(Example: 'Find Python files related to authentication')")
    print()
    search_query = input("Query: ").strip()

    if not search_query:
        print("No query provided. Exiting.")
        return

    print()
    print("=" * 70)
    print("Processing your search with CrewAI agents and RAG...")
    print("=" * 70)
    print()

    try:
        result = run_directory_search(search_query)

        print()
        print("=" * 70)
        print("CURATED SEARCH RESULTS")
        print("=" * 70)
        print()
        print(result)
        print()
        print("=" * 70)
        print("Search complete!")
        print("=" * 70)

    except Exception as e:
        print(f"\nError during directory search: {str(e)}")
        print("\nPlease check your configuration and try again.")


if __name__ == "__main__":
    main()
