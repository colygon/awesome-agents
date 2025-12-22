"""
Customer Service Tools - CrewAI Implementation
Migrated from Google ADK
"""

from crewai_tools import tool
from typing import Dict, List, Any
import logging
from datetime import datetime, timedelta
import uuid

logger = logging.getLogger(__name__)


@tool("Send Video Call Link")
def send_call_companion_link(phone_number: str) -> Dict[str, str]:
    """
    Sends a link to the user's phone number to start a video session.
    Useful for visual product identification.

    Args:
        phone_number: The phone number to send the link to

    Returns:
        Status message indicating if link was sent successfully
    """
    logger.info(f"Sending call companion link to {phone_number}")
    return {
        "status": "success",
        "message": f"Video link sent to {phone_number}"
    }


@tool("Approve Discount")
def approve_discount(discount_type: str, value: float, reason: str) -> Dict[str, str]:
    """
    Approve a discount for the customer (up to 10%).
    For discounts over 10%, use request_manager_approval instead.

    Args:
        discount_type: Either "percentage" or "flat"
        value: The discount value
        reason: Reason for the discount

    Returns:
        Approval status
    """
    if value > 10:
        return {
            "status": "rejected",
            "message": "Discount too large. Must be 10 or less. Use request_manager_approval for larger discounts."
        }

    logger.info(f"Approving {discount_type} discount of {value} because {reason}")
    return {"status": "approved", "discount_applied": value}


@tool("Request Manager Approval")
def request_manager_approval(discount_type: str, value: float, reason: str) -> Dict[str, str]:
    """
    Requests manager approval for discounts over 10%.

    Args:
        discount_type: Either "percentage" or "flat"
        value: The discount value
        reason: Reason for the discount

    Returns:
        Manager approval status
    """
    logger.info(f"Requesting manager approval for {discount_type} discount of {value}")
    # Simulated approval - in production, this would trigger actual workflow
    return {
        "status": "approved",
        "approval_id": str(uuid.uuid4()),
        "message": f"Manager approved {value}% discount"
    }


@tool("Access Cart Information")
def access_cart_information(customer_id: str) -> Dict[str, Any]:
    """
    Retrieves the customer's shopping cart contents.
    Always use this before modifying the cart.

    Args:
        customer_id: The customer's ID

    Returns:
        Cart contents with items and totals
    """
    logger.info(f"Accessing cart for customer {customer_id}")
    # Mocked cart data
    return {
        "customer_id": customer_id,
        "items": [
            {
                "id": "SOIL-001",
                "name": "Premium Potting Soil 20lb",
                "quantity": 2,
                "price": 12.99
            },
            {
                "id": "FERT-002",
                "name": "All-Purpose Fertilizer",
                "quantity": 1,
                "price": 15.99
            }
        ],
        "subtotal": 41.97,
        "tax": 3.78,
        "total": 45.75
    }


@tool("Modify Cart")
def modify_cart(customer_id: str, items_to_add: List[Dict], items_to_remove: List[str]) -> Dict[str, Any]:
    """
    Updates the customer's shopping cart by adding or removing items.
    Always access_cart_information first before modifying.

    Args:
        customer_id: The customer's ID
        items_to_add: List of items to add with id, name, quantity, price
        items_to_remove: List of product IDs to remove

    Returns:
        Updated cart information
    """
    logger.info(f"Modifying cart for customer {customer_id}")
    logger.info(f"Adding items: {items_to_add}")
    logger.info(f"Removing items: {items_to_remove}")

    return {
        "status": "success",
        "items_added": len(items_to_add),
        "items_removed": len(items_to_remove),
        "message": "Cart updated successfully"
    }


@tool("Get Product Recommendations")
def get_product_recommendations(plant_type: str, customer_id: str, location: str = "Las Vegas, NV") -> Dict[str, Any]:
    """
    Gets product recommendations based on plant type and customer location.
    Considers climate and customer purchase history.

    Args:
        plant_type: Type of plant (e.g., "petunias", "sun-loving annuals")
        customer_id: The customer's ID for personalization
        location: Customer's location for climate-specific recommendations

    Returns:
        List of recommended products with details
    """
    logger.info(f"Getting recommendations for {plant_type} in {location}")

    # Mocked recommendations
    return {
        "plant_type": plant_type,
        "location": location,
        "recommendations": [
            {
                "id": "SOIL-CACTI",
                "name": "Desert-Friendly Potting Mix",
                "price": 14.99,
                "reason": "Designed for arid climates like Las Vegas"
            },
            {
                "id": "FERT-BLOOM",
                "name": "Flower Bloom Fertilizer",
                "price": 18.99,
                "reason": "Perfect for sun-loving annuals"
            },
            {
                "id": "MULCH-001",
                "name": "Moisture-Retaining Mulch",
                "price": 9.99,
                "reason": "Helps retain moisture in hot, dry climates"
            }
        ]
    }


