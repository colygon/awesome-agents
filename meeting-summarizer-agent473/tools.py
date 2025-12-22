from crewai_tools import tool
import json
from typing import Dict, List, Any
from datetime import datetime, timedelta

class TranscriptionTools:
    @tool("Process Audio")
    def process_audio(audio_file: str) -> str:
        """
        Processes audio/video files to extract transcript.
        Useful for converting recordings to text.
        """
        # Simulated audio processing
        result = {
            "file": audio_file,
            "duration": "45m 30s",
            "format": "mp3",
            "quality": "high",
            "transcript_status": "completed",
            "word_count": 6789,
            "confidence_score": 0.94,
            "processing_time": "3m 12s"
        }

        return json.dumps(result, indent=2)

    @tool("Identify Speakers")
    def identify_speakers(transcript: str) -> str:
        """
        Identifies and labels different speakers in a transcript.
        Useful for multi-participant meetings.
        """
        speakers = {
            "total_speakers": 4,
            "speakers": [
                {
                    "id": "Speaker_1",
                    "name": "John (detected from intro)",
                    "speaking_time": "12m 30s",
                    "turns": 18,
                    "role": "Host/Facilitator"
                },
                {
                    "id": "Speaker_2",
                    "name": "Sarah",
                    "speaking_time": "10m 15s",
                    "turns": 15,
                    "role": "Participant"
                },
                {
                    "id": "Speaker_3",
                    "name": "Mike",
                    "speaking_time": "8m 45s",
                    "turns": 12,
                    "role": "Participant"
                },
                {
                    "id": "Speaker_4",
                    "name": "Unknown",
                    "speaking_time": "5m 20s",
                    "turns": 8,
                    "role": "Participant"
                }
            ],
            "labeled_transcript_sample": """
[00:00] John: Welcome everyone to today's meeting.
[00:15] Sarah: Thanks for having us. I'd like to discuss the project timeline.
[00:30] Mike: I agree, we should prioritize that discussion.
            """
        }

        return json.dumps(speakers, indent=2)

    @tool("Clean Transcript")
    def clean_transcript(raw_transcript: str) -> str:
        """
        Cleans and formats transcript by removing filler words and errors.
        Useful for improving readability.
        """
        cleaning_results = {
            "original_length": len(raw_transcript),
            "cleaned_length": len(raw_transcript) * 0.85,
            "removed_elements": {
                "filler_words": ["um", "uh", "like", "you know"],
                "repeated_words": 23,
                "false_starts": 15,
                "corrections": 8
            },
            "improvements": [
                "Removed 145 filler words",
                "Fixed 23 repeated phrases",
                "Corrected 8 transcription errors",
                "Improved punctuation and capitalization"
            ],
            "cleaned_sample": """
John: Welcome everyone to today's meeting. Let's start with the project updates.

Sarah: Thank you. I'd like to discuss the timeline for the Q4 deliverables. We're currently ahead of schedule.

Mike: That's great news. We should also address the budget allocation.
            """
        }

        return json.dumps(cleaning_results, indent=2)


