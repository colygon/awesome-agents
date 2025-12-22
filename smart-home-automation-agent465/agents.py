"""
CrewAI Agents for Smart Home Automation
Specialized agents for managing smart home devices and routines
"""

from crewai import Agent
import os


class SmartHomeAgents:
    """Factory class for creating smart home automation agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def device_coordinator(self) -> Agent:
        """Device Coordination Agent"""
        return Agent(
            role='Smart Device Coordinator',
            goal='Coordinate and control smart home devices across different protocols and platforms',
            backstory='You are an IoT expert specializing in smart home device integration, protocol translation, and device orchestration.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def automation_designer(self) -> Agent:
        """Automation Design Agent"""
        return Agent(
            role='Home Automation Designer',
            goal='Design intelligent automation routines based on user preferences, schedules, and environmental conditions',
            backstory='You excel at creating smart automation rules that enhance comfort, efficiency, and security.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def energy_optimizer(self) -> Agent:
        """Energy Optimization Agent"""
        return Agent(
            role='Energy Optimization Specialist',
            goal='Optimize energy consumption across smart home devices while maintaining comfort and convenience',
            backstory='You specialize in energy management and optimization for smart homes, balancing efficiency with usability.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def security_monitor(self) -> Agent:
        """Security Monitoring Agent"""
        return Agent(
            role='Home Security Specialist',
            goal='Monitor home security devices, detect anomalies, and respond to security events',
            backstory='You are a security expert focused on protecting homes through intelligent monitoring and automated responses.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )
