"""
Enhanced Multi-Agent System - Claude Code Agent CrewAI Implementation
Demonstrates advanced multi-agent collaboration beyond basic SDK patterns.
"""

from crewai import Agent
from tools import (
    read_file, write_file, edit_file, bash_command,
    glob_files, grep_search, share_knowledge, analyze_code_quality
)


def create_code_architect() -> Agent:
    """
    Code Architect - System design and delegation specialist.
    Maps to: SDK hierarchical agent pattern with delegation capabilities.

    Role: High-level design and task delegation
    Capabilities: System architecture, design decisions, team coordination
    Enhanced Feature: Can delegate to specialist agents
    """
    return Agent(
        role="Code Architect",
        goal="Design system architecture and coordinate development team",
        backstory="""You are a senior software architect with 15+ years of experience.
        You excel at breaking down complex problems into manageable components,
        making architectural decisions, and delegating tasks to specialist team members.
        You understand design patterns, system scalability, and best practices across
        multiple programming languages and frameworks.""",
        tools=[read_file, glob_files, grep_search, share_knowledge],
        verbose=True,
        allow_delegation=True,  # Key CrewAI feature: enables delegation to other agents
        max_iter=15
    )


def create_senior_developer() -> Agent:
    """
    Senior Developer - Feature implementation specialist.
    Maps to: SDK agent with full file manipulation tools.

    Role: Code implementation and feature development
    Capabilities: Writing code, refactoring, implementing features
    """
    return Agent(
        role="Senior Developer",
        goal="Implement features efficiently with clean, maintainable code",
        backstory="""You are an expert software developer with deep knowledge of
        Python, JavaScript, and modern development practices. You write clean,
        efficient code following SOLID principles and best practices. You're skilled
        at implementing complex features while maintaining code quality and readability.""",
        tools=[read_file, write_file, edit_file, glob_files, grep_search, bash_command],
        verbose=True,
        allow_delegation=False,
        max_iter=25
    )


def create_code_reviewer() -> Agent:
    """
    Code Reviewer - Security and quality assurance specialist.
    Maps to: SDK agent with read/analysis tools.

    Role: Code review, security analysis, quality checks
    Capabilities: Finding bugs, security vulnerabilities, code smells
    """
    return Agent(
        role="Code Reviewer",
        goal="Ensure code quality, security, and adherence to best practices",
        backstory="""You are a security-conscious code reviewer with expertise in
        identifying vulnerabilities, code smells, and potential bugs. You're familiar
        with OWASP top 10, common security pitfalls, and code quality metrics. You
        provide constructive feedback and actionable recommendations for improvement.""",
        tools=[read_file, glob_files, grep_search, analyze_code_quality, share_knowledge],
        verbose=True,
        allow_delegation=False,
        max_iter=15
    )


def create_qa_engineer() -> Agent:
    """
    QA Engineer - Testing and validation specialist.
    Maps to: SDK agent with execution tools.

    Role: Test creation, execution, and validation
    Capabilities: Writing tests, running test suites, validating functionality
    """
    return Agent(
        role="QA Engineer",
        goal="Ensure code reliability through comprehensive testing",
        backstory="""You are a meticulous QA engineer who believes in test-driven
        development and comprehensive test coverage. You write unit tests, integration
        tests, and end-to-end tests. You're skilled at identifying edge cases and
        ensuring code behaves correctly in all scenarios.""",
        tools=[read_file, write_file, bash_command, glob_files, grep_search],
        verbose=True,
        allow_delegation=False,
        max_iter=20
    )


def create_technical_writer() -> Agent:
    """
    Technical Writer - Documentation specialist.
    Maps to: SDK agent with file operations.

    Role: Documentation creation and maintenance
    Capabilities: Writing clear docs, README files, API documentation
    """
    return Agent(
        role="Technical Writer",
        goal="Create clear, comprehensive documentation for developers and users",
        backstory="""You are a skilled technical writer who excels at making complex
        technical concepts accessible. You write clear README files, API documentation,
        and user guides. You understand that good documentation is essential for project
        success and developer productivity.""",
        tools=[read_file, write_file, edit_file, glob_files, grep_search],
        verbose=True,
        allow_delegation=False,
        max_iter=15
    )


