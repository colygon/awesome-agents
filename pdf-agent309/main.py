"""
PDF Search Tool - Main Application

A CrewAI-powered application for intelligent PDF search with RAG capabilities
using multiple specialized agents working collaboratively.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from agents import (
    create_pdf_analyzer_agent,
    create_content_extractor_agent,
    create_insights_synthesizer_agent
)
from tasks import (
    create_pdf_analysis_task,
    create_extraction_task,
    create_synthesis_task
)


def initialize_crew():
    """
    Initialize the PDF Search crew with all agents.

    Returns:
        tuple: (analyzer_agent, extractor_agent, synthesizer_agent)
    """
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY not found in environment variables. "
            "Please set it in your .env file."
        )

    llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    analyzer_agent = create_pdf_analyzer_agent(llm)
    extractor_agent = create_content_extractor_agent(llm)
    synthesizer_agent = create_insights_synthesizer_agent(llm)

    return analyzer_agent, extractor_agent, synthesizer_agent


def run_pdf_search(search_query):
    """
    Run a complete PDF search workflow with RAG capabilities.

    Args:
        search_query: User's search query for PDF content

    Returns:
        str: Final synthesis report
    """
    analyzer, extractor, synthesizer = initialize_crew()

    analysis_task = create_pdf_analysis_task(analyzer, search_query)
    extraction_task = create_extraction_task(extractor, "Results from analysis")
    synthesis_task = create_synthesis_task(synthesizer, "Results from extraction")

    extraction_task.context = [analysis_task]
    synthesis_task.context = [analysis_task, extraction_task]

    crew = Crew(
        agents=[analyzer, extractor, synthesizer],
        tasks=[analysis_task, extraction_task, synthesis_task],
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
    print("PDF Search Tool - CrewAI Agent System with RAG")
    print("=" * 70)
    print()
    print("This system uses three specialized AI agents to help you:")
    print("  1. PDF Analyzer - Plans PDF extraction and search strategy")
    print("  2. RAG Content Extractor - Performs semantic PDF search")
    print("  3. Insights Synthesizer - Creates comprehensive reports")
    print()
    print("=" * 70)
    print()

    print("Enter your PDF search query:")
    print("(Example: 'Find information about machine learning algorithms')")
    print()
    search_query = input("Query: ").strip()

    if not search_query:
        print("No query provided. Exiting.")
        return

    print()
    print("=" * 70)
    print("Processing your PDF search with CrewAI agents and RAG...")
    print("=" * 70)
    print()

    try:
        result = run_pdf_search(search_query)

        print()
        print("=" * 70)
        print("PDF SEARCH SYNTHESIS REPORT")
        print("=" * 70)
        print()
        print(result)
        print()
        print("=" * 70)
        print("Search complete!")
        print("=" * 70)

    except Exception as e:
        print(f"\nError during PDF search: {str(e)}")
        print("\nPlease check your configuration and try again.")


if __name__ == "__main__":
    main()
