"""
MCP-Gemma CrewAI Agents
Model Context Protocol integration with Gemma models
"""

from crewai import Agent
from tools import MCPServerTool, GemmaInferenceTool, ContextManagerTool

mcp_coordinator = Agent(
    role="MCP Server Coordinator",
    goal="Coordinate MCP server interactions and tool usage",
    backstory="""Expert in Model Context Protocol who manages server connections,
    tool discovery, and resource access across MCP-enabled services.""",
    verbose=True,
    allow_delegation=False,
    tools=[MCPServerTool(), ContextManagerTool()]
)

gemma_specialist = Agent(
    role="Gemma Model Specialist",
    goal="Execute tasks using Gemma models with MCP context",
    backstory="""Specialist in Gemma model family who leverages MCP for enhanced
    context and tool access to solve complex problems.""",
    verbose=True,
    allow_delegation=False,
    tools=[GemmaInferenceTool(), ContextManagerTool()]
)

integration_expert = Agent(
    role="MCP Integration Expert",
    goal="Optimize MCP-Gemma integration for tasks",
    backstory="""Integration specialist who ensures seamless coordination between
    MCP servers, tools, and Gemma models for optimal performance.""",
    verbose=True,
    allow_delegation=False
)
