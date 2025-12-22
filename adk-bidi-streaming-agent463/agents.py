"""
CrewAI Agents for Bidirectional Streaming Agent
Specialized agents for real-time bidirectional communication
"""

from crewai import Agent
import os


class BidiStreamingAgents:
    """Factory class for creating bidirectional streaming agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def stream_manager(self) -> Agent:
        """Stream Management Agent"""
        return Agent(
            role='Stream Management Specialist',
            goal='Manage bidirectional streaming connections, handle flow control, and ensure reliable real-time communication',
            backstory='You are an expert in real-time streaming protocols with deep knowledge of WebSockets, gRPC streaming, and flow control mechanisms.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def message_processor(self) -> Agent:
        """Message Processing Agent"""
        return Agent(
            role='Message Processing Specialist',
            goal='Process incoming messages, validate data, and prepare responses in real-time',
            backstory='You excel at parsing, validating, and transforming streaming data with minimal latency.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def state_coordinator(self) -> Agent:
        """State Coordination Agent"""
        return Agent(
            role='State Coordination Specialist',
            goal='Maintain connection state, handle reconnections, and synchronize data across streams',
            backstory='You are skilled at managing stateful connections and ensuring data consistency in distributed streaming systems.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )
