#!/usr/bin/env python3
"""
Antom Payment Agent - CrewAI Implementation
Payment processing and transaction management system using CrewAI agents
"""

import os
import json
from crewai import Agent, Task, Crew, Process
from crewai_tools import BaseTool
from langchain_openai import ChatOpenAI
from typing import Type
from pydantic import BaseModel, Field
import datetime

# Initialize OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,  # Lower temperature for financial accuracy
    api_key=os.getenv("OPENAI_API_KEY")
)

# Custom Tools for Payment Processing

class PaymentValidationInput(BaseModel):
    """Input for payment validation"""
    payment_data: str = Field(..., description="JSON string with payment details")

class PaymentValidationTool(BaseTool):
    name: str = "validate_payment"
    description: str = "Validates payment information including amount, currency, and merchant details"
    args_schema: Type[BaseModel] = PaymentValidationInput

    def _run(self, payment_data: str) -> str:
        """Validate payment data"""
        try:
            data = json.loads(payment_data)

            validations = []
            errors = []

            # Validate amount
            if "amount" in data:
                amount = float(data["amount"])
                if amount > 0:
                    validations.append(f"Amount ${amount:.2f} is valid")
                else:
                    errors.append("Amount must be greater than 0")
            else:
                errors.append("Amount is required")

            # Validate currency
            if "currency" in data:
                currency = data["currency"].upper()
                valid_currencies = ["USD", "EUR", "GBP", "CNY", "JPY", "SGD", "HKD"]
                if currency in valid_currencies:
                    validations.append(f"Currency {currency} is supported")
                else:
                    errors.append(f"Currency {currency} not supported")
            else:
                errors.append("Currency is required")

            # Validate merchant
            if "merchant_id" in data:
                validations.append(f"Merchant ID {data['merchant_id']} verified")
            else:
                errors.append("Merchant ID is required")

            result = {
                "valid": len(errors) == 0,
                "validations": validations,
                "errors": errors
            }

            return json.dumps(result, indent=2)

        except Exception as e:
            return json.dumps({"valid": False, "error": str(e)})

class FraudDetectionInput(BaseModel):
    """Input for fraud detection"""
    transaction_data: str = Field(..., description="JSON string with transaction details")

class FraudDetectionTool(BaseTool):
    name: str = "detect_fraud"
    description: str = "Analyzes transactions for potential fraud indicators"
    args_schema: Type[BaseModel] = FraudDetectionInput

    def _run(self, transaction_data: str) -> str:
        """Detect potential fraud"""
        try:
            data = json.loads(transaction_data)

            risk_score = 0
            risk_factors = []

            # Check transaction amount
            amount = float(data.get("amount", 0))
            if amount > 10000:
                risk_score += 30
                risk_factors.append("High transaction amount")
            elif amount > 5000:
                risk_score += 15
                risk_factors.append("Moderate transaction amount")

            # Check unusual time
            if data.get("transaction_time"):
                hour = int(data["transaction_time"].split(":")[0])
                if hour < 6 or hour > 23:
                    risk_score += 10
                    risk_factors.append("Transaction at unusual hour")

            # Check location mismatch
            if data.get("location_mismatch"):
                risk_score += 25
                risk_factors.append("Location does not match user profile")

            # Check velocity
            if data.get("recent_transactions", 0) > 5:
                risk_score += 20
                risk_factors.append("High transaction velocity")

            risk_level = "LOW"
            if risk_score >= 50:
                risk_level = "HIGH"
            elif risk_score >= 25:
                risk_level = "MEDIUM"

            result = {
                "risk_score": risk_score,
                "risk_level": risk_level,
                "risk_factors": risk_factors,
                "recommendation": "BLOCK" if risk_score >= 50 else "REVIEW" if risk_score >= 25 else "APPROVE"
            }

            return json.dumps(result, indent=2)

        except Exception as e:
            return json.dumps({"error": str(e)})

# Initialize tools
payment_validator = PaymentValidationTool()
fraud_detector = FraudDetectionTool()

# Define Agents

# 1. Payment Processor Agent
payment_processor = Agent(
    role="Payment Processing Specialist",
    goal="Process and validate payment transactions accurately and securely",
    backstory="""You are an expert payment processing specialist with deep knowledge
    of payment systems, transaction flows, and validation requirements. You ensure
    all payment details are correct before processing and handle various payment
    methods including cards, wallets, and bank transfers.""",
    verbose=True,
    allow_delegation=False,
    tools=[payment_validator],
    llm=llm
)

# 2. Fraud Detection Agent
fraud_analyst = Agent(
    role="Fraud Detection Analyst",
    goal="Identify and prevent fraudulent transactions",
    backstory="""You are a skilled fraud detection analyst specializing in payment
    security. You analyze transaction patterns, detect anomalies, and identify
    potential fraud using various risk indicators. Your expertise helps protect
    both merchants and customers from fraudulent activities.""",
    verbose=True,
    allow_delegation=False,
    tools=[fraud_detector],
    llm=llm
)

