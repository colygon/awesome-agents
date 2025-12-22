# Product Ad Generator - CrewAI Edition

## Overview

The Product Ad Generator is a multi-agent system that creates comprehensive product advertisement campaigns using AI. It combines market research, persuasive copywriting, visual design strategy, performance analysis, and brand alignment to generate complete ad campaigns ready for production.

## Features

1. **Market Research** - Target audience analysis and competitive positioning
2. **Ad Copywriting** - Headlines, body copy, and CTAs optimized for conversion
3. **Visual Design Strategy** - Color psychology, typography, and layout recommendations
4. **Performance Analysis** - Evaluation against best practices and optimization suggestions
5. **Brand Alignment** - Ensures consistency with brand guidelines and values

## Architecture

### CrewAI Agents

1. **Market Research Specialist**
   - Analyzes target audience demographics and psychographics
   - Identifies customer pain points and desires
   - Researches competitive landscape
   - Defines unique selling propositions (USPs)
   - Recommends messaging themes

2. **Creative Copywriter**
   - Creates multiple headline variations
   - Develops short, medium, and long-form copy
   - Crafts compelling calls-to-action
   - Uses persuasive language and emotional triggers
   - Optimizes for specific platforms

3. **Visual Design Strategist**
   - Recommends color palettes based on psychology
   - Suggests typography and hierarchy
   - Defines imagery and visual style
   - Creates layout and composition guidelines
   - Ensures accessibility compliance

4. **Ad Performance Analyst**
   - Evaluates message clarity and impact
   - Assesses persuasion and conversion potential
   - Reviews visual effectiveness
   - Analyzes competitive differentiation
   - Provides A/B testing recommendations

5. **Brand Strategy Specialist**
   - Ensures brand voice consistency
   - Validates visual identity alignment
   - Checks messaging consistency
   - Verifies value proposition fit
   - Reviews compliance requirements

### Custom Tools

1. **Ad Copy Analyzer**
   - Analyzes readability and persuasion elements
   - Counts power words and action verbs
   - Evaluates sentence length and structure
   - Provides improvement recommendations

2. **Headline Generator**
   - Creates variations using proven formulas (How-To, Question, Number, etc.)
   - Generates 8+ headline options
   - Applies copywriting best practices

3. **Color Psychology Advisor**
   - Recommends colors based on emotion and industry
   - Explains color psychology principles
   - Ensures accessibility compliance

4. **CTA Optimizer**
   - Analyzes call-to-action effectiveness
   - Generates optimized variations
   - Provides A/B testing recommendations

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

1. **Clone or navigate to the directory**

```bash
cd product-ad-generator-agent461
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

### Basic Usage

```python
from main import generate_product_ad

# Define your product
product_info = {
    'name': 'EcoBottle Pro',
    'category': 'Sustainable Products',
    'description': 'Self-cleaning water bottle with UV-C purification',
    'features': [
        'UV-C sterilization kills 99.9% of bacteria',
        'Rechargeable battery (30-day life)',
        'Double-wall insulation (24hr cold/12hr hot)',
        'BPA-free stainless steel',
        'Smart reminder app integration'
    ],
    'target_market': 'Eco-conscious professionals aged 25-40',
    'price': '$79.99'
}

# Optional brand guidelines
brand_guidelines = {
    'colors': ['Forest Green (#228B22)', 'Ocean Blue (#006994)'],
    'fonts': ['Raleway', 'Lato'],
    'voice': 'Friendly, informative, and environmentally conscious'
}

# Generate campaign
result = generate_product_ad(
    product_info=product_info,
    platform="social",  # Options: social, search, display, email, general
    brand_guidelines=brand_guidelines
)

print(result)
```

### Command Line Usage

```bash
python main.py
```

This runs the example campaign defined in `main.py`.

### Platform-Specific Campaigns

```python
# Social Media Ad
result = generate_product_ad(product_info, platform="social")

# Search Engine Ad
result = generate_product_ad(product_info, platform="search")

# Display Banner Ad
result = generate_product_ad(product_info, platform="display")

# Email Marketing
result = generate_product_ad(product_info, platform="email")
```

## Campaign Output

The system generates a comprehensive campaign package including:

### 1. Executive Summary
- Product overview
- Target audience snapshot
- Key messaging themes
- Creative strategy overview

### 2. Final Ad Creative
- Primary headline (with alternatives)
- Primary body copy (short/medium/long versions)
- Call-to-action options
- Key selling points

### 3. Visual Specifications
- Recommended color palette with rationale
- Typography guidelines
- Layout and composition recommendations
- Imagery style guide

### 4. Implementation Guide
- Platform-specific adaptations
- Technical specifications (dimensions, character limits)
- Asset requirements
- Launch recommendations

### 5. Testing & Optimization Plan
- A/B test variations
- Success metrics and KPIs
- Optimization timeline
- Performance benchmarks

### 6. Next Steps
- Production requirements
- Review and approval process
- Launch timeline
- Monitoring and reporting plan

## Customization

### Modify Agent Behavior

Edit `agents.py` to customize agent roles, goals, and backstories:

```python
def market_researcher(self) -> Agent:
    return Agent(
        role='Your Custom Role',
        goal='Your specific goals...',
        backstory='Customized backstory...',
        # Add or modify parameters
    )
```

### Add Custom Tools

Create new tools in `tools.py`:

```python
from crewai_tools import BaseTool
from pydantic import BaseModel, Field

class YourCustomToolInput(BaseModel):
    param: str = Field(..., description="Parameter description")

