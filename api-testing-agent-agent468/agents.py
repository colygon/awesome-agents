"""
CrewAI Agents for API Testing
Specialized agents for comprehensive API testing and validation
"""

from crewai import Agent
import os


class APITestingAgents:
    """Factory class for creating API testing agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def test_designer(self) -> Agent:
        """Test Design Agent"""
        return Agent(
            role='API Test Designer',
            goal='Design comprehensive test suites covering functional, edge case, and error scenarios for APIs',
            backstory='You are a QA expert specializing in API testing with deep knowledge of RESTful and GraphQL APIs.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def endpoint_validator(self) -> Agent:
        """Endpoint Validation Agent"""
        return Agent(
            role='API Endpoint Validator',
            goal='Validate API endpoints for correct responses, status codes, and data formats',
            backstory='You excel at validating API contracts and ensuring endpoints meet specifications.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def performance_tester(self) -> Agent:
        """Performance Testing Agent"""
        return Agent(
            role='API Performance Tester',
            goal='Test API performance, load handling, and response times under various conditions',
            backstory='You specialize in performance testing and identifying bottlenecks in API systems.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def integration_tester(self) -> Agent:
        """Integration Testing Agent"""
        return Agent(
            role='API Integration Tester',
            goal='Test API integrations, authentication flows, and end-to-end workflows',
            backstory='You are skilled at testing complex API integrations and multi-step workflows.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )
