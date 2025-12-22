#!/usr/bin/env python
from crewai import Crew, Process
from agents import LucillaGameStudioAgents
from tasks import LucillaGameStudioTasks
from dotenv import load_dotenv

load_dotenv()

def run_game_studio():
    """
    Run AI-powered game development workflow
    """
    print("## Welcome to Lucilla AI Game Studio")
    print('-------------------------------')

    # Get user input
    game_idea = input("Enter your game idea or 'default' for sample: ")
    if game_idea.lower() == 'default':
        game_idea = "Fantasy action RPG with procedural content and dynamic AI NPCs"

    # Initialize agents and tasks
    agents = LucillaGameStudioAgents()
    tasks = LucillaGameStudioTasks()

    # Create agents
    designer = agents.game_designer()
    content_gen = agents.procedural_content_generator()
    npc_specialist = agents.npc_ai_specialist()
    director = agents.game_director()

    # Create tasks
    design_task = tasks.design_game_concept(designer, game_idea)
    content_task = tasks.generate_game_content(content_gen, "From design task")
    npc_task = tasks.create_npc_ai_system(npc_specialist, "From design task")
    finalize_task = tasks.finalize_game_design(director)

    # Create crew
    crew = Crew(
        agents=[designer, content_gen, npc_specialist, director],
        tasks=[design_task, content_task, npc_task, finalize_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()

    print("\n\n########################")
    print("## Game Design Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_game_studio()
