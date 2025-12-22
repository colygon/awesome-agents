"""
A2A ADK MCP - CrewAI Agent Definitions
Multi-Agent Agent-to-Agent Communication System

Agents for agent-to-agent communication protocol:
1. Protocol Designer - Designs communication protocols
2. Message Coordinator - Coordinates message routing
3. Integration Specialist - Integrates with MCP systems
"""

from crewai import Agent
from textwrap import dedent

def create_protocol_designer() -> Agent:
    return Agent(role="Protocol Designer", goal="Design robust agent-to-agent communication protocols",
        backstory="Protocol expert with deep knowledge of distributed systems and agent communication.", verbose=True, allow_delegation=False, memory=True)

def create_message_coordinator() -> Agent:
    return Agent(role="Message Coordinator", goal="Coordinate message routing between agents",
        backstory="Messaging systems expert specializing in reliable message delivery and coordination.", verbose=True, allow_delegation=False, memory=True)

def create_integration_specialist() -> Agent:
    return Agent(role="Integration Specialist", goal="Integrate agent systems with MCP (Model Context Protocol)",
        backstory="Integration architect with expertise in MCP and cross-system communication.", verbose=True, allow_delegation=False, memory=True)
