#!/usr/bin/env python
"""
Learning Content System - CrewAI Implementation
"""

import sys
from crewai import Crew, Process
from agents import curriculum_designer, content_creator, assessment_designer, learning_experience_designer, quality_reviewer
from tasks import create_tasks


def main():
    print("Learning Content System - CrewAI Edition")
    print("="*60)

    subject = input("Course subject: ").strip()
    level = input("Level (Beginner/Intermediate/Advanced): ").strip() or "Intermediate"
    duration = input("Duration (e.g., 4 weeks): ").strip() or "4 weeks"
    audience = input("Target audience: ").strip() or "General learners"

    course_info = {
        'subject': subject,
        'level': level,
        'duration': duration,
        'audience': audience
    }

    tasks = create_tasks(course_info)
    crew = Crew(
        agents=[curriculum_designer, content_creator, assessment_designer, learning_experience_designer, quality_reviewer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nCreating learning content...")
    result = crew.kickoff()
    print("\n" + "="*60)
    print("CONTENT CREATION COMPLETE")
    print("="*60)
    print(result)


if __name__ == "__main__":
    main()
