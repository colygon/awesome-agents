"""
Order Processing CrewAI Tasks
"""

from crewai import Task
from agents import order_validator, inventory_manager, payment_processor, fulfillment_coordinator

def create_tasks(order_data: dict):
    validate_task = Task(
        description=f"""Validate order: {order_data}

Check:
- Customer information completeness
- Shipping address validity
- Product availability
- Pricing accuracy
- Business rule compliance

Flag any issues for review.""",
        agent=order_validator,
        expected_output="Order validation report with approval status"
    )

    inventory_task = Task(
        description=f"""Check inventory for order items:

{order_data.get('items', [])}

Verify:
- Stock availability
- Warehouse location
- Reserve items
- Suggest alternatives if needed""",
        agent=inventory_manager,
        expected_output="Inventory status and reservation confirmation",
        context=[validate_task]
    )

    payment_task = Task(
        description=f"""Process payment for order:

Amount: ${order_data.get('total', 0)}
Payment method: {order_data.get('payment_method', 'credit card')}

Steps:
- Validate payment method
- Process transaction
- Handle any exceptions
- Generate receipt""",
        agent=payment_processor,
        expected_output="Payment confirmation or exception details",
        context=[validate_task, inventory_task]
    )

    fulfillment_task = Task(
        description=f"""Coordinate fulfillment:

Shipping address: {order_data.get('shipping_address', 'N/A')}
Items: {order_data.get('items', [])}

Steps:
- Select fulfillment center
- Choose shipping method
- Generate packing slip
- Create shipping label
- Estimate delivery date""",
        agent=fulfillment_coordinator,
        expected_output="Fulfillment plan with tracking information",
        context=[validate_task, inventory_task, payment_task]
    )

    return [validate_task, inventory_task, payment_task, fulfillment_task]
