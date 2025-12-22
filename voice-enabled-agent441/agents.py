from crewai import Agent
from tools import (
    speech_recognition_tool,
    text_to_speech_tool,
    natural_language_processor,
    voice_command_analyzer,
    audio_quality_checker
)

class VoiceAgents:
    def speech_recognition_agent(self):
        return Agent(
            role='Speech Recognition Specialist',
            goal='Convert voice input to accurate text transcription',
            backstory="""You are an expert in speech recognition and audio processing.
            You excel at converting spoken language into accurate text transcriptions,
            handling different accents, dialects, and audio quality levels.""",
            tools=[speech_recognition_tool, audio_quality_checker],
            verbose=True,
            allow_delegation=False
        )

    def natural_language_agent(self):
        return Agent(
            role='Natural Language Understanding Specialist',
            goal='Analyze and interpret voice commands and intent',
            backstory="""You are a specialist in natural language processing and
            understanding user intent. You excel at interpreting voice commands,
            extracting meaning, and identifying user intentions.""",
            tools=[natural_language_processor, voice_command_analyzer],
            verbose=True,
            allow_delegation=True
        )

    def voice_synthesis_agent(self):
        return Agent(
            role='Voice Synthesis Specialist',
            goal='Generate natural-sounding speech responses',
            backstory="""You are an expert in text-to-speech synthesis and voice
            generation. You create natural, expressive, and context-appropriate
            voice responses for users.""",
            tools=[text_to_speech_tool],
            verbose=True,
            allow_delegation=False
        )

    def conversation_manager_agent(self):
        return Agent(
            role='Conversation Manager',
            goal='Manage multi-turn voice conversations and maintain context',
            backstory="""You are a conversation management expert who orchestrates
            voice-based interactions, maintains conversation context, and ensures
            smooth, natural dialogue flow.""",
            tools=[natural_language_processor, voice_command_analyzer],
            verbose=True,
            allow_delegation=True
        )
