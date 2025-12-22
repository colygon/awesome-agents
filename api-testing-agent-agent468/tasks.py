"""CrewAI Tasks for API Testing"""

from crewai import Task
from textwrap import dedent


class APITestingTasks:
    """Factory class for API testing tasks"""

    def design_test_suite(self, agent, api_spec: dict) -> Task:
        return Task(
            description=dedent(f"""
                Design comprehensive API test suite:
                API Spec: {api_spec}

                Design tests for:
                1. Functional correctness
                2. Edge cases and boundary values
                3. Error handling
                4. Input validation
                5. Authentication/authorization
                6. Rate limiting
            """),
            agent=agent,
            expected_output='Complete test suite design with test cases'
        )

    def validate_endpoints(self, agent, endpoints: list) -> Task:
        return Task(
            description=dedent(f"""
                Validate API endpoints:
                Endpoints: {endpoints}

                Validate:
                1. HTTP methods and status codes
                2. Request/response schemas
                3. Headers and content types
                4. Data types and formats
                5. Required vs optional fields
                6. Default values
            """),
            agent=agent,
            expected_output='Endpoint validation report with pass/fail results',
            context=[]
        )

    def test_performance(self, agent, load_config: dict) -> Task:
        return Task(
            description=dedent(f"""
                Perform API performance testing:
                Load Config: {load_config}

                Test:
                1. Response time under normal load
                2. Throughput capacity
                3. Concurrent request handling
                4. Resource usage
                5. Error rates under stress
                6. Recovery and stability
            """),
            agent=agent,
            expected_output='Performance test results with metrics and recommendations',
            context=[]
        )

    def test_integration(self, agent, workflow: dict) -> Task:
        return Task(
            description=dedent(f"""
                Test API integration workflows:
                Workflow: {workflow}

                Test:
                1. Authentication flows
                2. Multi-step workflows
                3. Data consistency
                4. Error propagation
                5. Rollback scenarios
                6. Third-party integrations
            """),
            agent=agent,
            expected_output='Integration test results with workflow coverage',
            context=[]
        )
