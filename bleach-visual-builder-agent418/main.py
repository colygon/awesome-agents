#!/usr/bin/env python
"""Bleach Visual Builder - CrewAI Implementation"""

import sys
from crewai import Crew, Process
from agents import ui_designer, component_architect, accessibility_specialist, responsive_designer, code_generator
from tasks import create_tasks


def main():
    print("Bleach Visual Builder - UI/UX Design System")
    print("="*60)

    name = input("Project name: ").strip() or "My App"
    style = input("Design style (Modern/Minimal/Bold): ").strip() or "Modern"
    framework = input("Framework (React/Vue/HTML): ").strip() or "React"
    pages = input("Pages (comma-separated): ").strip() or "Home, About, Contact"

    project_spec = {
        'name': name,
        'style': style,
        'framework': framework,
        'pages': pages
    }

    tasks = create_tasks(project_spec)
    crew = Crew(
        agents=[ui_designer, component_architect, accessibility_specialist, responsive_designer, code_generator],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print(f"\nCreating design system for {name}...")
    result = crew.kickoff()
    print("\n" + "="*60)
    print("DESIGN COMPLETE")
    print("="*60)
    print(result)


if __name__ == "__main__":
    main()
