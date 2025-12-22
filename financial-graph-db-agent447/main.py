#!/usr/bin/env python
from crewai import Crew, Process
from agents import FinancialGraphAgents
from tasks import FinancialGraphTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_financial_graph():
    """
    Run the Financial Graph Database system
    """
    print("## Welcome to Financial Graph Database System")
    print("----------------------------------------------")

    print("\nEnter financial data to analyze (or 'sample' for example):")
    financial_data = input()
    if financial_data.lower() == 'sample':
        financial_data = "Company A owns 75% of Company B. John Doe is CEO of Company A."

    query_focus = input("Enter query focus (e.g., ownership, transactions): ")

    # Initialize agents and tasks
    agents = FinancialGraphAgents()
    tasks = FinancialGraphTasks()

    # Create agents
    extractor = agents.entity_extraction_agent()
    relationship_agent = agents.relationship_agent()
    builder = agents.graph_builder_agent()
    query_agent = agents.query_agent()
    visualizer = agents.visualization_agent()

    # Create tasks
    extraction_task = tasks.extract_entities_task(extractor, financial_data)
    relationship_task = tasks.analyze_relationships_task(relationship_agent, "{{extraction_output}}")
    build_task = tasks.build_graph_task(builder, "{{extraction_output}}", "{{relationship_output}}")
    query_task = tasks.query_graph_task(query_agent, query_focus)
    viz_task = tasks.visualize_graph_task(visualizer, "{{build_output}}", query_focus)

    # Create crew
    crew = Crew(
        agents=[extractor, relationship_agent, builder, query_agent, visualizer],
        tasks=[extraction_task, relationship_task, build_task, query_task, viz_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## Financial Graph Result")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_financial_graph()