@tool("Check Product Availability")
def check_product_availability(product_id: str, store_id: str) -> Dict[str, Any]:
    """
    Checks if a product is in stock at a specific store.

    Args:
        product_id: The product ID to check
        store_id: The store location ID

    Returns:
        Availability status and stock information
    """
    logger.info(f"Checking availability for {product_id} at store {store_id}")

    return {
        "product_id": product_id,
        "store_id": store_id,
        "in_stock": True,
        "quantity": 47,
        "aisle": "12B",
        "message": "In stock and ready for pickup"
    }


@tool("Get Available Planting Times")
def get_available_planting_times(date: str, service_type: str = "planting") -> List[str]:
    """
    Retrieves available time slots for planting services.

    Args:
        date: Date in YYYY-MM-DD format
        service_type: Type of service (default: "planting")

    Returns:
        List of available time slots
    """
    logger.info(f"Getting available times for {service_type} on {date}")

    return {
        "date": date,
        "available_slots": [
            "9:00 AM - 11:00 AM",
            "11:00 AM - 1:00 PM",
            "2:00 PM - 4:00 PM",
            "4:00 PM - 6:00 PM"
        ]
    }


@tool("Schedule Planting Service")
def schedule_planting_service(customer_id: str, date: str, time_range: str, details: str) -> Dict[str, Any]:
    """
    Schedules a professional planting service appointment.

    Args:
        customer_id: The customer's ID
        date: Date in YYYY-MM-DD format
        time_range: Selected time slot
        details: Service details and special requests

    Returns:
        Appointment confirmation
    """
    logger.info(f"Scheduling planting service for customer {customer_id}")

    appointment_id = str(uuid.uuid4())

    return {
        "status": "confirmed",
        "appointment_id": appointment_id,
        "customer_id": customer_id,
        "date": date,
        "time_range": time_range,
        "details": details,
        "message": "Appointment confirmed. Calendar invite sent to customer."
    }


@tool("Send Care Instructions")
def send_care_instructions(customer_id: str, plant_type: str, delivery_method: str, location: str = "Las Vegas, NV") -> Dict[str, str]:
    """
    Sends plant care instructions customized for customer location.

    Args:
        customer_id: The customer's ID
        plant_type: Type of plant
        delivery_method: "email" or "sms"
        location: Customer location for climate-specific advice

    Returns:
        Delivery confirmation
    """
    logger.info(f"Sending {plant_type} care instructions via {delivery_method}")

    return {
        "status": "sent",
        "delivery_method": delivery_method,
        "message": f"Care instructions for {plant_type} sent via {delivery_method}"
    }


@tool("Generate Discount QR Code")
def generate_qr_code(customer_id: str, discount_value: float, discount_type: str, expiration_days: int = 30) -> Dict[str, Any]:
    """
    Generates a QR code for in-store discounts for loyal customers.

    Args:
        customer_id: The customer's ID
        discount_value: Discount amount
        discount_type: "percentage" or "flat"
        expiration_days: Days until code expires

    Returns:
        QR code details and expiration
    """
    logger.info(f"Generating QR code for customer {customer_id}")

    expiration_date = (datetime.now() + timedelta(days=expiration_days)).strftime("%Y-%m-%d")

    return {
        "status": "generated",
        "qr_code_id": str(uuid.uuid4()),
        "discount_value": discount_value,
        "discount_type": discount_type,
        "expiration_date": expiration_date,
        "message": f"QR code sent to customer. Valid until {expiration_date}"
    }


@tool("Update CRM")
def update_salesforce_crm(customer_id: str, interaction_summary: str, tags: List[str]) -> Dict[str, str]:
    """
    Updates customer record in CRM system.

    Args:
        customer_id: The customer's ID
        interaction_summary: Summary of the interaction
        tags: List of tags for categorization

    Returns:
        Update confirmation
    """
    logger.info(f"Updating CRM for customer {customer_id}")

    return {
        "status": "updated",
        "customer_id": customer_id,
        "timestamp": datetime.now().isoformat(),
        "message": "CRM record updated successfully"
    }
