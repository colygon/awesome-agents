#!/usr/bin/env python
from crewai import Crew, Process
from agents import NexoraAIAgents
from tasks import NexoraAITasks
from dotenv import load_dotenv

load_dotenv()

def run_ai_development():
    """
    Run a complete AI model development workflow
    """
    print("## Welcome to the Nexora AI Development Crew")
    print('-------------------------------')

    # Get user input
    use_case = input("Enter AI use case or 'default' for sample project: ")
    if use_case.lower() == 'default':
        use_case = "Multi-modal content classification (images + text)"

    # Initialize agents and tasks
    agents = NexoraAIAgents()
    tasks = NexoraAITasks()

    # Create agents
    architect = agents.ai_model_architect()
    trainer = agents.training_specialist()
    deployer = agents.deployment_engineer()
    coordinator = agents.ai_project_coordinator()

    # Create tasks
    architecture_task = tasks.design_ai_architecture(architect, use_case)
    training_task = tasks.optimize_training_process(trainer, "From architecture task")
    deployment_task = tasks.plan_deployment_strategy(deployer, "From training task")
    coordination_task = tasks.coordinate_ai_project(coordinator)

    # Create crew
    crew = Crew(
        agents=[architect, trainer, deployer, coordinator],
        tasks=[architecture_task, training_task, deployment_task, coordination_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()

    print("\n\n########################")
    print("## AI Development Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_ai_development()
