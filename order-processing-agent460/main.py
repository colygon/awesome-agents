#!/usr/bin/env python
"""
Order Processing CrewAI Main Application
"""

import sys
from crewai import Crew, Process
from agents import order_validator, inventory_manager, payment_processor, fulfillment_coordinator
from tasks import create_tasks


def main():
    print("\n" + "="*80)
    print("ORDER PROCESSING SYSTEM")
    print("="*80)

    # Collect order information
    print("\nEnter order details:")
    customer_email = input("Customer email: ").strip()
    shipping_address = input("Shipping address: ").strip()
    items_input = input("Items (comma-separated): ").strip()
    items = [i.strip() for i in items_input.split(",")] if items_input else []
    total = input("Order total: $").strip()

    try:
        total_amount = float(total)
    except:
        total_amount = 0.0

    order_data = {
        "customer_email": customer_email,
        "shipping_address": shipping_address,
        "items": items,
        "total": total_amount,
        "payment_method": "credit card"
    }

    print("\n" + "="*80)
    print("Processing order...")
    print("="*80)

    tasks = create_tasks(order_data)
    crew = Crew(
        agents=[order_validator, inventory_manager, payment_processor, fulfillment_coordinator],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("ORDER PROCESSING COMPLETE")
    print("="*80)
    print("\n" + str(result))

    # Human-in-the-loop approval
    print("\n" + "="*80)
    approval = input("\nApprove this order for fulfillment? (yes/no): ").strip().lower()

    if approval == "yes":
        print("\n✓ Order APPROVED and submitted for fulfillment.")
        print("Customer will receive tracking information via email.")
    else:
        print("\n✗ Order REJECTED. Order placed on hold for review.")


if __name__ == "__main__":
    main()
