"""Software Bug Assistant Java CrewAI Tasks"""

from crewai import Task
from agents import java_bug_detective, java_analyzer, java_solution_architect, java_test_engineer, java_doc_specialist


def create_tasks(bug_report: str, java_code: str = ""):
    detect = Task(
        description=f"Analyze Java bug: {bug_report}\nCode: {java_code}",
        agent=java_bug_detective,
        expected_output="Java bug analysis with exception types and stack trace interpretation"
    )

    analyze = Task(
        description="Analyze Java code for root cause",
        agent=java_analyzer,
        expected_output="Java-specific root cause analysis",
        context=[detect]
    )

    solution = Task(
        description="Design Java solution with proper exception handling and patterns",
        agent=java_solution_architect,
        expected_output="Java code fix following best practices",
        context=[detect, analyze]
    )

    test = Task(
        description="Create JUnit test suite",
        agent=java_test_engineer,
        expected_output="JUnit 5 tests with Mockito",
        context=[solution]
    )

    doc = Task(
        description="Document with Javadoc standards",
        agent=java_doc_specialist,
        expected_output="Complete documentation with Javadoc",
        context=[detect, analyze, solution, test]
    )

    return [detect, analyze, solution, test, doc]
