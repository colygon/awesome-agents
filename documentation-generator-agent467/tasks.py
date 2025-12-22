"""CrewAI Tasks for Documentation Generator"""

from crewai import Task
from textwrap import dedent


class DocumentationTasks:
    """Factory class for documentation generation tasks"""

    def document_code(self, agent, source_files: list, language: str) -> Task:
        return Task(
            description=dedent(f"""
                Generate code documentation:
                Files: {source_files}
                Language: {language}

                Create:
                1. Function/method docstrings
                2. Class documentation
                3. Module-level documentation
                4. Parameter descriptions
                5. Return value documentation
                6. Usage examples
            """),
            agent=agent,
            expected_output='Complete code documentation with docstrings and examples'
        )

    def document_api(self, agent, api_spec: dict) -> Task:
        return Task(
            description=dedent(f"""
                Generate API documentation:
                API Spec: {api_spec}

                Document:
                1. Endpoint descriptions
                2. Request/response schemas
                3. Authentication methods
                4. Error codes and messages
                5. Rate limiting
                6. Code examples in multiple languages
            """),
            agent=agent,
            expected_output='Comprehensive API documentation with examples',
            context=[]
        )

    def create_tutorial(self, agent, project_info: dict) -> Task:
        return Task(
            description=dedent(f"""
                Create getting started tutorial:
                Project: {project_info}

                Tutorial sections:
                1. Introduction and overview
                2. Prerequisites
                3. Installation steps
                4. Basic usage examples
                5. Common use cases
                6. Troubleshooting
                7. Next steps
            """),
            agent=agent,
            expected_output='Step-by-step tutorial for beginners',
            context=[]
        )

    def generate_readme(self, agent, project_info: dict) -> Task:
        return Task(
            description=dedent(f"""
                Generate README.md:
                Project: {project_info}

                Include:
                1. Project title and description
                2. Features and benefits
                3. Installation instructions
                4. Quick start guide
                5. Usage examples
                6. Configuration options
                7. Contributing guidelines
                8. License information
                9. Contact and support
            """),
            agent=agent,
            expected_output='Complete README.md file',
            context=[]
        )
