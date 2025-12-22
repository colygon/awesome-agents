#!/usr/bin/env python3
"""
Customer Service Agent - CrewAI Implementation
Intelligent customer support system using multi-agent architecture
"""

import os
import json
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, BaseTool
from langchain_openai import ChatOpenAI
from typing import Type
from pydantic import BaseModel, Field
import datetime

# Initialize OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,  # Balanced temperature for customer service
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize search tool
search_tool = SerperDevTool()

# Custom Knowledge Base Tool

class KnowledgeBaseInput(BaseModel):
    """Input for knowledge base search"""
    query: str = Field(..., description="Search query for knowledge base")

class KnowledgeBaseTool(BaseTool):
    name: str = "search_knowledge_base"
    description: str = "Search the customer service knowledge base for product information, FAQs, and troubleshooting guides"
    args_schema: Type[BaseModel] = KnowledgeBaseInput

    def _run(self, query: str) -> str:
        """Search knowledge base (simulated)"""
        # In production, this would connect to a real knowledge base
        knowledge_base = {
            "password reset": {
                "answer": "To reset your password: 1) Click 'Forgot Password' on login page, 2) Enter your email, 3) Check email for reset link, 4) Create new password",
                "category": "Account Management"
            },
            "shipping": {
                "answer": "Standard shipping takes 5-7 business days. Express shipping takes 2-3 business days. Free shipping on orders over $50.",
                "category": "Shipping & Delivery"
            },
            "refund": {
                "answer": "Refunds are processed within 5-10 business days after we receive the returned item. Original shipping costs are non-refundable.",
                "category": "Returns & Refunds"
            },
            "product warranty": {
                "answer": "All products come with a 1-year manufacturer warranty covering defects. Extended warranties available for purchase.",
                "category": "Product Information"
            },
            "cancel order": {
                "answer": "Orders can be cancelled within 24 hours of placement. After that, please use our return process once item is received.",
                "category": "Order Management"
            }
        }

        query_lower = query.lower()
        results = []

        for key, value in knowledge_base.items():
            if key in query_lower or any(word in query_lower for word in key.split()):
                results.append(f"**{value['category']}**: {value['answer']}")

        if results:
            return "\n\n".join(results)
        else:
            return "No specific knowledge base articles found. Please provide general assistance based on best practices."

# Initialize tools
kb_tool = KnowledgeBaseTool()

# Define Agents

