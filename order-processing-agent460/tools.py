"""
Custom Tools for Order Processing
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import random


class OrderValidationInput(BaseModel):
    order_data: dict = Field(..., description="Order data to validate")


class OrderValidationTool(BaseTool):
    name: str = "Order Validator"
    description: str = "Validates order data against business rules"
    args_schema: Type[BaseModel] = OrderValidationInput

    def _run(self, order_data: dict) -> str:
        try:
            # Simulated validation
            issues = []
            if not order_data.get('customer_email'):
                issues.append("Missing customer email")
            if not order_data.get('shipping_address'):
                issues.append("Missing shipping address")

            if issues:
                return f"Validation FAILED:\n" + "\n".join(f"- {i}" for i in issues)

            return """Order validation PASSED:
- Customer information: Valid
- Shipping address: Valid
- Items: Valid
- Pricing: Correct
- Business rules: Compliant

Status: APPROVED for processing"""
        except Exception as e:
            return f"Error validating order: {str(e)}"


class InventoryCheckInput(BaseModel):
    items: list = Field(..., description="Items to check")


class InventoryCheckTool(BaseTool):
    name: str = "Inventory Checker"
    description: str = "Checks inventory availability across warehouses"
    args_schema: Type[BaseModel] = InventoryCheckInput

    def _run(self, items: list) -> str:
        try:
            results = []
            for item in items:
                stock = random.randint(0, 100)
                warehouse = random.choice(["WH-East", "WH-West", "WH-Central"])

                if stock > 0:
                    results.append(f"✓ {item}: {stock} units available at {warehouse}")
                else:
                    results.append(f"✗ {item}: OUT OF STOCK")

            return "Inventory Check Results:\n" + "\n".join(results) + "\n\nItems reserved for order."
        except Exception as e:
            return f"Error checking inventory: {str(e)}"


class PaymentProcessorInput(BaseModel):
    amount: float = Field(..., description="Payment amount")
    method: str = Field(default="credit_card", description="Payment method")


class PaymentProcessorTool(BaseTool):
    name: str = "Payment Processor"
    description: str = "Processes payments through payment gateway"
    args_schema: Type[BaseModel] = PaymentProcessorInput

    def _run(self, amount: float, method: str = "credit_card") -> str:
        try:
            transaction_id = f"TXN-{random.randint(100000000, 999999999)}"

            return f"""Payment processed successfully:

Transaction ID: {transaction_id}
Amount: ${amount:.2f}
Method: {method}
Status: APPROVED
Authorization Code: {random.randint(100000, 999999)}

Receipt sent to customer email."""
        except Exception as e:
            return f"Error processing payment: {str(e)}"
