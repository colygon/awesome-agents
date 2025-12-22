"""Forkcast - CrewAI Multi-Agent Forecasting System"""
import os, sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_data_analyst, create_forecast_modeler, create_insights_interpreter
from tasks import create_data_analysis_task, create_forecast_modeling_task, create_insights_task

def load_environment():
    load_dotenv()
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found.")
        sys.exit(1)

def run_forecasting(data_context: dict):
    analyst = create_data_analyst()
    modeler = create_forecast_modeler()
    interpreter = create_insights_interpreter()

    analysis_task = create_data_analysis_task(analyst, data_context)
    forecast_task = create_forecast_modeling_task(modeler, analysis_task)
    insights_task = create_insights_task(interpreter, analysis_task, forecast_task)

    crew = Crew(agents=[analyst, modeler, interpreter], tasks=[analysis_task, forecast_task, insights_task], process=Process.sequential, verbose=True)
    return {'result': crew.kickoff(), 'timestamp': datetime.now().isoformat()}

def main():
    load_environment()
    result = run_forecasting({'description': 'Sales data for Q1-Q4 2024'})
    print(f"\n\nFORECASTING RESULTS\n{result['result']}")

if __name__ == "__main__":
    main()
