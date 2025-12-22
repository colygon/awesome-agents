#!/usr/bin/env python
"""
Project Manager Agent - CrewAI Implementation
Comprehensive project management and planning system
"""

import sys
from crewai import Crew, Process
from agents import (
    project_planner,
    task_breakdown_specialist,
    resource_allocator,
    risk_manager,
    timeline_scheduler,
    documentation_specialist
)
from tasks import create_tasks


def collect_project_info():
    """Collect project information interactively"""
    print("\nPlease provide project information:\n")

    project_info = {}
    project_info['name'] = input("Project name: ").strip()
    project_info['description'] = input("Project description: ").strip()
    project_info['goals'] = input("Project goals/objectives: ").strip()
    project_info['team_size'] = input("Team size (number): ").strip()
    project_info['budget'] = input("Budget (e.g., $100K, 50 lakhs): ").strip()
    project_info['timeline'] = input("Desired timeline (e.g., 3 months, 6 months): ").strip()
    project_info['methodology'] = input("Preferred methodology (Agile/Waterfall/Hybrid): ").strip() or "Agile"

    return project_info


def run_project_manager(project_info: dict):
    """Run the project management crew"""

    print("\n" + "="*80)
    print("PROJECT MANAGER AGENT - CrewAI Edition")
    print("="*80)
    print(f"\nProject: {project_info.get('name', 'N/A')}")
    print(f"Timeline: {project_info.get('timeline', 'N/A')}")
    print(f"Team Size: {project_info.get('team_size', 'N/A')}\n")

    tasks = create_tasks(project_info)

    crew = Crew(
        agents=[
            project_planner,
            task_breakdown_specialist,
            resource_allocator,
            risk_manager,
            timeline_scheduler,
            documentation_specialist
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nCreating comprehensive project plan...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("PROJECT PLANNING COMPLETE")
    print("="*80)
    print("\n" + str(result))

    return result


def main():
    """Main entry point"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║         PROJECT MANAGER AGENT - CrewAI Edition                ║
    ║                                                               ║
    ║  Comprehensive project planning and management               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    print("Welcome! I will help you create a comprehensive project plan.\n")
    print("I can help you:")
    print("  • Define project scope and objectives")
    print("  • Break down work into manageable tasks")
    print("  • Allocate resources and budget")
    print("  • Identify and mitigate risks")
    print("  • Create realistic schedules")
    print("  • Generate project documentation\n")

    try:
        project_info = collect_project_info()

        if not project_info.get('name'):
            print("\nError: Project name is required.")
            sys.exit(1)

        result = run_project_manager(project_info)
        print("\n✓ Project planning complete!")

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
