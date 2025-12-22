#!/usr/bin/env python
"""Software Bug Assistant CrewAI Main Application"""

import sys
from crewai import Crew, Process
from agents import bug_detective, code_analyzer, solution_architect, test_engineer, documentation_specialist
from tasks import create_tasks


def analyze_bug(bug_report: str, code_context: str = ""):
    print(f"\n{'='*80}\nSOFTWARE BUG ASSISTANT\n{'='*80}\n")
    print(f"Bug Report: {bug_report}\n")

    tasks = create_tasks(bug_report, code_context)
    crew = Crew(
        agents=[bug_detective, code_analyzer, solution_architect, test_engineer, documentation_specialist],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print(f"\n{'='*80}\nANALYSIS COMPLETE\n{'='*80}\n{result}")
    return result


def main():
    if len(sys.argv) > 1:
        bug_report = sys.argv[1]
        code_context = sys.argv[2] if len(sys.argv) > 2 else ""
        analyze_bug(bug_report, code_context)
    else:
        print("Software Bug Assistant - CrewAI Edition")
        print("\nDescribe the bug:")
        bug = input("> ")
        print("\nProvide code context (press Enter to skip):")
        code = input("> ")
        analyze_bug(bug, code)


if __name__ == "__main__":
    main()
