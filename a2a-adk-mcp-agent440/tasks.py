"""A2A ADK MCP - CrewAI Task Definitions"""
from crewai import Task

def create_protocol_design_task(agent, communication_requirements: dict) -> Task:
    return Task(description=f"Design A2A protocol for: {communication_requirements.get('description', '')}. Include message formats and routing.", expected_output="A2A protocol specification document.", agent=agent)

def create_coordination_task(agent, protocol_output) -> Task:
    return Task(description=f"Implement message coordination based on protocol: {protocol_output}", expected_output="Message coordination system implementation.", agent=agent, context=[protocol_output] if isinstance(protocol_output, Task) else [])

def create_integration_task(agent, protocol_output, coordination_output) -> Task:
    return Task(description=f"Integrate with MCP. Protocol: {protocol_output}, Coordination: {coordination_output}", expected_output="MCP integration implementation.", agent=agent, context=[protocol_output, coordination_output] if isinstance(protocol_output, Task) else [])
