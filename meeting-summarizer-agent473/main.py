#!/usr/bin/env python
from crewai import Crew, Process
from agents import MeetingSummarizerAgents
from tasks import MeetingSummarizerTasks
from dotenv import load_dotenv

load_dotenv()

def run_meeting_summarizer():
    """
    Run the Meeting Summarizer crew to process and summarize meetings
    """
    print("## Welcome to the Meeting Summarizer Crew")
    print("------------------------------------------")

    # Get user input for meeting details
    meeting_title = input("What is the meeting title? ")
    meeting_type = input("What type of meeting? (e.g., planning, review, brainstorm): ")
    transcript_source = input("Transcript source? (e.g., recording file path, text file, or 'manual'): ")

    meeting_info = f"""
    Meeting Title: {meeting_title}
    Meeting Type: {meeting_type}
    Date: {input("Meeting date (YYYY-MM-DD): ")}
    Duration: {input("Meeting duration (e.g., 45m): ")}
    Attendees: {input("List attendees (comma-separated): ")}
    Transcript Source: {transcript_source}
    """

    # Sample transcript for demo (in production, this would be loaded from file)
    sample_transcript = """
    The meeting discussed Q4 project planning and resource allocation.
    Multiple decisions were made regarding timeline acceleration and budget.
    Action items were assigned to team members with specific deadlines.
    """

    # Initialize agents
    agents = MeetingSummarizerAgents()
    tasks_manager = MeetingSummarizerTasks()

    # Create agents
    transcription_specialist = agents.transcription_specialist()
    content_analyzer = agents.content_analyzer()
    action_item_coordinator = agents.action_item_coordinator()
    summary_writer = agents.summary_writer()

    # Create tasks
    transcript_task = tasks_manager.process_transcript(
        transcription_specialist,
        meeting_info
    )

    analysis_task = tasks_manager.analyze_content(
        content_analyzer,
        sample_transcript
    )

    action_items_task = tasks_manager.extract_action_items(
        action_item_coordinator,
        sample_transcript
    )

    summary_task = tasks_manager.create_summary(
        summary_writer,
        meeting_info
    )

    distribution_task = tasks_manager.generate_distribution_report(
        summary_writer,
        meeting_info
    )

    # Create and run crew
    crew = Crew(
        agents=[
            transcription_specialist,
            content_analyzer,
            action_item_coordinator,
            summary_writer
        ],
        tasks=[
            transcript_task,
            analysis_task,
            action_items_task,
            summary_task,
            distribution_task
        ],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Meeting Summary Results")
    print("########################\n")
    print(result)

    return result


if __name__ == "__main__":
    run_meeting_summarizer()
