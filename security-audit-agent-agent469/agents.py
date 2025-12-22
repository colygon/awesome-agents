"""
CrewAI Agents for Security Audit
Specialized agents for comprehensive security auditing and vulnerability assessment
"""

from crewai import Agent
from crewai_tools import FileReadTool
import os


class SecurityAuditAgents:
    """Factory class for creating security audit agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def vulnerability_scanner(self) -> Agent:
        """Vulnerability Scanning Agent"""
        return Agent(
            role='Vulnerability Assessment Specialist',
            goal='Identify security vulnerabilities including OWASP Top 10 and common security weaknesses',
            backstory='You are a security researcher with expertise in vulnerability assessment and penetration testing.',
            verbose=True,
            allow_delegation=False,
            tools=[FileReadTool()],
            llm='gpt-4o'
        )

    def dependency_auditor(self) -> Agent:
        """Dependency Audit Agent"""
        return Agent(
            role='Dependency Security Auditor',
            goal='Audit project dependencies for known vulnerabilities and outdated packages',
            backstory='You specialize in software supply chain security and dependency management.',
            verbose=True,
            allow_delegation=False,
            tools=[FileReadTool()],
            llm='gpt-4o'
        )

    def configuration_reviewer(self) -> Agent:
        """Configuration Security Reviewer Agent"""
        return Agent(
            role='Security Configuration Specialist',
            goal='Review security configurations, access controls, and authentication mechanisms',
            backstory='You excel at identifying misconfigurations and security weaknesses in system setups.',
            verbose=True,
            allow_delegation=False,
            tools=[FileReadTool()],
            llm='gpt-4o'
        )

    def compliance_checker(self) -> Agent:
        """Compliance Checking Agent"""
        return Agent(
            role='Security Compliance Specialist',
            goal='Verify compliance with security standards like GDPR, SOC 2, HIPAA, and industry best practices',
            backstory='You are a compliance expert who ensures systems meet regulatory and industry security standards.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )
