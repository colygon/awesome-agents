"""A2A ADK MCP - CrewAI Multi-Agent Communication System"""
import os, sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_protocol_designer, create_message_coordinator, create_integration_specialist
from tasks import create_protocol_design_task, create_coordination_task, create_integration_task

def load_environment():
    load_dotenv()
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found.")
        sys.exit(1)

def run_a2a_system(communication_requirements: dict):
    designer = create_protocol_designer()
    coordinator = create_message_coordinator()
    integrator = create_integration_specialist()

    protocol_task = create_protocol_design_task(designer, communication_requirements)
    coordination_task = create_coordination_task(coordinator, protocol_task)
    integration_task = create_integration_task(integrator, protocol_task, coordination_task)

    crew = Crew(agents=[designer, coordinator, integrator], tasks=[protocol_task, coordination_task, integration_task], process=Process.sequential, verbose=True)
    return {'result': crew.kickoff(), 'timestamp': datetime.now().isoformat()}

def main():
    load_environment()
    result = run_a2a_system({'description': 'Multi-agent collaboration protocol with MCP integration'})
    print(f"\n\nA2A SYSTEM RESULTS\n{result['result']}")

if __name__ == "__main__":
    main()