# 3. Settlement Agent
settlement_manager = Agent(
    role="Settlement Manager",
    goal="Manage payment settlements and reconciliation",
    backstory="""You are an experienced settlement manager responsible for ensuring
    payments are properly settled between parties. You handle reconciliation,
    manage settlement schedules, and ensure accurate fund transfers. You understand
    payment clearing processes and settlement timelines.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 4. Customer Support Agent
support_specialist = Agent(
    role="Payment Support Specialist",
    goal="Assist customers with payment issues and inquiries",
    backstory="""You are a knowledgeable payment support specialist who helps
    customers understand payment processes, resolve issues, and answer questions
    about transactions. You provide clear explanations and work to ensure customer
    satisfaction while maintaining security protocols.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def process_payment(payment_info: dict) -> dict:
    """
    Process a payment transaction through the full workflow

    Args:
        payment_info: Dictionary with payment details

    Returns:
        dict with processing results
    """

    payment_json = json.dumps(payment_info)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Task 1: Validate Payment
    validation_task = Task(
        description=f"""Validate the following payment information:
        {payment_json}

        Check:
        1. Amount is valid and positive
        2. Currency is supported
        3. Merchant details are complete
        4. Payment method is valid
        5. Required fields are present

        Use the validate_payment tool to perform validation.
        Provide a clear summary of validation results.""",
        agent=payment_processor,
        expected_output="Payment validation results with any errors identified"
    )

    # Task 2: Fraud Detection
    fraud_task = Task(
        description=f"""Analyze this transaction for fraud indicators:
        {payment_json}
        Transaction time: {current_time}

        Assess:
        1. Transaction amount risk
        2. Timing patterns
        3. Location consistency
        4. Transaction velocity
        5. Overall fraud risk score

        Use the detect_fraud tool to analyze the transaction.
        Provide risk assessment and recommendation.""",
        agent=fraud_analyst,
        expected_output="Fraud risk assessment with recommendation",
        context=[validation_task]
    )

    # Task 3: Settlement Processing
    settlement_task = Task(
        description=f"""Process settlement for this transaction:
        Payment: {payment_json}

        Based on validation and fraud check results:
        1. Determine settlement eligibility
        2. Calculate settlement amount (including fees if applicable)
        3. Determine settlement timeline
        4. Prepare settlement instructions
        5. Log transaction for reconciliation

        Provide detailed settlement plan.""",
        agent=settlement_manager,
        expected_output="Settlement processing plan and timeline",
        context=[validation_task, fraud_task]
    )

    # Task 4: Generate Customer Communication
    support_task = Task(
        description=f"""Prepare customer communication for this payment:
        Payment: {payment_json}

        Based on processing results:
        1. Create transaction confirmation message
        2. Explain any holds or delays
        3. Provide transaction reference
        4. Include next steps if needed
        5. Add support contact information

        Keep communication clear and customer-friendly.""",
        agent=support_specialist,
        expected_output="Customer-facing transaction confirmation message",
        context=[validation_task, fraud_task, settlement_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[payment_processor, fraud_analyst, settlement_manager, support_specialist],
        tasks=[validation_task, fraud_task, settlement_task, support_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "validation": validation_task.output.raw if hasattr(validation_task, 'output') else "",
        "fraud_check": fraud_task.output.raw if hasattr(fraud_task, 'output') else "",
        "settlement": settlement_task.output.raw if hasattr(settlement_task, 'output') else "",
        "customer_message": str(result),
        "metadata": {
            "payment_id": payment_info.get("payment_id", "N/A"),
            "processed_at": current_time
        }
    }

if __name__ == "__main__":
    print("Antom Payment Agent - CrewAI")
    print("=" * 60)

    # Example payment
    print("\nExample Payment Transaction")
    print("-" * 60)

    payment = {
        "payment_id": "PAY-2025-001",
        "amount": "150.00",
        "currency": "USD",
        "merchant_id": "MERCH-12345",
        "customer_id": "CUST-67890",
        "payment_method": "credit_card",
        "card_last4": "4242",
        "transaction_time": "14:30",
        "location_mismatch": False,
        "recent_transactions": 2
    }

    print(json.dumps(payment, indent=2))
    print("\nProcessing payment...\n")

    # Process payment
    result = process_payment(payment)

    # Display results
    print("\n" + "=" * 60)
    print("PAYMENT PROCESSING COMPLETE")
    print("=" * 60)

    print("\n--- Validation ---")
    print(result["validation"])

    print("\n--- Fraud Check ---")
    print(result["fraud_check"])

    print("\n--- Settlement ---")
    print(result["settlement"])

    print("\n--- Customer Message ---")
    print(result["customer_message"])
