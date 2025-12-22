"""
AI Customer Support CrewAI Tasks
Defines the workflow for customer support automation
"""

from crewai import Task
from agents import support_specialist, issue_resolver, escalation_manager

def create_tasks(customer_inquiry: str, customer_id: str = None, priority: str = "normal"):
    """
    Create tasks for customer support workflow

    Args:
        customer_inquiry: The customer's question or issue
        customer_id: Optional customer identifier
        priority: Priority level - "low", "normal", "high", or "urgent"

    Returns:
        List of Task objects
    """

    # Task 1: Analyze and respond to customer inquiry
    analyze_inquiry_task = Task(
        description=f"""Analyze and respond to this customer inquiry:

        Customer Inquiry: {customer_inquiry}
        {f"Customer ID: {customer_id}" if customer_id else ""}
        Priority: {priority}

        Your objectives:
        1. Understand the customer's issue or question
        2. Perform sentiment analysis to gauge emotional state
        3. Search the knowledge base for relevant information
        4. Determine if this is:
           - A simple question (provide direct answer)
           - A technical issue (needs troubleshooting)
           - A complex case (needs escalation)
        5. Draft an initial response that:
           - Acknowledges the customer's concern with empathy
           - Provides immediate value or information
           - Sets clear expectations for resolution
           - Uses a friendly, professional tone

        Provide:
        - Sentiment analysis (positive, neutral, negative, frustrated, urgent)
        - Issue classification (question, technical issue, complaint, feedback, request)
        - Relevant knowledge base articles or solutions
        - Draft response to customer
        - Recommendation for next steps (resolve, troubleshoot, or escalate)""",
        agent=support_specialist,
        expected_output="""A comprehensive analysis including:
        - Sentiment: [positive/neutral/negative/frustrated/urgent]
        - Issue Type: [question/technical/complaint/feedback/request]
        - Relevant KB Articles: [list of relevant resources]
        - Draft Response: [empathetic, helpful response text]
        - Next Steps: [resolve/troubleshoot/escalate]
        - Estimated Resolution Time"""
    )

    # Task 2: Technical troubleshooting (if needed)
    troubleshoot_task = Task(
        description=f"""Based on the initial analysis of the customer inquiry, provide
        detailed technical troubleshooting if needed.

        Customer Inquiry: {customer_inquiry}

        Your objectives:
        1. Identify the specific technical issue or problem
        2. Search knowledge base for:
           - Known issues and solutions
           - Troubleshooting guides
           - Common causes
           - Workarounds
        3. Create a step-by-step resolution plan:
           - Diagnostic steps to identify the root cause
           - Solution steps with clear instructions
           - Alternative approaches if first solution fails
           - Prevention tips for future
        4. Identify if the issue requires:
           - Customer self-service (can resolve themselves)
           - Agent assistance (needs guided support)
           - Engineering escalation (bug or system issue)
        5. Document the resolution for knowledge base updates

        Provide:
        - Root cause analysis
        - Step-by-step solution guide
        - Expected time to resolution
        - Escalation criteria if solution doesn't work
        - Follow-up recommendations""",
        agent=issue_resolver,
        expected_output="""A technical resolution guide including:
        - Root Cause: [identified problem]
        - Diagnostic Steps: [numbered list]
        - Solution Steps: [clear, actionable instructions]
        - Alternative Solutions: [if primary fails]
        - Time Estimate: [expected resolution time]
        - Escalation Path: [when to escalate]
        - Prevention Tips: [avoiding future issues]""",
        context=[analyze_inquiry_task]
    )

    # Task 3: Escalation handling (if needed)
    escalation_task = Task(
        description=f"""Handle escalation if the customer inquiry requires senior attention
        or special handling.

        Customer Inquiry: {customer_inquiry}
        {f"Customer ID: {customer_id}" if customer_id else ""}
        Priority: {priority}

        Your objectives:
        1. Assess why this case needs escalation:
           - Technical complexity beyond standard support
           - Customer frustration or dissatisfaction
           - High-value customer or business impact
           - Policy exception required
           - Systemic issue affecting multiple customers
        2. Create an escalation plan:
           - Immediate actions to satisfy customer
           - Internal team coordination needed
           - Timeline and milestones
           - Communication strategy
        3. Draft executive-level response if needed:
           - Acknowledge the situation with appropriate gravity
           - Outline the resolution plan
           - Set realistic expectations
           - Provide direct contact information
        4. Identify systemic improvements:
           - Is this a recurring issue?
           - Can processes be improved?
           - Should knowledge base be updated?
           - Training needs for support team?

        Provide:
        - Escalation justification
        - Resolution plan with timeline
        - Executive response draft (if needed)
        - Internal coordination required
        - Process improvement recommendations""",
        agent=escalation_manager,
        expected_output="""An escalation management plan including:
        - Escalation Reason: [why this needs senior attention]
        - Resolution Plan: [detailed action plan with timeline]
        - Executive Response: [draft if needed]
        - Team Coordination: [who needs to be involved]
        - Customer Expectations: [what to communicate]
        - Process Improvements: [systemic fixes to prevent recurrence]
        - Follow-up Schedule: [when to check in]""",
        context=[analyze_inquiry_task, troubleshoot_task]
    )

    return [analyze_inquiry_task, troubleshoot_task, escalation_task]
