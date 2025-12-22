# Customer Service Agent - CrewAI Implementation

Intelligent customer support system using multi-agent architecture for handling customer inquiries.

## Overview

An advanced customer service system powered by CrewAI with five specialized agents that collaborate to provide high-quality, empathetic, and accurate customer support responses.

### Agents

1. **Customer Service Triage Specialist**
   - Role: Analyze and categorize customer inquiries
   - Capabilities: Urgency assessment, sentiment analysis, issue categorization
   - Output: Structured triage assessment with routing recommendations

2. **Customer Support Representative**
   - Role: Provide helpful responses to customer inquiries
   - Capabilities: Knowledge base search, solution finding, clear communication
   - Tools: Knowledge base search, web search
   - Output: Empathetic customer support response

3. **Technical Support Specialist**
   - Role: Handle technical issues and troubleshooting
   - Capabilities: Technical diagnosis, detailed solutions, step-by-step guidance
   - Tools: Knowledge base search, web search
   - Output: Technically enhanced response with troubleshooting steps

4. **Customer Escalation Manager**
   - Role: Handle complex or sensitive issues
   - Capabilities: Decision-making authority, exception approval, conflict resolution
   - Output: Escalation handling and resolution

5. **Customer Service Quality Assurance**
   - Role: Ensure response quality and accuracy
   - Capabilities: Quality scoring, accuracy verification, tone assessment
   - Output: Final approved customer response

## Features

- **Multi-agent workflow**: Five agents collaborate on each inquiry
- **Intelligent triage**: Automatic urgency and sentiment assessment
- **Knowledge base integration**: Searchable FAQ and product information
- **Quality assurance**: Every response reviewed for accuracy and tone
- **Empathetic communication**: Professional, friendly, customer-focused responses
- **Technical support**: Detailed troubleshooting for technical issues
- **Scalable architecture**: Easy to extend with more agents or capabilities

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

Optional:
- `SERPER_API_KEY`: Serper API key for web search

## Usage

### Command Line

```bash
python main.py
```

Choose from example scenarios or enter a custom customer inquiry.

### Python API

```python
from main import handle_customer_inquiry

# Handle a customer inquiry
result = handle_customer_inquiry(
    customer_message="I can't log into my account and need urgent help",
    customer_name="Jane Smith",
    customer_history="Premium member since 2022, 3 previous support tickets"
)

# Access different components
print(result["triage"])
print(result["support_response"])
print(result["technical_review"])
print(result["final_response"])
```

## Support Workflow

### 1. Triage Assessment
The triage agent analyzes each inquiry for:
- **Urgency**: Low / Medium / High / Critical
- **Sentiment**: Positive / Neutral / Frustrated / Angry
- **Category**: Account, Product, Technical, Billing, Shipping, Other
- **Complexity**: Simple / Moderate / Complex
- **Recommended Routing**: Support / Technical / Escalation

### 2. Support Response
The support agent:
- Addresses customer by name
- Acknowledges concerns with empathy
- Searches knowledge base for accurate information
- Provides clear, actionable solutions
- Offers additional assistance
- Maintains professional tone

### 3. Technical Review
The technical specialist:
- Reviews for technical accuracy
- Adds detailed troubleshooting steps
- Includes technical specifications
- Provides alternative solutions
- Adds preventive measures

### 4. Quality Assurance
The QA agent checks:
- **Accuracy**: Information correctness
- **Completeness**: All concerns addressed
- **Tone**: Professional and empathetic
- **Clarity**: Easy to understand
- **Policy Compliance**: Follows guidelines

Provides quality score (1-10) and final approved response.

## Knowledge Base

The system includes a simulated knowledge base covering:

### Account Management
- Password resets
- Account security
- Profile updates
- Login issues

### Shipping & Delivery
- Shipping times and costs
- Tracking information
- Delivery issues
- International shipping

### Returns & Refunds
- Return process
- Refund timelines
- Return shipping
- Exchange policies

### Product Information
- Product warranties
- Product specifications
- Usage instructions
- Compatibility

### Order Management
- Order cancellation
- Order modifications
- Order tracking
- Order history

