"""ADK No-Code Builder - CrewAI Multi-Agent System"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_platform_architect, create_builder_engine_developer, create_template_designer
from tasks import create_platform_architecture_task, create_builder_development_task, create_template_design_task


def load_environment():
    load_dotenv()
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found.")
        sys.exit(1)


def run_nocode_platform_development(platform_requirements: dict, verbose: bool = True):
    architect = create_platform_architect()
    developer = create_builder_engine_developer()
    designer = create_template_designer()

    architecture_task = create_platform_architecture_task(architect, platform_requirements)
    development_task = create_builder_development_task(developer, architecture_task)
    template_task = create_template_design_task(designer, architecture_task, development_task)

    crew = Crew(
        agents=[architect, developer, designer],
        tasks=[architecture_task, development_task, template_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return {'result': result, 'timestamp': datetime.now().isoformat()}


def main():
    load_environment()
    requirements = {'description': 'Website builder for small businesses'}
    result = run_nocode_platform_development(requirements)
    print(f"\n\nRESULTS\n{result['result']}")


if __name__ == "__main__":
    main()
