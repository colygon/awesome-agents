from crewai import Task
from textwrap import dedent

class AgentFluxTasks:
    def orchestrate_workflow_task(self, agent, workflow_definition):
        return Task(
            description=dedent(f"""
                Orchestrate the execution of a multi-agent workflow.

                Workflow Definition: {workflow_definition}

                Steps:
                1. Parse workflow definition
                2. Identify required agents and their roles
                3. Create execution plan
                4. Coordinate agent activation and task assignment
                5. Monitor workflow progress
            """),
            agent=agent,
            expected_output="Workflow orchestration plan with execution status"
        )

    def manage_agent_registry_task(self, agent, agent_info):
        return Task(
            description=dedent(f"""
                Manage agent registration and lifecycle in the registry.

                Agent Information: {agent_info}

                Steps:
                1. Validate agent information
                2. Register agent in the registry
                3. Update agent metadata
                4. Enable agent discovery
                5. Track agent status
            """),
            agent=agent,
            expected_output="Agent registry status with registration confirmation"
        )

    def route_communications_task(self, agent, message_data):
        return Task(
            description=dedent(f"""
                Route communications between agents in the platform.

                Message Data: {message_data}

                Steps:
                1. Parse message and identify recipients
                2. Validate message format
                3. Route message to appropriate agents
                4. Handle delivery confirmation
                5. Manage retry logic for failures
            """),
            agent=agent,
            expected_output="Communication routing report with delivery status"
        )

    def design_workflow_task(self, agent, requirements):
        return Task(
            description=dedent(f"""
                Design an optimized multi-agent workflow.

                Requirements: {requirements}

                Steps:
                1. Analyze workflow requirements
                2. Identify necessary agent types
                3. Design agent interaction patterns
                4. Create workflow diagram
                5. Optimize for performance and reliability
            """),
            agent=agent,
            expected_output="Detailed workflow design with agent interactions"
        )

    def monitor_performance_task(self, agent, system_metrics):
        return Task(
            description=dedent(f"""
                Monitor agent and system performance.

                System Metrics: {system_metrics}

                Steps:
                1. Collect performance metrics
                2. Analyze agent execution times
                3. Identify bottlenecks
                4. Generate performance report
                5. Recommend optimizations
            """),
            agent=agent,
            expected_output="Performance analysis report with recommendations"
        )
