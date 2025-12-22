#!/usr/bin/env python
"""
Safety Plugins Agent CrewAI Main Application
Migrated from Google ADK to CrewAI
"""

import sys
import json
from crewai import Crew, Process
from agents import (
    content_moderator,
    toxicity_analyzer,
    sensitive_info_guardian,
    bias_detector,
    safety_coordinator
)
from tasks import create_tasks


def analyze_content_safety(content: str, context: dict = None):
    """
    Perform comprehensive safety analysis on content

    Args:
        content: The content to analyze
        context: Additional context (optional)

    Returns:
        Safety analysis results
    """

    print("\n" + "="*80)
    print("SAFETY PLUGINS AGENT - Comprehensive Safety Analysis")
    print("="*80)
    print(f"\nContent to analyze ({len(content)} characters):")
    print("-" * 80)
    print(content[:500] + ("..." if len(content) > 500 else ""))
    print("-" * 80)

    if context:
        print(f"\nContext: {json.dumps(context, indent=2)}")

    # Create tasks
    tasks = create_tasks(content, context)

    # Create crew
    crew = Crew(
        agents=[
            toxicity_analyzer,
            content_moderator,
            sensitive_info_guardian,
            bias_detector,
            safety_coordinator
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute the safety analysis workflow
    print("\nStarting safety analysis...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("SAFETY ANALYSIS COMPLETE")
    print("="*80)
    print("\n" + str(result))

    return result


def interactive_mode():
    """Run the agent in interactive mode"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║          SAFETY PLUGINS AGENT - CrewAI Edition                ║
    ║                                                               ║
    ║  Comprehensive content safety analysis including:            ║
    ║  • Toxicity Detection                                        ║
    ║  • Content Moderation                                        ║
    ║  • Privacy/PII Protection                                    ║
    ║  • Bias and Fairness Analysis                                ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    print("\nWelcome to the Safety Plugins Agent!")
    print("This tool performs comprehensive safety analysis on content.")
    print("\nYou can:")
    print("  1. Enter content directly")
    print("  2. Load content from a file")
    print("  3. Enter 'quit' to exit\n")

    while True:
        try:
            print("="*80)
            choice = input("\nEnter content or 'file <path>' to load from file (or 'quit'): ").strip()

            if not choice or choice.lower() in ['quit', 'exit']:
                print("\nThank you for using Safety Plugins Agent. Goodbye!")
                break

            # Load from file
            if choice.lower().startswith('file '):
                file_path = choice[5:].strip()
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    print(f"\nLoaded {len(content)} characters from {file_path}")
                except Exception as e:
                    print(f"\nError loading file: {e}")
                    continue
            else:
                # Use input as content
                content = choice

                # If content is short, allow multi-line input
                if len(content) < 100:
                    print("\nEnter additional lines (empty line to finish):")
                    lines = [content]
                    while True:
                        line = input()
                        if not line:
                            break
                        lines.append(line)
                    content = "\n".join(lines)

            if not content.strip():
                print("\nError: No content provided.")
                continue

            # Optional context
            context_input = input("\nAdd context? (press Enter to skip, or enter JSON): ").strip()
            context = None
            if context_input:
                try:
                    context = json.loads(context_input)
                except:
                    context = {"note": context_input}

            # Analyze content
            analyze_content_safety(content, context)

            # Ask if user wants to continue
            continue_choice = input("\n\nAnalyze more content? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("\nThank you for using Safety Plugins Agent. Goodbye!")
                break

        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Goodbye!")
            break

        except Exception as e:
            print(f"\nError: {str(e)}")
            import traceback
            traceback.print_exc()


def file_mode(file_path: str, context: dict = None):
    """Analyze content from a file"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║          SAFETY PLUGINS AGENT - CrewAI Edition                ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"\nLoaded content from: {file_path}")
        print(f"Content length: {len(content)} characters\n")

        result = analyze_content_safety(content, context)
        return result

    except Exception as e:
        print(f"\nError loading file: {str(e)}")
        sys.exit(1)


def main():
    """Main entry point for the application"""

    if len(sys.argv) > 1:
        # File mode - analyze content from file
        file_path = sys.argv[1]

        # Optional context as JSON
        context = None
        if len(sys.argv) > 2:
            try:
                context = json.loads(sys.argv[2])
            except:
                context = {"note": sys.argv[2]}

        file_mode(file_path, context)
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
