"""
Gemini Fullstack Multi-Agent System - CrewAI Main
Hierarchical multi-agent system for complete full-stack application development.
"""

from crewai import Crew, Process
from agents import all_agents, fullstack_architect
from tasks import (
    create_fullstack_development_tasks,
    create_todo_app_tasks,
    create_ecommerce_tasks,
    create_dashboard_tasks
)
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

def run_fullstack_crew(project_requirements: str, project_name: str = "Custom Project"):
    """
    Run the Fullstack CrewAI system with hierarchical process.

    Args:
        project_requirements: Complete project requirements
        project_name: Name of the project for logging

    Returns:
        Crew execution result
    """
    print(f"\n{'='*80}")
    print(f"Gemini Fullstack Development System - {project_name}")
    print(f"{'='*80}\n")
    print(f"Project Requirements:\n{project_requirements}\n")

    # Create tasks for this project
    tasks = create_fullstack_development_tasks(project_requirements)

    # Create crew with hierarchical process
    # The fullstack_architect acts as the manager in hierarchical mode
    crew = Crew(
        agents=all_agents,
        tasks=tasks,
        process=Process.hierarchical,
        manager_agent=fullstack_architect,
        verbose=True
    )

    # Execute the crew
    print(f"\n{'='*80}")
    print("Starting Hierarchical Fullstack Development...")
    print(f"{'='*80}\n")

    result = crew.kickoff()

    print(f"\n{'='*80}")
    print("Fullstack Development Complete")
    print(f"{'='*80}\n")
    print("Final Deliverables:")
    print(result)
    print(f"\n{'='*80}\n")

    return result


def main():
    """Main entry point for the Gemini Fullstack CrewAI system."""

    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║         Gemini Fullstack Multi-Agent Development System                 ║
║                         CrewAI Edition                                   ║
║                                                                          ║
║    Complete Stack Development: Frontend → Backend → Database → Deploy   ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
    """)

    print("\n" + "="*80)
    print("DEMONSTRATION PROJECTS")
    print("="*80)
    print("""
Select a demonstration project:

1. Todo List Application
   - Modern task management app
   - User authentication
   - Real-time updates
   - Mobile-responsive design

2. E-commerce Platform
   - Product catalog with search
   - Shopping cart and checkout
   - Payment integration (Stripe)
   - Admin dashboard

3. Analytics Dashboard
   - Real-time data visualization
   - Interactive charts and graphs
   - Export capabilities
   - Role-based access control

4. Custom Project
   - Enter your own requirements

0. Exit
    """)

    choice = input("\nSelect project (0-4): ").strip()

    if choice == "0":
        print("\nExiting. Thank you for using Gemini Fullstack Development System!")
        return

    elif choice == "1":
        print("\n" + "="*80)
        print("BUILDING: Todo List Application")
        print("="*80)
        tasks = create_todo_app_tasks()
        crew = Crew(
            agents=all_agents,
            tasks=tasks,
            process=Process.hierarchical,
            manager_agent=fullstack_architect,
            verbose=True
        )
        result = crew.kickoff()

    elif choice == "2":
        print("\n" + "="*80)
        print("BUILDING: E-commerce Platform")
        print("="*80)
        tasks = create_ecommerce_tasks()
        crew = Crew(
            agents=all_agents,
            tasks=tasks,
            process=Process.hierarchical,
            manager_agent=fullstack_architect,
            verbose=True
        )
        result = crew.kickoff()

    elif choice == "3":
        print("\n" + "="*80)
        print("BUILDING: Analytics Dashboard")
        print("="*80)
        tasks = create_dashboard_tasks()
        crew = Crew(
            agents=all_agents,
            tasks=tasks,
            process=Process.hierarchical,
            manager_agent=fullstack_architect,
            verbose=True
        )
        result = crew.kickoff()

    elif choice == "4":
        print("\n" + "="*80)
        print("CUSTOM PROJECT")
        print("="*80)
        print("\nEnter your project requirements (type 'DONE' on a new line when finished):")

        requirements = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            requirements.append(line)

        project_req = '\n'.join(requirements)
        result = run_fullstack_crew(project_req, "Custom Project")

    else:
        print("\nInvalid selection. Exiting.")
        return

    # Summary
    print("\n" + "="*80)
    print("FULLSTACK DEVELOPMENT SUMMARY")
    print("="*80)
    print(f"""
The Fullstack Development System demonstrates:
1. ✓ Hierarchical multi-agent coordination
2. ✓ Specialized agents for each stack layer
3. ✓ Parallel development of frontend, backend, and database
4. ✓ Seamless integration across components
5. ✓ Comprehensive testing and deployment preparation
6. ✓ Manager-led architecture with expert delegation

Deliverables:
- Frontend application (React/Vue components)
- Backend API (RESTful endpoints with auth)
- Database schema (with migrations and indexes)
- Integration layer (API connectors and services)
- Test suite (unit, integration, e2e tests)
- Deployment configuration (Docker, Kubernetes)
- Complete documentation

Final Result:
{result}
    """)

    # Interactive mode
    print("\n" + "="*80)
    print("INTERACTIVE MODE")
    print("="*80)
    response = input("\nWould you like to build another project? (y/n): ")

    if response.lower() == 'y':
        main()  # Recursive call to restart
    else:
        print("\nThank you for using Gemini Fullstack Development System!")


if __name__ == "__main__":
    main()
