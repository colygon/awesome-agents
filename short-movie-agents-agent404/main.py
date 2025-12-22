#!/usr/bin/env python
"""
Short Movie Agents CrewAI Main Application
Migrated from Google ADK to CrewAI
"""

import sys
from crewai import Crew, Process
from agents import (
    story_developer,
    screenwriter,
    storyboard_artist,
    character_developer,
    directors_vision
)
from tasks import create_tasks


def develop_short_film(concept: str, genre: str = "drama", duration: int = 10):
    """
    Develop a complete short film from concept to production-ready materials

    Args:
        concept: Initial story concept or prompt
        genre: Film genre
        duration: Target duration in minutes

    Returns:
        Complete film development package
    """

    print("\n" + "="*80)
    print("SHORT MOVIE AGENTS - Film Development System")
    print("="*80)
    print(f"\nConcept: {concept}")
    print(f"Genre: {genre}")
    print(f"Target Duration: {duration} minutes\n")

    # Create tasks
    tasks = create_tasks(concept, genre, duration)

    # Create crew
    crew = Crew(
        agents=[
            story_developer,
            character_developer,
            screenwriter,
            storyboard_artist,
            directors_vision
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute the film development workflow
    print("\nStarting film development process...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("FILM DEVELOPMENT COMPLETE")
    print("="*80)
    print("\n" + str(result))

    return result


def interactive_mode():
    """Run the agent in interactive mode"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║           SHORT MOVIE AGENTS - CrewAI Edition                 ║
    ║                                                               ║
    ║  Complete short film development system                      ║
    ║  From concept to production-ready materials                  ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    print("\nWelcome to Short Movie Agents!")
    print("This system develops complete short films including:")
    print("  • Story concept and structure")
    print("  • Character development")
    print("  • Full screenplay")
    print("  • Visual storyboards")
    print("  • Director's vision statement\n")

    # Get concept
    print("Enter your story concept or prompt:")
    print("(This can be a theme, situation, character idea, or full premise)")
    concept = input("> ").strip()

    if not concept:
        print("\nError: No concept provided.")
        return

    # Get genre
    print("\nGenre (drama/comedy/thriller/horror/sci-fi/romance/etc.):")
    genre = input("> ").strip() or "drama"

    # Get duration
    print("\nTarget duration in minutes (default: 10):")
    duration_input = input("> ").strip()
    try:
        duration = int(duration_input) if duration_input else 10
        if duration < 1 or duration > 30:
            print("Duration should be 1-30 minutes. Using default of 10.")
            duration = 10
    except ValueError:
        print("Invalid duration. Using default of 10 minutes.")
        duration = 10

    print("\n" + "="*80)
    print("Starting film development...")
    print("This may take several minutes as we develop your complete film package.")
    print("="*80 + "\n")

    # Develop the film
    try:
        result = develop_short_film(concept, genre, duration)
        print("\n✓ Film development complete!")
        print("\nYour short film package is ready for production.")

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting.")
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ Error during development: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    """Main entry point for the application"""

    if len(sys.argv) > 1:
        # Command line mode
        concept = sys.argv[1]
        genre = sys.argv[2] if len(sys.argv) > 2 else "drama"
        duration = int(sys.argv[3]) if len(sys.argv) > 3 else 10

        develop_short_film(concept, genre, duration)
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
