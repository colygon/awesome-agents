#!/usr/bin/env python
"""
AI Trends Pipeline CrewAI Main Application
"""

import sys
from crewai import Crew, Process
from agents import trend_monitor, data_analyst, report_generator
from tasks import create_tasks


def main():
    print("\n" + "="*80)
    print("AI TRENDS PIPELINE")
    print("="*80)

    timeframe = input("Timeframe (default: last 30 days): ").strip() or "last 30 days"

    tasks = create_tasks(timeframe)
    crew = Crew(
        agents=[trend_monitor, data_analyst, report_generator],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nGenerating AI trends report...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("TRENDS REPORT COMPLETE")
    print("="*80)
    print("\n" + str(result))


if __name__ == "__main__":
    main()
