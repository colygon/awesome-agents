#!/usr/bin/env python
from crewai import Crew, Process
from agents import ParticlePhysicsAgents
from tasks import ParticlePhysicsTasks
from dotenv import load_dotenv

load_dotenv()

def run_particle_physics_analysis():
    """
    Run a complete particle physics analysis workflow
    """
    print("## Welcome to the Particle Physics Research Crew")
    print('-------------------------------')

    # Get user input
    collision_data = input("Enter collision data specification or 'default' for sample analysis: ")
    if collision_data.lower() == 'default':
        collision_data = "LHC Run 3 data, 150 fb^-1, √s = 13.6 TeV"

    detector_config = input("Enter detector configuration or 'default': ")
    if detector_config.lower() == 'default':
        detector_config = "ATLAS detector, standard configuration"

    # Initialize agents and tasks
    agents = ParticlePhysicsAgents()
    tasks = ParticlePhysicsTasks()

    # Create agents
    data_analyst = agents.particle_data_analyst()
    theorist = agents.theoretical_physicist()
    detector_specialist = agents.detector_specialist()
    coordinator = agents.research_coordinator()

    # Create tasks
    analysis_task = tasks.analyze_collision_events(data_analyst, collision_data)
    theory_task = tasks.theoretical_interpretation(theorist, "From data analysis task")
    detector_task = tasks.detector_optimization(detector_specialist, detector_config)
    synthesis_task = tasks.synthesize_research_findings(coordinator)

    # Create crew
    crew = Crew(
        agents=[data_analyst, theorist, detector_specialist, coordinator],
        tasks=[analysis_task, theory_task, detector_task, synthesis_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()

    print("\n\n########################")
    print("## Research Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_particle_physics_analysis()
