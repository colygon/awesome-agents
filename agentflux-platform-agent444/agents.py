from crewai import Agent
from tools import (
    agent_orchestrator,
    workflow_manager,
    agent_registry,
    communication_router,
    performance_monitor
)

class AgentFluxAgents:
    def orchestration_agent(self):
        return Agent(
            role='Agent Orchestrator',
            goal='Coordinate and manage multi-agent workflows',
            backstory="""You are an expert in agent orchestration and workflow
            management. You coordinate multiple agents, manage their interactions,
            and ensure efficient execution of complex multi-agent tasks.""",
            tools=[agent_orchestrator, workflow_manager],
            verbose=True,
            allow_delegation=True
        )

    def registry_manager_agent(self):
        return Agent(
            role='Agent Registry Manager',
            goal='Manage agent registration, discovery, and lifecycle',
            backstory="""You are responsible for managing the agent registry.
            You handle agent registration, maintain agent metadata, enable
            agent discovery, and manage agent lifecycle states.""",
            tools=[agent_registry, performance_monitor],
            verbose=True,
            allow_delegation=False
        )

    def communication_agent(self):
        return Agent(
            role='Communication Router',
            goal='Route and manage inter-agent communication',
            backstory="""You are a communication specialist who manages message
            routing between agents. You ensure reliable message delivery,
            handle communication protocols, and maintain message queues.""",
            tools=[communication_router, agent_registry],
            verbose=True,
            allow_delegation=False
        )

    def workflow_designer_agent(self):
        return Agent(
            role='Workflow Designer',
            goal='Design and optimize agent workflows',
            backstory="""You are a workflow design expert who creates efficient
            multi-agent workflows. You analyze requirements, design agent
            interactions, and optimize workflow execution.""",
            tools=[workflow_manager, agent_orchestrator],
            verbose=True,
            allow_delegation=True
        )

    def monitoring_agent(self):
        return Agent(
            role='Performance Monitor',
            goal='Monitor agent performance and system health',
            backstory="""You are a monitoring specialist who tracks agent
            performance, system metrics, and health indicators. You identify
            bottlenecks and optimization opportunities.""",
            tools=[performance_monitor, agent_registry],
            verbose=True,
            allow_delegation=False
        )
