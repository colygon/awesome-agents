from crewai import Task
from textwrap import dedent

class MeetingSummarizerTasks:
    def process_transcript(self, agent, meeting_info):
        return Task(
            description=dedent(f"""
                Process the meeting recording and create a clean transcript:

                Meeting Information:
                {meeting_info}

                Your tasks:
                1. Process audio/video recording or raw transcript
                2. Identify and label different speakers
                3. Clean up transcription errors and filler words
                4. Format the transcript for readability
                5. Add timestamps for key moments
                6. Segment transcript by topics if needed

                Provide a clean, formatted transcript ready for analysis.
            """),
            agent=agent,
            expected_output="Clean, speaker-labeled meeting transcript with timestamps and proper formatting"
        )

    def analyze_content(self, agent, transcript):
        return Task(
            description=dedent(f"""
                Analyze the meeting content and extract key insights:

                Transcript:
                {transcript}

                Your tasks:
                1. Identify main topics discussed
                2. Extract key decisions made
                3. Note important questions raised
                4. Identify areas of agreement and disagreement
                5. Highlight significant quotes or statements
                6. Categorize discussion points by importance

                Provide a comprehensive content analysis.
            """),
            agent=agent,
            expected_output="Detailed content analysis with topics, decisions, key points, and discussion highlights"
        )

    def extract_action_items(self, agent, transcript):
        return Task(
            description=dedent(f"""
                Extract and organize all action items from the meeting:

                Transcript:
                {transcript}

                Your tasks:
                1. Identify all commitments and action items
                2. Assign owners to each action item
                3. Determine deadlines (explicit or implied)
                4. Set priority levels for each item
                5. Note any dependencies between items
                6. Flag any items that need clarification

                Provide a structured list of action items with all details.
            """),
            agent=agent,
            expected_output="Comprehensive action item list with owners, deadlines, priorities, and dependencies"
        )

    def create_summary(self, agent, meeting_data):
        return Task(
            description=dedent(f"""
                Create a comprehensive meeting summary:

                Meeting Data:
                {meeting_data}

                Your tasks:
                1. Write executive summary (2-3 sentences)
                2. List all attendees and participants
                3. Outline key topics and discussions
                4. Highlight main decisions and outcomes
                5. Include action items section
                6. Add next steps and follow-up items
                7. Note any parking lot items or unresolved questions

                Provide a complete, well-structured meeting summary.
            """),
            agent=agent,
            expected_output="Professional meeting summary with executive summary, discussions, decisions, and action items"
        )

    def generate_distribution_report(self, agent, summary_data):
        return Task(
            description=dedent(f"""
                Generate a distribution-ready meeting report:

                Summary Data:
                {summary_data}

                Your tasks:
                1. Format summary for email distribution
                2. Create separate sections for different audiences (attendees, stakeholders)
                3. Generate follow-up email templates
                4. Create calendar invites for action item deadlines
                5. Prepare presentation-ready slides if needed
                6. Export in multiple formats (PDF, Word, Markdown)

                Provide distribution-ready meeting documentation.
            """),
            agent=agent,
            expected_output="Complete distribution package with formatted reports, emails, and follow-up materials"
        )
