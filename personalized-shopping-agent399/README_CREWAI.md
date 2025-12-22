# Personalized Shopping Agent - CrewAI Implementation

An intelligent personal shopping assistant powered by CrewAI that analyzes preferences, researches products, finds deals, and provides personalized recommendations.

## Overview

This CrewAI implementation simulates a personal shopping service with specialized agents for preference analysis, product research, deal finding, style consulting, and shopping coordination.

## Agents

1. **Shopping Preference Analyst**: Understands customer preferences and builds detailed profiles
2. **Product Research Specialist**: Finds and evaluates products across multiple retailers
3. **Deal and Discount Expert**: Finds best prices, deals, and promotions
4. **Personal Style Consultant**: Provides personalized style advice and combinations
5. **Personal Shopping Coordinator**: Orchestrates the shopping experience and compiles recommendations

## Features

- Customer preference profiling
- Multi-retailer product search
- Price comparison across stores
- Deal and coupon finding
- Price tracking and trend analysis
- Style recommendations and outfit building
- Product combinations and versatility analysis
- Budget-conscious recommendations
- Personalized shopping lists
- Purchase timing optimization

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Required API keys:
- OpenAI API key (or Google Gemini)
- Optional: E-commerce platform APIs (Amazon, Shopify, etc.)

## Usage

### Full Shopping Assistant

```bash
python main.py full "casual style, size M, loves blue and black" "shirts" "$50-100" "wardrobe_refresh"
```

### Quick Product Recommendation

```bash
python main.py quick "comfortable running shoes for daily training" "$80-120"
```

### Programmatic Usage

```python
from main import personal_shopping_assistant

result = personal_shopping_assistant(
    customer_preferences="modern minimalist style, prefers quality over quantity",
    category="clothing",
    budget="$200-500",
    shopping_goal="seasonal_wardrobe"
)
```

## Parameters

### Customer Preferences

Include information about:
- **Style**: casual, formal, modern, classic, minimalist, etc.
- **Sizes**: clothing sizes, shoe sizes
- **Colors**: preferred and avoided colors
- **Brands**: favorite brands
- **Materials**: fabric preferences
- **Quality expectations**: budget, mid-range, premium

### Categories

- `clothing`: Shirts, pants, dresses, jackets, etc.
- `shoes`: All types of footwear
- `accessories`: Bags, jewelry, watches, belts
- `home`: Home decor and furnishings
- `electronics`: Tech gadgets and devices

### Shopping Goals

- `wardrobe_refresh`: Building or updating wardrobe
- `specific_item`: Looking for a specific product
- `gift`: Shopping for someone else
- `occasion`: Special event or occasion
- `seasonal`: Seasonal wardrobe update

## Output

The system generates a comprehensive shopping guide including:

### Customer Profile
- Style analysis
- Preference summary
- Budget considerations
- Lifestyle factors

### Product Recommendations
- 10-15 curated product options
- Why each product is recommended
- Match score for preferences
- Product features and benefits
- Customer ratings and reviews

### Price and Deal Information
- Current prices across retailers
- Available discounts and coupons
- Price history and trends
- Best time to buy
- Total cost breakdown

### Style Recommendations
- How to wear/use each product
- Product combinations
- Outfit suggestions
- Versatility analysis
- Styling tips

### Shopping List
- Prioritized recommendations
- Direct purchase links
- Budget allocation
- Alternative options
- Purchase strategy

## Customization

Modify these files to customize behavior:
- `agents.py`: Adjust agent expertise and roles
- `tasks.py`: Modify shopping workflow and deliverables
- `tools.py`: Add e-commerce API integrations
- `main.py`: Change assistant orchestration

## Advanced Features

### E-commerce API Integration

Integrate with real e-commerce platforms in `tools.py`:

**Amazon Product API**
```python
from amazon.paapi import AmazonAPI
```

**Shopify API**
```python
import shopify
```

**Price Tracking**
```python
# CamelCamelCamel, Honey, or similar
```

### Machine Learning Recommendations

Add ML-based recommendations:

```python
from sklearn.metrics.pairwise import cosine_similarity
# Collaborative filtering for product recommendations
```

### Visual Search

Add image-based product search:

```python
from google.cloud import vision
# Visual similarity search
```

### Size Recommendation

Integrate size recommendation systems:

```python
# Based on body measurements and fit preferences
```

## Example Use Cases

### Personal Wardrobe Building
```bash
python main.py full "professional casual, size 32x32, neutral colors" "clothing" "$500-1000" "wardrobe_refresh"
```

### Gift Shopping
```bash
python main.py full "tech-savvy, outdoor enthusiast, 30s" "accessories" "$100-200" "gift"
```

### Specific Item Search
```bash
python main.py quick "waterproof hiking boots, size 10" "$150-250"
```

### Seasonal Shopping
```bash
python main.py full "winter essentials, cold climate" "clothing" "$300-600" "seasonal"
```

## Shopping Workflow

1. **Preference Analysis**: Understanding your style and needs
2. **Product Research**: Finding matching products across retailers
3. **Deal Finding**: Identifying best prices and discounts
4. **Style Consulting**: Creating coordinated recommendations
5. **List Compilation**: Organizing final recommendations

## Best Practices

1. **Be Specific**: Provide detailed preferences for better matches
2. **Set Realistic Budgets**: Include some flexibility in budget range
3. **Review Alternatives**: Consider multiple price points
4. **Check Timing**: Some recommendations may suggest waiting for sales
5. **Verify Sizes**: Double-check sizing charts before purchase
6. **Read Reviews**: Pay attention to customer review summaries
7. **Compare Shipping**: Factor in shipping costs and time

## Integration Opportunities

- **Customer Loyalty Programs**: Track points and rewards
- **Wardrobe Management**: Catalog existing items
- **Trend Forecasting**: Predict upcoming trends
- **Sustainability Scoring**: Rate products on sustainability
- **Virtual Try-On**: AR/VR integration for visualization
- **Social Shopping**: Share and collaborate on recommendations

## Notes

- Shopping lists saved to text files for easy reference
- Price tracking helps optimize purchase timing
- Multi-retailer comparison ensures best value
- Style combinations maximize wardrobe versatility
- Budget-conscious alternatives always provided
- Best used with actual e-commerce API integrations
- Recommendations based on AI analysis of preferences
- Always verify product details before purchasing
