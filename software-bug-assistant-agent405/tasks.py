"""
Software Bug Assistant CrewAI Tasks
"""

from crewai import Task
from agents import bug_detective, code_analyzer, solution_architect, test_engineer, documentation_specialist


def create_tasks(bug_report: str, code_context: str = ""):
    """Create tasks for bug analysis and resolution workflow"""

    detect_task = Task(
        description=f"""Analyze the bug report and detect the issue.

        Bug Report: {bug_report}
        Code Context: {code_context if code_context else 'Not provided'}

        Identify:
        1. Bug type and severity
        2. Error messages and stack traces
        3. Reproduction steps
        4. Affected components
        5. Impact assessment""",
        agent=bug_detective,
        expected_output="Detailed bug analysis with type, severity, and affected components"
    )

    analyze_task = Task(
        description="""Perform code analysis to understand the bug's root cause.

        Analyze:
        1. Code flow and logic
        2. Dependencies and integrations
        3. Potential root causes
        4. Related code areas""",
        agent=code_analyzer,
        expected_output="Root cause analysis with code-level insights",
        context=[detect_task]
    )

    solution_task = Task(
        description="""Design and propose bug fix solutions.

        Provide:
        1. Recommended solution approach
        2. Code changes needed
        3. Alternative approaches
        4. Trade-offs and considerations""",
        agent=solution_architect,
        expected_output="Comprehensive fix proposal with code examples",
        context=[detect_task, analyze_task]
    )

    test_task = Task(
        description="""Create test cases to verify the fix.

        Design:
        1. Unit tests for the fix
        2. Regression tests
        3. Edge case tests
        4. Integration tests if needed""",
        agent=test_engineer,
        expected_output="Complete test suite with test code",
        context=[solution_task]
    )

    doc_task = Task(
        description="""Document the bug and its resolution.

        Create:
        1. Bug report summary
        2. Root cause explanation
        3. Solution documentation
        4. Testing verification
        5. Prevention recommendations""",
        agent=documentation_specialist,
        expected_output="Comprehensive bug resolution documentation",
        context=[detect_task, analyze_task, solution_task, test_task]
    )

    return [detect_task, analyze_task, solution_task, test_task, doc_task]
