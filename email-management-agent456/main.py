#!/usr/bin/env python
"""
Email Management CrewAI Main Application
"""

import sys
from crewai import Crew, Process
from agents import email_classifier, draft_writer, workflow_optimizer
from tasks import create_tasks


def main():
    print("\n" + "="*80)
    print("EMAIL MANAGEMENT ASSISTANT")
    print("="*80)

    print("\nPaste your email content (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "":
            if lines and lines[-1] == "":
                break
            lines.append(line)
        else:
            lines.append(line)

    email_content = "\n".join(lines).strip()

    if not email_content:
        print("No email content provided.")
        return

    context = input("\nAdditional context (optional): ").strip()

    tasks = create_tasks(email_content, context)
    crew = Crew(
        agents=[email_classifier, draft_writer, workflow_optimizer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nProcessing email...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("EMAIL ANALYSIS COMPLETE")
    print("="*80)
    print("\n" + str(result))


if __name__ == "__main__":
    main()
