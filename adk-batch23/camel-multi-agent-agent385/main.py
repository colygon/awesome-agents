#!/usr/bin/env python3
"""
CAMEL Multi-Agent Framework - CrewAI Implementation
Communicative Agents for Mind Exploration of Large Language Models

Implements role-playing scenarios where AI agents collaborate on tasks
through structured communication and reasoning.
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, FileReadTool
from langchain_openai import ChatOpenAI
import datetime

# Initialize OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.8,  # Higher temperature for creative collaboration
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize tools
search_tool = SerperDevTool()
file_tool = FileReadTool()

def create_camel_agents(task_domain: str, ai_user_role: str, ai_assistant_role: str):
    """
    Create CAMEL-style role-playing agents

    Args:
        task_domain: Domain of the task (e.g., "software development", "research", "business")
        ai_user_role: Role for the user agent (e.g., "Product Manager", "Researcher")
        ai_assistant_role: Role for the assistant agent (e.g., "Software Engineer", "Data Analyst")
    """

    # AI User Agent - Initiates and guides the conversation
    user_agent = Agent(
        role=ai_user_role,
        goal=f"Guide the collaboration as a {ai_user_role} to accomplish the task",
        backstory=f"""You are an experienced {ai_user_role} working in {task_domain}.
        Your role is to:
        - Define requirements and specifications
        - Ask clarifying questions
        - Provide feedback and direction
        - Ensure the solution meets objectives
        - Think from a strategic perspective

        You collaborate with a {ai_assistant_role} to accomplish complex tasks.
        You communicate clearly and provide constructive guidance.""",
        verbose=True,
        allow_delegation=True,
        tools=[search_tool],
        llm=llm
    )

    # AI Assistant Agent - Executes and implements solutions
    assistant_agent = Agent(
        role=ai_assistant_role,
        goal=f"Execute tasks as a {ai_assistant_role} based on requirements",
        backstory=f"""You are a skilled {ai_assistant_role} working in {task_domain}.
        Your role is to:
        - Understand requirements thoroughly
        - Propose and implement solutions
        - Explain your approach and reasoning
        - Ask for clarification when needed
        - Deliver high-quality work

        You work collaboratively with a {ai_user_role} who provides guidance.
        You are proactive, detail-oriented, and solution-focused.""",
        verbose=True,
        allow_delegation=True,
        tools=[search_tool, file_tool],
        llm=llm
    )

    # Critic Agent - Evaluates and provides feedback
    critic_agent = Agent(
        role="Solution Critic and Quality Assurance",
        goal="Evaluate solutions objectively and provide constructive feedback",
        backstory=f"""You are an impartial critic and quality assurance expert in {task_domain}.
        Your role is to:
        - Evaluate proposed solutions objectively
        - Identify potential issues and edge cases
        - Suggest improvements
        - Ensure quality standards are met
        - Provide constructive, actionable feedback

        You help the {ai_user_role} and {ai_assistant_role} produce the best
        possible outcomes through thoughtful critique.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    return user_agent, assistant_agent, critic_agent


