"""
CrewAI Agents for Event Planner - Agent 481
Multi-agent system for comprehensive event planning
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_venue_coordinator_agent(llm):
    """
    Agent 1: Venue Coordinator - Specializes in venue selection and logistics
    """
    return Agent(
        role='Venue Coordination Specialist',
        goal='Find and evaluate suitable venues based on event requirements, budget, and guest capacity',
        backstory="""You are an experienced venue coordinator with extensive knowledge of
        event spaces, logistics, and venue management. You excel at matching events with
        perfect venues by considering factors like location, capacity, amenities, accessibility,
        parking, catering options, and budget constraints. You have strong relationships with
        venue managers and understand contract negotiations, booking procedures, and venue
        layout optimization for different event types.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_schedule_planner_agent(llm):
    """
    Agent 2: Schedule Planner - Creates detailed event timelines and schedules
    """
    return Agent(
        role='Event Timeline Specialist',
        goal='Design comprehensive event schedules with optimal timing for all activities',
        backstory="""You are a meticulous schedule planner who creates detailed event timelines
        that ensure smooth flow and maximum engagement. You understand event pacing, guest
        psychology, and how to balance different activities. You excel at creating minute-by-minute
        rundowns, coordinating with vendors, planning buffer times, managing transitions between
        activities, and ensuring all critical moments are captured. Your schedules account for
        setup time, guest arrival patterns, meal service, entertainment, and cleanup.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_budget_manager_agent(llm):
    """
    Agent 3: Budget Manager - Manages event finances and cost optimization
    """
    return Agent(
        role='Event Budget Manager',
        goal='Create and optimize event budgets while maximizing value and staying within financial constraints',
        backstory="""You are a financial expert specializing in event budgeting and cost management.
        You excel at creating detailed budget breakdowns, identifying cost-saving opportunities,
        negotiating with vendors, and tracking expenses. You understand industry pricing standards,
        hidden costs, and where to allocate resources for maximum impact. You provide transparent
        budget reports with clear categories including venue, catering, entertainment, decorations,
        staffing, marketing, and contingency funds. You balance quality with cost-effectiveness.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_all_agents(model="gpt-4", temperature=0.7):
    """
    Create all event planning agents with the specified LLM configuration
    """
    llm = ChatOpenAI(
        model=model,
        temperature=temperature
    )

    return {
        'venue_coordinator': create_venue_coordinator_agent(llm),
        'schedule_planner': create_schedule_planner_agent(llm),
        'budget_manager': create_budget_manager_agent(llm)
    }
