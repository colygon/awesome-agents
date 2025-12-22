#!/usr/bin/env python
from crewai import Crew, Process
from agents import VoiceAgents
from tasks import VoiceTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_voice_agent():
    """
    Run the Voice-Enabled Agent system
    """
    print("## Welcome to the Voice-Enabled Agent System")
    print("----------------------------------------------")

    # Sample voice input (in production, this would be actual audio)
    audio_input = input("Enter voice input description (or path to audio file): ")

    # Initialize agents and tasks
    agents = VoiceAgents()
    tasks = VoiceTasks()

    # Create agents
    speech_agent = agents.speech_recognition_agent()
    nlu_agent = agents.natural_language_agent()
    synthesis_agent = agents.voice_synthesis_agent()
    conversation_agent = agents.conversation_manager_agent()

    # Create tasks
    transcription_task = tasks.process_voice_input_task(speech_agent, audio_input)
    intent_task = tasks.understand_intent_task(nlu_agent, "{{transcription_output}}")
    response_task = tasks.generate_response_task(synthesis_agent, "{{intent_output}}", "Response generated")
    conversation_task = tasks.manage_conversation_task(conversation_agent, [], audio_input)

    # Create crew
    crew = Crew(
        agents=[speech_agent, nlu_agent, synthesis_agent, conversation_agent],
        tasks=[transcription_task, intent_task, response_task, conversation_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## Voice Agent Result")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_voice_agent()
