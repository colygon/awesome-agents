"""
Side-by-side Comparison: SDK query() vs CrewAI

This example shows how to convert SDK query() calls to CrewAI patterns.
"""

# ==============================================================================
# SDK PATTERN (Original)
# ==============================================================================

"""
from claude_agent_sdk import query, ClaudeAgentOptions

async def sdk_example():
    # One-off query execution
    async for message in query(
        prompt="List Python files in current directory and analyze their imports",
        options=ClaudeAgentOptions(
            allowed_tools=["Bash", "Glob", "Grep"],
            system_prompt="You are a code analysis expert"
        )
    ):
        if hasattr(message, 'result'):
            print(message.result)

# Usage:
# import asyncio
# asyncio.run(sdk_example())
"""

# ==============================================================================
# CREWAI PATTERN (Migrated)
# ==============================================================================

from crewai import Agent, Task, Crew, Process
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools import bash_command, glob_files, grep_search


def crewai_example():
    """
    CrewAI equivalent of SDK query() pattern.

    Key differences:
    - No async/await needed
    - Agent defined separately from task
    - Explicit crew creation for execution
    - Synchronous result instead of streaming
    """

    # 1. Create agent (maps to SDK system_prompt + allowed_tools)
    agent = Agent(
        role="Code Analysis Expert",
        goal="Analyze code files and their structure",
        backstory="You are an expert at analyzing code structure and dependencies",
        tools=[bash_command, glob_files, grep_search],
        verbose=True
    )

    # 2. Create task (maps to SDK prompt)
    task = Task(
        description="List Python files in current directory and analyze their imports",
        agent=agent,
        expected_output="List of Python files with import analysis"
    )

    # 3. Create and execute crew
    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print("\n" + "="*80)
    print("RESULT:")
    print("="*80)
    print(result)


# ==============================================================================
# COMPARISON TABLE
# ==============================================================================

def print_comparison():
    """
    Print side-by-side comparison of SDK vs CrewAI patterns.
    """
    print("\n" + "="*80)
    print("SDK query() → CrewAI Pattern Mapping")
    print("="*80 + "\n")

    comparison = [
        ("Aspect", "SDK query()", "CrewAI"),
        ("-"*20, "-"*30, "-"*30),
        ("Execution Model", "Async generator (streaming)", "Sync function (result-based)"),
        ("Agent Definition", "Implicit in options", "Explicit Agent object"),
        ("Task Definition", "Prompt string", "Task object with description"),
        ("Tools", "allowed_tools list (strings)", "Tool function objects"),
        ("System Prompt", "system_prompt parameter", "role + goal + backstory"),
        ("Permissions", "permission_mode setting", "No built-in (use tool wrappers)"),
        ("Result", "Stream of messages", "Final result string"),
        ("Memory", "No memory (stateless)", "Optional with memory=True"),
        ("Context Usage", "Returns token usage", "Handled internally"),
    ]

    # Print table
    for row in comparison:
        print(f"{row[0]:<20} | {row[1]:<30} | {row[2]:<30}")

    print("\n")


# ==============================================================================
# MIGRATION STEPS
# ==============================================================================

def print_migration_steps():
    """
    Print step-by-step migration guide.
    """
    print("\n" + "="*80)
    print("Migration Steps: SDK query() → CrewAI")
    print("="*80 + "\n")

    steps = [
        ("Step 1", "Extract System Prompt", "Convert SDK system_prompt to CrewAI Agent role/goal/backstory"),
        ("Step 2", "Map Tools", "Convert SDK allowed_tools strings to CrewAI tool functions"),
        ("Step 3", "Create Agent", "Define Agent with role, goal, backstory, and tools"),
        ("Step 4", "Create Task", "Convert SDK prompt to Task with description and expected_output"),
        ("Step 5", "Create Crew", "Wrap agent and task in Crew for execution"),
        ("Step 6", "Execute", "Call crew.kickoff() instead of iterating over query()"),
        ("Step 7", "Handle Result", "Use synchronous result instead of async messages"),
    ]

    for step_num, step_name, description in steps:
        print(f"{step_num}. {step_name}")
        print(f"   {description}\n")


# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    SDK query() → CrewAI Pattern Example                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

    # Show comparison table
    print_comparison()

    # Show migration steps
    print_migration_steps()

    # Ask if user wants to run the example
    run = input("\nWould you like to run the CrewAI example? (y/n): ").strip().lower()

    if run == 'y':
        print("\nRunning CrewAI example...\n")
        crewai_example()
    else:
        print("\nExample not executed. You can run it by calling crewai_example() directly.")
