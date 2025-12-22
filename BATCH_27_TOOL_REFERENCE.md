# Batch 27: Custom Tool Reference Guide

## 📚 Overview

This document provides detailed reference for all 18 custom tools created for Batch 27 apps.

**Total Tools:** 18 across 6 domains
**Architecture:** All tools use Pydantic validation with BaseTool interface
**Pattern:** Type-safe inputs, JSON outputs, comprehensive error handling

---

## 💳 Payment Tools (Antom Payment - 382)

### 1. PaymentGatewayTool

**Purpose:** Process payments through various payment gateways

**Input Schema:**
```python
class PaymentGatewayInput(BaseModel):
    amount: float        # Payment amount (required)
    currency: str        # Currency code, e.g., USD, EUR (required)
    payment_method: str  # Payment method: card, bank, wallet (required)
    customer_id: str     # Customer identifier (required)
```

**Output Format:**
```json
{
  "status": "success",
  "transaction_id": "TXN-...",
  "amount": 99.99,
  "currency": "USD",
  "payment_method": "card",
  "timestamp": "2025-12-21T10:30:00Z"
}
```

**Use Cases:**
- Process credit card payments
- Handle bank transfers
- Process digital wallet payments
- Support multiple currencies

---

### 2. TransactionValidatorTool

**Purpose:** Validate transactions for compliance and fraud

**Input Schema:**
```python
class TransactionValidatorInput(BaseModel):
    transaction_data: str  # JSON string of transaction data (required)
```

**Output Format:**
```json
{
  "amount_valid": true,
  "currency_valid": true,
  "customer_verified": true,
  "fraud_score": 0.05,
  "compliance_passed": true
}
```

**Validation Checks:**
- Amount validation (positive, within limits)
- Currency validation (supported currencies)
- Customer verification
- Fraud detection (scoring)
- Compliance requirements

---

### 3. ReceiptGeneratorTool

**Purpose:** Generate and send payment receipts

**Input Schema:**
```python
class ReceiptGeneratorInput(BaseModel):
    transaction_id: str    # Transaction ID (required)
    customer_email: str    # Customer email (required)
```

**Output Format:**
```json
{
  "receipt_id": "RCP-TXN-...",
  "sent_to": "customer@example.com",
  "format": "PDF",
  "delivery_status": "sent"
}
```

**Features:**
- PDF receipt generation
- Email delivery
- Transaction details inclusion
- Branding customization

---

## 🔍 SEO Tools (Brand Search Optimization - 384)

### 4. SEOAnalyzerTool

**Purpose:** Analyze website SEO performance

**Input Schema:**
```python
class SEOAnalyzerInput(BaseModel):
    url: str         # URL to analyze (required)
    keywords: str    # Target keywords, comma-separated (required)
```

**Output Format:**
```json
{
  "url": "https://example.com",
  "seo_score": 78,
  "meta_tags": {
    "title": "Good",
    "description": "Needs improvement"
  },
  "keywords_density": {
    "primary": 2.5,
    "secondary": 1.2
  },
  "page_speed": 85,
  "mobile_friendly": true,
  "recommendations": [
    "Improve meta description",
    "Add alt tags to images"
  ]
}
```

**Analysis Areas:**
- Meta tags quality
- Keyword density
- Page speed
- Mobile compatibility
- Technical SEO

---

### 5. KeywordResearchTool

**Purpose:** Research keywords with search volume and competition data

**Input Schema:**
```python
class KeywordResearchInput(BaseModel):
    topic: str                # Topic or industry (required)
    location: str = "US"      # Target location (optional, default: US)
```

**Output Format:**
```json
{
  "primary_keywords": [
    {
      "keyword": "AI productivity tools",
      "volume": 5400,
      "difficulty": "medium"
    }
  ],
  "long_tail_keywords": [
    {
      "keyword": "how to use AI productivity tools",
      "volume": 2200,
      "difficulty": "low"
    }
  ],
  "trending": true
}
```

**Data Points:**
- Search volume estimates
- Competition difficulty
- Long-tail opportunities
- Trend indicators

---

### 6. RankingTrackerTool

**Purpose:** Monitor search engine rankings

**Input Schema:**
```python
class RankingTrackerInput(BaseModel):
    domain: str      # Domain to track (required)
    keywords: str    # Keywords to monitor, comma-separated (required)
```

**Output Format:**
```json
{
  "domain": "example.com",
  "date": "2025-12-21",
  "rankings": [
    {
      "keyword": "AI tools",
      "position": 7,
      "change": "+2"
    }
  ],
  "visibility_score": 42.3
}
```

**Metrics:**
- Current positions
- Position changes
- Visibility score
- Ranking history

---

## 🖼️ Vision Tools (Image Scoring - 394)

### 7. VisionAnalysisTool

**Purpose:** Perform computer vision analysis on images

