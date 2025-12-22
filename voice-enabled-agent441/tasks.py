from crewai import Task
from textwrap import dedent

class VoiceTasks:
    def process_voice_input_task(self, agent, audio_input):
        return Task(
            description=dedent(f"""
                Process the voice input and convert it to accurate text transcription.

                Audio Input: {audio_input}

                Steps:
                1. Analyze audio quality and apply preprocessing if needed
                2. Perform speech recognition to convert audio to text
                3. Validate and correct transcription accuracy
                4. Return the transcribed text with confidence scores
            """),
            agent=agent,
            expected_output="Accurate text transcription of the voice input with confidence metrics"
        )

    def understand_intent_task(self, agent, transcribed_text):
        return Task(
            description=dedent(f"""
                Analyze the transcribed text to understand user intent and extract commands.

                Transcribed Text: {transcribed_text}

                Steps:
                1. Parse the text using NLP techniques
                2. Identify the main intent and action requested
                3. Extract entities and parameters
                4. Classify the command type (query, action, conversation)
                5. Return structured intent data
            """),
            agent=agent,
            expected_output="Structured intent data with action type, entities, and parameters"
        )

    def generate_response_task(self, agent, intent_data, response_text):
        return Task(
            description=dedent(f"""
                Generate a natural voice response based on the intent and response content.

                Intent Data: {intent_data}
                Response Text: {response_text}

                Steps:
                1. Analyze the response context and tone requirements
                2. Format the text for natural speech synthesis
                3. Apply appropriate prosody and emotion
                4. Generate high-quality voice output
                5. Return the synthesized audio
            """),
            agent=agent,
            expected_output="Natural-sounding synthesized voice response"
        )

    def manage_conversation_task(self, agent, conversation_history, current_input):
        return Task(
            description=dedent(f"""
                Manage the ongoing conversation by maintaining context and flow.

                Conversation History: {conversation_history}
                Current Input: {current_input}

                Steps:
                1. Review conversation history for context
                2. Integrate current input with previous exchanges
                3. Determine appropriate response strategy
                4. Manage turn-taking and interruptions
                5. Update conversation state
            """),
            agent=agent,
            expected_output="Conversation state update with recommended next actions"
        )
