"""Documentation Generator - CrewAI Implementation"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import DocumentationAgents
from tasks import DocumentationTasks

load_dotenv()


def generate_documentation(source_files: list, project_info: dict, api_spec: dict = None) -> str:
    """Generate comprehensive project documentation"""

    agents = DocumentationAgents()
    tasks_factory = DocumentationTasks()

    code_documenter = agents.code_documenter()
    api_documenter = agents.api_documenter()
    tutorial_writer = agents.tutorial_writer()
    readme_generator = agents.readme_generator()

    code_doc_task = tasks_factory.document_code(code_documenter, source_files, project_info.get('language', 'Python'))
    readme_task = tasks_factory.generate_readme(readme_generator, project_info)
    tutorial_task = tasks_factory.create_tutorial(tutorial_writer, project_info)
    tutorial_task.context = [code_doc_task, readme_task]

    tasks = [code_doc_task, readme_task, tutorial_task]

    if api_spec:
        api_doc_task = tasks_factory.document_api(api_documenter, api_spec)
        tasks.append(api_doc_task)

    crew = Crew(
        agents=[code_documenter, readme_generator, tutorial_writer, api_documenter],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


def main():
    project_info = {'name': 'MyProject', 'description': 'A cool project', 'language': 'Python'}
    result = generate_documentation(['main.py', 'utils.py'], project_info)
    print(result)


if __name__ == "__main__":
    main()
