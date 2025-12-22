#!/usr/bin/env python
from crewai import Crew, Process
from agents import DataVisualizationAgents
from tasks import DataVisualizationTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_data_visualization():
    """
    Run the Data Visualization system
    """
    print("## Welcome to AI Data Visualization System")
    print("-------------------------------------------")

    # Gather requirements
    print("\nLet's visualize your data!")
    dataset_desc = input("Describe your dataset (or 'sample' for example): ")
    if dataset_desc.lower() == 'sample':
        dataset_desc = "Sales data with columns: date, region, product, sales_amount, customer_count"

    purpose = input("What's the purpose of this visualization? (e.g., quarterly report): ")
    if not purpose:
        purpose = "business analysis"

    # Initialize agents and tasks
    agents = DataVisualizationAgents()
    tasks = DataVisualizationTasks()

    # Create agents
    analyst = agents.data_analyst_agent()
    designer = agents.visualization_designer_agent()
    chart_specialist = agents.chart_specialist_agent()
    dashboard_architect = agents.dashboard_architect_agent()
    insight_analyst = agents.insight_analyst_agent()

    # Create tasks
    analysis_task = tasks.analyze_data_task(analyst, dataset_desc)
    design_task = tasks.design_visualization_task(designer, "{{analysis_output}}", purpose)
    chart_task = tasks.generate_charts_task(chart_specialist, "{{design_output}}", dataset_desc)
    dashboard_task = tasks.build_dashboard_task(dashboard_architect, "{{chart_output}}", purpose)
    insights_task = tasks.extract_insights_task(insight_analyst, "{{dashboard_output}}")

    # Create crew
    crew = Crew(
        agents=[analyst, designer, chart_specialist, dashboard_architect, insight_analyst],
        tasks=[analysis_task, design_task, chart_task, dashboard_task, insights_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## Visualization Result")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_data_visualization()
