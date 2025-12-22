from crewai import Agent
from tools import TranscriptionTools, AnalysisTools, ActionItemTools

class MeetingSummarizerAgents:
    def transcription_specialist(self):
        return Agent(
            role='Transcription Specialist',
            goal='Process and clean meeting transcripts for analysis',
            backstory="""You are an expert in processing audio and video recordings
            into accurate, readable transcripts. You understand how to handle
            multiple speakers, identify speaker changes, and clean up transcription
            errors to produce high-quality text for analysis.""",
            tools=[
                TranscriptionTools.process_audio,
                TranscriptionTools.identify_speakers,
                TranscriptionTools.clean_transcript
            ],
            verbose=True,
            allow_delegation=False
        )

    def content_analyzer(self):
        return Agent(
            role='Content Analyzer',
            goal='Analyze meeting content and extract key insights',
            backstory="""You are a skilled analyst who can quickly identify
            important topics, decisions, and discussions from meeting transcripts.
            You understand meeting dynamics and can distinguish between main
            topics and tangential discussions.""",
            tools=[
                AnalysisTools.extract_key_topics,
                AnalysisTools.identify_decisions,
                AnalysisTools.summarize_discussions
            ],
            verbose=True,
            allow_delegation=False
        )

    def action_item_coordinator(self):
        return Agent(
            role='Action Item Coordinator',
            goal='Extract and organize action items and next steps',
            backstory="""You are an expert at identifying commitments, tasks,
            and action items from meeting discussions. You know how to assign
            ownership, set priorities, and establish clear deadlines from
            conversational context.""",
            tools=[
                ActionItemTools.extract_action_items,
                ActionItemTools.assign_owners,
                ActionItemTools.set_deadlines
            ],
            verbose=True,
            allow_delegation=False
        )

    def summary_writer(self):
        return Agent(
            role='Summary Writer',
            goal='Create clear, concise meeting summaries and reports',
            backstory="""You are a skilled writer who creates clear, well-organized
            meeting summaries. You know how to structure information logically,
            highlight key points, and present information in a scannable format
            that busy professionals can quickly digest.""",
            tools=[
                AnalysisTools.summarize_discussions,
                ActionItemTools.create_summary_report
            ],
            verbose=True,
            allow_delegation=False
        )
