"""
ADK Test Automation - CrewAI Multi-Agent Test Automation System
Main execution script for sequential test automation workflow

Usage:
    python main.py
"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import (
    create_test_strategist,
    create_test_generator,
    create_test_reviewer
)
from tasks import (
    create_test_strategy_task,
    create_test_generation_task,
    create_test_review_task
)


def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        sys.exit(1)


def get_sample_application_context():
    """Provides sample application context for demonstration."""
    return {
        'app_type': 'Web Application',
        'tech_stack': ['React', 'Node.js', 'Express', 'MongoDB'],
        'features': ['User Authentication', 'CRUD Operations', 'Real-time Updates', 'File Upload'],
        'description': """
            A collaborative task management web application built with React and Node.js.
            Users can create, update, and delete tasks, organize them into projects,
            and collaborate with team members in real-time. The app includes user
            authentication with JWT, file attachments, and WebSocket-based real-time updates.
        """
    }


def run_test_automation(application_context: dict, verbose: bool = True):
    """
    Executes the multi-agent test automation workflow.

    Args:
        application_context: Dictionary containing application information
        verbose: Whether to print detailed progress

    Returns:
        dict: Results containing test strategy, generated tests, and review
    """
    if verbose:
        print("\n" + "="*80)
        print("Initializing Test Automation Multi-Agent System")
        print("="*80 + "\n")

    # Create agents
    test_strategist = create_test_strategist()
    test_generator = create_test_generator()
    test_reviewer = create_test_reviewer()

    if verbose:
        print("  ✓ Test Strategist")
        print("  ✓ Test Generator")
        print("  ✓ Test Reviewer\n")

    # Create tasks
    strategy_task = create_test_strategy_task(test_strategist, application_context)
    generation_task = create_test_generation_task(test_generator, strategy_task, application_context)
    review_task = create_test_review_task(test_reviewer, strategy_task, generation_task)

    if verbose:
        print("  ✓ Test Strategy Task")
        print("  ✓ Test Generation Task")
        print("  ✓ Test Review Task\n")

    # Create and execute crew
    crew = Crew(
        agents=[test_strategist, test_generator, test_reviewer],
        tasks=[strategy_task, generation_task, review_task],
        process=Process.sequential,
        verbose=True
    )

    start_time = datetime.now()
    result = crew.kickoff()
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    if verbose:
        print(f"\nTest Automation Complete! (Duration: {duration:.2f} seconds)\n")

    return {
        'result': result,
        'duration': duration,
        'timestamp': datetime.now().isoformat()
    }


def main():
    """Main entry point for the CLI application."""
    load_environment()

    print("\n" + "="*80)
    print("ADK Test Automation - Multi-Agent System")
    print("="*80 + "\n")

    application_context = get_sample_application_context()
    result = run_test_automation(application_context, verbose=True)

    print("\n" + "="*80)
    print("TEST AUTOMATION RESULTS")
    print("="*80 + "\n")
    print(result['result'])


if __name__ == "__main__":
    main()
