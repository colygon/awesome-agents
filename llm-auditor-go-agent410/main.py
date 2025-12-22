#!/usr/bin/env python
"""LLM Auditor Go - CrewAI Main"""

import sys
from crewai import Crew, Process
from agents import model_evaluator, bias_auditor, safety_evaluator, performance_analyzer, compliance_auditor, report_generator
from tasks import create_tasks


def main():
    print("LLM Auditor (Go) - CrewAI Edition\n")
    print("Comprehensive LLM Audit System\n")

    model = input("Model to audit: ") if len(sys.argv) == 1 else sys.argv[1]
    scope = input("Evaluation scope (comprehensive/quick/custom): ") if len(sys.argv) <= 2 else sys.argv[2] if len(sys.argv) > 2 else "comprehensive"

    print(f"\nStarting comprehensive audit of {model}...\n")

    tasks = create_tasks(model, scope)
    crew = Crew(
        agents=[
            model_evaluator,
            bias_auditor,
            safety_evaluator,
            performance_analyzer,
            compliance_auditor,
            report_generator
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print(f"\n{'='*80}\nAUDIT COMPLETE\n{'='*80}\n{result}")


if __name__ == "__main__":
    main()
