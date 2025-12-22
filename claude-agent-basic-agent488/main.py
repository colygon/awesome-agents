"""
Claude Code Python Agent SDK → CrewAI Migration Demo

This script demonstrates the Basic app showing 1:1 SDK→CrewAI pattern mapping.
Run different demos to see how SDK concepts translate to CrewAI.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import (
    create_query_agent,
    create_stateful_agent,
    create_file_operations_agent,
    create_code_analyst_agent,
    AgentFactory
)
from tasks import (
    create_one_off_task,
    create_conversational_task_sequence,
    create_file_analysis_task,
    TaskBuilder
)


def setup_environment():
    """Load environment variables and check API key."""
    load_dotenv()

    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found in environment.")
        print("Please create a .env file with your API key.")
        print("See .env.example for the required format.")
        return False

    return True


def demo_query_pattern():
    """
    Demo 1: SDK query() → CrewAI Agent + Task

    SDK Equivalent:
    ```python
    async for message in query(
        prompt="List Python files in current directory",
        options=ClaudeAgentOptions(allowed_tools=["Bash", "Glob"])
    ):
        print(message)
    ```
    """
    print("\n" + "="*80)
    print("DEMO 1: query() Pattern → Simple Agent + Task")
    print("="*80 + "\n")

    # Create agent matching query pattern
    agent = create_query_agent()

    # Create one-off task
    task = create_one_off_task(
        agent=agent,
        description="List all Python files in the current directory and subdirectories",
        expected_output="List of Python files with brief summary"
    )

    # Execute with crew
    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n" + "-"*80)
    print("RESULT:")
    print("-"*80)
    print(result)
    print("\n")


def demo_client_pattern():
    """
    Demo 2: SDK ClaudeSDKClient → CrewAI with Memory

    SDK Equivalent:
    ```python
    async with ClaudeSDKClient(options) as client:
        await client.query("What files are in the current directory?")
        await client.query("Now analyze the Python files")  # Has context
    ```
    """
    print("\n" + "="*80)
    print("DEMO 2: ClaudeSDKClient Pattern → Stateful Agent with Memory")
    print("="*80 + "\n")

    # Create stateful agent (has memory=True)
    agent = create_stateful_agent()

    # Create sequence of related tasks
    tasks = create_conversational_task_sequence(
        agent=agent,
        task_descriptions=[
            ("List all files in the current directory", "File listing"),
            ("Now analyze the .py files from that list", "Analysis of Python files"),
            ("Based on the analysis, summarize the project structure", "Project structure summary")
        ]
    )

    # Execute with crew that maintains context
    crew = Crew(
        agents=[agent],
        tasks=tasks,
        process=Process.sequential,
        memory=True,  # Like SDK sessions
        verbose=True
    )

    result = crew.kickoff()

    print("\n" + "-"*80)
    print("FINAL RESULT:")
    print("-"*80)
    print(result)
    print("\n")


def demo_file_operations():
    """
    Demo 3: SDK File Tools → CrewAI File Operations Agent

    SDK Equivalent:
    ```python
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Edit"],
        permission_mode="acceptEdits"
    )
    await query("Create a sample config file", options)
    ```
    """
    print("\n" + "="*80)
    print("DEMO 3: File Operations Pattern")
    print("="*80 + "\n")

    agent = create_file_operations_agent()

    task = create_one_off_task(
        agent=agent,
        description="""Create a sample configuration file named 'sample_config.txt'
        with the following content:
        - Project name: Claude Agent Demo
        - Version: 1.0.0
        - Framework: CrewAI

        Then read it back to verify.""",
        expected_output="Confirmation that file was created and its contents"
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n" + "-"*80)
    print("RESULT:")
    print("-"*80)
    print(result)
    print("\n")


def demo_code_analysis():
    """
    Demo 4: SDK Code Analysis → CrewAI Code Analyst

    SDK Equivalent:
    ```python
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Glob", "Grep"],
        system_prompt="You are an expert code analyst"
    )
    await query("Analyze Python files for import statements", options)
    ```
    """
    print("\n" + "="*80)
    print("DEMO 4: Code Analysis Pattern")
    print("="*80 + "\n")

    agent = create_code_analyst_agent()

    # Use TaskBuilder for complex task
    builder = TaskBuilder()
    builder.add_code_search(
        agent=agent,
        pattern="^import |^from .* import",
        file_type="*.py"
    )

    tasks = builder.build()

    crew = Crew(
        agents=[agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n" + "-"*80)
    print("RESULT:")
    print("-"*80)
    print(result)
    print("\n")


def demo_sdk_comparison():
    """
    Demo 5: Side-by-side SDK vs CrewAI comparison

    Shows the conceptual mapping between SDK patterns and CrewAI implementation.
    """
    print("\n" + "="*80)
    print("DEMO 5: SDK vs CrewAI Concept Mapping")
    print("="*80 + "\n")

    print("SDK Pattern → CrewAI Pattern Mapping:\n")

    mappings = [
        ("query(prompt, options)", "Agent + Task + Crew.kickoff()"),
        ("ClaudeSDKClient()", "Crew with memory=True"),
        ("ClaudeAgentOptions(allowed_tools=[...])", "Agent(tools=[...])"),
        ("system_prompt", "Agent(role=..., goal=..., backstory=...)"),
        ("agents={...} (subagents)", "Multiple Agent instances with delegation"),
        ("hooks={'PreToolUse': ...}", "Tool wrappers with logging"),
        ("resume=session_id", "Crew memory + cache persistence"),
        ("permission_mode", "Custom tool validation logic"),
    ]

    for sdk, crewai in mappings:
        print(f"  SDK:     {sdk}")
        print(f"  CrewAI:  {crewai}")
        print()

    print("\nKey Differences:")
    print("  • SDK: Async streaming responses")
    print("  • CrewAI: Synchronous result-based execution")
    print()
    print("  • SDK: Session-based memory with IDs")
    print("  • CrewAI: Automatic crew-level memory")
    print()
    print("  • SDK: Single agent with tool delegation")
    print("  • CrewAI: Multi-agent collaboration")
    print()


def main():
    """Main entry point with demo menu."""
    if not setup_environment():
        return

    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║           Claude Code Python Agent SDK → CrewAI Migration Demo              ║
║                          Basic: Feature Parity                               ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

This demo shows 1:1 mappings between SDK patterns and CrewAI implementations.

Available Demos:
  1. query() Pattern → Simple Agent + Task
  2. ClaudeSDKClient Pattern → Stateful Agent with Memory
  3. File Operations → File Operations Agent
  4. Code Analysis → Code Analyst Agent
  5. SDK vs CrewAI Concept Mapping (no execution)
  6. Run all demos
  0. Exit

    """)

    demos = {
        '1': demo_query_pattern,
        '2': demo_client_pattern,
        '3': demo_file_operations,
        '4': demo_code_analysis,
        '5': demo_sdk_comparison,
    }

    while True:
        choice = input("Select demo (0-6): ").strip()

        if choice == '0':
            print("\nExiting. Thank you!")
            break
        elif choice == '6':
            print("\nRunning all demos...\n")
            for demo_func in demos.values():
                try:
                    demo_func()
                    input("\nPress Enter to continue to next demo...")
                except Exception as e:
                    print(f"\nError in demo: {str(e)}")
                    input("\nPress Enter to continue...")
            print("\nAll demos complete!")
            break
        elif choice in demos:
            try:
                demos[choice]()
                input("\nPress Enter to return to menu...")
            except Exception as e:
                print(f"\nError: {str(e)}")
                input("\nPress Enter to continue...")
        else:
            print("Invalid choice. Please select 0-6.")


if __name__ == "__main__":
    main()