**Input Schema:**
```python
class VisionAnalysisInput(BaseModel):
    image_url: str                              # Image URL or path (required)
    analysis_type: str = "comprehensive"        # Analysis type (optional)
```

**Output Format:**
```json
{
  "image_url": "https://example.com/image.jpg",
  "objects_detected": ["person", "laptop", "desk"],
  "scene": "office workspace",
  "dominant_colors": ["#4A90E2", "#F5F5F5"],
  "composition": "rule of thirds",
  "lighting": "natural, well-balanced",
  "resolution": "1920x1080",
  "format": "JPEG"
}
```

**Analysis Types:**
- comprehensive (default)
- objects (object detection only)
- quality (technical quality only)

---

### 8. QualityScorerTool

**Purpose:** Score image quality across multiple dimensions

**Input Schema:**
```python
class QualityScorerInput(BaseModel):
    image_data: str  # Image analysis data as JSON string (required)
```

**Output Format:**
```json
{
  "overall_quality": 8.5,
  "technical_score": 9.0,
  "composition_score": 8.2,
  "aesthetic_score": 8.3,
  "metrics": {
    "sharpness": 0.92,
    "exposure": 0.88,
    "noise_level": 0.15,
    "color_balance": 0.85
  },
  "grade": "A-"
}
```

**Scoring Dimensions:**
- Technical quality (0-10)
- Composition (0-10)
- Aesthetic appeal (0-10)
- Individual metrics (0-1)
- Letter grade (A-F)

---

### 9. ContentDetectionTool

**Purpose:** Detect objects, faces, text, and inappropriate content

**Input Schema:**
```python
class ContentDetectionInput(BaseModel):
    image_url: str                         # Image URL or path (required)
    detection_categories: str = "all"      # Categories (optional, default: all)
```

**Output Format:**
```json
{
  "objects": [
    {
      "name": "laptop",
      "confidence": 0.95,
      "bbox": [100, 200, 400, 500]
    }
  ],
  "faces": [
    {
      "bbox": [120, 150, 180, 220],
      "age": "25-35",
      "expression": "neutral"
    }
  ],
  "text": ["MacBook Pro", "2025"],
  "safety": {
    "appropriate": true,
    "categories_flagged": []
  }
}
```

**Detection Categories:**
- all (default)
- objects
- faces
- text

---

## 🤖 Evaluation Tools (LLM Auditor - 395)

### 10. ModelEvaluationTool

**Purpose:** Evaluate LLM responses across quality criteria

**Input Schema:**
```python
class ModelEvaluationInput(BaseModel):
    model_name: str                                 # Model name (required)
    test_prompt: str                                # Test prompt (required)
    criteria: str = "accuracy,relevance,coherence"  # Evaluation criteria (optional)
```

**Output Format:**
```json
{
  "model": "claude-sonnet-4-5",
  "prompt": "Explain quantum computing",
  "response_quality": {
    "accuracy": 0.87,
    "relevance": 0.92,
    "coherence": 0.89,
    "helpfulness": 0.85
  },
  "safety_checks": {
    "toxicity": 0.02,
    "bias": 0.15,
    "appropriate": true
  },
  "performance": {
    "response_time_ms": 450,
    "tokens_generated": 230
  }
}
```

**Evaluation Criteria:**
- Accuracy (0-1)
- Relevance (0-1)
- Coherence (0-1)
- Helpfulness (0-1)
- Safety metrics (0-1)

---

### 11. BenchmarkTool

**Purpose:** Run performance benchmarks on LLMs

**Input Schema:**
```python
class BenchmarkInput(BaseModel):
    model_name: str                    # Model to benchmark (required)
    benchmark_suite: str = "standard"  # Benchmark suite (optional)
```

**Output Format:**
```json
{
  "model": "claude-sonnet-4-5",
  "suite": "standard",
  "scores": {
    "reasoning": 0.82,
    "knowledge": 0.88,
    "coding": 0.75,
    "math": 0.79,
    "creative_writing": 0.91
  },
  "latency_p95_ms": 520,
  "throughput_tokens_per_sec": 180,
  "overall_score": 0.83
}
```

**Benchmark Suites:**
- standard (default)
- reasoning
- coding
- creative

---

### 12. MetricsAggregatorTool

**Purpose:** Aggregate metrics from multiple evaluations

**Input Schema:**
```python
class MetricsAggregatorInput(BaseModel):
    evaluation_results: str  # JSON string of evaluation results (required)
    benchmark_results: str   # JSON string of benchmark results (required)
```

**Output Format:**
```json
{
  "summary": {
    "overall_performance": 0.84,
    "quality_score": 0.88,
    "efficiency_score": 0.80,
    "safety_score": 0.95
  },
  "strengths": ["creative tasks", "knowledge retrieval"],
  "weaknesses": ["coding", "mathematical reasoning"],
  "recommendations": [
    "Improve code generation",
    "Enhance math reasoning"
  ],
  "grade": "B+"
}
```

