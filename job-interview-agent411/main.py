#!/usr/bin/env python
"""
Job Interview Agent - CrewAI Implementation
Comprehensive interview preparation system
"""

import sys
import os
from crewai import Crew, Process
from agents import (
    resume_analyzer,
    company_researcher,
    question_generator,
    answer_coach,
    mock_interviewer
)
from tasks import create_tasks


def run_interview_prep(resume_path: str, job_title: str, company_name: str):
    """
    Run the interview preparation crew

    Args:
        resume_path: Path to candidate's resume
        job_title: Target job title
        company_name: Company name

    Returns:
        Comprehensive interview preparation guide
    """

    print("\n" + "="*80)
    print("JOB INTERVIEW PREPARATION AGENT - CrewAI Edition")
    print("="*80)
    print(f"\nPosition: {job_title}")
    print(f"Company: {company_name}")
    print(f"Resume: {resume_path}\n")

    # Create tasks
    tasks = create_tasks(resume_path, job_title, company_name)

    # Create crew
    crew = Crew(
        agents=[
            resume_analyzer,
            company_researcher,
            question_generator,
            answer_coach,
            mock_interviewer
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute the interview preparation workflow
    print("\nStarting interview preparation workflow...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("INTERVIEW PREPARATION COMPLETE")
    print("="*80)
    print("\n" + str(result))

    return result


def main():
    """Main entry point for the application"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║         JOB INTERVIEW AGENT - CrewAI Edition                  ║
    ║                                                               ║
    ║  Comprehensive interview preparation with AI assistance      ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    # Interactive mode
    print("Welcome! I will help you prepare for your job interview.\n")
    print("I can help you:")
    print("  • Analyze your resume and identify key strengths")
    print("  • Research the target company")
    print("  • Generate relevant interview questions")
    print("  • Provide model answers and coaching")
    print("  • Conduct mock interview preparation\n")

    # Get inputs
    resume_path = input("Resume file path (PDF/DOCX/TXT): ").strip()
    if not resume_path:
        print("\nError: Resume path is required.")
        sys.exit(1)

    if not os.path.exists(resume_path):
        print(f"\nError: File not found: {resume_path}")
        sys.exit(1)

    job_title = input("Job title/role: ").strip()
    if not job_title:
        print("\nError: Job title is required.")
        sys.exit(1)

    company_name = input("Company name: ").strip()
    if not company_name:
        print("\nError: Company name is required.")
        sys.exit(1)

    # Run the interview preparation workflow
    try:
        result = run_interview_prep(resume_path, job_title, company_name)
        print("\n✓ Interview preparation complete!")
        print("\nGood luck with your interview!")

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting.")
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ Error during preparation: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
