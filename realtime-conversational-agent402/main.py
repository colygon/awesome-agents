#!/usr/bin/env python
"""
Realtime Conversational Agent CrewAI Main Application
Migrated from Google ADK to CrewAI
"""

import sys
from crewai import Crew, Process
from agents import (
    conversation_manager,
    intent_recognizer,
    response_generator,
    knowledge_retriever
)
from tasks import create_tasks


class ConversationalAgent:
    """Main conversational agent class"""

    def __init__(self):
        self.conversation_history = []

    def process_message(self, user_message: str) -> str:
        """
        Process a user message and generate a response

        Args:
            user_message: The message from the user

        Returns:
            The agent's response
        """
        print(f"\n{'='*80}")
        print(f"User: {user_message}")
        print(f"{'='*80}")

        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Create tasks for this conversation turn
        tasks = create_tasks(user_message, self.conversation_history)

        # Create crew
        crew = Crew(
            agents=[
                intent_recognizer,
                knowledge_retriever,
                conversation_manager,
                response_generator
            ],
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )

        # Execute the conversational workflow
        print("\nProcessing your message...\n")
        result = crew.kickoff()

        # Extract the response (the final task output)
        response = str(result)

        # Add assistant response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })

        print(f"\n{'='*80}")
        print(f"Assistant: {response}")
        print(f"{'='*80}\n")

        return response

    def get_conversation_history(self):
        """Return the conversation history"""
        return self.conversation_history

    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
        print("Conversation history cleared.")


def interactive_mode():
    """Run the agent in interactive chat mode"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║       REALTIME CONVERSATIONAL AGENT - CrewAI Edition          ║
    ║                                                               ║
    ║  An intelligent conversational agent that understands        ║
    ║  context and provides helpful, natural responses             ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    print("Welcome! I'm your conversational AI assistant.")
    print("I can help you with questions, tasks, and general conversation.")
    print("\nCommands:")
    print("  - Type your message to chat")
    print("  - 'history' to see conversation history")
    print("  - 'clear' to clear conversation history")
    print("  - 'quit' or 'exit' to end the session")
    print(f"\n{'='*80}\n")

    agent = ConversationalAgent()

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            # Handle special commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nThank you for chatting! Goodbye!")
                break

            elif user_input.lower() == 'history':
                print("\n--- Conversation History ---")
                for i, turn in enumerate(agent.get_conversation_history(), 1):
                    print(f"\n{i}. {turn['role'].upper()}: {turn['content'][:100]}...")
                print(f"\n{'-'*80}\n")
                continue

            elif user_input.lower() == 'clear':
                agent.clear_history()
                continue

            # Process the message
            agent.process_message(user_input)

        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Goodbye!")
            break

        except Exception as e:
            print(f"\nError: {str(e)}")
            import traceback
            traceback.print_exc()


def single_message_mode(message: str):
    """Process a single message"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║       REALTIME CONVERSATIONAL AGENT - CrewAI Edition          ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    agent = ConversationalAgent()
    response = agent.process_message(message)
    return response


def main():
    """Main entry point for the application"""

    if len(sys.argv) > 1:
        # Single message mode - process command line argument
        message = " ".join(sys.argv[1:])
        single_message_mode(message)
    else:
        # Interactive chat mode
        interactive_mode()


if __name__ == "__main__":
    main()
