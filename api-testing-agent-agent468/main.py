"""API Testing Agent - CrewAI Implementation"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import APITestingAgents
from tasks import APITestingTasks

load_dotenv()


def test_api(api_spec: dict, endpoints: list, load_config: dict, workflow: dict) -> str:
    """Comprehensive API testing"""

    agents = APITestingAgents()
    tasks_factory = APITestingTasks()

    test_designer = agents.test_designer()
    endpoint_validator = agents.endpoint_validator()
    performance_tester = agents.performance_tester()
    integration_tester = agents.integration_tester()

    design_task = tasks_factory.design_test_suite(test_designer, api_spec)
    validate_task = tasks_factory.validate_endpoints(endpoint_validator, endpoints)
    validate_task.context = [design_task]

    performance_task = tasks_factory.test_performance(performance_tester, load_config)
    integration_task = tasks_factory.test_integration(integration_tester, workflow)

    crew = Crew(
        agents=[test_designer, endpoint_validator, performance_tester, integration_tester],
        tasks=[design_task, validate_task, performance_task, integration_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


def main():
    api_spec = {'version': '1.0', 'base_url': 'https://api.example.com'}
    endpoints = ['/users', '/products', '/orders']
    load_config = {'concurrent_users': 100, 'duration': '5m'}
    workflow = {'name': 'checkout_flow', 'steps': ['login', 'add_to_cart', 'checkout']}
    result = test_api(api_spec, endpoints, load_config, workflow)
    print(result)


if __name__ == "__main__":
    main()