# 1. Triage Agent
triage_agent = Agent(
    role="Customer Service Triage Specialist",
    goal="Analyze customer inquiries and determine the appropriate response strategy",
    backstory="""You are an experienced customer service triage specialist who
    quickly assesses customer inquiries to determine urgency, sentiment, and
    the type of support needed. You categorize issues and route them appropriately.
    You recognize patterns in customer problems and identify when escalation is needed.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 2. Support Agent
support_agent = Agent(
    role="Customer Support Representative",
    goal="Provide helpful, accurate responses to customer inquiries",
    backstory="""You are a knowledgeable and empathetic customer support representative.
    You excel at understanding customer needs, finding solutions, and communicating
    clearly. You use the knowledge base to provide accurate information and can
    troubleshoot common issues. You maintain a friendly, professional tone.""",
    verbose=True,
    allow_delegation=False,
    tools=[kb_tool, search_tool],
    llm=llm
)

# 3. Technical Support Agent
technical_agent = Agent(
    role="Technical Support Specialist",
    goal="Resolve technical issues and provide detailed troubleshooting",
    backstory="""You are a technical support specialist with deep product knowledge
    and troubleshooting expertise. You can diagnose technical problems, provide
    step-by-step solutions, and explain complex concepts in simple terms. You're
    patient and methodical in your approach.""",
    verbose=True,
    allow_delegation=False,
    tools=[kb_tool, search_tool],
    llm=llm
)

# 4. Escalation Manager
escalation_agent = Agent(
    role="Customer Escalation Manager",
    goal="Handle escalated issues and ensure customer satisfaction",
    backstory="""You are a senior customer escalation manager who handles complex
    or sensitive customer issues. You have authority to make decisions, offer
    solutions, and ensure customers feel heard and valued. You balance customer
    satisfaction with company policies and can approve exceptions when warranted.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 5. Quality Assurance Agent
qa_agent = Agent(
    role="Customer Service Quality Assurance",
    goal="Review responses for quality, accuracy, and professionalism",
    backstory="""You are a customer service quality assurance specialist who
    ensures all customer communications meet high standards. You check for
    accuracy, tone, completeness, and compliance with policies. You provide
    feedback to improve response quality.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def handle_customer_inquiry(
    customer_message: str,
    customer_name: str = "Customer",
    customer_history: str = None
) -> dict:
    """
    Handle a customer service inquiry through the multi-agent workflow

    Args:
        customer_message: The customer's inquiry or issue
        customer_name: Customer's name
        customer_history: Optional customer history context

    Returns:
        dict with support response and metadata
    """

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history_context = f"\n\nCustomer History: {customer_history}" if customer_history else ""

    # Task 1: Triage the inquiry
    triage_task = Task(
        description=f"""Analyze this customer inquiry and provide triage assessment:

        Customer: {customer_name}
        Message: {customer_message}{history_context}

        Assess:
        1. **Urgency**: Low / Medium / High / Critical
        2. **Sentiment**: Positive / Neutral / Frustrated / Angry
        3. **Category**: Account, Product, Technical, Billing, Shipping, Other
        4. **Complexity**: Simple / Moderate / Complex
        5. **Recommended Agent**: Support / Technical / Escalation
        6. **Key Issues**: List main concerns

        Provide structured triage assessment.""",
        agent=triage_agent,
        expected_output="Structured triage assessment with urgency and routing recommendation"
    )

    # Task 2: Determine response path and generate initial response
    # This will be dynamic based on triage, but we'll create support response
    support_task = Task(
        description=f"""Based on the triage assessment, provide customer support response:

        Customer: {customer_name}
        Inquiry: {customer_message}{history_context}

        Your response should:
        1. Address the customer by name warmly
        2. Acknowledge their concern with empathy
        3. Use the knowledge base to find relevant information
        4. Provide clear, actionable solutions or next steps
        5. Offer additional assistance
        6. Maintain professional, friendly tone

        Use search_knowledge_base tool to find accurate information.
        Use web search if you need current product information.

        Provide complete customer response.""",
        agent=support_agent,
        expected_output="Complete, empathetic customer support response",
        context=[triage_task]
    )

    # Task 3: Technical review if needed
    technical_task = Task(
        description=f"""Review the support response and enhance with technical details if needed:

        Customer Inquiry: {customer_message}
        Support Response: [See previous response]

        If this is a technical issue:
        1. Add detailed troubleshooting steps
        2. Include technical specifications if relevant
        3. Provide alternative solutions
        4. Add preventive measures
        5. Include links to technical documentation

        If not technical, simply approve the support response.

        Provide enhanced response or approval.""",
        agent=technical_agent,
        expected_output="Technically enhanced response or approval of support response",
        context=[triage_task, support_task]
    )

    # Task 4: Quality assurance review
    qa_task = Task(
        description=f"""Review the customer response for quality assurance:

        Original Inquiry: {customer_message}
        Response: [See previous responses]

        Check:
        1. **Accuracy**: Information is correct
        2. **Completeness**: All concerns addressed
        3. **Tone**: Professional and empathetic
        4. **Clarity**: Easy to understand
        5. **Policy Compliance**: Follows company guidelines

        Provide:
        - Quality score (1-10)
        - Any corrections needed
        - Final approved response

        Deliver the final, approved customer response.""",
        agent=qa_agent,
        expected_output="Quality-approved final customer response",
        context=[support_task, technical_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[triage_agent, support_agent, technical_agent, qa_agent],
        tasks=[triage_task, support_task, technical_task, qa_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "triage": triage_task.output.raw if hasattr(triage_task, 'output') else "",
        "support_response": support_task.output.raw if hasattr(support_task, 'output') else "",
        "technical_review": technical_task.output.raw if hasattr(technical_task, 'output') else "",
        "final_response": str(result),
        "metadata": {
            "customer": customer_name,
            "timestamp": current_time,
            "inquiry_preview": customer_message[:100] + "..." if len(customer_message) > 100 else customer_message
        }
    }

if __name__ == "__main__":
    print("Customer Service Agent - CrewAI")
    print("=" * 60)

    # Example customer inquiries
    examples = [
        {
            "name": "Sarah Johnson",
            "message": "I forgot my password and the reset link isn't working. I've tried three times!",
            "history": "Premium member since 2023, 5 previous support tickets (all resolved)"
        },
        {
            "name": "Michael Chen",
            "message": "Where is my order? It's been 10 days and the tracking hasn't updated.",
            "history": "New customer, first order"
        },
        {
            "name": "Alex Rivera",
            "message": "The product stopped working after 2 weeks. This is unacceptable! I want a full refund.",
            "history": "Regular customer, no previous complaints"
        }
    ]

    print("\nExample Scenarios:")
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example['name']}: {example['message'][:60]}...")

    print(f"{len(examples) + 1}. Custom inquiry")

    choice = input(f"\nSelect scenario (1-{len(examples) + 1}): ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(examples):
        selected = examples[int(choice) - 1]
        customer_name = selected["name"]
        customer_message = selected["message"]
        customer_history = selected["history"]
    else:
        customer_name = input("\nEnter customer name: ").strip() or "Customer"
        customer_message = input("Enter customer inquiry: ").strip()
        if not customer_message:
            customer_message = "I need help with my recent order."
        customer_history = input("Enter customer history (optional): ").strip() or None

    print(f"\nProcessing inquiry from {customer_name}...")
    print(f"Message: {customer_message}\n")

    # Handle inquiry
    result = handle_customer_inquiry(customer_message, customer_name, customer_history)

    # Display results
    print("\n" + "=" * 60)
    print("CUSTOMER SERVICE RESPONSE")
    print("=" * 60)

    print("\n--- Triage Assessment ---")
    print(result["triage"])

    print("\n--- Support Response ---")
    print(result["support_response"])

    print("\n--- Technical Review ---")
    print(result["technical_review"])

    print("\n--- Final Approved Response ---")
    print(result["final_response"])
