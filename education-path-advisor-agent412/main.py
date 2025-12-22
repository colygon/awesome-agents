#!/usr/bin/env python
"""
Education Path Advisor for India - CrewAI Implementation
Personalized education and career guidance for Indian students
"""

import sys
from crewai import Crew, Process
from agents import (
    student_analyst,
    career_researcher,
    education_expert,
    stream_advisor,
    roadmap_creator
)
from tasks import create_tasks


def collect_student_info():
    """
    Collect student information interactively

    Returns:
        Dictionary with student information
    """
    print("\nPlease provide student information:\n")

    student_info = {}

    student_info['name'] = input("Student name: ").strip()
    student_info['grade'] = input("Current grade (e.g., 10th, 12th, 1st year): ").strip()
    student_info['board'] = input("Education board (CBSE/ICSE/State): ").strip()

    print("\nAcademic Performance:")
    student_info['subjects'] = input("Current subjects (comma-separated): ").strip()
    student_info['marks'] = input("Overall percentage/CGPA and subject-wise performance: ").strip()

    print("\nInterests and Activities:")
    student_info['interests'] = input("Areas of interest (e.g., technology, art, business, science): ").strip()
    student_info['activities'] = input("Extracurricular activities/achievements: ").strip()

    print("\nPractical Information:")
    student_info['location'] = input("City/State: ").strip()
    student_info['budget'] = input("Education budget (low/moderate/high or amount): ").strip()

    return student_info


def run_education_advisor(student_info: dict):
    """
    Run the education path advisory crew

    Args:
        student_info: Student information dictionary

    Returns:
        Comprehensive education guidance
    """

    print("\n" + "="*80)
    print("EDUCATION PATH ADVISOR FOR INDIA - CrewAI Edition")
    print("="*80)
    print(f"\nStudent: {student_info.get('name', 'N/A')}")
    print(f"Grade: {student_info.get('grade', 'N/A')}")
    print(f"Location: {student_info.get('location', 'India')}\n")

    # Create tasks
    tasks = create_tasks(student_info)

    # Create crew with all agents
    all_agents = [
        student_analyst,
        career_researcher,
        education_expert,
        stream_advisor,
        roadmap_creator
    ]

    crew = Crew(
        agents=all_agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute the advisory workflow
    print("\nAnalyzing your profile and creating personalized education roadmap...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("EDUCATION GUIDANCE COMPLETE")
    print("="*80)
    print("\n" + str(result))

    return result


def main():
    """Main entry point for the application"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║      EDUCATION PATH ADVISOR FOR INDIA - CrewAI Edition        ║
    ║                                                               ║
    ║  Personalized career guidance and education planning         ║
    ║  for Indian students                                         ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    print("Welcome! I will help you plan your educational journey.\n")
    print("I can help you:")
    print("  • Analyze your academic strengths and interests")
    print("  • Explore suitable career options")
    print("  • Choose the right stream and subjects")
    print("  • Identify colleges and entrance exams")
    print("  • Create a detailed roadmap to achieve your goals\n")

    # Collect student information
    try:
        student_info = collect_student_info()

        if not student_info.get('name') or not student_info.get('grade'):
            print("\nError: Student name and grade are required.")
            sys.exit(1)

        # Run the education advisory workflow
        result = run_education_advisor(student_info)

        print("\n✓ Education guidance complete!")
        print("\nYour personalized roadmap has been created.")
        print("Best wishes for your educational journey!")

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
