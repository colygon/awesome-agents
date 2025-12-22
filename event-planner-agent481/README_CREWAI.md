# Event Planner - CrewAI Edition

## Overview

The Event Planner is a multi-agent system built with CrewAI that helps plan comprehensive events by coordinating three specialized agents:

1. **Venue Coordinator** - Finds and evaluates suitable venues
2. **Schedule Planner** - Creates detailed event timelines
3. **Budget Manager** - Develops financial plans and cost optimization

## Features

- Intelligent venue selection based on capacity, location, and requirements
- Minute-by-minute event schedules with buffer times
- Detailed budget breakdowns with cost-saving recommendations
- Coordination of multiple event aspects (catering, AV, entertainment)
- Contingency planning and risk mitigation
- Per-person cost analysis

## Architecture

### CrewAI Agents

#### 1. Venue Coordination Specialist
- **Role**: Find and evaluate suitable venues
- **Expertise**: Venue logistics, capacity planning, amenities assessment
- **Output**: Ranked venue recommendations with pros/cons

#### 2. Event Timeline Specialist
- **Role**: Design comprehensive event schedules
- **Expertise**: Event pacing, activity coordination, vendor scheduling
- **Output**: Minute-by-minute timeline with contingencies

#### 3. Event Budget Manager
- **Role**: Create and optimize event budgets
- **Expertise**: Cost estimation, vendor negotiations, value optimization
- **Output**: Detailed budget breakdown with payment schedules

### Process Flow

```
Event Details Input
        ↓
Venue Coordinator → Venue Recommendations
        ↓
Schedule Planner → Event Timeline
        ↓
Budget Manager → Financial Plan
        ↓
Comprehensive Event Plan
```

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

1. **Navigate to directory**

```bash
cd event-planner-agent481
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment**

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

### Interactive Mode

```bash
python main.py
```

### Programmatic Usage

```python
from main import plan_event

event_details = {
    "type": "Corporate Conference",
    "guest_count": 150,
    "date": "September 20, 2024",
    "duration": "Full day (8 hours)",
    "location": "Downtown Seattle",
    "budget": "$25,000 - $35,000",
    "requirements": [
        "Conference center with breakout rooms",
        "AV equipment for presentations",
        "Catering for breakfast, lunch, and breaks",
        "Registration area",
        "WiFi for all attendees"
    ]
}

result = plan_event(event_details)
print(result)
```

### Example Output

The system produces:

1. **Venue Report**
   - 3-5 venue options ranked by suitability
   - Detailed comparison matrix
   - Pros/cons for each option
   - Logistics considerations

2. **Event Schedule**
   - Pre-event setup timeline
   - Guest-facing schedule
   - Vendor coordination timeline
   - Contingency plans

3. **Budget Plan**
   - Line-item budget breakdown
   - Cost ranges for each category
   - Payment schedule
   - Cost-saving recommendations

## Event Types Supported

- Corporate events (conferences, team building, meetings)
- Weddings and celebrations
- Birthday parties
- Networking events
- Fundraisers and charity events
- Product launches
- Academic events (graduations, seminars)
- Community gatherings

## Customization

### Adjust Agent Models

```python
# In main.py
agents = create_all_agents(
    model="gpt-3.5-turbo",  # Use faster, cheaper model
    temperature=0.5          # Lower temperature for more consistent output
)
```

### Add Custom Tools

```python
# In tools.py
from crewai_tools import tool

@tool("Vendor Database")
def search_vendors(category: str, location: str) -> str:
    """Search for vendors in specific category and location"""
    # Implement vendor search
    pass
