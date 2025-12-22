"""ADK No-Code Builder - CrewAI Task Definitions"""

from crewai import Task
from textwrap import dedent


def create_platform_architecture_task(agent, platform_requirements: dict) -> Task:
    return Task(
        description=dedent(f"""
            Design no-code platform architecture for: {platform_requirements.get('description', '')}
            Include: component system, workflow engine, data models, user management.
        """),
        expected_output="Platform architecture document with system design and component specifications.",
        agent=agent
    )


def create_builder_development_task(agent, architecture_output) -> Task:
    return Task(
        description=f"Implement drag-and-drop builder based on: {architecture_output}",
        expected_output="Complete builder implementation with drag-and-drop functionality.",
        agent=agent,
        context=[architecture_output] if isinstance(architecture_output, Task) else []
    )


def create_template_design_task(agent, architecture_output, builder_output) -> Task:
    return Task(
        description=f"Create template library for platform. Architecture: {architecture_output}, Builder: {builder_output}",
        expected_output="Template library with reusable components and starter templates.",
        agent=agent,
        context=[architecture_output, builder_output] if isinstance(architecture_output, Task) else []
    )
