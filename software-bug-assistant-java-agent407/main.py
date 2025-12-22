#!/usr/bin/env python
"""Software Bug Assistant Java - CrewAI Main Application"""

import sys
from crewai import Crew, Process
from agents import java_bug_detective, java_analyzer, java_solution_architect, java_test_engineer, java_doc_specialist
from tasks import create_tasks


def main():
    print("Software Bug Assistant (Java) - CrewAI Edition\n")
    bug = input("Describe the Java bug: ") if len(sys.argv) == 1 else sys.argv[1]
    code = input("Java code context (optional): ") if len(sys.argv) <= 2 else sys.argv[2] if len(sys.argv) > 2 else ""

    tasks = create_tasks(bug, code)
    crew = Crew(
        agents=[java_bug_detective, java_analyzer, java_solution_architect, java_test_engineer, java_doc_specialist],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print(f"\n{'='*80}\nANALYSIS COMPLETE\n{'='*80}\n{result}")


if __name__ == "__main__":
    main()