```

### Modify Task Priorities

```python
# In tasks.py - adjust task order or dependencies
tasks = [
    create_budget_task(agents['budget_manager'], event_details),  # Budget first
    create_venue_task(agents['venue_coordinator'], event_details),
    create_schedule_task(agents['schedule_planner'], event_details)
]
```

## Integration Options

### Venue APIs
- Eventbrite Venue
- Tripleseat
- Social Tables
- Google Places API

### Calendar Integration
- Google Calendar
- Microsoft Outlook
- iCal export

### Payment Processing
- Stripe
- PayPal
- Square

### Communication
- SendGrid (email invitations)
- Twilio (SMS reminders)
- Slack notifications

## Best Practices

### Input Specifications

Provide detailed event requirements:
- Event type and purpose
- Expected guest count (with range)
- Preferred date and backup dates
- Location (city/neighborhood)
- Budget range
- Must-have requirements
- Nice-to-have preferences
- Special considerations

### Budget Planning

- Include 10-15% contingency
- Get multiple vendor quotes
- Consider hidden costs (permits, insurance, overtime)
- Track deposits and payment schedules
- Plan for last-minute changes

### Timeline Management

- Allow buffer time between activities
- Account for guest arrival patterns
- Plan for setup and teardown
- Coordinate vendor schedules
- Have backup plans for delays

## Troubleshooting

### "OPENAI_API_KEY not found"

```bash
# Set in .env file
echo "OPENAI_API_KEY=sk-..." > .env
```

### Agent responses too generic

Provide more specific event details:
```python
event_details = {
    "type": "Tech Startup Product Launch",  # More specific
    "theme": "Innovation and Sustainability",
    "target_audience": "Tech investors and early adopters",
    # ... more details
}
```

### Budget estimates inaccurate

Specify your location and tier preferences:
```python
event_details = {
    "location": "San Francisco, CA",  # Specific city
    "tier": "premium",  # budget/moderate/premium
    "cost_priorities": "Quality food and venue over decorations"
}
```

## Performance Optimization

### Reduce API Costs

```python
# Use GPT-3.5-turbo for initial planning
agents = create_all_agents(model="gpt-3.5-turbo", temperature=0.7)

# Use GPT-4 only for final review
review_agent = create_budget_manager_agent(
    ChatOpenAI(model="gpt-4", temperature=0.3)
)
```

### Parallel Processing

For independent tasks, modify the crew process:

```python
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    process=Process.parallel,  # Run tasks in parallel
    verbose=True
)
```

## Advanced Features

### Multi-Day Events

```python
event_details = {
    "type": "Multi-day Conference",
    "duration": "3 days",
    "daily_schedules": {
        "day1": "Registration and workshops",
        "day2": "Main conference sessions",
        "day3": "Networking and closing"
    }
}
```

### Hybrid Events (In-Person + Virtual)

```python
event_details = {
    "format": "hybrid",
    "in_person_capacity": 100,
    "virtual_capacity": 500,
    "streaming_requirements": "Professional AV with live streaming"
}
```

### Vendor Coordination

```python
# Add vendor coordination task
def create_vendor_coordination_task(agent, vendors):
    return Task(
        description=f"Coordinate with vendors: {vendors}",
        agent=agent,
        expected_output="Vendor schedule and contract summaries"
    )
```

## Future Enhancements

Potential improvements:
1. **Real-time venue availability** via API integrations
2. **Automated vendor matching** based on requirements
3. **Guest management** with RSVP tracking
4. **Weather integration** for outdoor events
5. **Post-event analytics** and reporting
6. **Template library** for common event types

## Example Use Cases

### Corporate Team Building
```python
event = {
    "type": "Team Building Retreat",
    "guest_count": 30,
    "duration": "2 days",
    "activities": ["outdoor activities", "team workshops", "dinner"]
}
```

### Wedding Planning
```python
event = {
    "type": "Wedding Reception",
    "guest_count": 120,
    "duration": "6 hours",
    "requirements": ["dance floor", "DJ", "full catering", "bar service"]
}
```

### Product Launch
```python
event = {
    "type": "Product Launch Event",
    "guest_count": 200,
    "duration": "3 hours",
    "requirements": ["demo area", "presentation stage", "media coverage"]
}
```

## License

Apache 2.0

## Support

For issues or questions:
- Check the troubleshooting section
- Review example use cases
- Adjust agent parameters for better results

---

**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
**Agent 481** - Event Planner
