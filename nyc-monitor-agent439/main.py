"""NYC Monitor - CrewAI Multi-Agent NYC Data Monitoring System"""
import os, sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_data_collector, create_trend_analyzer, create_alert_generator
from tasks import create_data_collection_task, create_trend_analysis_task, create_alert_generation_task

def load_environment():
    load_dotenv()
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found.")
        sys.exit(1)

def run_nyc_monitoring(data_sources: list):
    collector = create_data_collector()
    analyzer = create_trend_analyzer()
    alerter = create_alert_generator()

    collection_task = create_data_collection_task(collector, data_sources)
    analysis_task = create_trend_analysis_task(analyzer, collection_task)
    alert_task = create_alert_generation_task(alerter, collection_task, analysis_task)

    crew = Crew(agents=[collector, analyzer, alerter], tasks=[collection_task, analysis_task, alert_task], process=Process.sequential, verbose=True)
    return {'result': crew.kickoff(), 'timestamp': datetime.now().isoformat()}

def main():
    load_environment()
    result = run_nyc_monitoring(['311 Service Requests', 'MTA Subway Performance', 'Air Quality'])
    print(f"\n\nNYC MONITORING RESULTS\n{result['result']}")

if __name__ == "__main__":
    main()