class YourCustomTool(BaseTool):
    name: str = "Your Tool Name"
    description: str = "What your tool does"
    args_schema: Type[BaseModel] = YourCustomToolInput

    def _run(self, param: str) -> str:
        # Your tool logic here
        return "Tool output"
```

### Adjust Task Workflow

Modify `tasks.py` to change the campaign creation process:

```python
def custom_task(self, agent, product_info: dict) -> Task:
    return Task(
        description="Your task description...",
        agent=agent,
        expected_output="Expected deliverable",
        context=[]  # Add dependencies
    )
```

## Best Practices

### Product Information

Provide comprehensive product details:
- Clear, specific product name
- Detailed feature list (3-7 key features)
- Target market demographics
- Pricing information
- Known competitors
- Unique selling propositions

### Brand Guidelines

Include brand specifications for consistency:
- Brand color palette (hex codes)
- Typography (font families)
- Brand voice and tone
- Logo usage guidelines
- Any specific brand requirements

### Platform Selection

Choose the appropriate platform:
- **Social Media**: Short, engaging, visual-first
- **Search Ads**: Keyword-rich, direct response
- **Display Ads**: Visual-focused, brief copy
- **Email**: Longer form, narrative-driven
- **General**: Versatile, multi-platform

## Advanced Features

### Multi-Variation Testing

Generate multiple campaign variations:

```python
platforms = ['social', 'search', 'display']
campaigns = {}

for platform in platforms:
    campaigns[platform] = generate_product_ad(
        product_info=product_info,
        platform=platform,
        brand_guidelines=brand_guidelines
    )
```

### Custom Evaluation Criteria

Add custom performance criteria in `tasks.py`:

```python
def evaluate_ad_performance(self, agent, product_info: dict) -> Task:
    # Add custom evaluation metrics
    # Modify scoring criteria
    # Include industry-specific benchmarks
```

### Industry-Specific Templates

Create pre-configured templates for different industries:

```python
# E-commerce template
ecommerce_guidelines = {
    'colors': ['Trust Blue', 'Conversion Orange'],
    'voice': 'Urgent, benefit-focused, social proof-heavy'
}

# B2B SaaS template
saas_guidelines = {
    'colors': ['Professional Blue', 'Modern Gray'],
    'voice': 'Professional, ROI-focused, data-driven'
}
```

## Performance Optimization

### Reduce API Costs

```python
# Use GPT-3.5-turbo instead of GPT-4
# In agents.py:
llm='gpt-3.5-turbo'

# Reduce verbose logging
# In main.py:
verbose=False
```

### Parallel Processing

For multiple products, process in batches:

```python
from concurrent.futures import ThreadPoolExecutor

products = [product1, product2, product3]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(lambda p: generate_product_ad(p), products)
```

## Troubleshooting

### "OPENAI_API_KEY not found"

```bash
# Ensure .env file exists with your API key
echo "OPENAI_API_KEY=sk-..." > .env
```

### Long execution times

- Reduce the number of agents
- Use GPT-3.5-turbo instead of GPT-4
- Simplify task descriptions
- Disable verbose mode

### Generic or low-quality output

- Provide more detailed product information
- Include specific brand guidelines
- Add competitor information
- Use more specific platform targeting
- Enhance agent backstories with industry expertise

## Integration Examples

### Export to Marketing Platforms

```python
import json

# Save campaign as JSON
campaign_data = {
    'product': product_info,
    'creative': result,
    'platform': platform,
    'timestamp': datetime.now().isoformat()
}

with open('campaign.json', 'w') as f:
    json.dump(campaign_data, f, indent=2)
```

### Batch Processing

```python
import pandas as pd

# Load products from CSV
products_df = pd.read_csv('products.csv')

results = []
for _, row in products_df.iterrows():
    product = {
        'name': row['name'],
        'category': row['category'],
        'description': row['description'],
        'features': row['features'].split('|')
    }

    campaign = generate_product_ad(product)
    results.append(campaign)

# Save results
results_df = pd.DataFrame(results)
results_df.to_csv('campaigns.csv')
```

### API Endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/generate-ad")
async def create_ad(product: dict):
    campaign = generate_product_ad(product)
    return {"campaign": campaign}
```

## Use Cases

1. **E-commerce Product Launches** - Generate ads for new products
2. **Seasonal Campaigns** - Create holiday/event-specific ads
3. **A/B Testing** - Generate multiple variations for testing
4. **Multi-Channel Marketing** - Create platform-specific adaptations
5. **Rebranding** - Align ads with new brand guidelines
6. **Competitor Response** - Quick turnaround competitive ads
7. **Agency Workflows** - Streamline creative development
8. **Content Marketing** - Generate ad content at scale

## Future Enhancements

Potential improvements:

1. **Image Generation** - Integration with DALL-E or Midjourney
2. **Video Ad Scripts** - Extend to video advertising
3. **Localization** - Multi-language campaign generation
4. **Performance Prediction** - ML-based performance forecasting
5. **Real-time A/B Testing** - Integration with ad platforms
6. **Sentiment Analysis** - Analyze emotional impact
7. **Compliance Checking** - Industry-specific regulations
8. **Template Library** - Pre-built industry templates

## License

This implementation is provided as-is for educational and commercial use.

## Acknowledgments

- CrewAI framework for multi-agent orchestration
- OpenAI for language models
- Advertising and copywriting best practices from industry experts

---

**Version:** 1.0.0
**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
**Last Updated:** December 2025
