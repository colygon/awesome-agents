#!/usr/bin/env python
from crewai import Crew, Process
from agents import FitnessCoachAgents
from tasks import FitnessCoachTasks
from dotenv import load_dotenv

load_dotenv()

def run_fitness_coach():
    print("## Welcome to the Fitness Coach Crew")
    print("------------------------------------")

    goal = input("Fitness goal? (e.g., weight loss, muscle gain): ")
    level = input("Fitness level? (beginner/intermediate/advanced): ")
    equipment = input("Available equipment? (e.g., gym, home, bodyweight): ")

    user_profile = f"Goal: {goal}, Level: {level}, Equipment: {equipment}"

    agents = FitnessCoachAgents()
    tasks_manager = FitnessCoachTasks()

    trainer = agents.personal_trainer()
    nutrition_coach = agents.nutrition_coach()
    progress_tracker = agents.progress_tracker()
    motivator = agents.motivation_coach()

    workout_task = tasks_manager.create_workout_program(trainer, user_profile)
    nutrition_task = tasks_manager.design_nutrition_plan(nutrition_coach, goal)
    progress_task = tasks_manager.track_progress(progress_tracker, "Initial assessment")
    motivation_task = tasks_manager.create_motivation_plan(motivator, goal)

    crew = Crew(
        agents=[trainer, nutrition_coach, progress_tracker, motivator],
        tasks=[workout_task, nutrition_task, progress_task, motivation_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print("\n## Fitness Coach Results\n")
    print(result)
    return result

if __name__ == "__main__":
    run_fitness_coach()
