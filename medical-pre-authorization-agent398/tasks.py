"""
Medical Pre-Authorization Tasks - CrewAI Implementation
Defines the workflow tasks for pre-authorization processing
"""

from crewai import Task
from typing import Dict, List, Any
from agents import create_request_validator, create_policy_checker, create_authorization_agent


def create_validation_task(request_data: Dict[str, Any]) -> Task:
    """
    Creates a task to validate the pre-authorization request.

    Args:
        request_data: Complete pre-authorization request data

    Returns:
        Task for validating the request
    """
    request_validator = create_request_validator()

    return Task(
        description=f"""Validate the pre-authorization request:

Patient ID: {request_data.get('patient_id')}
Procedure Code: {request_data.get('procedure_code')}
Diagnosis Codes: {', '.join(request_data.get('diagnosis_codes', []))}

Your validation should include:
1. Verify all required fields are present and complete
2. Validate medical procedure code (CPT/HCPCS)
3. Validate all diagnosis codes (ICD-10)
4. Verify that diagnosis codes support the requested procedure
5. Check if prior authorization is required for this procedure
6. Identify any missing or incomplete information

If any required information is missing, clearly specify what is needed.
If codes are invalid or don't match, explain the issue.

Provide a clear validation summary.""",
        agent=request_validator,
        expected_output="Complete validation report indicating whether request is complete, all codes are valid, and any missing information that needs to be requested"
    )


def create_policy_check_task(request_data: Dict[str, Any]) -> Task:
    """
    Creates a task to verify insurance coverage and eligibility.

    Args:
        request_data: Complete pre-authorization request data

    Returns:
        Task for checking policy coverage
    """
    policy_checker = create_policy_checker()

    return Task(
        description=f"""Verify insurance coverage and patient eligibility:

Patient ID: {request_data.get('patient_id')}
Insurance ID: {request_data.get('insurance_id')}
Procedure Code: {request_data.get('procedure_code')}
Diagnosis Codes: {', '.join(request_data.get('diagnosis_codes', []))}
Date of Service: {request_data.get('date_of_service')}

Your policy check should include:
1. Verify patient has active insurance coverage on the date of service
2. Check insurance eligibility and benefit details
3. Lookup policy coverage for the requested procedure
4. Verify coverage percentage and patient cost-sharing (copay, deductible)
5. Check for any service limits or visit maximums
6. Identify any exclusions or restrictions
7. Verify if diagnosis codes qualify for coverage

Provide comprehensive coverage analysis with specific details.""",
        agent=policy_checker,
        expected_output="Detailed coverage analysis including eligibility status, coverage percentage, patient costs, any limits or exclusions, and coverage determination",
        context=[create_validation_task(request_data)]
    )


def create_authorization_decision_task(request_data: Dict[str, Any]) -> Task:
    """
    Creates a task to make the authorization decision.

    Args:
        request_data: Complete pre-authorization request data

    Returns:
        Task for making authorization decision
    """
    authorization_agent = create_authorization_agent()

    return Task(
        description=f"""Make authorization decision for pre-authorization request:

Patient: {request_data.get('patient_name')} (ID: {request_data.get('patient_id')})
Provider ID: {request_data.get('provider_id')}
Procedure: {request_data.get('procedure_code')}
Diagnosis: {', '.join(request_data.get('diagnosis_codes', []))}
Clinical Notes: {request_data.get('clinical_notes', 'See attached')}

Based on the validation and policy check, make your decision:

1. Evaluate medical necessity based on:
   - Clinical documentation provided
   - Diagnosis codes supporting the procedure
   - Evidence-based medicine guidelines

2. If APPROVED:
   - Generate unique authorization number
   - Create authorization record
   - Specify validity period (typically 30 days)
   - Send approval notification to provider and patient
   - Include authorization number, valid dates, and any limitations

3. If DENIED:
   - List specific denial reasons
   - Cite policy sections or medical necessity criteria
   - Inform patient of appeal rights
   - Set appeal deadline (typically 60 days)
   - Send denial notification with appeal instructions

4. If MORE INFORMATION NEEDED:
   - Specify exactly what information is required
   - Request from appropriate party (provider/patient)
   - Set response deadline
   - Place request in pending status

Your decision should be clear, well-documented, and compliant with
healthcare regulations. Include all necessary details for the decision
to be implemented.""",
        agent=authorization_agent,
        expected_output="Final authorization decision (approved/denied/pending) with authorization number if approved, detailed reasons if denied, complete documentation, and all notifications sent",
        context=[
            create_validation_task(request_data),
            create_policy_check_task(request_data)
        ]
    )


def create_preauth_tasks(request_data: Dict[str, Any]):
    """
    Creates all tasks for the pre-authorization workflow.

    Args:
        request_data: Complete pre-authorization request including:
            - patient_id, patient_name, date_of_birth
            - insurance_id, provider_id
            - procedure_code, diagnosis_codes
            - date_of_service, clinical_notes

    Returns:
        List of tasks in execution order
    """
    return [
        create_validation_task(request_data),
        create_policy_check_task(request_data),
        create_authorization_decision_task(request_data)
    ]