## Example Scenarios

### Password Reset Issue
```python
result = handle_customer_inquiry(
    customer_message="I forgot my password and the reset link isn't working. I've tried three times!",
    customer_name="Sarah Johnson",
    customer_history="Premium member since 2023"
)
```

### Shipping Inquiry
```python
result = handle_customer_inquiry(
    customer_message="Where is my order? It's been 10 days and the tracking hasn't updated.",
    customer_name="Michael Chen",
    customer_history="New customer, first order"
)
```

### Product Complaint
```python
result = handle_customer_inquiry(
    customer_message="The product stopped working after 2 weeks. This is unacceptable! I want a full refund.",
    customer_name="Alex Rivera",
    customer_history="Regular customer, no previous complaints"
)
```

## Sentiment Handling

The system adapts responses based on customer sentiment:

### Positive/Neutral
- Friendly, helpful tone
- Standard support process
- Focus on solution

### Frustrated
- Extra empathy and acknowledgment
- Expedited handling
- Proactive follow-up offers

### Angry
- Immediate empathy and apology
- Senior agent involvement
- Exception consideration
- Retention focus

## Response Quality Standards

Every response must:
1. Address customer by name
2. Acknowledge the specific issue
3. Show empathy and understanding
4. Provide clear, actionable solutions
5. Explain next steps
6. Offer additional assistance
7. Include contact information for follow-up
8. Maintain professional tone
9. Use clear, simple language
10. Be accurate and complete

## Migration from ADK

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| Triage system | Triage Specialist agent |
| Support bot | Support Representative agent |
| Technical support | Technical Specialist agent |
| Escalation handler | Escalation Manager agent |
| Quality checker | QA Specialist agent |
| Gemini model | OpenAI GPT-4 |
| Knowledge retrieval | Custom Knowledge Base Tool |

### Architecture Differences

- **ADK**: Rule-based routing with AI enhancement
- **CrewAI**: Full multi-agent collaboration workflow
- **LLM**: Migrated from Google Gemini to OpenAI GPT-4
- **Tools**: Custom CrewAI BaseTool for knowledge base

## Customization

### Extending the Knowledge Base

Edit the `KnowledgeBaseTool._run()` method to add more FAQs:

```python
knowledge_base = {
    "your_topic": {
        "answer": "Your answer here",
        "category": "Your Category"
    },
    # Add more entries...
}
```

### Adding New Agent Roles

Create additional specialized agents:

```python
billing_agent = Agent(
    role="Billing Specialist",
    goal="Handle billing and payment inquiries",
    backstory="...",
    tools=[kb_tool],
    llm=llm
)
```

### Customizing Response Tone

Adjust agent backstories to change communication style:
- More formal for enterprise customers
- More casual for consumer products
- Multilingual for international support

## Best Practices

### For Customer Service Teams
1. Train agents with real customer interactions
2. Regularly update knowledge base
3. Monitor quality scores
4. Review escalated cases
5. Collect customer feedback

### For Implementation
1. Start with core scenarios
2. Expand knowledge base iteratively
3. Integrate with ticketing system
4. Set up monitoring and analytics
5. Establish escalation procedures

## Performance Metrics

Track these KPIs:
- **First Response Time**: Time to initial response
- **Resolution Rate**: Percentage resolved without escalation
- **Quality Score**: Average QA score
- **Customer Satisfaction**: CSAT ratings
- **Escalation Rate**: Percentage requiring escalation

## Limitations

- Knowledge base is simulated (needs real integration)
- No CRM/ticketing system integration in demo
- Limited customer history tracking
- No sentiment analysis training on company data
- Requires API costs for production use

## Future Enhancements

- Integration with CRM systems (Salesforce, HubSpot)
- Connection to ticketing systems (Zendesk, Freshdesk)
- Real-time sentiment analysis
- Multi-language support
- Chat and email channel support
- Automated follow-up scheduling
- Customer feedback loop
- Performance analytics dashboard
- A/B testing for response strategies

## Original ADK Agent

Based on: Google Agent Development Kit (ADK) Customer Service sample

## License

Apache License 2.0