def run_camel_collaboration(
    task_description: str,
    task_domain: str = "software development",
    user_role: str = "Product Manager",
    assistant_role: str = "Software Engineer"
) -> dict:
    """
    Run a CAMEL-style collaborative task

    Args:
        task_description: Description of the task to accomplish
        task_domain: Domain of the task
        user_role: Role for the user agent
        assistant_role: Role for the assistant agent

    Returns:
        dict with collaboration results
    """

    user_agent, assistant_agent, critic_agent = create_camel_agents(
        task_domain, user_role, assistant_role
    )

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Task 1: User Agent defines requirements
    requirements_task = Task(
        description=f"""As a {user_role}, analyze this task and define clear requirements:

        Task: {task_description}
        Domain: {task_domain}

        Your responsibilities:
        1. Break down the task into specific requirements
        2. Identify key objectives and success criteria
        3. Highlight important constraints or considerations
        4. Define the scope and deliverables
        5. Ask clarifying questions if needed

        Provide a comprehensive requirements specification.""",
        agent=user_agent,
        expected_output="Detailed requirements specification for the task"
    )

    # Task 2: Assistant Agent proposes solution
    solution_task = Task(
        description=f"""As a {assistant_role}, propose a solution to address the requirements:

        Based on the requirements specification, develop a comprehensive solution that:
        1. Addresses all specified requirements
        2. Explains your approach and methodology
        3. Outlines implementation steps
        4. Identifies potential challenges
        5. Provides concrete examples or code if applicable

        Use web search if you need current information or best practices.
        Date: {current_date}

        Deliver a detailed solution proposal.""",
        agent=assistant_agent,
        expected_output="Comprehensive solution proposal with implementation details",
        context=[requirements_task]
    )

    # Task 3: Critic evaluates solution
    critique_task = Task(
        description=f"""Evaluate the proposed solution objectively:

        Review the requirements and proposed solution. Provide:
        1. Strengths of the solution
        2. Potential weaknesses or gaps
        3. Edge cases not addressed
        4. Suggestions for improvement
        5. Risk assessment
        6. Overall quality rating (1-10)

        Be constructive and specific in your feedback.""",
        agent=critic_agent,
        expected_output="Detailed critique with specific improvement suggestions",
        context=[requirements_task, solution_task]
    )

    # Task 4: Assistant Agent refines solution
    refinement_task = Task(
        description=f"""As a {assistant_role}, refine your solution based on the critique:

        Address the feedback provided by incorporating:
        1. Improvements suggested in the critique
        2. Solutions to identified edge cases
        3. Mitigation for identified risks
        4. Enhanced explanations where needed
        5. Additional examples or details

        Deliver the refined, final solution.""",
        agent=assistant_agent,
        expected_output="Final refined solution addressing all feedback",
        context=[solution_task, critique_task]
    )

    # Task 5: User Agent validates final solution
    validation_task = Task(
        description=f"""As a {user_role}, validate the final solution:

        Review the refined solution and:
        1. Verify all requirements are met
        2. Assess quality and completeness
        3. Confirm it aligns with objectives
        4. Identify any remaining concerns
        5. Provide final approval or request changes

        Deliver final validation and approval status.""",
        agent=user_agent,
        expected_output="Final validation and approval of the solution",
        context=[requirements_task, refinement_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[user_agent, assistant_agent, critic_agent],
        tasks=[requirements_task, solution_task, critique_task, refinement_task, validation_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "requirements": requirements_task.output.raw if hasattr(requirements_task, 'output') else "",
        "initial_solution": solution_task.output.raw if hasattr(solution_task, 'output') else "",
        "critique": critique_task.output.raw if hasattr(critique_task, 'output') else "",
        "final_solution": refinement_task.output.raw if hasattr(refinement_task, 'output') else "",
        "validation": str(result),
        "metadata": {
            "task_domain": task_domain,
            "user_role": user_role,
            "assistant_role": assistant_role,
            "date": current_date
        }
    }


def save_collaboration_output(content: str, filename: str):
    """Save collaboration output to file"""
    if not filename.endswith('.md'):
        filename += '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nCollaboration output saved to: {filename}")


if __name__ == "__main__":
    print("CAMEL Multi-Agent Framework - CrewAI")
    print("=" * 60)
    print("Communicative Agents for Mind Exploration")
    print("=" * 60)

    # Get task information
    print("\nDefine the collaborative task:")
    task = input("\nEnter task description: ").strip()
    if not task:
        task = "Design and implement a real-time chat application with user authentication"

    domain = input("Enter task domain [software development]: ").strip()
    if not domain:
        domain = "software development"

    user_role = input("Enter user agent role [Product Manager]: ").strip()
    if not user_role:
        user_role = "Product Manager"

    assistant_role = input("Enter assistant agent role [Software Engineer]: ").strip()
    if not assistant_role:
        assistant_role = "Software Engineer"

    print(f"\nTask: {task}")
    print(f"Domain: {domain}")
    print(f"User Role: {user_role}")
    print(f"Assistant Role: {assistant_role}")
    print("\nStarting CAMEL collaboration...\n")

    # Run collaboration
    result = run_camel_collaboration(task, domain, user_role, assistant_role)

    # Display results
    print("\n" + "=" * 60)
    print("CAMEL COLLABORATION COMPLETE")
    print("=" * 60)

    print("\n--- Requirements ---")
    print(result["requirements"])

    print("\n--- Initial Solution ---")
    print(result["initial_solution"])

    print("\n--- Critique ---")
    print(result["critique"])

    print("\n--- Final Solution ---")
    print(result["final_solution"])

    print("\n--- Validation ---")
    print(result["validation"])

    # Save option
    save = input("\n\nSave collaboration to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without .md extension): ").strip()
        if filename:
            full_output = f"""# CAMEL Collaboration Output

**Task**: {task}
**Domain**: {domain}
**User Role**: {user_role}
**Assistant Role**: {assistant_role}

## Requirements
{result["requirements"]}

## Initial Solution
{result["initial_solution"]}

## Critique
{result["critique"]}

## Final Solution
{result["final_solution"]}

## Validation
{result["validation"]}
"""
            save_collaboration_output(full_output, filename)
