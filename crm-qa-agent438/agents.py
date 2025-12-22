"""
CRM Q&A Agent - CrewAI Agent Definitions
Multi-Agent CRM Question Answering System

Agents for CRM data querying and analysis:
1. Query Interpreter - Interprets user questions about CRM data
2. Data Retriever - Retrieves relevant CRM data
3. Answer Synthesizer - Synthesizes comprehensive answers
"""

from crewai import Agent
from textwrap import dedent

def create_query_interpreter() -> Agent:
    return Agent(role="Query Interpreter", goal="Interpret natural language questions about CRM data",
        backstory="Expert in natural language understanding and CRM systems.", verbose=True, allow_delegation=False, memory=True)

def create_data_retriever() -> Agent:
    return Agent(role="Data Retriever", goal="Retrieve relevant CRM data efficiently",
        backstory="Database expert with deep knowledge of CRM schemas and data relationships.", verbose=True, allow_delegation=False, memory=True)

def create_answer_synthesizer() -> Agent:
    return Agent(role="Answer Synthesizer", goal="Synthesize comprehensive answers from CRM data",
        backstory="Communication specialist who transforms data into clear, actionable insights.", verbose=True, allow_delegation=False, memory=True)
