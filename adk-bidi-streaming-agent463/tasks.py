"""CrewAI Tasks for Bidirectional Streaming"""

from crewai import Task
from textwrap import dedent


class BidiStreamingTasks:
    """Factory class for creating bidirectional streaming tasks"""

    def manage_connection(self, agent, connection_config: dict) -> Task:
        return Task(
            description=dedent(f"""
                Manage bidirectional streaming connection:
                Config: {connection_config}

                Requirements:
                1. Establish and maintain WebSocket/gRPC connection
                2. Implement flow control and backpressure
                3. Handle connection lifecycle (open, close, error)
                4. Monitor connection health
                5. Implement reconnection logic
            """),
            agent=agent,
            expected_output='Connection management strategy with flow control and error handling'
        )

    def process_messages(self, agent, message_schema: dict) -> Task:
        return Task(
            description=dedent(f"""
                Process streaming messages in real-time:
                Schema: {message_schema}

                Tasks:
                1. Validate incoming message format
                2. Parse and transform data
                3. Apply business logic
                4. Prepare response messages
                5. Handle message ordering
            """),
            agent=agent,
            expected_output='Message processing pipeline with validation and transformation',
            context=[]
        )

    def coordinate_state(self, agent) -> Task:
        return Task(
            description=dedent("""
                Coordinate state across bidirectional streams:

                Responsibilities:
                1. Track connection state
                2. Synchronize data between client and server
                3. Handle state transitions
                4. Implement conflict resolution
                5. Maintain consistency guarantees
            """),
            agent=agent,
            expected_output='State coordination strategy with consistency guarantees',
            context=[]
        )
