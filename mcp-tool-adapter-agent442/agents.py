from crewai import Agent
from tools import (
    mcp_protocol_analyzer,
    tool_schema_validator,
    adapter_generator,
    integration_tester,
    compatibility_checker
)

class MCPAdapterAgents:
    def protocol_analyst_agent(self):
        return Agent(
            role='MCP Protocol Analyst',
            goal='Analyze and understand MCP protocol specifications',
            backstory="""You are an expert in the Model Context Protocol (MCP).
            You understand protocol specifications, message formats, and communication
            patterns. You excel at analyzing MCP requirements and specifications.""",
            tools=[mcp_protocol_analyzer, compatibility_checker],
            verbose=True,
            allow_delegation=False
        )

    def schema_validator_agent(self):
        return Agent(
            role='Tool Schema Validator',
            goal='Validate and verify tool schemas against MCP standards',
            backstory="""You are a schema validation specialist who ensures that
            tool definitions comply with MCP standards. You validate schemas,
            check data types, and ensure compatibility.""",
            tools=[tool_schema_validator, compatibility_checker],
            verbose=True,
            allow_delegation=False
        )

    def adapter_engineer_agent(self):
        return Agent(
            role='Adapter Engineer',
            goal='Generate MCP adapters for various tools and services',
            backstory="""You are a software engineer specializing in creating
            adapters that bridge different tools with the MCP protocol. You
            generate clean, efficient, and maintainable adapter code.""",
            tools=[adapter_generator, tool_schema_validator],
            verbose=True,
            allow_delegation=True
        )

    def integration_tester_agent(self):
        return Agent(
            role='Integration Testing Specialist',
            goal='Test and validate MCP tool integrations',
            backstory="""You are a quality assurance expert who specializes in
            testing MCP integrations. You create comprehensive test suites and
            validate that adapters work correctly with the protocol.""",
            tools=[integration_tester, compatibility_checker],
            verbose=True,
            allow_delegation=False
        )
