"""
Medical Pre-Authorization Agent - Main Entry Point
CrewAI implementation of Google ADK medical pre-authorization agent
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_preauth_agents
from tasks import create_preauth_tasks

# Load environment variables
load_dotenv()


def run_preauthorization(request_data: Dict[str, Any]):
    """
    Run the medical pre-authorization crew to process an authorization request.

    Args:
        request_data: Complete pre-authorization request including:
            - patient_id: Patient identifier
            - patient_name: Patient full name
            - date_of_birth: DOB in YYYY-MM-DD format
            - insurance_id: Insurance member ID
            - provider_id: Ordering provider ID
            - procedure_code: CPT or HCPCS code
            - diagnosis_codes: List of ICD-10 codes
            - date_of_service: Planned service date (YYYY-MM-DD)
            - clinical_notes: Clinical justification

    Returns:
        Authorization decision with details
    """

    # Create agents
    request_validator, policy_checker, authorization_agent = create_preauth_agents()

    # Create tasks
    tasks = create_preauth_tasks(request_data)

    # Create crew
    crew = Crew(
        agents=[request_validator, policy_checker, authorization_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute
    try:
        result = crew.kickoff()
        return result
    except Exception as e:
        return f"Error processing pre-authorization: {str(e)}"


def main():
    """
    Main function with example pre-authorization request.
    """
    print("=== Medical Pre-Authorization System ===\n")

    # Example pre-authorization request
    request_data = {
        "patient_id": "P123456",
        "patient_name": "John Smith",
        "date_of_birth": "1975-05-15",
        "insurance_id": "INS987654321",
        "provider_id": "DR12345",
        "provider_name": "Dr. Jane Wilson",
        "procedure_code": "99213",
        "procedure_description": "Office visit, established patient",
        "diagnosis_codes": ["E11.9", "I10"],
        "date_of_service": "2025-01-15",
        "clinical_notes": """Patient presents with uncontrolled Type 2 diabetes and hypertension.
        Follow-up visit needed to adjust medications and monitor blood glucose levels.
        Recent HbA1c: 8.5%. Blood pressure: 145/92."""
    }

    print("Processing Pre-Authorization Request:")
    print(f"Patient: {request_data['patient_name']} (ID: {request_data['patient_id']})")
    print(f"Procedure: {request_data['procedure_code']} - {request_data['procedure_description']}")
    print(f"Diagnosis: {', '.join(request_data['diagnosis_codes'])}")
    print(f"Date of Service: {request_data['date_of_service']}\n")
    print("Processing with Pre-Authorization Crew...\n")

    result = run_preauthorization(request_data)

    print("\n=== Authorization Decision ===")
    print(result)


if __name__ == "__main__":
    main()
