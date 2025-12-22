#!/usr/bin/env python
"""
YouTube Thumbnail CrewAI Main Application
AI-powered thumbnail design and optimization system
"""

import sys
from crewai import Crew, Process
from agents import thumbnail_analyst, design_strategist, optimization_expert
from tasks import create_tasks


def run_thumbnail_creator(video_topic: str, target_audience: str = "general", existing_thumbnail: str = None):
    """
    Run the YouTube Thumbnail crew to analyze and create thumbnails

    Args:
        video_topic: Topic or title of the YouTube video
        target_audience: Target audience description
        existing_thumbnail: Optional URL of existing thumbnail to analyze

    Returns:
        Thumbnail design concepts and optimization strategy
    """

    print("\n" + "="*80)
    print("YOUTUBE THUMBNAIL CREATOR - AI Edition")
    print("="*80)
    print(f"\nVideo Topic: {video_topic}")
    print(f"Target Audience: {target_audience}")
    if existing_thumbnail:
        print(f"Existing Thumbnail: {existing_thumbnail}")
    print()

    # Create tasks
    tasks = create_tasks(video_topic, target_audience, existing_thumbnail)

    # Create crew
    crew = Crew(
        agents=[thumbnail_analyst, design_strategist, optimization_expert],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute the thumbnail creation workflow
    print("\nStarting thumbnail design workflow...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("THUMBNAIL DESIGNS COMPLETE")
    print("="*80)
    print("\n" + str(result))

    return result


def main():
    """Main entry point for the application"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║         YOUTUBE THUMBNAIL CREATOR - CrewAI Edition            ║
    ║                                                               ║
    ║  AI-Powered Thumbnail Design & Optimization                   ║
    ║  Create high-converting thumbnails backed by data             ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    # Check for command line arguments
    if len(sys.argv) > 1:
        video_topic = " ".join(sys.argv[1:])
        target_audience = "general"
        existing_thumbnail = None
    else:
        # Interactive mode
        print("Welcome to YouTube Thumbnail Creator!\n")
        print("I help you create high-performing thumbnails using AI.\n")
        print("I can:")
        print("  • Analyze successful thumbnails in your niche")
        print("  • Create multiple design concepts optimized for clicks")
        print("  • Generate A/B testing variations")
        print("  • Provide implementation guides and best practices\n")

        video_topic = input("What is your video about? (topic or title): ").strip()

        if not video_topic:
            print("\nError: No video topic provided. Exiting.")
            sys.exit(1)

        target_audience = input("Who is your target audience? (default: general): ").strip() or "general"

        existing = input("Do you have an existing thumbnail to analyze? (URL or leave blank): ").strip()
        existing_thumbnail = existing if existing else None

    # Run the thumbnail creation workflow
    try:
        result = run_thumbnail_creator(video_topic, target_audience, existing_thumbnail)
        print("\n✓ Thumbnail designs complete!")
        print("\nNext steps:")
        print("  1. Review the design concepts above")
        print("  2. Create the thumbnails using design software (Canva, Photoshop, etc.)")
        print("  3. Implement A/B testing strategy")
        print("  4. Track CTR and iterate based on results")

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting.")
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ Error during thumbnail creation: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
