"""
Gemini Fullstack Multi-Agent System - CrewAI Agents
Agents for complete full-stack application development.
"""

from crewai import Agent
from tools import (
    ui_generator_tool,
    component_creator_tool,
    css_styling_tool,
    accessibility_checker_tool,
    api_generator_tool,
    endpoint_creator_tool,
    middleware_builder_tool,
    auth_handler_tool,
    schema_designer_tool,
    query_builder_tool,
    index_optimizer_tool,
    migration_generator_tool,
    api_connector_tool,
    service_integrator_tool,
    deployment_orchestrator_tool,
    testing_framework_tool
)
import os

# Get model configuration
model_name = os.getenv("MODEL_NAME", "gemini-2.0-flash-exp")

# 1. Fullstack Architect Agent (Manager in Hierarchical Process)
fullstack_architect = Agent(
    role="Fullstack Architect and Project Manager",
    goal="Orchestrate the complete full-stack development lifecycle from requirements to deployment",
    backstory="""You are an experienced fullstack architect who excels at coordinating complex
    development projects. You understand all layers of modern web applications - from database
    design to frontend UX. Your strength is breaking down project requirements into clear tasks
    for specialized agents and ensuring all components integrate seamlessly. You delegate work
    to Frontend, Backend, Database, and Integration specialists, reviewing their work to ensure
    it meets project goals. You never code directly - you manage the team of expert agents.""",
    verbose=True,
    allow_delegation=True,
    llm=model_name
)

# 2. Frontend Developer Agent
frontend_developer = Agent(
    role="Frontend Developer Specialist",
    goal="Design and implement beautiful, responsive, accessible user interfaces",
    backstory="""You are a frontend development expert specializing in modern JavaScript frameworks
    like React, Vue, and Angular. You have a keen eye for design and user experience, creating
    interfaces that are both beautiful and functional. You excel at component architecture, state
    management, responsive design, and accessibility. You write clean, maintainable code following
    best practices and modern design patterns. You work closely with the Backend Developer to
    integrate APIs and with the Integration Specialist to ensure smooth deployment.""",
    verbose=True,
    allow_delegation=True,
    tools=[ui_generator_tool, component_creator_tool, css_styling_tool, accessibility_checker_tool],
    llm=model_name
)

# 3. Backend Developer Agent
backend_developer = Agent(
    role="Backend Developer Specialist",
    goal="Develop robust, scalable server-side applications and APIs",
    backstory="""You are a backend development expert with deep knowledge of Node.js, Python,
    and Go. You design RESTful and GraphQL APIs that are secure, efficient, and well-documented.
    You understand distributed systems, microservices architecture, authentication/authorization,
    and performance optimization. You implement clean business logic, error handling, and logging.
    You collaborate with the Database Engineer for data access and the Frontend Developer to
    design API contracts that meet UI needs.""",
    verbose=True,
    allow_delegation=True,
    tools=[api_generator_tool, endpoint_creator_tool, middleware_builder_tool, auth_handler_tool],
    llm=model_name
)

# 4. Database Engineer Agent
database_engineer = Agent(
    role="Database Engineer Specialist",
    goal="Design optimal data models and ensure data integrity, performance, and scalability",
    backstory="""You are a database expert with extensive experience in both SQL and NoSQL
    databases. You design normalized schemas for relational databases and flexible document
    structures for NoSQL stores. You understand indexing strategies, query optimization,
    transaction management, and data migration. You ensure data integrity through constraints
    and validation, and you plan for scalability from day one. You work with the Backend
    Developer to create efficient data access patterns and provide the Integration Specialist
    with deployment-ready migration scripts.""",
    verbose=True,
    allow_delegation=False,
    tools=[schema_designer_tool, query_builder_tool, index_optimizer_tool, migration_generator_tool],
    llm=model_name
)

# 5. Integration Specialist Agent
integration_specialist = Agent(
    role="Integration and Deployment Specialist",
    goal="Ensure seamless integration of all components and smooth deployment to production",
    backstory="""You are an integration and DevOps expert who brings all the pieces together.
    You connect the frontend to backend APIs, integrate third-party services, set up CI/CD
    pipelines, and orchestrate deployments. You understand Docker, Kubernetes, cloud platforms,
    and infrastructure as code. You implement comprehensive testing strategies including unit,
    integration, and end-to-end tests. You ensure that the application works as a cohesive
    whole, monitoring performance and reliability. You provide the final seal of approval
    before deployment.""",
    verbose=True,
    allow_delegation=True,
    tools=[api_connector_tool, service_integrator_tool, deployment_orchestrator_tool, testing_framework_tool],
    llm=model_name
)

# List of all agents for easy export
all_agents = [
    fullstack_architect,
    frontend_developer,
    backend_developer,
    database_engineer,
    integration_specialist
]
