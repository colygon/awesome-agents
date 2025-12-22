"""
CrewAI Agents for Documentation Generator
Specialized agents for creating comprehensive technical documentation
"""

from crewai import Agent
from crewai_tools import FileReadTool, CodeDocsSearchTool
import os


class DocumentationAgents:
    """Factory class for creating documentation generation agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def code_documenter(self) -> Agent:
        """Code Documentation Agent"""
        return Agent(
            role='Code Documentation Specialist',
            goal='Generate clear, comprehensive documentation from source code including docstrings, comments, and API references',
            backstory='You are a technical writer with deep programming knowledge, skilled at explaining complex code in clear, accessible language.',
            verbose=True,
            allow_delegation=False,
            tools=[FileReadTool()],
            llm='gpt-4o'
        )

    def api_documenter(self) -> Agent:
        """API Documentation Agent"""
        return Agent(
            role='API Documentation Specialist',
            goal='Create detailed API documentation including endpoints, parameters, responses, and examples',
            backstory='You excel at documenting APIs in formats like OpenAPI/Swagger with clear examples and use cases.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def tutorial_writer(self) -> Agent:
        """Tutorial and Guide Writer Agent"""
        return Agent(
            role='Technical Tutorial Writer',
            goal='Write beginner-friendly tutorials, guides, and how-to documentation',
            backstory='You are skilled at breaking down complex topics into step-by-step tutorials that help users get started quickly.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def readme_generator(self) -> Agent:
        """README Generator Agent"""
        return Agent(
            role='README Documentation Specialist',
            goal='Create comprehensive README files with installation, usage, and contribution guidelines',
            backstory='You create engaging, informative README files that help users understand and adopt projects quickly.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )
