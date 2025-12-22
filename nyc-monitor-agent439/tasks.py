"""NYC Monitor - CrewAI Task Definitions"""
from crewai import Task

def create_data_collection_task(agent, data_sources: list) -> Task:
    return Task(description=f"Collect data from NYC sources: {', '.join(data_sources)}. Aggregate and clean data.", expected_output="Collected and cleaned NYC data.", agent=agent)

def create_trend_analysis_task(agent, collection_output) -> Task:
    return Task(description=f"Analyze trends in collected data: {collection_output}", expected_output="Trend analysis report with insights.", agent=agent, context=[collection_output] if isinstance(collection_output, Task) else [])

def create_alert_generation_task(agent, collection_output, analysis_output) -> Task:
    return Task(description=f"Generate alerts based on data and analysis. Data: {collection_output}, Analysis: {analysis_output}", expected_output="Alert notifications with context.", agent=agent, context=[collection_output, analysis_output] if isinstance(collection_output, Task) else [])
