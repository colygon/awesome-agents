"""
CrewAI Task Definitions - SDK Pattern Mapping

This module shows how to create tasks that correspond to SDK query patterns.
"""

from crewai import Task
from typing import List, Optional


def create_one_off_task(agent, description: str, expected_output: str) -> Task:
    """
    Creates a task matching SDK query() pattern.

    SDK Equivalent:
    ```python
    result = await query(
        prompt="Your task description",
        options=ClaudeAgentOptions(...)
    )
    ```

    Args:
        agent: The agent to execute this task
        description: Task description (maps to SDK prompt)
        expected_output: What the task should produce

    Returns:
        Task configured for one-off execution
    """
    return Task(
        description=description,
        agent=agent,
        expected_output=expected_output
    )


def create_conversational_task_sequence(
    agent,
    task_descriptions: List[tuple[str, str]]
) -> List[Task]:
    """
    Creates a sequence of tasks with context, matching SDK ClaudeSDKClient pattern.

    SDK Equivalent:
    ```python
    async with ClaudeSDKClient(options) as client:
        await client.query("First task")
        await client.query("Second task")  # Has context from first
    ```

    Args:
        agent: The stateful agent (should have memory=True)
        task_descriptions: List of (description, expected_output) tuples

    Returns:
        List of tasks where later tasks have context from earlier ones
    """
    tasks = []

    for i, (description, expected_output) in enumerate(task_descriptions):
        task = Task(
            description=description,
            agent=agent,
            expected_output=expected_output,
            context=tasks.copy()  # Each task has context from previous ones
        )
        tasks.append(task)

    return tasks


def create_file_analysis_task(agent, file_path: str) -> Task:
    """
    Creates a task for file analysis.

    SDK Equivalent:
    ```python
    await query(
        prompt=f"Analyze {file_path}",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Grep"])
    )
    ```

    Args:
        agent: Agent with file reading capabilities
        file_path: Path to file to analyze

    Returns:
        Task for analyzing the specified file
    """
    return Task(
        description=f"""Analyze the file at {file_path}.

        Your analysis should include:
        1. File size and structure
        2. Key patterns or issues found
        3. Summary of contents
        4. Recommendations for improvements (if applicable)

        Use the read_file and grep_search tools as needed.""",
        agent=agent,
        expected_output=f"Comprehensive analysis of {file_path} with insights and recommendations"
    )


def create_code_search_task(agent, pattern: str, file_type: str = "*.py") -> Task:
    """
    Creates a task for searching code.

    SDK Equivalent:
    ```python
    await query(
        prompt=f"Search for {pattern} in {file_type}",
        options=ClaudeAgentOptions(allowed_tools=["Glob", "Grep"])
    )
    ```

    Args:
        agent: Agent with search capabilities
        pattern: Regex pattern to search for
        file_type: File glob pattern (default: *.py)

    Returns:
        Task for searching code
    """
    return Task(
        description=f"""Search for pattern '{pattern}' in {file_type} files.

        Steps:
        1. Use glob_files to find all {file_type} files
        2. Use grep_search to find occurrences of '{pattern}'
        3. Analyze the results and identify patterns
        4. Provide summary of findings

        Report the locations and context of all matches.""",
        agent=agent,
        expected_output=f"Search results for '{pattern}' with analysis and locations"
    )


def create_hierarchical_task(
    manager_agent,
    specialist_agent,
    task_description: str,
    expected_output: str
) -> Task:
    """
    Creates a task for hierarchical delegation.

    SDK Equivalent:
    ```python
    options = ClaudeAgentOptions(
        agents={"specialist": AgentDefinition(...)},
        allowed_tools=["Task"]
    )
    await query("Delegate this to specialist", options)
    ```

    Args:
        manager_agent: Agent that delegates (allow_delegation=True)
        specialist_agent: Agent that performs the work
        task_description: What needs to be done
        expected_output: Expected result

    Returns:
        Task configured for delegation
    """
    # Note: In CrewAI, you set up the crew with hierarchical process
    # and the manager automatically delegates. This task represents
    # the high-level goal that will be broken down.
    return Task(
        description=task_description,
        agent=manager_agent,  # Manager will delegate to specialists
        expected_output=expected_output
    )


def create_parallel_tasks(
    agents: List,
    task_configs: List[tuple[str, str]]
) -> List[Task]:
    """
    Creates tasks that can run in parallel.

    SDK Equivalent:
    Multiple SDK calls could be made concurrently, but SDK is primarily sequential.
    CrewAI allows true parallel execution.

    Args:
        agents: List of agents (one per task)
        task_configs: List of (description, expected_output) tuples

    Returns:
        List of tasks configured for parallel execution
    """
    tasks = []

    for agent, (description, expected_output) in zip(agents, task_configs):
        task = Task(
            description=description,
            agent=agent,
            expected_output=expected_output,
            async_execution=True  # Enables parallel execution
        )
        tasks.append(task)

    return tasks


# Task builder for complex scenarios
class TaskBuilder:
    """
    Builder class for constructing task workflows that match SDK patterns.
    """

    def __init__(self):
        self.tasks = []

    def add_one_off(self, agent, description: str, expected_output: str):
        """Add a one-off task (query pattern)."""
        task = create_one_off_task(agent, description, expected_output)
        self.tasks.append(task)
        return self

    def add_conversational_sequence(
        self,
        agent,
        task_descriptions: List[tuple[str, str]]
    ):
        """Add a conversational sequence (ClaudeSDKClient pattern)."""
        tasks = create_conversational_task_sequence(agent, task_descriptions)
        self.tasks.extend(tasks)
        return self

    def add_file_analysis(self, agent, file_path: str):
        """Add a file analysis task."""
        task = create_file_analysis_task(agent, file_path)
        self.tasks.append(task)
        return self

    def add_code_search(self, agent, pattern: str, file_type: str = "*.py"):
        """Add a code search task."""
        task = create_code_search_task(agent, pattern, file_type)
        self.tasks.append(task)
        return self

    def build(self) -> List[Task]:
        """Return the built task list."""
        return self.tasks


# Convenience exports
__all__ = [
    'create_one_off_task',
    'create_conversational_task_sequence',
    'create_file_analysis_task',
    'create_code_search_task',
    'create_hierarchical_task',
    'create_parallel_tasks',
    'TaskBuilder'
]
