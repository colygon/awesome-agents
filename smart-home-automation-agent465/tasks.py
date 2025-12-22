"""CrewAI Tasks for Smart Home Automation"""

from crewai import Task
from textwrap import dedent


class SmartHomeTasks:
    """Factory class for smart home automation tasks"""

    def coordinate_devices(self, agent, devices: list) -> Task:
        return Task(
            description=dedent(f"""
                Coordinate smart home devices:
                Devices: {devices}

                Tasks:
                1. Discover and inventory devices
                2. Establish device connections
                3. Synchronize device states
                4. Handle device failures
                5. Optimize device communication
            """),
            agent=agent,
            expected_output='Device coordination plan with state management'
        )

    def design_automation(self, agent, user_preferences: dict) -> Task:
        return Task(
            description=dedent(f"""
                Design automation routines:
                Preferences: {user_preferences}

                Requirements:
                1. Create morning/evening routines
                2. Design presence-based automation
                3. Implement environmental triggers
                4. Setup scene configurations
                5. Define fallback behaviors
            """),
            agent=agent,
            expected_output='Comprehensive automation routines and triggers',
            context=[]
        )

    def optimize_energy(self, agent, usage_data: dict = None) -> Task:
        return Task(
            description=dedent(f"""
                Optimize energy consumption:
                Usage Data: {usage_data}

                Optimization:
                1. Analyze energy consumption patterns
                2. Identify optimization opportunities
                3. Create efficiency schedules
                4. Balance comfort vs savings
                5. Recommend device upgrades
            """),
            agent=agent,
            expected_output='Energy optimization strategy with projected savings',
            context=[]
        )

    def monitor_security(self, agent, security_config: dict) -> Task:
        return Task(
            description=dedent(f"""
                Monitor home security:
                Config: {security_config}

                Monitoring:
                1. Track sensor states
                2. Detect anomalies
                3. Define alert conditions
                4. Create response protocols
                5. Maintain activity logs
            """),
            agent=agent,
            expected_output='Security monitoring plan with alert protocols',
            context=[]
        )
