"""
CrewAI Agent Definitions - SDK Pattern Mapping

This module demonstrates how to map Claude Code Python Agent SDK patterns
to CrewAI agent architectures. Each function creates an agent that corresponds
to a specific SDK usage pattern.
"""

from crewai import Agent
from tools import (
    read_file,
    write_file,
    edit_file,
    bash_command,
    glob_files,
    grep_search
)


def create_query_agent():
    """
    Maps to SDK query() pattern - one-off task execution.

    SDK Equivalent:
    ```python
    async for message in query(
        prompt="Your task",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Bash"])
    ):
        print(message)
    ```

    Returns:
        Agent configured for single-task execution
    """
    return Agent(
        role="Task Executor",
        goal="Execute one-off tasks efficiently and accurately",
        backstory="""You are a helpful assistant that executes individual tasks.
        You are good at reading files, running commands, and providing results
        without needing ongoing conversation.""",
        tools=[read_file, bash_command, glob_files],
        verbose=True,
        allow_delegation=False
    )


def create_stateful_agent():
    """
    Maps to SDK ClaudeSDKClient pattern - conversational agent with memory.

    SDK Equivalent:
    ```python
    async with ClaudeSDKClient(options=options) as client:
        await client.query("First question")
        await client.query("Follow-up question")  # Remembers context
    ```

    Returns:
        Agent configured for stateful conversations
    """
    return Agent(
        role="Conversational Assistant",
        goal="Maintain context across multiple interactions and provide helpful assistance",
        backstory="""You are an expert assistant who remembers previous
        conversations and builds upon them. You understand context and can
        reference earlier interactions to provide more relevant help.""",
        tools=[read_file, write_file, edit_file, bash_command],
        verbose=True,
        allow_delegation=False,
        memory=True  # Enables context retention like SDK sessions
    )


def create_file_operations_agent():
    """
    Maps to SDK with file-specific tools (Read, Write, Edit).

    SDK Equivalent:
    ```python
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Edit"],
        permission_mode="acceptEdits"
    )
    ```

    Returns:
        Agent specialized in file operations
    """
    return Agent(
        role="File Operations Specialist",
        goal="Manage file reading, writing, and editing tasks",
        backstory="""You are an expert at file manipulation. You can read,
        analyze, create, and modify files with precision. You always
        validate your changes and provide clear summaries of what you did.""",
        tools=[read_file, write_file, edit_file, glob_files],
        verbose=True,
        allow_delegation=False
    )


def create_code_analyst_agent():
    """
    Maps to SDK with code analysis tools (Read, Glob, Grep).

    SDK Equivalent:
    ```python
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Glob", "Grep"],
        system_prompt="You are an expert code analyst"
    )
    ```

    Returns:
        Agent specialized in code analysis
    """
    return Agent(
        role="Code Analyst",
        goal="Analyze code structure, patterns, and quality",
        backstory="""You are a senior software engineer specializing in code
        analysis. You can quickly find patterns, identify issues, and provide
        insights about code structure and quality. You use grep and glob to
        efficiently search codebases.""",
        tools=[read_file, glob_files, grep_search],
        verbose=True,
        allow_delegation=False
    )


def create_delegating_agent():
    """
    Maps to SDK hierarchical pattern with subagents.

    SDK Equivalent:
    ```python
    options = ClaudeAgentOptions(
        agents={
            "code-reviewer": AgentDefinition(
                description="Reviews code",
                tools=["Read", "Grep"]
            )
        },
        allowed_tools=["Task"]  # Can delegate to subagents
    )
    ```

    Returns:
        Agent that can delegate to other specialized agents
    """
    return Agent(
        role="Development Lead",
        goal="Coordinate and delegate tasks to specialized team members",
        backstory="""You are an experienced development lead who knows when
        to delegate tasks to specialists. You coordinate work across multiple
        areas and ensure quality outcomes by leveraging your team's expertise.""",
        tools=[read_file, glob_files],  # Limited tools, relies on delegation
        verbose=True,
        allow_delegation=True  # Key difference: can delegate to other agents
    )


def create_specialist_agent(specialization: str):
    """
    Creates a specialist agent for delegation scenarios.

    This demonstrates how SDK subagents map to CrewAI specialist agents
    that work alongside a delegating agent.

    Args:
        specialization: Type of specialist ("reviewer", "tester", "documenter")

    Returns:
        Specialized agent for specific tasks
    """
    specializations = {
        "reviewer": {
            "role": "Code Reviewer",
            "goal": "Review code for quality, security, and best practices",
            "backstory": """You are a meticulous code reviewer with expertise
            in security, performance, and maintainability. You catch bugs and
            suggest improvements.""",
            "tools": [read_file, grep_search]
        },
        "tester": {
            "role": "Quality Assurance Engineer",
            "goal": "Test code and ensure quality standards",
            "backstory": """You are a QA engineer who writes and runs tests.
            You ensure code works correctly and meets requirements.""",
            "tools": [read_file, bash_command]
        },
        "documenter": {
            "role": "Technical Writer",
            "goal": "Create clear, comprehensive documentation",
            "backstory": """You are a technical writer who creates excellent
            documentation. You explain complex concepts clearly and maintain
            up-to-date documentation.""",
            "tools": [read_file, write_file]
        }
    }

    config = specializations.get(specialization, specializations["reviewer"])

    return Agent(
        role=config["role"],
        goal=config["goal"],
        backstory=config["backstory"],
        tools=config["tools"],
        verbose=True,
        allow_delegation=False
    )


# Agent factory for easy creation
class AgentFactory:
    """
    Factory class for creating agents based on SDK patterns.

    This provides a clean interface for instantiating agents that match
    specific SDK usage patterns.
    """

    @staticmethod
    def from_sdk_pattern(pattern: str) -> Agent:
        """
        Create an agent matching a specific SDK pattern.

        Args:
            pattern: SDK pattern name
                - "query": One-off query() execution
                - "client": ClaudeSDKClient stateful conversation
                - "file_ops": File operations specialist
                - "code_analyst": Code analysis specialist
                - "delegating": Hierarchical delegation
                - "specialist_{type}": Specialist for delegation

        Returns:
            Configured CrewAI agent

        Example:
            agent = AgentFactory.from_sdk_pattern("query")
        """
        pattern_map = {
            "query": create_query_agent,
            "client": create_stateful_agent,
            "file_ops": create_file_operations_agent,
            "code_analyst": create_code_analyst_agent,
            "delegating": create_delegating_agent,
        }

        # Handle specialist agents
        if pattern.startswith("specialist_"):
            spec_type = pattern.split("_", 1)[1]
            return create_specialist_agent(spec_type)

        creator = pattern_map.get(pattern)
        if not creator:
            raise ValueError(
                f"Unknown pattern: {pattern}. "
                f"Valid patterns: {', '.join(pattern_map.keys())}, specialist_*"
            )

        return creator()


# Convenience exports
__all__ = [
    'create_query_agent',
    'create_stateful_agent',
    'create_file_operations_agent',
    'create_code_analyst_agent',
    'create_delegating_agent',
    'create_specialist_agent',
    'AgentFactory'
]
