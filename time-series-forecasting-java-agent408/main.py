#!/usr/bin/env python
"""Time Series Forecasting Java - CrewAI Main"""

import sys
from crewai import Crew, Process
from agents import data_analyzer, forecasting_specialist, anomaly_detector, validation_engineer, reporting_specialist
from tasks import create_tasks


def main():
    print("Time Series Forecasting (Java) - CrewAI Edition\n")
    data_desc = input("Describe your time series data: ") if len(sys.argv) == 1 else sys.argv[1]
    horizon = int(input("Forecast horizon (days): ") or "30") if len(sys.argv) <= 2 else int(sys.argv[2]) if len(sys.argv) > 2 else 30

    tasks = create_tasks(data_desc, horizon)
    crew = Crew(
        agents=[data_analyzer, anomaly_detector, forecasting_specialist, validation_engineer, reporting_specialist],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print(f"\n{'='*80}\nFORECAST COMPLETE\n{'='*80}\n{result}")


if __name__ == "__main__":
    main()
