# Personalized Shopping CrewAI Agent

Converted from Google ADK Personalized Shopping to CrewAI implementation with OpenAI.

## Overview

An AI-powered shopping assistant that provides personalized product recommendations based on customer preferences, needs, and budget.

### Agents

1. **Customer Preference Analyst**
   - Role: Analyze customer preferences and shopping behavior
   - Tools: Web search for trend research
   - Output: Comprehensive preference profile with prioritized requirements

2. **Product Research Specialist**
   - Role: Research and evaluate products across e-commerce platforms
   - Tools: Web search for product discovery and reviews
   - Output: Detailed product research with specifications and pricing

3. **Personalized Recommendation Expert**
   - Role: Generate tailored product recommendations
   - Tools: None (synthesizes previous research)
   - Output: Ranked list of personalized recommendations with rationale

## Features

- **Preference analysis**: Deep understanding of customer needs and priorities
- **Product research**: Comprehensive market research across retailers
- **Personalized recommendations**: Tailored suggestions with detailed rationale
- **Budget-aware**: Recommendations within specified budget constraints
- **Multi-criteria matching**: Considers features, price, reviews, brand, style
- **Interactive chat**: Conversational interface for gathering preferences

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
- `SERPER_API_KEY`: Serper API key for web search

## Usage

### Interactive Mode (Recommended)

```bash
python main.py
```

The assistant will guide you through:
1. What you're shopping for
2. Your preferences (brands, features, style, etc.)
3. Budget range
4. Number of recommendations desired

### Python API

```python
from main import get_shopping_recommendations, save_recommendations

# Define preferences
preferences = {
    "primary_use": "Gaming and video editing",
    "must_have_features": "16GB+ RAM, dedicated GPU, SSD",
    "preferred_brands": "ASUS, Dell, Lenovo",
    "style_preferences": "Sleek, professional look"
}

# Get recommendations
result = get_shopping_recommendations(
    product_category="laptop",
    preferences=preferences,
    budget_range="$1000-$1500",
    num_recommendations=5
)

# Save recommendations
save_recommendations(result["recommendations"], "laptop-recommendations.md")
```

## Workflow

1. **Preference Analysis**: Analyst builds comprehensive preference profile
2. **Product Research**: Researcher finds and evaluates matching products
3. **Recommendation Generation**: Engine creates personalized ranked list

## Recommendation Components

Each recommendation includes:
- Product name and brand
- Key specifications
- Price and availability
- Match rationale (why it fits your preferences)
- Pros and cons
- Best use case
- Rating/review summary
- Where to buy (retailers/links)

## Example Use Cases

### Electronics Shopping
```
Category: Laptop
Preferences:
  - Primary use: Software development
  - Must-have: 16GB+ RAM, i7/i9 processor
  - Budget: $1200-$1800
  - Preferred brands: Dell, Lenovo, Apple
```

### Fashion & Apparel
```
Category: Running shoes
Preferences:
  - Primary use: Marathon training
  - Must-have: Good cushioning, arch support
  - Budget: Under $150
  - Style: Bright colors preferred
```

### Home & Garden
```
Category: Coffee maker
Preferences:
  - Primary use: Daily morning coffee for 2 people
  - Must-have: Programmable, thermal carafe
  - Budget: $50-$150
  - Style: Modern, compact
```

## Migration from ADK

### Architecture

This shopping assistant provides:
- E-commerce product recommendations
- Personalized shopping experience
- Conversational interface
- Product discovery and comparison

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| Gemini model | OpenAI GPT-4 |
| `google_search` tool | SerperDevTool |
| Single agent | Three specialized agents |
| ADK conversational flow | CrewAI sequential workflow |

### Agent Design

- **Preference Analyzer**: Understands customer needs and priorities
- **Product Researcher**: Finds and evaluates products
- **Recommendation Engine**: Synthesizes research into personalized suggestions

## Features Not Yet Implemented

- Order history integration
- User profile persistence
- Price tracking and alerts
- Comparison tables
- Visual product gallery

## Customization

### Adding Custom Preferences

Modify the `interactive_shopping_assistant()` function to collect additional preference data:

```python
preferences["color_preference"] = input("Preferred color: ").strip()
preferences["warranty_preference"] = input("Warranty requirements: ").strip()
```

### Adjusting Recommendation Format

Modify the `recommendation_task` description to change output format:
- Add comparison tables
- Include pros/cons scoring
- Add visual descriptions
- Include sustainability ratings

## Best Practices

1. Be specific about requirements and preferences
2. Provide use case context for better recommendations
3. Specify deal-breakers to filter out unsuitable options
4. Use realistic budget ranges
5. Review multiple recommendations to find the best fit

## Original ADK Agent

Based on: Personalized Shopping from [adk-samples](https://github.com/colygon/adk-samples/tree/main/python/agents/personalized-shopping)

## License

Apache License 2.0
