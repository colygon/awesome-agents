"""Customer Service Tasks"""

from crewai import Task
from agents import ticket_intake, knowledge_agent, response_composer, escalation_manager, qa_agent


def create_tasks(customer_message: str, customer_info: str = ""):
    intake = Task(
        description=f"Analyze customer ticket: {customer_message}\nCustomer: {customer_info}",
        agent=ticket_intake,
        expected_output="Ticket analysis with category, priority, and sentiment"
    )

    knowledge = Task(
        description="Search knowledge base for relevant solutions",
        agent=knowledge_agent,
        expected_output="Relevant knowledge base articles and solutions",
        context=[intake]
    )

    response = Task(
        description="Compose customer service response",
        agent=response_composer,
        expected_output="Professional, empathetic response with solution",
        context=[intake, knowledge]
    )

    escalation = Task(
        description="Evaluate if escalation is needed",
        agent=escalation_manager,
        expected_output="Escalation decision with routing recommendation",
        context=[intake, response]
    )

    qa = Task(
        description="Review response quality",
        agent=qa_agent,
        expected_output="QA assessment with approval or improvements",
        context=[response, escalation]
    )

    return [intake, knowledge, response, escalation, qa]
