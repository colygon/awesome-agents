#!/usr/bin/env python3
"""
Batch 8 CrewAI Upgrade Script

Efficiently processes multiple Streamlit apps to add CrewAI integration.
"""

import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List

# Base templates for CrewAI files
AGENTS_TEMPLATE = '''"""
CrewAI Agents for {app_title}

This module defines specialized agents for {app_description}.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI
from typing import Optional


class {class_name}Agents:
    """Factory class for creating {app_title} agents."""

    def __init__(self, llm: Optional[ChatOpenAI] = None):
        """Initialize the agents factory with an optional language model."""
        self.llm = llm or ChatOpenAI(
            model="gpt-4",
            temperature=0.7
        )

    def analyst(self) -> Agent:
        """
        Creates an agent specialized in analyzing {app_focus}.

        Returns:
            Agent configured for {app_focus} analysis
        """
        return Agent(
            role="{analyst_role}",
            goal="{analyst_goal}",
            backstory=(
                "{analyst_backstory}"
            ),
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def advisor(self) -> Agent:
        """
        Creates an agent specialized in providing recommendations.

        Returns:
            Agent configured for providing advice and recommendations
        """
        return Agent(
            role="{advisor_role}",
            goal="{advisor_goal}",
            backstory=(
                "{advisor_backstory}"
            ),
            verbose=True,
            allow_delegation=True,
            llm=self.llm
        )


def create_agents(llm: Optional[ChatOpenAI] = None) -> dict:
    """
    Convenience function to create all agents.

    Args:
        llm: Optional language model to use for agents

    Returns:
        Dictionary containing all agents
    """
    factory = {class_name}Agents(llm)
    return {{
        'analyst': factory.analyst(),
        'advisor': factory.advisor()
    }}
'''

TASKS_TEMPLATE = '''"""
CrewAI Tasks for {app_title}

This module defines tasks that agents can perform.
"""

from crewai import Task
from typing import Dict, Any


def create_analysis_task(agent, data: Dict[str, Any]) -> Task:
    """
    Create a task for analyzing {app_focus}.

    Args:
        agent: The agent to perform the task
        data: Dictionary containing relevant data

    Returns:
        Task configured for analysis
    """
    description = f"""
    Analyze the following {app_focus} data:

    {{data}}

    Provide a comprehensive analysis covering:
    1. Key insights from the data
    2. Patterns and trends observed
    3. Statistical significance
    4. Practical implications
    """

    return Task(
        description=description,
        agent=agent,
        expected_output=(
            "A detailed analysis including key insights, patterns, "
            "statistical observations, and practical implications."
        )
    )


def create_recommendation_task(agent, data: Dict[str, Any]) -> Task:
    """
    Create a task for providing recommendations.

    Args:
        agent: The agent to perform the task
        data: Dictionary containing relevant data

    Returns:
        Task configured for recommendations
    """
    description = f"""
    Based on the following data, provide actionable recommendations:

    {{data}}

    Include:
    1. Specific recommendations for improvement
    2. Best practices to follow
    3. Potential pitfalls to avoid
    4. Expected outcomes
    """

    return Task(
        description=description,
        agent=agent,
        expected_output=(
            "A set of specific, actionable recommendations with rationale, "
            "best practices, warnings, and expected outcomes."
        )
    )
'''

