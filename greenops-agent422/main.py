#!/usr/bin/env python
from crewai import Crew, Process
from agents import GreenOpsAgents
from tasks import GreenOpsTasks
from dotenv import load_dotenv

load_dotenv()

def run_greenops_analysis():
    """
    Run a comprehensive GreenOps sustainability analysis
    """
    print("## Welcome to the GreenOps Sustainability Crew")
    print('-------------------------------')

    # Get user input
    infrastructure_data = input("Enter infrastructure data or 'default' for sample analysis: ")
    if infrastructure_data.lower() == 'default':
        infrastructure_data = "AWS multi-region deployment, 450 instances, 3.2 PB storage"

    current_setup = input("Enter current setup details or 'default': ")
    if current_setup.lower() == 'default':
        current_setup = "Standard deployment across US-East, EU-West, Asia-Pacific"

    workload_profile = input("Enter workload profile or 'default': ")
    if workload_profile.lower() == 'default':
        workload_profile = "Web applications, ML training, batch processing, databases"

    # Initialize agents and tasks
    agents = GreenOpsAgents()
    tasks = GreenOpsTasks()

    # Create agents
    sustainability_analyst = agents.sustainability_analyst()
    infrastructure_optimizer = agents.infrastructure_optimizer()
    renewable_coordinator = agents.renewable_energy_coordinator()
    reporter = agents.sustainability_reporter()

    # Create tasks
    impact_analysis = tasks.analyze_environmental_impact(sustainability_analyst, infrastructure_data)
    optimization_task = tasks.optimize_green_infrastructure(infrastructure_optimizer, current_setup)
    renewable_task = tasks.maximize_renewable_energy(renewable_coordinator, workload_profile)
    report_task = tasks.generate_sustainability_report(reporter)

    # Create crew
    crew = Crew(
        agents=[sustainability_analyst, infrastructure_optimizer, renewable_coordinator, reporter],
        tasks=[impact_analysis, optimization_task, renewable_task, report_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()

    print("\n\n########################")
    print("## GreenOps Analysis Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_greenops_analysis()
