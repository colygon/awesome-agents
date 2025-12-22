#!/usr/bin/env python
from crewai import Crew, Process
from agents import AgentFluxAgents
from tasks import AgentFluxTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_agentflux():
    """
    Run the AgentFlux Platform system
    """
    print("## Welcome to the AgentFlux Platform")
    print("-------------------------------------")

    workflow_definition = input("Enter workflow definition (or 'default' for sample): ")
    if workflow_definition.lower() == 'default':
        workflow_definition = '{"name": "data_processing", "agents": ["analyzer", "processor", "validator"]}'

    # Initialize agents and tasks
    agents = AgentFluxAgents()
    tasks = AgentFluxTasks()

    # Create agents
    orchestrator = agents.orchestration_agent()
    registry_manager = agents.registry_manager_agent()
    communicator = agents.communication_agent()
    workflow_designer = agents.workflow_designer_agent()
    monitor = agents.monitoring_agent()

    # Create tasks
    orchestration_task = tasks.orchestrate_workflow_task(orchestrator, workflow_definition)
    registry_task = tasks.manage_agent_registry_task(registry_manager, "new_agent_registration")
    communication_task = tasks.route_communications_task(communicator, "inter_agent_message")
    design_task = tasks.design_workflow_task(workflow_designer, workflow_definition)
    monitoring_task = tasks.monitor_performance_task(monitor, "system_metrics")

    # Create crew
    crew = Crew(
        agents=[orchestrator, registry_manager, communicator, workflow_designer, monitor],
        tasks=[design_task, registry_task, orchestration_task, communication_task, monitoring_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## AgentFlux Result")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_agentflux()