class AnalysisTools:
    @tool("Extract Key Topics")
    def extract_key_topics(transcript: str) -> str:
        """
        Extracts main topics and themes from meeting transcript.
        Useful for understanding meeting content.
        """
        topics = {
            "total_topics": 5,
            "main_topics": [
                {
                    "topic": "Q4 Project Timeline",
                    "duration": "12 minutes",
                    "participants": ["John", "Sarah", "Mike"],
                    "importance": "high",
                    "timestamp": "00:05 - 00:17"
                },
                {
                    "topic": "Budget Allocation",
                    "duration": "8 minutes",
                    "participants": ["Mike", "Sarah"],
                    "importance": "high",
                    "timestamp": "00:17 - 00:25"
                },
                {
                    "topic": "Team Resources",
                    "duration": "10 minutes",
                    "participants": ["John", "Unknown"],
                    "importance": "medium",
                    "timestamp": "00:25 - 00:35"
                },
                {
                    "topic": "Next Sprint Planning",
                    "duration": "7 minutes",
                    "participants": ["All"],
                    "importance": "high",
                    "timestamp": "00:35 - 00:42"
                },
                {
                    "topic": "Questions and Concerns",
                    "duration": "5 minutes",
                    "participants": ["All"],
                    "importance": "medium",
                    "timestamp": "00:42 - 00:47"
                }
            ]
        }

        return json.dumps(topics, indent=2)

    @tool("Identify Decisions")
    def identify_decisions(transcript: str) -> str:
        """
        Identifies decisions made during the meeting.
        Useful for tracking outcomes.
        """
        decisions = {
            "total_decisions": 6,
            "decisions": [
                {
                    "decision": "Move Q4 deadline forward by one week",
                    "rationale": "Team is ahead of schedule",
                    "impact": "high",
                    "stakeholders": ["Sarah", "Mike"],
                    "timestamp": "00:14"
                },
                {
                    "decision": "Allocate additional $50K to marketing budget",
                    "rationale": "Strong ROI from previous campaigns",
                    "impact": "high",
                    "stakeholders": ["Mike"],
                    "timestamp": "00:22"
                },
                {
                    "decision": "Hire two additional developers",
                    "rationale": "Increased project scope",
                    "impact": "medium",
                    "stakeholders": ["John"],
                    "timestamp": "00:30"
                },
                {
                    "decision": "Implement weekly check-ins",
                    "rationale": "Improve team coordination",
                    "impact": "low",
                    "stakeholders": ["All"],
                    "timestamp": "00:38"
                }
            ],
            "consensus_level": "high",
            "unresolved_items": [
                "Specific roles for new developers",
                "Exact marketing budget breakdown"
            ]
        }

        return json.dumps(decisions, indent=2)

    @tool("Summarize Discussions")
    def summarize_discussions(transcript: str) -> str:
        """
        Creates concise summaries of meeting discussions.
        Useful for quick reference.
        """
        summary = {
            "executive_summary": "Team meeting focused on Q4 project acceleration, budget reallocation, and resource planning. Key decisions include moving deadline forward, increasing marketing budget, and expanding development team.",
            "detailed_summaries": {
                "Q4_Project_Timeline": {
                    "summary": "Team is ahead of schedule on Q4 deliverables. Decision made to accelerate deadline by one week to capitalize on market opportunity.",
                    "key_points": [
                        "Currently 2 weeks ahead of original schedule",
                        "All milestones completed on time",
                        "Client feedback positive",
                        "Team capacity sufficient for acceleration"
                    ]
                },
                "Budget_Allocation": {
                    "summary": "Additional budget approved for marketing based on strong Q3 performance. Finance team to provide detailed breakdown by next week.",
                    "key_points": [
                        "$50K additional marketing budget approved",
                        "Q3 marketing ROI exceeded targets by 40%",
                        "Focus on digital channels",
                        "Detailed plan due next week"
                    ]
                },
                "Team_Resources": {
                    "summary": "Decision to expand development team with two new hires. Recruitment to begin immediately with focus on senior developers.",
                    "key_points": [
                        "Two senior developer positions approved",
                        "Recruitment starting this week",
                        "Focus on full-stack capabilities",
                        "Onboarding plan to be developed"
                    ]
                }
            },
            "sentiment": "positive",
            "energy_level": "high"
        }

        return json.dumps(summary, indent=2)


