#!/usr/bin/env python
"""
Cognisphere CrewAI Main Application
A knowledge exploration and cognitive analysis system
"""

import sys
from crewai import Crew, Process
from agents import knowledge_explorer, concept_analyzer, insight_generator
from tasks import create_tasks


def run_cognisphere(topic: str, depth: str = "comprehensive"):
    """
    Run the Cognisphere crew to explore knowledge domains and generate insights

    Args:
        topic: The knowledge domain or topic to explore
        depth: Analysis depth - "overview", "detailed", or "comprehensive"

    Returns:
        Knowledge analysis and insights
    """

    print("\n" + "="*80)
    print("COGNISPHERE - Knowledge Exploration & Cognitive Analysis")
    print("="*80)
    print(f"\nExploring topic: {topic}")
    print(f"Analysis depth: {depth}\n")

    # Create tasks
    tasks = create_tasks(topic, depth)

    # Create crew
    crew = Crew(
        agents=[knowledge_explorer, concept_analyzer, insight_generator],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute the knowledge exploration workflow
    print("\nStarting knowledge exploration workflow...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print("\n" + str(result))

    return result


def main():
    """Main entry point for the application"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║              COGNISPHERE - CrewAI Edition                     ║
    ║                                                               ║
    ║  Knowledge Exploration & Cognitive Analysis System            ║
    ║  Discover, analyze, and synthesize knowledge domains          ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    if len(sys.argv) > 1:
        # Topic provided as command line argument
        topic = " ".join(sys.argv[1:])
        depth = "comprehensive"
    else:
        # Interactive mode
        print("Welcome to Cognisphere!\n")
        print("I help you explore knowledge domains through comprehensive analysis.\n")
        print("I can:")
        print("  • Map knowledge domains and their structures")
        print("  • Analyze concepts and their relationships")
        print("  • Generate actionable insights and recommendations\n")

        topic = input("What topic or knowledge domain would you like to explore? ").strip()

        if not topic:
            print("\nError: No topic provided. Exiting.")
            sys.exit(1)

        print("\nAnalysis depth options:")
        print("  1. overview - High-level exploration")
        print("  2. detailed - In-depth analysis")
        print("  3. comprehensive - Exhaustive investigation (default)")

        depth_choice = input("\nSelect depth (1-3, default=3): ").strip()
        depth_map = {"1": "overview", "2": "detailed", "3": "comprehensive", "": "comprehensive"}
        depth = depth_map.get(depth_choice, "comprehensive")

    # Run the knowledge exploration workflow
    try:
        result = run_cognisphere(topic, depth)
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
