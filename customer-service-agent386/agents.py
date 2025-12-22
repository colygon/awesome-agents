"""
Customer Service Agents - CrewAI Implementation
Migrated from Google ADK single-agent to multi-agent workflow
"""

from crewai import Agent
from tools import (
    send_call_companion_link,
    approve_discount,
    request_manager_approval,
    access_cart_information,
    modify_cart,
    get_product_recommendations,
    check_product_availability,
    get_available_planting_times,
    schedule_planting_service,
    send_care_instructions,
    generate_qr_code,
    update_salesforce_crm
)


def create_ticket_analyzer() -> Agent:
    """
    Creates the Ticket Analyzer agent.
    Analyzes incoming support requests and categorizes issues.
    """
    return Agent(
        role="Support Ticket Analyst",
        goal="Analyze customer support requests, identify needs, and determine appropriate response strategy",
        backstory="""You are an expert customer service analyst for Cymbal Home & Garden,
        a big-box retailer specializing in home improvement and gardening supplies. You have
        years of experience understanding customer needs, categorizing support tickets, and
        identifying the best path to resolution. You're skilled at reading between the lines
        and understanding customer emotions and urgency levels.""",
        verbose=True,
        allow_delegation=False,
        tools=[
            access_cart_information,
        ]
    )


def create_solution_researcher() -> Agent:
    """
    Creates the Solution Researcher agent.
    Researches products and solutions for customer needs.
    """
    return Agent(
        role="Product & Solutions Expert",
        goal="Research and identify the best products, services, and solutions for customer needs",
        backstory="""You are a product specialist and gardening expert at Cymbal Home & Garden.
        You have deep knowledge of plants, gardening supplies, climate considerations, and
        product compatibility. You're excellent at matching customer needs with the right
        products, considering factors like location (especially arid climates like Las Vegas),
        plant types, and customer experience level. You stay updated on inventory, sales,
        and can identify opportunities for upselling services like professional planting.""",
        verbose=True,
        allow_delegation=False,
        tools=[
            get_product_recommendations,
            check_product_availability,
            access_cart_information,
            get_available_planting_times,
            send_call_companion_link
        ]
    )


def create_response_generator() -> Agent:
    """
    Creates the Response Generator agent.
    Crafts personalized, helpful customer responses.
    """
    return Agent(
        role="Customer Communication Specialist",
        goal="Create personalized, empathetic, and helpful customer responses that resolve issues and build loyalty",
        backstory="""You are a senior customer service representative at Cymbal Home & Garden,
        known for your warm, friendly communication style and ability to make customers feel
        valued. You excel at crafting responses that are both professional and personable,
        explaining product benefits clearly, and smoothly suggesting upgrades or services
        when appropriate. You're authorized to approve small discounts (up to 10%) and know
        when to escalate for manager approval. You never sound robotic or mention internal
        system details to customers.""",
        verbose=True,
        allow_delegation=False,
        tools=[
            modify_cart,
            approve_discount,
            request_manager_approval,
            schedule_planting_service,
            send_care_instructions,
            generate_qr_code,
            update_salesforce_crm
        ]
    )


def create_customer_service_agents():
    """
    Creates and returns all customer service agents.

    Returns:
        Tuple of (ticket_analyzer, solution_researcher, response_generator)
    """
    return (
        create_ticket_analyzer(),
        create_solution_researcher(),
        create_response_generator()
    )
