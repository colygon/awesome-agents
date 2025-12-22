# Travel Planner - CrewAI Implementation

## Overview
An intelligent multi-agent travel planning system that creates personalized trip itineraries with flights, hotels, and activities.

## Agents

### 1. Destination Research Expert
- Researches travel destinations
- Considers seasonal factors
- Recommends based on preferences

### 2. Flight Booking Specialist
- Searches for optimal flights
- Compares prices and routes
- Balances cost and convenience

### 3. Accommodation Specialist
- Finds suitable hotels
- Matches lodging to preferences
- Compares prices and reviews

### 4. Itinerary Planning Specialist
- Creates day-by-day itineraries
- Plans activities and attractions
- Balances schedule and rest

### 5. Travel Budget Advisor
- Calculates trip costs
- Provides budget breakdowns
- Identifies savings opportunities

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Run the system:
```bash
python main.py
```

## Features
- Personalized destination recommendations
- Flight search and comparison
- Hotel and accommodation finder
- Detailed daily itineraries
- Comprehensive budget planning
- Activity recommendations

## Planning Process
1. Understand traveler preferences
2. Research suitable destinations
3. Find flights and accommodations
4. Plan daily activities
5. Calculate total budget

## Use Cases
- Vacation planning
- Business trip organization
- Honeymoon planning
- Group travel coordination
- Solo travel itineraries
- Family vacation planning

## Customization
- Budget levels (budget, mid-range, luxury)
- Travel styles (adventure, relaxation, cultural)
- Group size considerations
- Dietary restrictions
- Accessibility needs

## Integration Options
- Flight booking APIs
- Hotel booking platforms
- Activity booking services
- Weather services
- Maps and navigation
