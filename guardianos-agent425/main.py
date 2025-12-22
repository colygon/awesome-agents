#!/usr/bin/env python
from crewai import Crew, Process
from agents import GuardianOSAgents
from tasks import GuardianOSTasks
from dotenv import load_dotenv

load_dotenv()

def run_security_operations():
    """Run comprehensive security operations analysis"""
    print("## Welcome to GuardianOS Security Platform")
    print('-------------------------------')

    system_data = input("Enter system data or 'default': ")
    if system_data.lower() == 'default':
        system_data = "Enterprise network, 150 endpoints, 12 servers, cloud infrastructure"

    standards = input("Enter compliance standards or 'default': ")
    if standards.lower() == 'default':
        standards = "NIST CSF, ISO 27001, SOC 2"

    agents = GuardianOSAgents()
    tasks = GuardianOSTasks()

    detector = agents.threat_detector()
    responder = agents.security_responder()
    auditor = agents.compliance_auditor()
    coordinator = agents.security_coordinator()

    detect_task = tasks.detect_threats(detector, system_data)
    respond_task = tasks.respond_to_incidents(responder, "From detection task")
    audit_task = tasks.audit_compliance(auditor, standards)
    coordinate_task = tasks.coordinate_security(coordinator)

    crew = Crew(
        agents=[detector, responder, auditor, coordinator],
        tasks=[detect_task, respond_task, audit_task, coordinate_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Security Analysis Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_security_operations()
