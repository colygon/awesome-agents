#!/usr/bin/env python
"""
Incident Management CrewAI Main Application
"""

import sys
from crewai import Crew, Process
from agents import incident_coordinator, status_tracker, resolution_specialist
from tasks import create_tasks


def main():
    print("\n" + "="*80)
    print("SERVICENOW INCIDENT MANAGEMENT")
    print("="*80)
    print("\n1. Create new incident")
    print("2. Check incident status")
    print("3. Resolve incident")

    choice = input("\nSelect option (1-3): ").strip()

    if choice == "1":
        description = input("Describe the incident: ").strip()
        tasks = create_tasks("create", description=description)
        agents = [incident_coordinator]

    elif choice == "2":
        incident_num = input("Incident number: ").strip()
        tasks = create_tasks("status", incident_number=incident_num)
        agents = [status_tracker]

    elif choice == "3":
        incident_num = input("Incident number: ").strip()
        description = input("Issue description: ").strip()
        tasks = create_tasks("resolve", incident_number=incident_num, description=description)
        agents = [resolution_specialist, incident_coordinator]

    else:
        print("Invalid option.")
        return

    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nProcessing...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("COMPLETE")
    print("="*80)
    print("\n" + str(result))


if __name__ == "__main__":
    main()
