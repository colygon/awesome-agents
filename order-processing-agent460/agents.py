"""
Order Processing CrewAI Agents
Automated order management with human-in-the-loop approval
"""

from crewai import Agent
from tools import OrderValidationTool, InventoryCheckTool, PaymentProcessorTool

order_validator = Agent(
    role="Order Validation Specialist",
    goal="Validate and verify order details",
    backstory="""You are an order processing specialist who validates customer
    orders, checks for completeness, and identifies potential issues before
    processing. You ensure orders meet business rules and policies.""",
    verbose=True,
    allow_delegation=False,
    tools=[OrderValidationTool()]
)

inventory_manager = Agent(
    role="Inventory Manager",
    goal="Check inventory availability and reserve stock",
    backstory="""You manage inventory across warehouses and fulfillment centers.
    You check stock levels, reserve items for orders, and suggest alternatives
    for out-of-stock items.""",
    verbose=True,
    allow_delegation=False,
    tools=[InventoryCheckTool()]
)

payment_processor = Agent(
    role="Payment Processing Specialist",
    goal="Process payments securely and handle exceptions",
    backstory="""You process customer payments, handle payment exceptions,
    and ensure PCI compliance. You coordinate with payment gateways and
    handle refunds when needed.""",
    verbose=True,
    allow_delegation=False,
    tools=[PaymentProcessorTool()]
)

fulfillment_coordinator = Agent(
    role="Order Fulfillment Coordinator",
    goal="Coordinate order fulfillment and shipping",
    backstory="""You coordinate the fulfillment process, select shipping methods,
    generate shipping labels, and track orders through delivery. You optimize
    for cost and delivery time.""",
    verbose=True,
    allow_delegation=False
)
