#!/usr/bin/env python
"""Energy Agent AI - CrewAI Implementation"""

import sys
from crewai import Crew, Process
from agents import energy_auditor, renewable_energy_advisor, cost_optimizer, sustainability_advisor, implementation_planner
from tasks import create_tasks


def main():
    print("Energy Agent AI - Energy Management System")
    print("="*60)

    property_type = input("Property type (Residential/Commercial/Industrial): ").strip() or "Residential"
    size = input("Property size (sq ft or kW): ").strip() or "2000 sq ft"
    location = input("Location: ").strip() or "California"

    property_info = {
        'type': property_type,
        'size': size,
        'location': location
    }

    tasks = create_tasks(property_info)
    crew = Crew(
        agents=[energy_auditor, renewable_energy_advisor, cost_optimizer, sustainability_advisor, implementation_planner],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print(f"\nAnalyzing energy for {property_type} property...")
    result = crew.kickoff()
    print("\n" + "="*60)
    print("ENERGY ANALYSIS COMPLETE")
    print("="*60)
    print(result)


if __name__ == "__main__":
    main()
