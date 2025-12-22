"""
CrewAI Agents for Weather Advisor - Agent 484
Multi-agent system for weather analysis and activity planning
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_weather_analyst_agent(llm):
    """
    Agent 1: Weather Analyst - Interprets weather data and forecasts
    """
    return Agent(
        role='Weather Analysis Specialist',
        goal='Analyze weather conditions, forecasts, and trends to provide accurate weather insights',
        backstory="""You are a meteorologist with expertise in weather pattern analysis,
        forecast interpretation, and atmospheric science. You excel at reading weather data
        including temperature, precipitation, wind, humidity, pressure systems, and radar
        imagery. You understand weather patterns, frontal systems, and how conditions evolve
        over time. You can interpret complex forecasts and translate them into practical
        insights. You track severe weather alerts, seasonal patterns, and microclimates.
        Your analysis helps people understand what weather to expect and why.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_activity_planner_agent(llm):
    """
    Agent 2: Activity Planner - Recommends activities based on weather conditions
    """
    return Agent(
        role='Weather-Based Activity Advisor',
        goal='Suggest appropriate activities and plans based on weather conditions and forecasts',
        backstory="""You are an outdoor activity expert who helps people make the most of
        any weather conditions. You understand how different weather affects various activities
        (outdoor sports, events, gardening, construction, travel, etc.). You excel at suggesting
        indoor alternatives when weather is poor and optimal outdoor activities when conditions
        are favorable. You consider factors like temperature comfort zones, precipitation timing,
        wind conditions, UV index, and air quality. You provide practical advice on what to do,
        what to wear, and when to schedule activities for best conditions.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_preparation_advisor_agent(llm):
    """
    Agent 3: Preparation Advisor - Provides weather preparedness recommendations
    """
    return Agent(
        role='Weather Preparedness Expert',
        goal='Help people prepare for weather conditions with appropriate gear, safety measures, and planning',
        backstory="""You are a safety and preparedness specialist who helps people get ready
        for various weather conditions. You provide detailed advice on what to wear, what gear
        to bring, how to stay safe, and what precautions to take. You understand layering
        strategies for temperature changes, rain gear selection, sun protection, severe weather
        safety, travel preparation, and home protection. You consider specific scenarios like
        commuting, outdoor events, travel, construction work, and emergency situations. Your
        guidance helps people stay comfortable, safe, and prepared for any weather.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_all_agents(model="gpt-4", temperature=0.7):
    """
    Create all weather advisor agents with the specified LLM configuration
    """
    llm = ChatOpenAI(
        model=model,
        temperature=temperature
    )

    return {
        'weather_analyst': create_weather_analyst_agent(llm),
        'activity_planner': create_activity_planner_agent(llm),
        'preparation_advisor': create_preparation_advisor_agent(llm)
    }
