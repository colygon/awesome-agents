# Antom Payment Agent - CrewAI Implementation

Payment processing and transaction management system using CrewAI multi-agent architecture.

## Overview

An intelligent payment processing system powered by CrewAI with four specialized agents that handle the complete payment lifecycle from validation to customer communication.

### Agents

1. **Payment Processing Specialist**
   - Role: Process and validate payment transactions
   - Capabilities: Validation, payment method verification, data completeness checks
   - Tools: Payment validation tool
   - Output: Payment validation results

2. **Fraud Detection Analyst**
   - Role: Identify and prevent fraudulent transactions
   - Capabilities: Risk scoring, pattern analysis, anomaly detection
   - Tools: Fraud detection tool
   - Output: Risk assessment with recommendations

3. **Settlement Manager**
   - Role: Manage payment settlements and reconciliation
   - Capabilities: Settlement scheduling, fee calculation, fund transfer management
   - Tools: None (uses context from validation and fraud check)
   - Output: Settlement processing plan

4. **Payment Support Specialist**
   - Role: Customer communication and support
   - Capabilities: Transaction confirmations, issue explanation, support guidance
   - Tools: None (focuses on communication)
   - Output: Customer-facing messages

## Features

- **Multi-agent workflow**: Four agents collaborate on payment processing
- **Payment validation**: Comprehensive validation of amount, currency, merchant
- **Fraud detection**: Risk scoring based on multiple indicators
- **Settlement management**: Automated settlement processing and reconciliation
- **Customer communication**: Clear, professional transaction confirmations
- **Multi-currency support**: USD, EUR, GBP, CNY, JPY, SGD, HKD

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys
```

## Configuration

Required API keys:
- `OPENAI_API_KEY`: OpenAI API key for GPT-4

Optional (for production integration):
- `ANTOM_API_KEY`: Antom Payment Gateway API key
- `ANTOM_MERCHANT_ID`: Merchant identification

## Usage

### Command Line

```bash
python main.py
```

The script runs with an example payment transaction and shows the full processing workflow.

### Python API

```python
from main import process_payment

# Create payment information
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

# Process payment
result = process_payment(payment)

# Access results
print(result["validation"])
print(result["fraud_check"])
print(result["settlement"])
print(result["customer_message"])
```

## Payment Processing Workflow

1. **Validation Phase**
   - Verify payment amount is positive
   - Check currency is supported
   - Validate merchant details
   - Ensure required fields are present

2. **Fraud Detection Phase**
   - Analyze transaction amount
   - Check transaction timing
   - Verify location consistency
   - Assess transaction velocity
   - Calculate risk score and recommendation

3. **Settlement Phase**
   - Determine settlement eligibility
   - Calculate settlement amount and fees
   - Set settlement timeline
   - Prepare settlement instructions

4. **Customer Communication Phase**
   - Generate transaction confirmation
   - Explain any holds or delays
   - Provide transaction reference
   - Include support contact info

## Fraud Detection

The fraud detection system analyzes multiple risk factors:

### Risk Factors
- **High Amount**: Transactions over $10,000 (+30 points)
- **Moderate Amount**: Transactions over $5,000 (+15 points)
- **Unusual Hours**: Transactions between 11 PM and 6 AM (+10 points)
- **Location Mismatch**: User location doesn't match profile (+25 points)
- **High Velocity**: More than 5 recent transactions (+20 points)

### Risk Levels
- **LOW** (0-24): Safe to approve
- **MEDIUM** (25-49): Requires review
- **HIGH** (50+): Recommend blocking

### Recommendations
- **APPROVE**: Low risk, process normally
- **REVIEW**: Medium risk, manual review needed
- **BLOCK**: High risk, block transaction

## Supported Currencies

- USD - US Dollar
- EUR - Euro
- GBP - British Pound
- CNY - Chinese Yuan
- JPY - Japanese Yen
- SGD - Singapore Dollar
- HKD - Hong Kong Dollar

## Custom Tools

### Payment Validation Tool
Validates payment information including:
- Amount validation (must be positive)
- Currency support check
- Merchant ID verification
- Required field validation

### Fraud Detection Tool
Analyzes transactions for fraud indicators:
- Transaction amount analysis
- Timing pattern detection
- Location verification
- Velocity checking
- Risk score calculation

## Migration from ADK

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| Payment processor | Payment Processing Specialist agent |
| Fraud detector | Fraud Detection Analyst agent |
| Settlement handler | Settlement Manager agent |
| Support system | Payment Support Specialist agent |
| Gemini model | OpenAI GPT-4 |
| Custom tools | CrewAI BaseTool implementations |

### Architecture Differences

- **ADK**: Uses task-based orchestration
- **CrewAI**: Sequential agent workflow with context passing
- **LLM**: Migrated from Google Gemini to OpenAI GPT-4
- **Tools**: Custom tools implemented using CrewAI BaseTool

## Example Output

```
Payment Processing Complete
---------------------------
Validation: ✓ All checks passed
Fraud Check: LOW RISK (Score: 15)
Settlement: Approved for next-day settlement
Customer Message: Your payment of $150.00 has been successfully processed.
```

## Security Considerations

- Never log full card numbers (only last 4 digits)
- Use environment variables for API keys
- Implement proper authentication for production
- Follow PCI DSS compliance guidelines
- Use HTTPS for all API communications
- Implement rate limiting and monitoring

## Limitations

- This is a demonstration system, not production-ready
- Fraud detection uses simplified rules (production systems need ML models)
- No actual payment gateway integration in demo mode
- Requires proper PCI compliance for handling real card data

## Future Enhancements

- Integration with real Antom Payment Gateway API
- Machine learning-based fraud detection
- Support for additional payment methods (wallets, bank transfers)
- Subscription and recurring payment support
- Refund and chargeback handling
- Advanced settlement reconciliation

## Original ADK Agent

Based on: Google Agent Development Kit (ADK) Antom Payment sample

## License

Apache License 2.0
