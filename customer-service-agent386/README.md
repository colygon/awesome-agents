# Customer Service Agent - CrewAI Implementation

Upgraded from Google ADK to CrewAI framework.

## Overview

AI-powered customer support system for Cymbal Home & Garden that handles support tickets, provides product assistance, and manages customer interactions through a multi-agent workflow.

## Architecture

### CrewAI Agents

1. **Ticket Analyzer**
   - Role: Support Ticket Analyst
   - Analyzes incoming support requests
   - Categorizes issues and determines priority
   - Identifies customer needs and context

2. **Solution Researcher**
   - Role: Product & Solutions Expert
   - Researches product information and solutions
   - Accesses knowledge base and documentation
   - Identifies relevant products and alternatives

3. **Response Generator**
   - Role: Customer Communication Specialist
   - Crafts personalized customer responses
   - Handles upselling and service recommendations
   - Ensures professional and empathetic communication

## Original ADK Features

- Personalized customer assistance with purchase history
- Product identification and recommendations
- Shopping cart management
- Appointment scheduling for services
- Discount approval workflows
- CRM integration (Salesforce)
- Video call companion for visual support

## CrewAI Implementation

### Tools Implemented

- **Ticket Analysis Tools**: Categorize and prioritize tickets
- **Product Lookup Tools**: Search product catalog and check availability
- **Cart Management Tools**: Access and modify customer carts
- **CRM Tools**: Update customer records
- **Communication Tools**: Send emails, SMS, and care instructions
- **Scheduling Tools**: Check availability and book appointments
- **Approval Tools**: Handle discount requests

### Workflow

1. Ticket Analyzer receives and analyzes customer request
2. Solution Researcher finds relevant products and solutions
3. Response Generator creates personalized response with recommendations
4. System handles cart updates, appointments, and follow-ups

## Setup

```bash
cd customer-service-agent386
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python main.py
```

## Usage

```python
from agents import run_customer_service

result = run_customer_service(
    customer_id="123",
    message="I need help with my garden plants"
)
print(result)
```

## Migration Notes

- ADK single-agent architecture → CrewAI multi-agent workflow
- ADK tools → CrewAI custom tools
- State management migrated to task context
- Callbacks replaced with CrewAI task observers
