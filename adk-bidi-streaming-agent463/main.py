"""Bidirectional Streaming Agent - CrewAI Implementation"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import BidiStreamingAgents
from tasks import BidiStreamingTasks

load_dotenv()


def setup_bidi_streaming(connection_config: dict, message_schema: dict) -> str:
    """Setup bidirectional streaming system"""

    agents = BidiStreamingAgents()
    tasks_factory = BidiStreamingTasks()

    stream_manager = agents.stream_manager()
    message_processor = agents.message_processor()
    state_coordinator = agents.state_coordinator()

    manage_task = tasks_factory.manage_connection(stream_manager, connection_config)
    process_task = tasks_factory.process_messages(message_processor, message_schema)
    process_task.context = [manage_task]

    coordinate_task = tasks_factory.coordinate_state(state_coordinator)
    coordinate_task.context = [manage_task, process_task]

    crew = Crew(
        agents=[stream_manager, message_processor, state_coordinator],
        tasks=[manage_task, process_task, coordinate_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


def main():
    connection_config = {'protocol': 'websocket', 'endpoint': 'wss://api.example.com/stream'}
    message_schema = {'type': 'json', 'fields': ['timestamp', 'data', 'metadata']}
    result = setup_bidi_streaming(connection_config, message_schema)
    print(result)


if __name__ == "__main__":
    main()
