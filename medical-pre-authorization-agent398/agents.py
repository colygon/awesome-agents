"""
Medical Pre-Authorization Agents - CrewAI Implementation
Migrated from Google ADK to multi-agent workflow
"""

from crewai import Agent
from tools import (
    validate_request_completeness,
    verify_medical_codes,
    evaluate_medical_necessity,
    check_prior_authorization_required,
    check_patient_eligibility,
    lookup_policy_coverage,
    check_service_limits,
    request_additional_information,
    approve_authorization,
    deny_authorization,
    generate_authorization_number,
    create_authorization_record,
    send_authorization_decision
)


def create_request_validator() -> Agent:
    """
    Creates the Request Validator agent.
    Validates pre-authorization request completeness and medical codes.
    """
    return Agent(
        role="Medical Request Validation Specialist",
        goal="Ensure pre-authorization requests are complete, accurate, and contain valid medical codes before processing",
        backstory="""You are a meticulous healthcare administration specialist with extensive
        experience in medical coding and pre-authorization requirements. You have deep knowledge
        of CPT, HCPCS, and ICD-10 coding systems. You ensure that every pre-authorization request
        contains all required information and that all medical codes are valid and appropriately
        matched. You understand HIPAA compliance and handle protected health information with care.
        Your attention to detail prevents processing delays and ensures smooth authorization workflows.
        You know when additional clinical information is needed and can clearly communicate what's
        missing to providers.""",
        verbose=True,
        allow_delegation=False,
        tools=[
            validate_request_completeness,
            verify_medical_codes,
            check_prior_authorization_required,
            request_additional_information
        ]
    )


def create_policy_checker() -> Agent:
    """
    Creates the Policy Checker agent.
    Verifies insurance coverage and patient eligibility.
    """
    return Agent(
        role="Insurance Policy Analyst",
        goal="Verify patient eligibility, insurance coverage, and policy limits for requested procedures",
        backstory="""You are an experienced insurance policy analyst specializing in healthcare
        benefits verification. You have comprehensive knowledge of insurance plan structures,
        coverage policies, benefit limits, and exclusions. You excel at navigating complex
        insurance policies to determine coverage for specific procedures. You understand how
        diagnosis codes affect coverage decisions and can identify when a procedure requires
        prior authorization. You're familiar with various insurance carriers, plan types (HMO,
        PPO, Medicare, Medicaid), and their specific requirements. You verify patient eligibility,
        check deductibles and copays, and identify any service limits. Your thorough analysis
        prevents claim denials and ensures patients understand their coverage.""",
        verbose=True,
        allow_delegation=False,
        tools=[
            check_patient_eligibility,
            lookup_policy_coverage,
            check_service_limits,
            verify_medical_codes
        ]
    )


def create_authorization_agent() -> Agent:
    """
    Creates the Authorization Agent.
    Makes final authorization decisions and generates documentation.
    """
    return Agent(
        role="Medical Authorization Decision Maker",
        goal="Make informed authorization decisions based on medical necessity, policy coverage, and clinical guidelines",
        backstory="""You are a senior authorization specialist with clinical training and
        healthcare policy expertise. You make authorization decisions by synthesizing medical
        necessity evaluations, insurance policy coverage, and clinical guidelines. You understand
        evidence-based medicine and can evaluate whether requested procedures meet medical
        necessity criteria. You balance patient needs with policy requirements and make fair,
        consistent decisions. When approving, you generate clear authorization documentation.
        When denying, you provide specific reasons and inform patients of their appeal rights.
        You know when cases require peer-to-peer review with the ordering physician. You maintain
        high standards for documentation and ensure all decisions comply with regulatory
        requirements. You communicate decisions clearly and professionally to both providers and
        patients.""",
        verbose=True,
        allow_delegation=False,
        tools=[
            evaluate_medical_necessity,
            approve_authorization,
            deny_authorization,
            generate_authorization_number,
            create_authorization_record,
            send_authorization_decision,
            request_additional_information
        ]
    )


def create_preauth_agents():
    """
    Creates and returns all medical pre-authorization agents.

    Returns:
        Tuple of (request_validator, policy_checker, authorization_agent)
    """
    return (
        create_request_validator(),
        create_policy_checker(),
        create_authorization_agent()
    )
