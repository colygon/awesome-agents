"""
ADK No-Code Builder - CrewAI Agent Definitions
Multi-Agent No-Code Platform Development System

Agents for building no-code/low-code platforms:
1. Platform Architect - Designs no-code platform architecture
2. Builder Engine Developer - Implements drag-and-drop builders
3. Template Designer - Creates reusable templates and components
"""

from crewai import Agent
from textwrap import dedent


def create_platform_architect() -> Agent:
    return Agent(
        role="Platform Architect",
        goal="Design scalable no-code platform architecture",
        backstory=dedent("""
            You are a platform architect specialized in no-code/low-code systems with
            expertise in visual builders, workflow engines, and extensible architectures.
        """),
        verbose=True,
        allow_delegation=False,
        memory=True
    )


def create_builder_engine_developer() -> Agent:
    return Agent(
        role="Builder Engine Developer",
        goal="Implement drag-and-drop builder functionality",
        backstory=dedent("""
            You are an expert in building visual editors, drag-and-drop interfaces,
            and no-code builder engines with React, Vue, or similar frameworks.
        """),
        verbose=True,
        allow_delegation=False,
        memory=True
    )


def create_template_designer() -> Agent:
    return Agent(
        role="Template Designer",
        goal="Create reusable templates and component libraries",
        backstory=dedent("""
            You are a UX designer and developer specialized in creating beautiful,
            functional templates for no-code platforms.
        """),
        verbose=True,
        allow_delegation=False,
        memory=True
    )
