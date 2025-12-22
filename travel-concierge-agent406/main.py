#!/usr/bin/env python
"""Travel Concierge Agent CrewAI Main Application"""

import sys
from crewai import Crew, Process
from agents import destination_expert, flight_coordinator, accommodation_specialist, itinerary_planner, travel_coordinator
from tasks import create_tasks


def plan_travel(request: str, budget: str = "moderate", dates: str = "flexible"):
    print(f"\n{'='*80}\nTRAVEL CONCIERGE AGENT\n{'='*80}\n")
    tasks = create_tasks(request, budget, dates)
    crew = Crew(
        agents=[destination_expert, flight_coordinator, accommodation_specialist, itinerary_planner, travel_coordinator],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    result = crew.kickoff()
    print(f"\n{'='*80}\nTRAVEL PLAN COMPLETE\n{'='*80}\n{result}")
    return result


def main():
    if len(sys.argv) > 1:
        plan_travel(sys.argv[1])
    else:
        print("Travel Concierge Agent\n")
        request = input("Describe your ideal trip: ")
        budget = input("Budget (low/moderate/high): ") or "moderate"
        dates = input("Travel dates (or 'flexible'): ") or "flexible"
        plan_travel(request, budget, dates)


if __name__ == "__main__":
    main()
