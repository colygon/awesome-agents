#!/usr/bin/env python
"""
Job Finder CrewAI Main Application
"""

import sys
from crewai import Crew, Process
from agents import job_researcher, resume_matcher, application_strategist
from tasks import create_tasks


def main():
    print("\n" + "="*80)
    print("JOB FINDER")
    print("="*80)

    job_title = input("Job title: ").strip() or "Software Engineer"
    location = input("Location: ").strip() or "San Francisco, CA"
    skills_input = input("Your skills (comma-separated): ").strip()
    skills = [s.strip() for s in skills_input.split(",")] if skills_input else ["Python", "React"]

    tasks = create_tasks(job_title, location, skills)
    crew = Crew(
        agents=[job_researcher, resume_matcher, application_strategist],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nFinding jobs...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("JOB SEARCH COMPLETE")
    print("="*80)
    print("\n" + str(result))


if __name__ == "__main__":
    main()
