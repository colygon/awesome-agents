#!/usr/bin/env python
from crewai import Crew, Process
from agents import DeepSearchAgents
from tasks import DeepSearchTasks
from dotenv import load_dotenv
import os

load_dotenv()

def run_deep_search(query: str):
    """
    Run a deep search on a given query using a team of specialized agents.
    """
    print(f"\n{'='*60}")
    print(f"Starting Deep Search for: {query}")
    print(f"{'='*60}\n")

    # Initialize agents and tasks
    agents = DeepSearchAgents()
    tasks = DeepSearchTasks()

    # Create agents
    search_strategist = agents.search_strategist()
    information_analyst = agents.information_analyst()
    fact_checker = agents.fact_checker()
    research_synthesizer = agents.research_synthesizer()

    # Create tasks
    strategy_task = tasks.plan_search_strategy(
        agent=search_strategist,
        query=query
    )

    search_task = tasks.execute_deep_search(
        agent=information_analyst,
        search_plan="Use the search strategy to gather comprehensive information"
    )

    analysis_task = tasks.analyze_information(
        agent=information_analyst,
        search_results="Analyze all gathered search results"
    )

    verification_task = tasks.verify_facts(
        agent=fact_checker,
        key_claims="Verify key claims from the analysis"
    )

    synthesis_task = tasks.synthesize_report(
        agent=research_synthesizer,
        query=query,
        analysis="Synthesize all findings",
        verification="Include verification results"
    )

    # Create crew
    crew = Crew(
        agents=[
            search_strategist,
            information_analyst,
            fact_checker,
            research_synthesizer
        ],
        tasks=[
            strategy_task,
            search_task,
            analysis_task,
            verification_task,
            synthesis_task
        ],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print(f"\n{'='*60}")
    print("Deep Search Complete!")
    print(f"{'='*60}\n")
    print(result)

    return result

if __name__ == "__main__":
    # Example usage
    search_query = input("Enter your search query: ")
    if search_query:
        run_deep_search(search_query)
    else:
        # Default example
        run_deep_search("What are the latest developments in quantum computing?")