def create_devops_engineer() -> Agent:
    """
    DevOps Engineer - Deployment and infrastructure specialist.
    Maps to: SDK agent with bash/execution tools.

    Role: CI/CD, deployment, infrastructure management
    Capabilities: Build processes, deployment automation, infrastructure
    """
    return Agent(
        role="DevOps Engineer",
        goal="Automate deployment and ensure reliable infrastructure",
        backstory="""You are a DevOps expert skilled in CI/CD pipelines, containerization,
        and cloud infrastructure. You automate repetitive tasks, ensure smooth deployments,
        and maintain system reliability. You're proficient with Docker, Git workflows,
        and deployment automation.""",
        tools=[bash_command, read_file, write_file, glob_files, grep_search],
        verbose=True,
        allow_delegation=False,
        max_iter=15
    )


def create_research_analyst() -> Agent:
    """
    Research Analyst - Code analysis and pattern research specialist.
    Enhanced agent for deep codebase analysis.

    Role: Pattern detection, dependency analysis, codebase understanding
    Capabilities: Analyzing code structure, identifying patterns, research
    """
    return Agent(
        role="Research Analyst",
        goal="Analyze codebases and identify patterns, dependencies, and insights",
        backstory="""You are a research analyst specialized in code archaeology and
        pattern detection. You excel at understanding unfamiliar codebases, tracing
        dependencies, and identifying architectural patterns. You provide insights
        that help teams make informed decisions about refactoring and improvements.""",
        tools=[read_file, glob_files, grep_search, analyze_code_quality, share_knowledge],
        verbose=True,
        allow_delegation=False,
        max_iter=20
    )


class EnhancedAgentFactory:
    """
    Factory for creating specialized agents in different configurations.
    Demonstrates CrewAI's flexibility in agent composition.
    """

    @staticmethod
    def create_by_role(role: str) -> Agent:
        """
        Create an agent by role name.

        Args:
            role: One of: architect, developer, reviewer, qa, writer, devops, analyst

        Returns:
            Configured Agent instance

        Example:
            agent = EnhancedAgentFactory.create_by_role('architect')
        """
        role_map = {
            'architect': create_code_architect,
            'developer': create_senior_developer,
            'reviewer': create_code_reviewer,
            'qa': create_qa_engineer,
            'writer': create_technical_writer,
            'devops': create_devops_engineer,
            'analyst': create_research_analyst
        }

        if role not in role_map:
            raise ValueError(f"Unknown role: {role}. Valid roles: {list(role_map.keys())}")

        return role_map[role]()

    @staticmethod
    def create_development_team() -> list[Agent]:
        """
        Create a complete development team.

        Returns:
            List of agents representing a full development team

        Example:
            team = EnhancedAgentFactory.create_development_team()
            crew = Crew(agents=team, tasks=tasks, process=Process.hierarchical)
        """
        return [
            create_code_architect(),
            create_senior_developer(),
            create_code_reviewer(),
            create_qa_engineer(),
            create_technical_writer(),
            create_devops_engineer()
        ]

    @staticmethod
    def create_code_review_team() -> list[Agent]:
        """
        Create a specialized code review team.

        Returns:
            List of agents for code review workflow
        """
        return [
            create_code_reviewer(),
            create_qa_engineer(),
            create_senior_developer()
        ]

    @staticmethod
    def create_research_team() -> list[Agent]:
        """
        Create a research and analysis team.

        Returns:
            List of agents for research and analysis tasks
        """
        return [
            create_research_analyst(),
            create_code_architect(),
            create_technical_writer()
        ]


# Convenience functions for quick agent creation
def get_full_team() -> list[Agent]:
    """Get all 7 specialized agents."""
    return [
        create_code_architect(),
        create_senior_developer(),
        create_code_reviewer(),
        create_qa_engineer(),
        create_technical_writer(),
        create_devops_engineer(),
        create_research_analyst()
    ]


def get_minimal_team() -> list[Agent]:
    """Get a minimal team (architect + developer + reviewer)."""
    return [
        create_code_architect(),
        create_senior_developer(),
        create_code_reviewer()
    ]


# Export all agent creators
__all__ = [
    'create_code_architect',
    'create_senior_developer',
    'create_code_reviewer',
    'create_qa_engineer',
    'create_technical_writer',
    'create_devops_engineer',
    'create_research_analyst',
    'EnhancedAgentFactory',
    'get_full_team',
    'get_minimal_team'
]
