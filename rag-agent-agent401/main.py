#!/usr/bin/env python
"""
RAG Agent CrewAI Main Application
Migrated from Google ADK to CrewAI
"""

import sys
from crewai import Crew, Process
from agents import document_retriever, query_analyzer, answer_synthesizer
from tasks import create_tasks, create_simple_task


def run_rag_agent(user_query: str, mode: str = "simple"):
    """
    Run the RAG agent to answer user queries

    Args:
        user_query: User's question
        mode: "simple" for single-agent or "multi" for multi-agent workflow

    Returns:
        Answer with citations
    """

    print("\n" + "="*80)
    print("RAG AGENT - CrewAI Edition")
    print("="*80)
    print(f"\nQuery: {user_query}\n")

    if mode == "multi":
        # Multi-agent workflow
        print("Running multi-agent workflow...")
        tasks = create_tasks(user_query)
        crew = Crew(
            agents=[query_analyzer, document_retriever, answer_synthesizer],
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )
    else:
        # Simple single-agent workflow
        print("Running simple RAG workflow...")
        tasks = create_simple_task(user_query)
        crew = Crew(
            agents=[document_retriever],
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )

    # Execute the workflow
    result = crew.kickoff()

    print("\n" + "="*80)
    print("ANSWER")
    print("="*80)
    print("\n" + str(result))

    return result


def interactive_mode():
    """Run RAG agent in interactive chat mode"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║              RAG AGENT - CrewAI Edition                       ║
    ║                                                               ║
    ║  Ask questions about your document corpus                    ║
    ║  Type 'quit' or 'exit' to end session                        ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    print("Welcome! I am a Documentation Assistant with access to your knowledge base.")
    print("You can ask me questions about the documents in the corpus.\n")

    while True:
        try:
            query = input("\n> ").strip()

            if not query:
                continue

            if query.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye!")
                break

            # Run RAG agent
            run_rag_agent(query, mode="simple")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

        except Exception as e:
            print(f"\nError: {str(e)}")


def main():
    """Main entry point for the application"""

    if len(sys.argv) > 1:
        # Command line query
        query = " ".join(sys.argv[1:])
        mode = "multi" if "--multi" in sys.argv else "simple"

        try:
            run_rag_agent(query, mode=mode)
        except Exception as e:
            print(f"\nError: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
