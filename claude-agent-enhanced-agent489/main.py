"""
Enhanced Multi-Agent System - Main Demo Application
Demonstrates advanced CrewAI patterns: hierarchical workflows, parallel execution, multi-agent collaboration.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process

from agents import (
    create_code_architect,
    create_senior_developer,
    create_code_reviewer,
    create_qa_engineer,
    create_technical_writer,
    create_devops_engineer,
    create_research_analyst,
    EnhancedAgentFactory
)

from tasks import (
    create_architecture_task,
    create_implementation_task,
    create_code_review_task,
    create_testing_task,
    create_documentation_task,
    create_deployment_task,
    create_parallel_review_tasks,
    create_synthesis_task,
    TaskOrchestrator
)

# Load environment variables
load_dotenv()


def demo_hierarchical_workflow():
    """
    Demo 1: Hierarchical Development Workflow
    Architect leads the team, delegates tasks to specialists.
    """
    print("\n" + "="*80)
    print("DEMO 1: Hierarchical Development Workflow")
    print("="*80 + "\n")

    # Create agents
    architect = create_code_architect()
    developer = create_senior_developer()
    reviewer = create_code_reviewer()

    # Create tasks
    project_desc = """Create a simple Python web API for a todo list application.
    Requirements:
    - RESTful endpoints (GET, POST, PUT, DELETE)
    - In-memory data storage
    - Input validation
    - Error handling"""

    tasks = TaskOrchestrator.create_full_development_workflow(
        architect=architect,
        developer=developer,
        reviewer=reviewer,
        qa=create_qa_engineer(),
        writer=create_technical_writer(),
        devops=create_devops_engineer(),
        project_description=project_desc,
        feature_description="RESTful todo API with CRUD operations"
    )

    # Create crew with hierarchical process
    crew = Crew(
        agents=[architect, developer, reviewer, create_qa_engineer(), create_technical_writer(), create_devops_engineer()],
        tasks=tasks,
        process=Process.hierarchical,  # Architect manages and delegates
        manager_agent=architect,  # Architect is the manager
        verbose=True
    )

    print("\nStarting hierarchical workflow with Code Architect as manager...")
    print("The architect will delegate tasks to appropriate specialists.\n")

    result = crew.kickoff()

    print("\n" + "-"*80)
    print("Result:")
    print("-"*80)
    print(result)

    return result


def demo_parallel_execution():
    """
    Demo 2: Parallel Task Execution
    Multiple agents work simultaneously on different aspects.
    """
    print("\n" + "="*80)
    print("DEMO 2: Parallel Review Workflow")
    print("="*80 + "\n")

    # Create specialized review agents
    security_reviewer = create_code_reviewer()
    performance_analyst = create_research_analyst()
    quality_reviewer = create_code_reviewer()
    architect = create_code_architect()

    # Create parallel review tasks
    parallel_tasks = create_parallel_review_tasks(
        security_agent=security_reviewer,
        performance_agent=performance_analyst,
        quality_agent=quality_reviewer,
        file_paths=["tools.py", "agents.py", "tasks.py"]
    )

    # Create synthesis task that waits for all parallel tasks
    synthesis_task = create_synthesis_task(architect, parallel_tasks)

    # Combine tasks
    all_tasks = parallel_tasks + [synthesis_task]

    # Create crew with sequential process (async tasks run in parallel automatically)
    crew = Crew(
        agents=[security_reviewer, performance_analyst, quality_reviewer, architect],
        tasks=all_tasks,
        process=Process.sequential,  # Sequential process, but tasks marked async_execution=True run in parallel
        verbose=True
    )

    print("\nStarting parallel review workflow...")
    print("Three agents will review code simultaneously, then architect will synthesize findings.\n")

    result = crew.kickoff()

    print("\n" + "-"*80)
    print("Result:")
    print("-"*80)
    print(result)

    return result


def demo_collaborative_research():
    """
    Demo 3: Collaborative Research Team
    Multiple analysts research different aspects, writer synthesizes.
    """
    print("\n" + "="*80)
    print("DEMO 3: Collaborative Research Team")
    print("="*80 + "\n")

    # Create research team
    team = EnhancedAgentFactory.create_research_team()
    analyst, architect, writer = team

    # Create tasks
    tasks = [
        create_architecture_task(
            architect,
            "Analyze the current codebase structure and recommend improvements"
        ),
        create_documentation_task(
            writer,
            "Codebase Analysis Report",
            context=[]
        )
    ]

    # Create crew
    crew = Crew(
        agents=team,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nStarting collaborative research...")
    print("Analyst and architect will analyze the codebase, writer will document findings.\n")

    result = crew.kickoff()

    print("\n" + "-"*80)
    print("Result:")
    print("-"*80)
    print(result)

    return result


def demo_full_dev_team():
    """
    Demo 4: Complete Development Team
    All 6 specialists working together.
    """
    print("\n" + "="*80)
    print("DEMO 4: Complete Development Team")
    print("="*80 + "\n")

    # Create full team
    team = EnhancedAgentFactory.create_development_team()

    # Simple feature implementation workflow
    architect = team[0]
    developer = team[1]

    feature_spec = """Implement a data validation utility module.
    Requirements:
    - Email validation
    - Phone number validation
    - Date format validation
    - Strong password validation
    - Input sanitization"""

    tasks = [
        create_architecture_task(architect, feature_spec),
        create_implementation_task(
            developer,
            "utils/validators.py",
            "Data validation functions",
            context=[]
        )
    ]

    # Create crew
    crew = Crew(
        agents=team,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nStarting full development team workflow...")
    print("Complete team from architect to devops will collaborate on the feature.\n")

    result = crew.kickoff()

    print("\n" + "-"*80)
    print("Result:")
    print("-"*80)
    print(result)

    return result


def demo_code_review_scenario():
    """
    Demo 5: Dedicated Code Review Workflow
    Import and run the code review scenario from scenarios/code_review.py
    """
    print("\n" + "="*80)
    print("DEMO 5: Code Review Scenario")
    print("="*80 + "\n")

    try:
        from scenarios.code_review import run_code_review_workflow
        result = run_code_review_workflow()
        return result
    except ImportError:
        print("Code review scenario not yet implemented.")
        print("See scenarios/code_review.py for the full workflow example.")
        return None


def print_menu():
    """Print the interactive menu."""
    print("\n" + "="*80)
    print("Enhanced Multi-Agent System - Demo Menu")
    print("="*80 + "\n")
    print("This demo showcases advanced CrewAI patterns:")
    print("- Hierarchical workflows with delegation")
    print("- Parallel task execution")
    print("- Multi-agent collaboration")
    print("- Specialized agent teams\n")
    print("Available Demos:")
    print("  1. Hierarchical Development Workflow (Architect-led team)")
    print("  2. Parallel Review Workflow (Concurrent code reviews)")
    print("  3. Collaborative Research Team (Analysis and documentation)")
    print("  4. Complete Development Team (All 6 specialists)")
    print("  5. Code Review Scenario (Dedicated review workflow)")
    print("  6. Show Agent Capabilities")
    print("  0. Exit\n")


def show_agent_capabilities():
    """Display information about each specialized agent."""
    print("\n" + "="*80)
    print("Specialized Agents and Their Capabilities")
    print("="*80 + "\n")

    agents_info = [
        ("Code Architect", "System design, task delegation, architectural decisions"),
        ("Senior Developer", "Feature implementation, code writing, refactoring"),
        ("Code Reviewer", "Security analysis, code quality checks, best practices"),
        ("QA Engineer", "Test creation, test execution, quality validation"),
        ("Technical Writer", "Documentation, README files, API docs"),
        ("DevOps Engineer", "CI/CD, deployment, infrastructure automation"),
        ("Research Analyst", "Code analysis, pattern detection, dependency mapping")
    ]

    for name, capabilities in agents_info:
        print(f"• {name}")
        print(f"  Capabilities: {capabilities}\n")

    print("These agents can work:")
    print("- Hierarchically (with a manager delegating tasks)")
    print("- Sequentially (one after another with context sharing)")
    print("- In parallel (multiple agents working simultaneously)")
    print("\nPress Enter to continue...")
    input()


def main():
    """Main entry point with interactive menu."""
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️  WARNING: OPENAI_API_KEY not found in environment!")
        print("Please create a .env file with your OpenAI API key.")
        print("Example: OPENAI_API_KEY=sk-your-key-here\n")
        return

    while True:
        print_menu()
        choice = input("Select a demo (0-6): ").strip()

        if choice == '0':
            print("\nExiting. Thank you for exploring the Enhanced Multi-Agent System!\n")
            break
        elif choice == '1':
            demo_hierarchical_workflow()
        elif choice == '2':
            demo_parallel_execution()
        elif choice == '3':
            demo_collaborative_research()
        elif choice == '4':
            demo_full_dev_team()
        elif choice == '5':
            demo_code_review_scenario()
        elif choice == '6':
            show_agent_capabilities()
        else:
            print("\n❌ Invalid choice. Please select 0-6.\n")

        if choice in ['1', '2', '3', '4', '5']:
            input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║         Enhanced Multi-Agent System - Claude Code Agent Migration           ║
║                                                                              ║
║  Demonstrates advanced CrewAI patterns beyond basic SDK feature parity      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    main()