class ActionItemTools:
    @tool("Extract Action Items")
    def extract_action_items(transcript: str) -> str:
        """
        Extracts all action items and tasks from meeting.
        Useful for tracking follow-ups.
        """
        action_items = {
            "total_items": 8,
            "items": [
                {
                    "id": "AI-001",
                    "action": "Update project timeline and share with stakeholders",
                    "owner": "Sarah",
                    "deadline": "End of week",
                    "priority": "high",
                    "status": "pending",
                    "dependencies": []
                },
                {
                    "id": "AI-002",
                    "action": "Prepare detailed marketing budget breakdown",
                    "owner": "Mike",
                    "deadline": "Next Tuesday",
                    "priority": "high",
                    "status": "pending",
                    "dependencies": []
                },
                {
                    "id": "AI-003",
                    "action": "Post job descriptions for developer positions",
                    "owner": "John",
                    "deadline": "This week",
                    "priority": "high",
                    "status": "pending",
                    "dependencies": []
                },
                {
                    "id": "AI-004",
                    "action": "Schedule follow-up meeting with client",
                    "owner": "Sarah",
                    "deadline": "Within 2 weeks",
                    "priority": "medium",
                    "status": "pending",
                    "dependencies": ["AI-001"]
                },
                {
                    "id": "AI-005",
                    "action": "Create onboarding plan for new developers",
                    "owner": "John",
                    "deadline": "Next month",
                    "priority": "medium",
                    "status": "pending",
                    "dependencies": ["AI-003"]
                }
            ]
        }

        return json.dumps(action_items, indent=2)

    @tool("Assign Owners")
    def assign_owners(action_item: str) -> str:
        """
        Assigns owners to action items based on context.
        Useful for accountability.
        """
        assignment = {
            "action_item": action_item,
            "recommended_owner": "Sarah Johnson",
            "reasoning": "Based on discussion context and role responsibilities",
            "alternative_owners": ["Mike Chen", "Project Team Lead"],
            "skills_required": ["Project Management", "Stakeholder Communication"],
            "estimated_effort": "2-3 hours",
            "urgency": "high"
        }

        return json.dumps(assignment, indent=2)

    @tool("Set Deadlines")
    def set_deadlines(action_item: str) -> str:
        """
        Determines appropriate deadlines for action items.
        Useful for project planning.
        """
        now = datetime.now()
        deadline_info = {
            "action_item": action_item,
            "suggested_deadline": (now + timedelta(days=7)).strftime("%Y-%m-%d"),
            "reasoning": "Based on priority and dependencies",
            "milestones": [
                {
                    "milestone": "Initial draft",
                    "date": (now + timedelta(days=3)).strftime("%Y-%m-%d")
                },
                {
                    "milestone": "Review",
                    "date": (now + timedelta(days=5)).strftime("%Y-%m-%d")
                },
                {
                    "milestone": "Final version",
                    "date": (now + timedelta(days=7)).strftime("%Y-%m-%d")
                }
            ],
            "buffer_time": "1 day",
            "risk_level": "low"
        }

        return json.dumps(deadline_info, indent=2)

    @tool("Create Summary Report")
    def create_summary_report(meeting_data: str) -> str:
        """
        Creates a formatted meeting summary report.
        Useful for distribution to stakeholders.
        """
        report = {
            "meeting_title": "Q4 Planning & Strategy Meeting",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "duration": "45 minutes",
            "attendees": ["John Smith", "Sarah Johnson", "Mike Chen", "Guest"],

            "executive_summary": "Productive meeting focused on accelerating Q4 deliverables and resource planning. Team is ahead of schedule, leading to decision to move deadline forward. Additional budget allocated for marketing and team expansion approved.",

            "key_decisions": [
                "Q4 deadline moved forward by one week",
                "Additional $50K allocated to marketing",
                "Two senior developer positions approved",
                "Weekly check-ins implemented"
            ],

            "action_items_summary": {
                "total": 8,
                "high_priority": 3,
                "due_this_week": 3,
                "due_next_week": 2
            },

            "next_steps": [
                "Sarah to update project timeline",
                "Mike to prepare budget breakdown",
                "John to post job descriptions",
                "Team to begin weekly check-ins next Monday"
            ],

            "parking_lot": [
                "Specific marketing channel allocation",
                "Developer role definitions",
                "Q1 2024 planning timeline"
            ],

            "next_meeting": {
                "date": (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d"),
                "agenda": "Review progress on action items and Q4 status update"
            }
        }

        return json.dumps(report, indent=2)
