"""
Medical Pre-Authorization Tools - CrewAI Implementation
Migrated from Google ADK
"""

from crewai_tools import tool
from typing import Dict, List, Any, Optional
import logging
from datetime import datetime, timedelta
import uuid

logger = logging.getLogger(__name__)


@tool("Validate Request Completeness")
def validate_request_completeness(request_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates that a pre-authorization request contains all required fields.

    Args:
        request_data: Dictionary containing request information

    Returns:
        Validation result with missing fields if any
    """
    logger.info("Validating request completeness")

    required_fields = [
        "patient_id", "patient_name", "date_of_birth",
        "insurance_id", "provider_id", "procedure_code",
        "diagnosis_codes", "date_of_service"
    ]

    missing_fields = [field for field in required_fields if field not in request_data or not request_data[field]]

    return {
        "is_complete": len(missing_fields) == 0,
        "missing_fields": missing_fields,
        "validated_at": datetime.now().isoformat(),
        "status": "complete" if len(missing_fields) == 0 else "incomplete"
    }


@tool("Verify Medical Codes")
def verify_medical_codes(procedure_code: str, diagnosis_codes: List[str]) -> Dict[str, Any]:
    """
    Verifies that medical procedure and diagnosis codes are valid.

    Args:
        procedure_code: CPT or HCPCS procedure code
        diagnosis_codes: List of ICD-10 diagnosis codes

    Returns:
        Validation result with code descriptions
    """
    logger.info(f"Verifying procedure code: {procedure_code}, diagnosis codes: {diagnosis_codes}")

    # Mocked validation - in production, check against medical code databases
    return {
        "procedure_valid": True,
        "procedure_code": procedure_code,
        "procedure_description": "Office visit, established patient",
        "diagnosis_valid": True,
        "diagnosis_details": [
            {"code": diagnosis_codes[0], "description": "Type 2 diabetes mellitus"} if len(diagnosis_codes) > 0 else {},
            {"code": diagnosis_codes[1], "description": "Essential hypertension"} if len(diagnosis_codes) > 1 else {}
        ],
        "codes_match": True,
        "status": "valid"
    }


@tool("Check Patient Eligibility")
def check_patient_eligibility(patient_id: str, insurance_id: str, date_of_service: str) -> Dict[str, Any]:
    """
    Checks if patient has active insurance coverage on the date of service.

    Args:
        patient_id: Patient identifier
        insurance_id: Insurance member ID
        date_of_service: Planned service date (YYYY-MM-DD)

    Returns:
        Eligibility status and coverage details
    """
    logger.info(f"Checking eligibility for patient {patient_id}")

    return {
        "patient_id": patient_id,
        "insurance_id": insurance_id,
        "is_eligible": True,
        "coverage_active": True,
        "effective_date": "2024-01-01",
        "termination_date": "2025-12-31",
        "plan_name": "Premium Health Plan",
        "group_number": "GRP12345",
        "copay": 25.00,
        "deductible": 1500.00,
        "deductible_met": 800.00,
        "status": "eligible"
    }


@tool("Lookup Policy Coverage")
def lookup_policy_coverage(insurance_plan: str, procedure_code: str, diagnosis_codes: List[str]) -> Dict[str, Any]:
    """
    Looks up whether the insurance policy covers the requested procedure.

    Args:
        insurance_plan: Insurance plan name/ID
        procedure_code: CPT/HCPCS code
        diagnosis_codes: List of ICD-10 codes

    Returns:
        Coverage details including limits and exclusions
    """
    logger.info(f"Looking up coverage for procedure {procedure_code} under plan {insurance_plan}")

    return {
        "insurance_plan": insurance_plan,
        "procedure_code": procedure_code,
        "is_covered": True,
        "coverage_percentage": 80,
        "requires_preauth": True,
        "annual_limit": None,
        "visit_limit": None,
        "exclusions": [],
        "covered_diagnosis_codes": diagnosis_codes,
        "status": "covered"
    }


@tool("Evaluate Medical Necessity")
def evaluate_medical_necessity(procedure_code: str, diagnosis_codes: List[str],
                               clinical_notes: str) -> Dict[str, Any]:
    """
    Evaluates whether the requested procedure is medically necessary.

    Args:
        procedure_code: CPT/HCPCS code
        diagnosis_codes: List of ICD-10 codes
        clinical_notes: Clinical justification from provider

    Returns:
        Medical necessity determination
    """
    logger.info("Evaluating medical necessity")

    return {
        "procedure_code": procedure_code,
        "diagnosis_codes": diagnosis_codes,
        "is_medically_necessary": True,
        "criteria_met": [
            "Diagnosis supports the requested procedure",
            "Procedure is appropriate first-line treatment",
            "Clinical documentation supports medical necessity"
        ],
        "criteria_not_met": [],
        "confidence": "high",
        "status": "approved"
    }


@tool("Check Prior Authorization Required")
def check_prior_authorization_required(procedure_code: str, insurance_plan: str) -> Dict[str, bool]:
    """
    Checks if the procedure requires prior authorization.

    Args:
        procedure_code: CPT/HCPCS code
        insurance_plan: Insurance plan name/ID

    Returns:
        Whether prior auth is required and urgency level
    """
    logger.info(f"Checking if prior auth required for {procedure_code}")

    return {
        "prior_auth_required": True,
        "urgency": "standard",
        "turnaround_time_days": 3,
        "can_be_expedited": True,
        "requires_peer_review": False
    }


@tool("Generate Authorization Number")
def generate_authorization_number(procedure_code: str, patient_id: str) -> str:
    """
    Generates a unique authorization number for approved requests.

    Args:
        procedure_code: CPT/HCPCS code
        patient_id: Patient identifier

    Returns:
        Unique authorization number
    """
    logger.info(f"Generating authorization number for patient {patient_id}")

    auth_number = f"AUTH-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8].upper()}"

    return {
        "authorization_number": auth_number,
        "generated_at": datetime.now().isoformat(),
        "status": "generated"
    }


@tool("Create Authorization Record")
def create_authorization_record(auth_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Creates an authorization record in the system.

    Args:
        auth_data: Complete authorization data

    Returns:
        Created authorization record with ID
    """
    logger.info("Creating authorization record")

    record_id = str(uuid.uuid4())

    return {
        "record_id": record_id,
        "authorization_number": auth_data.get("auth_number", ""),
        "status": "active",
        "created_at": datetime.now().isoformat(),
        "valid_from": datetime.now().strftime("%Y-%m-%d"),
        "valid_until": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
        "message": "Authorization record created successfully"
    }


@tool("Check Service Limits")
def check_service_limits(patient_id: str, procedure_code: str, insurance_plan: str) -> Dict[str, Any]:
    """
    Checks if patient has reached any service limits for the procedure.

    Args:
        patient_id: Patient identifier
        procedure_code: CPT/HCPCS code
        insurance_plan: Insurance plan name/ID

    Returns:
        Service limit information
    """
    logger.info(f"Checking service limits for patient {patient_id}")

    return {
        "patient_id": patient_id,
        "procedure_code": procedure_code,
        "annual_limit": 20,
        "visits_used": 3,
        "visits_remaining": 17,
        "limit_exceeded": False,
        "reset_date": "2025-01-01",
        "status": "within_limits"
    }


@tool("Send Authorization Decision")
def send_authorization_decision(decision: str, recipient: str, auth_details: Dict[str, Any]) -> Dict[str, str]:
    """
    Sends the authorization decision to provider and/or patient.

    Args:
        decision: "approved" or "denied"
        recipient: "provider", "patient", or "both"
        auth_details: Authorization details to include

    Returns:
        Notification status
    """
    logger.info(f"Sending {decision} decision to {recipient}")

    return {
        "status": "sent",
        "decision": decision,
        "recipient": recipient,
        "sent_at": datetime.now().isoformat(),
        "message": f"Authorization {decision} notification sent to {recipient}"
    }


@tool("Request Additional Information")
def request_additional_information(request_id: str, required_info: List[str],
                                  recipient: str) -> Dict[str, Any]:
    """
    Requests additional information needed for authorization decision.

    Args:
        request_id: Pre-authorization request ID
        required_info: List of required information items
        recipient: Who to request from (provider/patient)

    Returns:
        Information request status
    """
    logger.info(f"Requesting additional information for request {request_id}")

    return {
        "request_id": request_id,
        "status": "pending_information",
        "required_info": required_info,
        "recipient": recipient,
        "due_date": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"),
        "message": f"Additional information requested from {recipient}"
    }


@tool("Deny Authorization")
def deny_authorization(request_id: str, denial_reasons: List[str],
                      appeal_rights: bool = True) -> Dict[str, Any]:
    """
    Creates a denial decision with reasons and appeal rights.

    Args:
        request_id: Pre-authorization request ID
        denial_reasons: List of reasons for denial
        appeal_rights: Whether patient has appeal rights

    Returns:
        Denial record
    """
    logger.info(f"Denying authorization for request {request_id}")

    return {
        "request_id": request_id,
        "decision": "denied",
        "denial_reasons": denial_reasons,
        "appeal_rights": appeal_rights,
        "appeal_deadline": (datetime.now() + timedelta(days=60)).strftime("%Y-%m-%d") if appeal_rights else None,
        "denied_at": datetime.now().isoformat(),
        "status": "denied"
    }


@tool("Approve Authorization")
def approve_authorization(request_id: str, procedure_code: str, patient_id: str,
                         approval_duration_days: int = 30) -> Dict[str, Any]:
    """
    Approves the pre-authorization request.

    Args:
        request_id: Pre-authorization request ID
        procedure_code: CPT/HCPCS code
        patient_id: Patient identifier
        approval_duration_days: Number of days authorization is valid

    Returns:
        Approval record with authorization number
    """
    logger.info(f"Approving authorization for request {request_id}")

    auth_number = f"AUTH-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8].upper()}"

    return {
        "request_id": request_id,
        "decision": "approved",
        "authorization_number": auth_number,
        "patient_id": patient_id,
        "procedure_code": procedure_code,
        "valid_from": datetime.now().strftime("%Y-%m-%d"),
        "valid_until": (datetime.now() + timedelta(days=approval_duration_days)).strftime("%Y-%m-%d"),
        "approved_at": datetime.now().isoformat(),
        "status": "approved"
    }
