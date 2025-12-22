# AI Customer Support - CrewAI Edition

## Overview

An intelligent customer service automation system that analyzes customer inquiries, performs sentiment analysis, searches knowledge bases, provides troubleshooting guidance, and manages escalations. Built on CrewAI to deliver empathetic, efficient customer support.

## Features

1. **Sentiment Analysis** - Understands customer emotional state and urgency
2. **Knowledge Base Search** - Finds relevant solutions and documentation
3. **Technical Troubleshooting** - Provides step-by-step resolution guides
4. **Escalation Management** - Handles complex cases appropriately
5. **Draft Responses** - Generates empathetic, professional responses
6. **Priority Assessment** - Classifies and prioritizes support tickets

## Architecture

### CrewAI Agents

1. **Support Specialist Agent** (`support_specialist`)
   - Role: Provides accurate, empathetic customer support
   - Tools: KnowledgeBaseTool, SentimentAnalysisTool
   - Analyzes inquiries and drafts responses

2. **Issue Resolver Agent** (`issue_resolver`)
   - Role: Diagnoses and resolves technical issues
   - Tools: KnowledgeBaseTool, TicketAnalysisTool
   - Creates troubleshooting guides

3. **Escalation Manager Agent** (`escalation_manager`)
   - Role: Manages complex and escalated cases
   - Tools: TicketAnalysisTool, SentimentAnalysisTool
   - Coordinates resolution plans

### Custom Tools

1. **KnowledgeBaseTool**
   - Searches company knowledge base
   - Returns solutions, guides, and documentation
   - Categorized search capabilities

2. **TicketAnalysisTool**
   - Analyzes support tickets comprehensively
   - Identifies root causes and resolution strategies
   - Assesses priority and urgency

3. **SentimentAnalysisTool**
   - Analyzes customer emotional state
   - Detects frustration, urgency, satisfaction
   - Provides response recommendations

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

```bash
cd ai-customer-support-agent453
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Usage

### Command Line
```bash
python main.py "My account is locked and I can't log in"
```

### Interactive Mode
```bash
python main.py
```

## Use Cases

- **Customer Service Teams** - Augment human agents
- **Self-Service Portals** - Power chatbots and help centers
- **Ticket Triage** - Automatically classify and route tickets
- **Quality Assurance** - Generate model responses for training
- **24/7 Support** - Provide after-hours assistance

## License

Apache 2.0

---

**Version:** 1.0.0
**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
