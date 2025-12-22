"""
CrewAI Agents for Code Review Assistant
Specialized agents for comprehensive code review and analysis
"""

from crewai import Agent
from crewai_tools import FileReadTool, CodeDocsSearchTool
import os


class CodeReviewAgents:
    """Factory class for creating code review agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def code_analyzer(self) -> Agent:
        """Code Analysis Agent"""
        return Agent(
            role='Code Quality Analyst',
            goal='Analyze code for quality issues, bugs, code smells, and adherence to best practices',
            backstory='You are a senior software engineer with expertise in code quality, static analysis, and software craftsmanship.',
            verbose=True,
            allow_delegation=False,
            tools=[FileReadTool()],
            llm='gpt-4o'
        )

    def security_reviewer(self) -> Agent:
        """Security Review Agent"""
        return Agent(
            role='Security Code Reviewer',
            goal='Identify security vulnerabilities, injection risks, and security anti-patterns in code',
            backstory='You are a security expert specializing in secure coding practices and vulnerability assessment.',
            verbose=True,
            allow_delegation=False,
            tools=[FileReadTool()],
            llm='gpt-4o'
        )

    def performance_reviewer(self) -> Agent:
        """Performance Review Agent"""
        return Agent(
            role='Performance Optimization Specialist',
            goal='Identify performance bottlenecks, inefficient algorithms, and optimization opportunities',
            backstory='You excel at performance analysis and optimization with deep knowledge of algorithmic complexity.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def style_checker(self) -> Agent:
        """Style and Convention Checker Agent"""
        return Agent(
            role='Code Style Specialist',
            goal='Ensure code follows style guides, naming conventions, and formatting standards',
            backstory='You are meticulous about code consistency, readability, and adherence to team standards.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )
