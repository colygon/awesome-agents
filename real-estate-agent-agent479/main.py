#!/usr/bin/env python
from crewai import Crew, Process
from agents import RealEstateAgentAgents
from tasks import RealEstateAgentTasks
from dotenv import load_dotenv

load_dotenv()

def run_real_estate_agent():
    print("## Welcome to the Real Estate Agent Crew")
    print("----------------------------------------")

    transaction_type = input("Buying or Selling? ")
    location = input("Location/Area? ")
    budget = input("Budget/Price range? ")
    requirements = input("Key requirements? (e.g., 3 bed, 2 bath, garage): ")

    criteria = f"{transaction_type} in {location}, Budget: {budget}, Requirements: {requirements}"

    agents = RealEstateAgentAgents()
    tasks_manager = RealEstateAgentTasks()

    finder = agents.property_finder()
    analyst = agents.market_analyst()
    negotiator = agents.negotiation_specialist()
    advisor = agents.client_advisor()

    search_task = tasks_manager.search_properties(finder, criteria)
    market_task = tasks_manager.analyze_market(analyst, location)
    offer_task = tasks_manager.prepare_offer(negotiator, criteria)
    guide_task = tasks_manager.guide_client(advisor, transaction_type)

    crew = Crew(
        agents=[finder, analyst, negotiator, advisor],
        tasks=[search_task, market_task, offer_task, guide_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print("\n## Real Estate Agent Results\n")
    print(result)
    return result

if __name__ == "__main__":
    run_real_estate_agent()
