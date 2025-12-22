#!/usr/bin/env python
from crewai import Crew, Process
from agents import DAForgeAgents
from tasks import DAForgeTasks
from dotenv import load_dotenv

load_dotenv()

def run_da_forge():
    print("## Welcome to DA-Forge Data Science Platform")
    print('-------------------------------')

    dataset_info = input("Enter dataset info or 'default': ")
    if dataset_info.lower() == 'default':
        dataset_info = "Customer dataset, 10K rows, 25 features"

    problem_type = input("Enter problem type or 'default': ")
    if problem_type.lower() == 'default':
        problem_type = "Customer churn prediction (classification)"

    agents = DAForgeAgents()
    tasks = DAForgeTasks()

    analyst = agents.data_analyst()
    ml_eng = agents.ml_engineer()
    viz_spec = agents.visualization_specialist()
    lead = agents.data_science_lead()

    analyze_task = tasks.analyze_data(analyst, dataset_info)
    model_task = tasks.build_ml_models(ml_eng, problem_type)
    viz_task = tasks.create_visualizations(viz_spec, "From analysis")
    solution_task = tasks.deliver_solution(lead)

    crew = Crew(
        agents=[analyst, ml_eng, viz_spec, lead],
        tasks=[analyze_task, model_task, viz_task, solution_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Data Science Solution Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_da_forge()