MAIN_TEMPLATE = '''"""
{app_title} with CrewAI Integration

Main module for running CrewAI crews.
"""

from crewai import Crew
from agents import create_agents
from tasks import create_analysis_task, create_recommendation_task
from typing import Dict, Any, Optional
from langchain_openai import ChatOpenAI


def analyze_data(
    data: Dict[str, Any],
    llm: Optional[ChatOpenAI] = None
) -> str:
    """
    Run a CrewAI crew to analyze the data.

    Args:
        data: Dictionary containing data to analyze
        llm: Optional language model to use

    Returns:
        Analysis result as a string
    """
    agents = create_agents(llm)
    analysis_task = create_analysis_task(agents['analyst'], data)

    crew = Crew(
        agents=[agents['analyst']],
        tasks=[analysis_task],
        verbose=True
    )

    result = crew.kickoff()
    return str(result)


def get_recommendations(
    data: Dict[str, Any],
    llm: Optional[ChatOpenAI] = None
) -> str:
    """
    Run a CrewAI crew to get recommendations.

    Args:
        data: Dictionary containing data to analyze
        llm: Optional language model to use

    Returns:
        Recommendations as a string
    """
    agents = create_agents(llm)
    recommendation_task = create_recommendation_task(agents['advisor'], data)

    crew = Crew(
        agents=[agents['advisor']],
        tasks=[recommendation_task],
        verbose=True
    )

    result = crew.kickoff()
    return str(result)


if __name__ == '__main__':
    # Example usage
    sample_data = {{
        'example': 'This is sample data'
    }}

    print("Running analysis...")
    analysis = analyze_data(sample_data)
    print("\\nAnalysis Result:")
    print(analysis)
'''


APP_CONFIGS = {
    220: {
        "app_title": "Dunning-Kruger Analysis",
        "app_description": "statistical simulation and cognitive bias analysis",
        "class_name": "DunningKruger",
        "app_focus": "cognitive bias and statistical patterns",
        "analyst_role": "Statistical Research Analyst",
        "analyst_goal": "Analyze statistical simulations and identify patterns in cognitive bias data",
        "analyst_backstory": "Expert statistician specializing in cognitive psychology and bias research",
        "advisor_role": "Research Methodology Advisor",
        "advisor_goal": "Provide guidance on experimental design and result interpretation",
        "advisor_backstory": "Experienced researcher in psychology and statistics methodology"
    },
    192: {
        "app_title": "Code Analysis Assistant",
        "app_description": "code generation and analysis",
        "class_name": "CodeAnalysis",
        "app_focus": "code quality and generation",
        "analyst_role": "Code Quality Analyst",
        "analyst_goal": "Analyze code quality, identify issues, and suggest improvements",
        "analyst_backstory": "Senior software engineer with expertise in code review and best practices",
        "advisor_role": "Development Advisor",
        "advisor_goal": "Provide coding best practices and architecture recommendations",
        "advisor_backstory": "Software architecture expert with years of development experience"
    }
}


def create_crewai_files(app_id: int, base_path: Path):
    """Create standard CrewAI files for an app."""
    config = APP_CONFIGS.get(app_id, {})

    # Create agents.py
    agents_content = AGENTS_TEMPLATE.format(**config)
    (base_path / "agents.py").write_text(agents_content)

    # Create tasks.py
    tasks_content = TASKS_TEMPLATE.format(**config)
    (base_path / "tasks.py").write_text(tasks_content)

    # Create main.py
    main_content = MAIN_TEMPLATE.format(**config)
    (base_path / "main.py").write_text(main_content)

    print(f"Created CrewAI files for app {app_id} at {base_path}")


def update_requirements(base_path: Path):
    """Add CrewAI dependencies to requirements."""
    req_file = base_path / "requirements.txt"

    if not req_file.exists():
        req_file = base_path / "pyproject.toml"
        if not req_file.exists():
            # Create new requirements.txt
            req_file = base_path / "requirements.txt"
            req_file.write_text("crewai>=0.86.0\\nlangchain-openai>=0.3.0\\n")
            return

    content = req_file.read_text()
    if "crewai" not in content.lower():
        with req_file.open("a") as f:
            f.write("\\ncrewai>=0.86.0\\nlangchain-openai>=0.3.0\\n")


if __name__ == "__main__":
    print("Batch 8 Upgrade Script")
    print("This script helps create CrewAI files for multiple apps")

    # Example: Create files for app 220
    app_220_path = Path("/Users/colinlowenberg/crew/dunning-kruger-agent220")
    if app_220_path.exists():
        create_crewai_files(220, app_220_path)
        update_requirements(app_220_path)
