"""A2A ADK MCP - CrewAI Tools"""
from crewai_tools import tool

@tool("Protocol Validator")
def validate_protocol(protocol_spec: dict) -> dict:
    return {"valid": True, "issues": []}

@tool("MCP Connector")
def connect_to_mcp(endpoint: str) -> dict:
    return {"status": "connected", "capabilities": []}
