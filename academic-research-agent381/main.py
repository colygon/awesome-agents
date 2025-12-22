#!/usr/bin/env python
"""
Academic Research CrewAI Main Application
Migrated from Google ADK to CrewAI
"""

import sys
from crewai import Crew, Process
from agents import document_analyzer, citation_researcher, future_research_synthesizer
from tasks import create_tasks


def run_academic_research(seminal_paper_path: str):
    """
    Run the academic research crew to analyze a seminal paper and propose future research

    Args:
        seminal_paper_path: Path to the seminal paper PDF file

    Returns:
        Research findings and future directions
    """

    print("\n" + "="*80)
    print("ACADEMIC RESEARCH ASSISTANT - CrewAI Edition")
    print("="*80)
    print(f"\nAnalyzing seminal paper: {seminal_paper_path}\n")

    # Create tasks
    tasks = create_tasks(seminal_paper_path)

    # Create crew
    crew = Crew(
        agents=[document_analyzer, citation_researcher, future_research_synthesizer],
        tasks=tasks,
        process=Process.sequential,  # Sequential process for ordered execution
        verbose=True
    )

    # Execute the research workflow
    print("\nStarting academic research workflow...\n")
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
    ║         ACADEMIC RESEARCH ASSISTANT - CrewAI Edition          ║
    ║                                                               ║
    ║  Analyzes seminal papers, finds recent citations, and        ║
    ║  proposes future research directions                         ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    if len(sys.argv) > 1:
        # PDF path provided as command line argument
        paper_path = sys.argv[1]
    else:
        # Interactive mode
        print("Welcome! I am an AI Research Assistant.\n")
        print("My purpose is to help you explore the academic landscape related to a seminal paper.\n")
        print("I can:")
        print("  • Analyze a seminal paper you provide")
        print("  • Find recent academic papers that cite the seminal work")
        print("  • Suggest potential future research directions\n")

        paper_path = input("Please provide the path to the seminal paper PDF: ").strip()

        if not paper_path:
            print("\nError: No PDF path provided. Exiting.")
            sys.exit(1)

    # Validate file exists
    import os
    if not os.path.exists(paper_path):
        print(f"\nError: File not found: {paper_path}")
        sys.exit(1)

    # Run the research workflow
    try:
        result = run_academic_research(paper_path)
        print("\n✓ Analysis complete!")

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting.")
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ Error during analysis: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
