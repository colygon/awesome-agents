#!/usr/bin/env python
"""
Academic Research Assistant - CrewAI Implementation
Comprehensive research support system
"""

import sys
from crewai import Crew, Process
from agents import (
    literature_searcher,
    paper_summarizer,
    citation_manager,
    literature_synthesizer,
    research_question_developer
)
from tasks import create_tasks


def run_research_assistant(research_topic: str, num_papers: int = 15):
    """
    Run the research assistant crew

    Args:
        research_topic: Research topic or question
        num_papers: Number of papers to find

    Returns:
        Comprehensive research package
    """

    print("\n" + "="*80)
    print("ACADEMIC RESEARCH ASSISTANT - CrewAI Edition")
    print("="*80)
    print(f"\nResearch Topic: {research_topic}")
    print(f"Target Papers: {num_papers}\n")

    # Create tasks
    tasks = create_tasks(research_topic, num_papers)

    # Create crew
    crew = Crew(
        agents=[
            literature_searcher,
            paper_summarizer,
            citation_manager,
            literature_synthesizer,
            research_question_developer
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute the research workflow
    print("\nStarting comprehensive research workflow...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("RESEARCH COMPLETE")
    print("="*80)
    print("\n" + str(result))

    return result


def main():
    """Main entry point for the application"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║      ACADEMIC RESEARCH ASSISTANT - CrewAI Edition             ║
    ║                                                               ║
    ║  Comprehensive research support for academic work            ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    print("Welcome! I will help you with your academic research.\n")
    print("I can help you:")
    print("  • Search for relevant academic literature")
    print("  • Summarize key papers")
    print("  • Generate proper citations")
    print("  • Create literature reviews")
    print("  • Develop research questions\n")

    # Get inputs
    research_topic = input("Enter your research topic or question: ").strip()
    if not research_topic:
        print("\nError: Research topic is required.")
        sys.exit(1)

    num_papers_input = input("Number of papers to find (default: 15): ").strip()
    num_papers = int(num_papers_input) if num_papers_input.isdigit() else 15

    # Run the research workflow
    try:
        result = run_research_assistant(research_topic, num_papers)
        print("\n✓ Research assistance complete!")
        print("\nYour research package is ready.")

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting.")
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ Error during research: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
