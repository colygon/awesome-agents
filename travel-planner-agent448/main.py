#!/usr/bin/env python
from crewai import Crew, Process
from agents import TravelPlannerAgents
from tasks import TravelPlannerTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_travel_planner():
    """
    Run the Travel Planner system
    """
    print("## Welcome to AI Travel Planner")
    print("--------------------------------")

    # Gather trip information
    print("\nLet's plan your trip!")
    preferences = input("What are your travel interests? (e.g., culture, adventure, relaxation): ")
    budget = input("What's your approximate budget? (e.g., $2000): ")
    duration = input("How many days? ")
    dates = input("Travel dates (e.g., June 15-22, 2024): ")

    # Initialize agents and tasks
    agents = TravelPlannerAgents()
    tasks = TravelPlannerTasks()

    # Create agents
    destination_expert = agents.destination_expert_agent()
    flight_specialist = agents.flight_specialist_agent()
    accommodation_specialist = agents.accommodation_agent()
    itinerary_planner = agents.itinerary_planner_agent()
    budget_advisor = agents.budget_advisor_agent()

    # Create tasks
    destination_task = tasks.research_destination_task(destination_expert, preferences)
    flight_task = tasks.search_flights_task(flight_specialist, "{{destination_output}}", dates, budget)
    hotel_task = tasks.find_accommodation_task(accommodation_specialist, "{{destination_output}}", dates, preferences)
    itinerary_task = tasks.create_itinerary_task(itinerary_planner, "{{destination_output}}", duration, preferences)
    budget_task = tasks.calculate_budget_task(budget_advisor, f"duration:{duration}, budget:{budget}")

    # Create crew
    crew = Crew(
        agents=[destination_expert, flight_specialist, accommodation_specialist, itinerary_planner, budget_advisor],
        tasks=[destination_task, flight_task, hotel_task, itinerary_task, budget_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## Your Travel Plan")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_travel_planner()