**Aggregation Methods:**
- Weighted averages
- Comparative analysis
- Trend identification
- Recommendation generation

---

## 🛡️ Safety Tools (Safety Plugins - 403)

### 13. ContentFilterTool

**Purpose:** Filter unsafe and inappropriate content

**Input Schema:**
```python
class ContentFilterInput(BaseModel):
    content: str                      # Content to filter (required)
    filter_level: str = "moderate"    # Filter level (optional)
```

**Output Format:**
```json
{
  "content_length": 150,
  "filter_level": "moderate",
  "passed": true,
  "flags": [],
  "filtered_content": "...",
  "severity": "low",
  "categories_checked": [
    "profanity",
    "violence",
    "hate_speech",
    "adult_content"
  ]
}
```

**Filter Levels:**
- strict
- moderate (default)
- permissive

---

### 14. ToxicityDetectorTool

**Purpose:** Detect toxic and harmful content

**Input Schema:**
```python
class ToxicityDetectorInput(BaseModel):
    text: str  # Text to analyze (required)
```

**Output Format:**
```json
{
  "toxicity_score": 0.08,
  "categories": {
    "harassment": 0.05,
    "threat": 0.02,
    "insult": 0.08,
    "identity_attack": 0.03,
    "profanity": 0.04
  },
  "is_toxic": false,
  "confidence": 0.94,
  "flagged_segments": []
}
```

**Toxicity Categories:**
- harassment
- threat
- insult
- identity_attack
- profanity

---

### 15. RiskScorerTool

**Purpose:** Score content for safety risks

**Input Schema:**
```python
class RiskScorerInput(BaseModel):
    content: str              # Content to score (required)
    context: str = "general"  # Context (optional, default: general)
```

**Output Format:**
```json
{
  "overall_risk": 0.12,
  "risk_level": "low",
  "risk_categories": {
    "legal_risk": 0.05,
    "reputational_risk": 0.08,
    "user_safety_risk": 0.15,
    "compliance_risk": 0.10
  },
  "context": "general",
  "recommended_action": "approve",
  "mitigation_suggestions": []
}
```

**Risk Contexts:**
- general (default)
- workplace
- education
- public

---

## ✈️ Travel Tools (Travel Concierge - 406)

### 16. TravelAPITool

**Purpose:** Search flights, hotels, and activities

**Input Schema:**
```python
class TravelAPIInput(BaseModel):
    search_type: str    # Type: flights, hotels, activities (required)
    destination: str    # Destination city/location (required)
    start_date: str     # Start date YYYY-MM-DD (required)
    end_date: str       # End date YYYY-MM-DD (required)
```

**Output Format (Flights):**
```json
{
  "flights": [
    {
      "airline": "United Airlines",
      "flight_number": "UA1234",
      "departure": "2025-12-25T10:00:00",
      "arrival": "2025-12-25T14:30:00",
      "price": 450.00,
      "class": "economy"
    }
  ]
}
```

**Output Format (Hotels):**
```json
{
  "hotels": [
    {
      "name": "Grand Hotel",
      "rating": 4.5,
      "price_per_night": 180.00,
      "amenities": ["wifi", "pool", "gym"],
      "location": "Paris, France"
    }
  ]
}
```

**Output Format (Activities):**
```json
{
  "activities": [
    {
      "name": "City Walking Tour",
      "duration": "3 hours",
      "price": 45.00,
      "rating": 4.8
    }
  ]
}
```

**Search Types:**
- flights
- hotels
- activities

---

### 17. BookingTool

**Purpose:** Make travel reservations

**Input Schema:**
```python
class BookingInput(BaseModel):
    booking_type: str     # Type: flight, hotel, activity (required)
    booking_details: str  # JSON string of booking details (required)
```

**Output Format:**
```json
{
  "booking_id": "BKG-12345",
  "type": "flight",
  "status": "confirmed",
  "confirmation_number": "CONF-FLIGHT-12345",
  "timestamp": "2025-12-21T10:30:00",
  "payment_status": "completed"
}
```

**Booking Types:**
- flight
- hotel
- activity

---

### 18. ItineraryBuilderTool

**Purpose:** Create detailed travel itineraries

**Input Schema:**
```python
class ItineraryBuilderInput(BaseModel):
    destination: str                  # Destination (required)
    start_date: str                   # Start date YYYY-MM-DD (required)
    end_date: str                     # End date YYYY-MM-DD (required)
    preferences: str = "balanced"     # Preferences (optional)
```

