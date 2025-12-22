"""ADK Next.js Starter - CrewAI Multi-Agent Next.js Development System"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_architecture_planner, create_fullstack_developer, create_performance_optimizer
from tasks import create_architecture_planning_task, create_development_task, create_optimization_task


def load_environment():
    load_dotenv()
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found.")
        sys.exit(1)


def run_nextjs_development(app_requirements: dict, verbose: bool = True):
    if verbose:
        print("\nInitializing Next.js Development System\n")

    planner = create_architecture_planner()
    developer = create_fullstack_developer()
    optimizer = create_performance_optimizer()

    architecture_task = create_architecture_planning_task(planner, app_requirements)
    development_task = create_development_task(developer, architecture_task, app_requirements)
    optimization_task = create_optimization_task(optimizer, architecture_task, development_task)

    crew = Crew(
        agents=[planner, developer, optimizer],
        tasks=[architecture_task, development_task, optimization_task],
        process=Process.sequential,
        verbose=True
    )

    start_time = datetime.now()
    result = crew.kickoff()
    duration = (datetime.now() - start_time).total_seconds()

    return {'result': result, 'duration': duration, 'timestamp': datetime.now().isoformat()}


def main():
    load_environment()
    app_requirements = {'description': 'E-commerce platform with product catalog, shopping cart, and checkout'}
    result = run_nextjs_development(app_requirements, verbose=True)
    print(f"\n\nNEXT.JS DEVELOPMENT RESULTS\n{result['result']}")


if __name__ == "__main__":
    main()
