"""
Customer Service Tasks - CrewAI Implementation
Defines the workflow tasks for the customer service system
"""

from crewai import Task
from agents import create_ticket_analyzer, create_solution_researcher, create_response_generator


def create_analyze_ticket_task(customer_message: str, customer_id: str = "123") -> Task:
    """
    Creates a task to analyze the customer support request.

    Args:
        customer_message: The customer's message or request
        customer_id: The customer's ID for context

    Returns:
        Task for analyzing the support ticket
    """
    ticket_analyzer = create_ticket_analyzer()

    return Task(
        description=f"""Analyze this customer support request:

Customer ID: {customer_id}
Message: {customer_message}

Your analysis should:
1. Identify the customer's primary need or issue
2. Determine the urgency and sentiment
3. Check if the customer has items in their cart that are relevant
4. Categorize the request (product inquiry, order issue, service request, etc.)
5. Note any opportunities for upselling or service recommendations
6. Identify what information the solution researcher will need

Provide a structured analysis that will guide the next steps.""",
        agent=ticket_analyzer,
        expected_output="A detailed analysis of the customer request including issue type, urgency, current cart context, and recommended next steps"
    )


def create_research_solutions_task(customer_message: str, customer_id: str = "123", location: str = "Las Vegas, NV") -> Task:
    """
    Creates a task to research products and solutions.

    Args:
        customer_message: The customer's message or request
        customer_id: The customer's ID
        location: Customer location for climate-specific recommendations

    Returns:
        Task for researching solutions
    """
    solution_researcher = create_solution_researcher()

    return Task(
        description=f"""Based on the ticket analysis, research and identify solutions:

Customer ID: {customer_id}
Location: {location}
Request: {customer_message}

Your research should:
1. Identify specific products that meet the customer's needs
2. Check product availability at their local store
3. Consider climate factors (especially for {location})
4. Look for better alternatives to items already in their cart
5. Identify opportunities for professional services (planting, installation, etc.)
6. Check for current promotions or sales on recommended items
7. If visual identification is needed, prepare to send video call link

Provide detailed product recommendations with reasoning.""",
        agent=solution_researcher,
        expected_output="Comprehensive product and service recommendations with availability, pricing, and climate-appropriate suggestions",
        context=[create_analyze_ticket_task(customer_message, customer_id)]
    )


def create_generate_response_task(customer_message: str, customer_id: str = "123", customer_name: str = "Alex") -> Task:
    """
    Creates a task to generate the customer response.

    Args:
        customer_message: The customer's message or request
        customer_id: The customer's ID
        customer_name: The customer's name for personalization

    Returns:
        Task for generating the response
    """
    response_generator = create_response_generator()

    return Task(
        description=f"""Create a personalized response to the customer:

Customer Name: {customer_name}
Customer ID: {customer_id}
Original Request: {customer_message}

Your response should:
1. Greet the customer warmly by name
2. Address their specific needs based on the analysis and research
3. Explain product recommendations and why they're a good fit
4. Suggest better alternatives if items in cart can be improved
5. Offer relevant services (planting, installation) naturally
6. Apply appropriate discounts (up to 10% directly, or request manager approval)
7. Update the cart if customer approved recommendations
8. Schedule services if requested
9. Send care instructions or promotional QR codes as appropriate
10. Update CRM with interaction summary
11. Maintain a friendly, helpful, empathetic tone
12. NEVER mention internal system details, tools, or technical processes

Write as a helpful human customer service representative, not a bot.""",
        agent=response_generator,
        expected_output="A complete, personalized customer response with all actions taken (cart updates, appointments scheduled, etc.)",
        context=[
            create_analyze_ticket_task(customer_message, customer_id),
            create_research_solutions_task(customer_message, customer_id)
        ]
    )


def create_customer_service_tasks(customer_message: str, customer_id: str = "123",
                                  customer_name: str = "Alex", location: str = "Las Vegas, NV"):
    """
    Creates all tasks for the customer service workflow.

    Args:
        customer_message: The customer's message or request
        customer_id: The customer's ID
        customer_name: The customer's name
        location: Customer location

    Returns:
        List of tasks in execution order
    """
    return [
        create_analyze_ticket_task(customer_message, customer_id),
        create_research_solutions_task(customer_message, customer_id, location),
        create_generate_response_task(customer_message, customer_id, customer_name)
    ]