**Output Format:**
```json
{
  "destination": "Paris, France",
  "dates": "2025-12-25 to 2025-12-30",
  "days": [
    {
      "day": 1,
      "date": "2025-12-25",
      "activities": [
        {
          "time": "09:00",
          "activity": "Hotel check-in"
        },
        {
          "time": "14:00",
          "activity": "City walking tour"
        }
      ]
    }
  ],
  "recommendations": {
    "restaurants": ["Local Bistro"],
    "tips": ["Book attractions in advance"]
  }
}
```

**Preferences:**
- balanced (default)
- adventure
- relaxation
- culture

---

## 🔧 Common Patterns

### Error Handling

All tools should handle errors gracefully:

```python
def _run(self, **kwargs) -> str:
    try:
        # Tool logic here
        result = process_data(kwargs)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({
            "error": str(e),
            "status": "failed"
        })
```

### Input Validation

Pydantic automatically validates inputs:

```python
class ToolInput(BaseModel):
    required_field: str = Field(..., description="This is required")
    optional_field: str = Field(default="default", description="This is optional")
    validated_field: int = Field(..., ge=0, le=100, description="0-100 only")
```

### JSON Output Format

Always return JSON strings:

```python
def _run(self, **kwargs) -> str:
    result = {
        "status": "success",
        "data": process(kwargs)
    }
    return json.dumps(result)
```

---

## 📊 Tool Usage Matrix

| Tool | Input Complexity | Output Format | API Required | Data Processing |
|------|-----------------|---------------|--------------|-----------------|
| PaymentGatewayTool | Medium | JSON | Yes | Payment API |
| TransactionValidatorTool | Low | JSON | No | Validation logic |
| ReceiptGeneratorTool | Low | JSON | Optional | Email service |
| SEOAnalyzerTool | Medium | JSON | Yes | SEO API |
| KeywordResearchTool | Low | JSON | Yes | Keyword API |
| RankingTrackerTool | Medium | JSON | Yes | Ranking API |
| VisionAnalysisTool | Medium | JSON | Yes | Vision API |
| QualityScorerTool | High | JSON | No | Scoring algorithm |
| ContentDetectionTool | Medium | JSON | Yes | Vision API |
| ModelEvaluationTool | High | JSON | Yes | LLM API |
| BenchmarkTool | High | JSON | Yes | Benchmark suite |
| MetricsAggregatorTool | High | JSON | No | Aggregation logic |
| ContentFilterTool | Low | JSON | Optional | Filter rules |
| ToxicityDetectorTool | Medium | JSON | Yes | Toxicity API |
| RiskScorerTool | High | JSON | No | Risk algorithm |
| TravelAPITool | Medium | JSON | Yes | Travel APIs |
| BookingTool | Medium | JSON | Yes | Booking API |
| ItineraryBuilderTool | High | JSON | Optional | Planning logic |

---

## 🎯 Best Practices

### 1. Tool Design
- Keep tools focused on single responsibilities
- Use clear, descriptive names
- Provide comprehensive descriptions
- Include usage examples

### 2. Input Validation
- Use Pydantic models for all inputs
- Provide clear field descriptions
- Set sensible defaults
- Validate ranges and formats

### 3. Output Format
- Always return JSON strings
- Use consistent structure
- Include status indicators
- Provide error details

### 4. Error Handling
- Catch all exceptions
- Return structured error messages
- Log errors appropriately
- Don't expose sensitive data

### 5. Documentation
- Document all fields
- Provide usage examples
- Explain output formats
- List any prerequisites

---

## 🔍 Tool Selection Guide

**Choose the right tool for your needs:**

| Use Case | Recommended Tools |
|----------|------------------|
| Process payments | PaymentGatewayTool + TransactionValidatorTool |
| SEO optimization | SEOAnalyzerTool + KeywordResearchTool |
| Image evaluation | VisionAnalysisTool + QualityScorerTool |
| LLM auditing | ModelEvaluationTool + BenchmarkTool |
| Content safety | ContentFilterTool + ToxicityDetectorTool |
| Travel planning | TravelAPITool + ItineraryBuilderTool |

---

## 📝 Custom Tool Template

Use this template to create new tools:

```python
from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json

class YourToolInput(BaseModel):
    """Input schema for Your Tool"""
    required_param: str = Field(..., description="Description of required parameter")
    optional_param: str = Field(default="default", description="Description of optional parameter")

class YourTool(BaseTool):
    name: str = "Your Tool Name"
    description: str = "Clear description of what your tool does"
    args_schema: Type[BaseModel] = YourToolInput

    def _run(self, required_param: str, optional_param: str = "default") -> str:
        try:
            # Your tool logic here
            result = {
                "status": "success",
                "data": f"Processed {required_param}"
            }
            return json.dumps(result)
        except Exception as e:
            return json.dumps({
                "error": str(e),
                "status": "failed"
            })
```

---

**Document Version:** 1.0
**Last Updated:** December 21, 2025
**Total Tools Documented:** 18
