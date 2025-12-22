#!/usr/bin/env python
"""Customer Service TypeScript - CrewAI Main"""

import sys
from crewai import Crew, Process
from agents import ticket_intake, knowledge_agent, response_composer, escalation_manager, qa_agent
from tasks import create_tasks


def main():
    print("Customer Service (TypeScript) - CrewAI Edition\n")
    message = input("Customer message: ") if len(sys.argv) == 1 else sys.argv[1]
    customer = input("Customer info (optional): ") if len(sys.argv) <= 2 else sys.argv[2] if len(sys.argv) > 2 else ""

    tasks = create_tasks(message, customer)
    crew = Crew(
        agents=[ticket_intake, knowledge_agent, response_composer, escalation_manager, qa_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print(f"\n{'='*80}\nRESPONSE READY\n{'='*80}\n{result}")


if __name__ == "__main__":
    main()
