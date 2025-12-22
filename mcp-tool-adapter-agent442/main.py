#!/usr/bin/env python
from crewai import Crew, Process
from agents import MCPAdapterAgents
from tasks import MCPAdapterTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_mcp_adapter():
    """
    Run the MCP Tool Adapter system
    """
    print("## Welcome to the MCP Tool Adapter System")
    print("------------------------------------------")

    tool_description = input("Enter tool description to create MCP adapter for: ")
    tool_schema = input("Enter tool schema (or 'default' for sample): ")

    if tool_schema.lower() == 'default':
        tool_schema = '{"name": "example_tool", "parameters": {"type": "object"}}'

    # Initialize agents and tasks
    agents = MCPAdapterAgents()
    tasks = MCPAdapterTasks()

    # Create agents
    protocol_agent = agents.protocol_analyst_agent()
    validator_agent = agents.schema_validator_agent()
    engineer_agent = agents.adapter_engineer_agent()
    tester_agent = agents.integration_tester_agent()

    # Create tasks
    analysis_task = tasks.analyze_protocol_task(protocol_agent, tool_description)
    validation_task = tasks.validate_schema_task(validator_agent, tool_schema)
    generation_task = tasks.generate_adapter_task(engineer_agent, "{{analysis_output}}", tool_description)
    testing_task = tasks.test_integration_task(tester_agent, "{{generation_output}}")

    # Create crew
    crew = Crew(
        agents=[protocol_agent, validator_agent, engineer_agent, tester_agent],
        tasks=[analysis_task, validation_task, generation_task, testing_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## MCP Adapter Result")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_mcp_adapter()
