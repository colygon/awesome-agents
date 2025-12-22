"""CRM Q&A Agent - CrewAI Task Definitions"""
from crewai import Task

def create_query_interpretation_task(agent, user_question: str) -> Task:
    return Task(description=f"Interpret question: {user_question}. Identify data requirements and intent.", expected_output="Query interpretation with data requirements.", agent=agent)

def create_data_retrieval_task(agent, interpretation_output) -> Task:
    return Task(description=f"Retrieve CRM data based on: {interpretation_output}", expected_output="Retrieved CRM data with context.", agent=agent, context=[interpretation_output] if isinstance(interpretation_output, Task) else [])

def create_answer_synthesis_task(agent, interpretation_output, data_output, user_question: str) -> Task:
    return Task(description=f"Synthesize answer for: {user_question}. Using: {interpretation_output}, Data: {data_output}", expected_output="Comprehensive answer with insights.", agent=agent, context=[interpretation_output, data_output] if isinstance(interpretation_output, Task) else [])
