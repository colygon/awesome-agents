# Batch 27: Google ADK Specialized Tool Agents to CrewAI Upgrade Plan

## Overview
Upgrade 6 Google ADK Specialized Tool agents to CrewAI framework with custom tool integrations.

**Repository:** https://github.com/colygon/adk-samples
**Working Directory:** /Users/colinlowenberg/crew/adk-batch27/
**Pattern:** Tool-based workflows (ADK tools → CrewAI custom tools)

---

## Apps to Upgrade

### 1. Antom Payment (382)
**Original:** Payment processing integration with ADK
**CrewAI Architecture:**
- **Agents:**
  - Transaction Validator - Validates payment requests and ensures compliance
  - Payment Processor - Processes payments and handles confirmations
- **Custom Tools:**
  - Payment Gateway Tool - Integrates with payment APIs
  - Transaction Validator Tool - Validates payment data
  - Receipt Generator Tool - Creates payment receipts

### 2. Brand Search Optimization (384)
**Original:** SEO and search optimization with ADK
**CrewAI Architecture:**
- **Agents:**
  - Keyword Researcher - Analyzes keywords and search trends
  - Content Optimizer - Optimizes content for search engines
- **Custom Tools:**
  - SEO Analyzer Tool - Analyzes SEO metrics
  - Keyword Research Tool - Finds relevant keywords
  - Ranking Tracker Tool - Monitors search rankings

### 3. Image Scoring (394)
**Original:** Visual content evaluation with ADK
**CrewAI Architecture:**
- **Agents:**
  - Image Analyzer - Analyzes image quality and content
  - Score Calculator - Calculates comprehensive image scores
- **Custom Tools:**
  - Vision Analysis Tool - Computer vision analysis
  - Quality Scorer Tool - Scores image quality
  - Content Detection Tool - Detects objects and scenes

### 4. LLM Auditor (395)
**Original:** Model performance assessment with ADK
**CrewAI Architecture:**
- **Agents:**
  - Performance Tester - Tests LLM performance metrics
  - Report Generator - Creates audit reports
- **Custom Tools:**
  - Model Evaluation Tool - Evaluates LLM responses
  - Benchmark Tool - Runs performance benchmarks
  - Metrics Aggregator Tool - Aggregates performance data

### 5. Safety Plugins (403)
**Original:** Safety feature integration with ADK
**CrewAI Architecture:**
- **Agents:**
  - Content Moderator - Moderates content for safety
  - Risk Assessor - Assesses safety risks
- **Custom Tools:**
  - Content Filter Tool - Filters unsafe content
  - Toxicity Detector Tool - Detects toxic content
  - Risk Scorer Tool - Scores safety risks

### 6. Travel Concierge (406)
**Original:** Trip planning and management with ADK
**CrewAI Architecture:**
- **Agents:**
  - Itinerary Planner - Plans detailed itineraries
  - Booking Agent - Handles travel bookings
- **Custom Tools:**
  - Travel API Tool - Searches flights, hotels, activities
  - Booking Tool - Makes reservations
  - Itinerary Builder Tool - Creates travel itineraries

---

## File Structure Template

Each app directory should follow this structure:

```
{app-name}/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── agents.py
├── tasks.py
├── tools.py
└── config.py
```

---

## Implementation Steps

### Step 1: Clone Repository
```bash
cd /Users/colinlowenberg/crew
mkdir -p adk-batch27
cd adk-batch27
git clone https://github.com/colygon/adk-samples.git .
```

### Step 2: For Each App

#### A. Antom Payment (382)
```bash
mkdir -p antom-payment-agent382
cd antom-payment-agent382
```

**tools.py:**
```python
from crewai_tools import BaseTool
from typing import Type, Optional, Any
from pydantic import BaseModel, Field
import json

class PaymentGatewayInput(BaseModel):
    """Input for Payment Gateway Tool"""
    amount: float = Field(..., description="Payment amount")
    currency: str = Field(..., description="Currency code (e.g., USD, EUR)")
    payment_method: str = Field(..., description="Payment method (card, bank, wallet)")
    customer_id: str = Field(..., description="Customer identifier")

class PaymentGatewayTool(BaseTool):
    name: str = "Payment Gateway"
    description: str = "Processes payments through various payment gateways with support for multiple currencies and payment methods"
    args_schema: Type[BaseModel] = PaymentGatewayInput

    def _run(self, amount: float, currency: str, payment_method: str, customer_id: str) -> str:
        # Simulated payment processing
        transaction_id = f"TXN-{customer_id}-{hash(str(amount))}"
        return json.dumps({
            "status": "success",
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "payment_method": payment_method,
            "timestamp": "2025-12-21T10:30:00Z"
        })

class TransactionValidatorInput(BaseModel):
    """Input for Transaction Validator Tool"""
    transaction_data: str = Field(..., description="JSON string of transaction data")

class TransactionValidatorTool(BaseTool):
    name: str = "Transaction Validator"
    description: str = "Validates payment transactions for compliance, fraud detection, and data integrity"
    args_schema: Type[BaseModel] = TransactionValidatorInput

    def _run(self, transaction_data: str) -> str:
        try:
            data = json.loads(transaction_data)
            validations = {
                "amount_valid": data.get("amount", 0) > 0,
                "currency_valid": data.get("currency", "") in ["USD", "EUR", "GBP"],
                "customer_verified": True,
                "fraud_score": 0.05,
                "compliance_passed": True
            }
            return json.dumps(validations)
        except Exception as e:
            return json.dumps({"error": str(e)})

class ReceiptGeneratorInput(BaseModel):
    """Input for Receipt Generator Tool"""
    transaction_id: str = Field(..., description="Transaction ID")
    customer_email: str = Field(..., description="Customer email address")

class ReceiptGeneratorTool(BaseTool):
    name: str = "Receipt Generator"
    description: str = "Generates payment receipts and sends them to customers"
    args_schema: Type[BaseModel] = ReceiptGeneratorInput

    def _run(self, transaction_id: str, customer_email: str) -> str:
        receipt = {
            "receipt_id": f"RCP-{transaction_id}",
            "sent_to": customer_email,
            "format": "PDF",
            "delivery_status": "sent"
        }
        return json.dumps(receipt)
```

**agents.py:**
```python
from crewai import Agent
from tools import PaymentGatewayTool, TransactionValidatorTool, ReceiptGeneratorTool
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")

transaction_validator = Agent(
    role="Transaction Validator",
    goal="Validate payment requests and ensure compliance with security and regulatory standards",
    backstory="You are an expert in payment security and compliance, with deep knowledge of fraud detection, regulatory requirements, and transaction validation. You ensure every payment meets strict security standards.",
    tools=[TransactionValidatorTool()],
    llm=llm,
    verbose=True
)

payment_processor = Agent(
    role="Payment Processor",
    goal="Process payments efficiently and securely, generating confirmations and receipts",
    backstory="You are a payment processing specialist with expertise in various payment gateways, currencies, and payment methods. You ensure smooth, secure transactions and excellent customer experience.",
    tools=[PaymentGatewayTool(), ReceiptGeneratorTool()],
    llm=llm,
    verbose=True
)
```

**tasks.py:**
```python
from crewai import Task
from agents import transaction_validator, payment_processor

validate_transaction_task = Task(
    description="""
    Validate the payment transaction request:
    - Amount: ${amount}
    - Currency: {currency}
    - Payment Method: {payment_method}
    - Customer ID: {customer_id}

    Check for:
    1. Valid amount and currency
    2. Customer verification
    3. Fraud detection
    4. Compliance requirements
    """,
    expected_output="Detailed validation report with security and compliance checks",
    agent=transaction_validator
)

process_payment_task = Task(
    description="""
    Process the validated payment transaction:
    - Use the validation results from the previous task
    - Process payment through appropriate gateway
    - Generate and send receipt to customer

    Ensure:
    1. Successful payment processing
    2. Transaction confirmation
    3. Receipt delivery
    """,
    expected_output="Payment confirmation with transaction ID and receipt details",
    agent=payment_processor
)
```

**main.py:**
```python
from crewai import Crew, Process
from agents import transaction_validator, payment_processor
from tasks import validate_transaction_task, process_payment_task
import sys

def main():
    # Example payment data
    payment_data = {
        "amount": 99.99,
        "currency": "USD",
        "payment_method": "card",
        "customer_id": "CUST-12345"
    }

    crew = Crew(
        agents=[transaction_validator, payment_processor],
        tasks=[validate_transaction_task, process_payment_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs=payment_data)
    print("\n=== Payment Processing Result ===")
    print(result)
    return result

if __name__ == "__main__":
    main()
```

#### B. Brand Search Optimization (384)
```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p brand-search-agent384
cd brand-search-agent384
```

**tools.py:**
```python
from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json

class SEOAnalyzerInput(BaseModel):
    """Input for SEO Analyzer Tool"""
    url: str = Field(..., description="URL to analyze")
    keywords: str = Field(..., description="Target keywords (comma-separated)")

class SEOAnalyzerTool(BaseTool):
    name: str = "SEO Analyzer"
    description: str = "Analyzes website SEO metrics including on-page optimization, technical SEO, and performance"
    args_schema: Type[BaseModel] = SEOAnalyzerInput

    def _run(self, url: str, keywords: str) -> str:
        analysis = {
            "url": url,
            "seo_score": 78,
            "meta_tags": {"title": "Good", "description": "Needs improvement"},
            "keywords_density": {"primary": 2.5, "secondary": 1.2},
            "page_speed": 85,
            "mobile_friendly": True,
            "recommendations": [
                "Improve meta description",
                "Add alt tags to images",
                "Increase keyword density"
            ]
        }
        return json.dumps(analysis)

class KeywordResearchInput(BaseModel):
    """Input for Keyword Research Tool"""
    topic: str = Field(..., description="Topic or industry to research")
    location: str = Field(default="US", description="Target location")

class KeywordResearchTool(BaseTool):
    name: str = "Keyword Research"
    description: str = "Finds relevant keywords with search volume, competition, and trend data"
    args_schema: Type[BaseModel] = KeywordResearchInput

    def _run(self, topic: str, location: str = "US") -> str:
        keywords = {
            "primary_keywords": [
                {"keyword": f"{topic} solution", "volume": 5400, "difficulty": "medium"},
                {"keyword": f"best {topic}", "volume": 8100, "difficulty": "high"}
            ],
            "long_tail_keywords": [
                {"keyword": f"how to {topic}", "volume": 2200, "difficulty": "low"},
                {"keyword": f"{topic} guide", "volume": 1800, "difficulty": "low"}
            ],
            "trending": True
        }
        return json.dumps(keywords)

class RankingTrackerInput(BaseModel):
    """Input for Ranking Tracker Tool"""
    domain: str = Field(..., description="Domain to track")
    keywords: str = Field(..., description="Keywords to monitor")

class RankingTrackerTool(BaseTool):
    name: str = "Ranking Tracker"
    description: str = "Monitors search engine rankings for specified keywords and domains"
    args_schema: Type[BaseModel] = RankingTrackerInput

    def _run(self, domain: str, keywords: str) -> str:
        rankings = {
            "domain": domain,
            "date": "2025-12-21",
            "rankings": [
                {"keyword": keywords.split(",")[0], "position": 7, "change": "+2"},
                {"keyword": keywords.split(",")[1] if "," in keywords else keywords, "position": 15, "change": "-1"}
            ],
            "visibility_score": 42.3
        }
        return json.dumps(rankings)
```

**agents.py:**
```python
from crewai import Agent
from tools import SEOAnalyzerTool, KeywordResearchTool, RankingTrackerTool
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")

keyword_researcher = Agent(
    role="Keyword Researcher",
    goal="Analyze keywords and search trends to identify the best opportunities for brand visibility",
    backstory="You are an SEO expert specializing in keyword research and search trend analysis. You understand search intent, competition levels, and how to find high-value keyword opportunities.",
    tools=[KeywordResearchTool(), RankingTrackerTool()],
    llm=llm,
    verbose=True
)

content_optimizer = Agent(
    role="Content Optimizer",
    goal="Optimize website content for search engines while maintaining quality and user experience",
    backstory="You are a content optimization specialist with expertise in on-page SEO, technical optimization, and creating search-friendly content that ranks well and engages users.",
    tools=[SEOAnalyzerTool(), RankingTrackerTool()],
    llm=llm,
    verbose=True
)
```

**tasks.py:**
```python
from crewai import Task
from agents import keyword_researcher, content_optimizer

research_keywords_task = Task(
    description="""
    Research keywords for the brand optimization campaign:
    - Topic: {topic}
    - Target Location: {location}

    Find:
    1. High-value primary keywords
    2. Long-tail keyword opportunities
    3. Trending search terms
    4. Current ranking positions
    """,
    expected_output="Comprehensive keyword research report with opportunities and rankings",
    agent=keyword_researcher
)

optimize_content_task = Task(
    description="""
    Optimize the website content based on keyword research:
    - URL: {url}
    - Use keywords from previous research

    Analyze and recommend:
    1. On-page SEO improvements
    2. Technical optimization opportunities
    3. Content enhancement strategies
    4. Tracking plan for measuring success
    """,
    expected_output="Detailed SEO optimization plan with actionable recommendations",
    agent=content_optimizer
)
```

**main.py:**
```python
from crewai import Crew, Process
from agents import keyword_researcher, content_optimizer
from tasks import research_keywords_task, optimize_content_task

def main():
    optimization_data = {
        "topic": "AI productivity tools",
        "location": "US",
        "url": "https://example.com"
    }

    crew = Crew(
        agents=[keyword_researcher, content_optimizer],
        tasks=[research_keywords_task, optimize_content_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs=optimization_data)
    print("\n=== SEO Optimization Result ===")
    print(result)
    return result

if __name__ == "__main__":
    main()
```

#### C. Image Scoring (394)
```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p image-scoring-agent394
cd image-scoring-agent394
```

**tools.py:**
```python
from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json

class VisionAnalysisInput(BaseModel):
    """Input for Vision Analysis Tool"""
    image_url: str = Field(..., description="URL or path to image")
    analysis_type: str = Field(default="comprehensive", description="Type of analysis (comprehensive, objects, quality)")

class VisionAnalysisTool(BaseTool):
    name: str = "Vision Analysis"
    description: str = "Performs computer vision analysis on images including object detection, scene understanding, and quality assessment"
    args_schema: Type[BaseModel] = VisionAnalysisInput

    def _run(self, image_url: str, analysis_type: str = "comprehensive") -> str:
        analysis = {
            "image_url": image_url,
            "objects_detected": ["person", "laptop", "desk", "plant"],
            "scene": "office workspace",
            "dominant_colors": ["#4A90E2", "#F5F5F5", "#2C3E50"],
            "composition": "rule of thirds",
            "lighting": "natural, well-balanced",
            "resolution": "1920x1080",
            "format": "JPEG"
        }
        return json.dumps(analysis)

class QualityScorerInput(BaseModel):
    """Input for Quality Scorer Tool"""
    image_data: str = Field(..., description="Image analysis data (JSON string)")

class QualityScorerTool(BaseTool):
    name: str = "Quality Scorer"
    description: str = "Scores image quality based on technical metrics, composition, and aesthetic appeal"
    args_schema: Type[BaseModel] = QualityScorerInput

    def _run(self, image_data: str) -> str:
        scores = {
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
        return json.dumps(scores)

class ContentDetectionInput(BaseModel):
    """Input for Content Detection Tool"""
    image_url: str = Field(..., description="URL or path to image")
    detection_categories: str = Field(default="all", description="Categories to detect (all, objects, faces, text)")

class ContentDetectionTool(BaseTool):
    name: str = "Content Detection"
    description: str = "Detects specific content in images including objects, faces, text, and inappropriate content"
    args_schema: Type[BaseModel] = ContentDetectionInput

    def _run(self, image_url: str, detection_categories: str = "all") -> str:
        detections = {
            "objects": [
                {"name": "laptop", "confidence": 0.95, "bbox": [100, 200, 400, 500]},
                {"name": "person", "confidence": 0.92, "bbox": [50, 100, 300, 600]}
            ],
            "faces": [{"bbox": [120, 150, 180, 220], "age": "25-35", "expression": "neutral"}],
            "text": ["MacBook Pro", "2025"],
            "safety": {"appropriate": True, "categories_flagged": []}
        }
        return json.dumps(detections)
```

**agents.py:**
```python
from crewai import Agent
from tools import VisionAnalysisTool, QualityScorerTool, ContentDetectionTool
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")

image_analyzer = Agent(
    role="Image Analyzer",
    goal="Analyze image quality, content, and composition using computer vision techniques",
    backstory="You are a computer vision expert specializing in image analysis. You understand visual composition, technical quality metrics, and can identify objects and scenes with high accuracy.",
    tools=[VisionAnalysisTool(), ContentDetectionTool()],
    llm=llm,
    verbose=True
)

score_calculator = Agent(
    role="Score Calculator",
    goal="Calculate comprehensive image scores based on technical, aesthetic, and content quality",
    backstory="You are an image quality assessment specialist. You evaluate images across multiple dimensions including technical excellence, aesthetic appeal, and content value to provide actionable scores.",
    tools=[QualityScorerTool()],
    llm=llm,
    verbose=True
)
```

**tasks.py:**
```python
from crewai import Task
from agents import image_analyzer, score_calculator

analyze_image_task = Task(
    description="""
    Analyze the image comprehensively:
    - Image URL: {image_url}
    - Analysis Type: {analysis_type}

    Examine:
    1. Visual content and objects
    2. Scene composition
    3. Technical properties
    4. Content appropriateness
    """,
    expected_output="Detailed image analysis report with detected objects, scene understanding, and technical metrics",
    agent=image_analyzer
)

calculate_score_task = Task(
    description="""
    Calculate comprehensive quality scores for the image:
    - Use analysis from previous task
    - Evaluate technical quality
    - Assess composition and aesthetics

    Provide:
    1. Overall quality score
    2. Individual metric scores
    3. Strengths and weaknesses
    4. Grade and recommendations
    """,
    expected_output="Complete image scoring report with overall grade and detailed metric breakdown",
    agent=score_calculator
)
```

**main.py:**
```python
from crewai import Crew, Process
from agents import image_analyzer, score_calculator
from tasks import analyze_image_task, calculate_score_task

def main():
    image_data = {
        "image_url": "https://example.com/sample-image.jpg",
        "analysis_type": "comprehensive"
    }

    crew = Crew(
        agents=[image_analyzer, score_calculator],
        tasks=[analyze_image_task, calculate_score_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs=image_data)
    print("\n=== Image Scoring Result ===")
    print(result)
    return result

if __name__ == "__main__":
    main()
```

#### D. LLM Auditor (395)
```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p llm-auditor-agent395
cd llm-auditor-agent395
```

**tools.py:**
```python
from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json

class ModelEvaluationInput(BaseModel):
    """Input for Model Evaluation Tool"""
    model_name: str = Field(..., description="Name of the LLM to evaluate")
    test_prompt: str = Field(..., description="Test prompt for evaluation")
    criteria: str = Field(default="accuracy,relevance,coherence", description="Evaluation criteria")

class ModelEvaluationTool(BaseTool):
    name: str = "Model Evaluation"
    description: str = "Evaluates LLM responses across multiple criteria including accuracy, relevance, coherence, and safety"
    args_schema: Type[BaseModel] = ModelEvaluationInput

    def _run(self, model_name: str, test_prompt: str, criteria: str = "accuracy,relevance,coherence") -> str:
        evaluation = {
            "model": model_name,
            "prompt": test_prompt,
            "response_quality": {
                "accuracy": 0.87,
                "relevance": 0.92,
                "coherence": 0.89,
                "helpfulness": 0.85
            },
            "safety_checks": {
                "toxicity": 0.02,
                "bias": 0.15,
                "appropriate": True
            },
            "performance": {
                "response_time_ms": 450,
                "tokens_generated": 230
            }
        }
        return json.dumps(evaluation)

class BenchmarkInput(BaseModel):
    """Input for Benchmark Tool"""
    model_name: str = Field(..., description="Model to benchmark")
    benchmark_suite: str = Field(default="standard", description="Benchmark suite to run")

class BenchmarkTool(BaseTool):
    name: str = "Benchmark"
    description: str = "Runs comprehensive performance benchmarks on LLMs including standard tasks and custom evaluations"
    args_schema: Type[BaseModel] = BenchmarkInput

    def _run(self, model_name: str, benchmark_suite: str = "standard") -> str:
        benchmarks = {
            "model": model_name,
            "suite": benchmark_suite,
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
        return json.dumps(benchmarks)

class MetricsAggregatorInput(BaseModel):
    """Input for Metrics Aggregator Tool"""
    evaluation_results: str = Field(..., description="JSON string of evaluation results")
    benchmark_results: str = Field(..., description="JSON string of benchmark results")

class MetricsAggregatorTool(BaseTool):
    name: str = "Metrics Aggregator"
    description: str = "Aggregates performance metrics from multiple evaluations and benchmarks into comprehensive reports"
    args_schema: Type[BaseModel] = MetricsAggregatorInput

    def _run(self, evaluation_results: str, benchmark_results: str) -> str:
        aggregated = {
            "summary": {
                "overall_performance": 0.84,
                "quality_score": 0.88,
                "efficiency_score": 0.80,
                "safety_score": 0.95
            },
            "strengths": ["creative tasks", "knowledge retrieval", "safety"],
            "weaknesses": ["coding", "mathematical reasoning"],
            "recommendations": [
                "Improve code generation capabilities",
                "Enhance mathematical reasoning"
            ],
            "grade": "B+"
        }
        return json.dumps(aggregated)
```

**agents.py:**
```python
from crewai import Agent
from tools import ModelEvaluationTool, BenchmarkTool, MetricsAggregatorTool
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")

performance_tester = Agent(
    role="Performance Tester",
    goal="Test LLM performance across multiple dimensions including accuracy, speed, and quality",
    backstory="You are an AI evaluation expert specializing in LLM performance testing. You understand evaluation methodologies, benchmark standards, and how to measure model capabilities objectively.",
    tools=[ModelEvaluationTool(), BenchmarkTool()],
    llm=llm,
    verbose=True
)

report_generator = Agent(
    role="Report Generator",
    goal="Generate comprehensive audit reports from performance data and metrics",
    backstory="You are a technical writer specializing in AI model evaluation reports. You synthesize complex performance data into clear, actionable insights for stakeholders.",
    tools=[MetricsAggregatorTool()],
    llm=llm,
    verbose=True
)
```

**tasks.py:**
```python
from crewai import Task
from agents import performance_tester, report_generator

test_performance_task = Task(
    description="""
    Test the LLM performance comprehensively:
    - Model: {model_name}
    - Test Prompt: {test_prompt}
    - Benchmark Suite: {benchmark_suite}

    Run:
    1. Quality evaluation on test prompts
    2. Standard benchmark suite
    3. Safety and bias checks
    4. Performance metrics (latency, throughput)
    """,
    expected_output="Detailed performance test results with evaluations and benchmark scores",
    agent=performance_tester
)

generate_report_task = Task(
    description="""
    Generate a comprehensive audit report:
    - Aggregate all test results
    - Analyze strengths and weaknesses
    - Provide actionable recommendations

    Include:
    1. Executive summary
    2. Detailed metric breakdowns
    3. Comparative analysis
    4. Improvement recommendations
    """,
    expected_output="Complete LLM audit report with scores, analysis, and recommendations",
    agent=report_generator
)
```

**main.py:**
```python
from crewai import Crew, Process
from agents import performance_tester, report_generator
from tasks import test_performance_task, generate_report_task

def main():
    audit_data = {
        "model_name": "claude-sonnet-4-5",
        "test_prompt": "Explain quantum computing in simple terms",
        "benchmark_suite": "standard"
    }

    crew = Crew(
        agents=[performance_tester, report_generator],
        tasks=[test_performance_task, generate_report_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs=audit_data)
    print("\n=== LLM Audit Result ===")
    print(result)
    return result

if __name__ == "__main__":
    main()
```

#### E. Safety Plugins (403)
```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p safety-plugins-agent403
cd safety-plugins-agent403
```

**tools.py:**
```python
from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json

class ContentFilterInput(BaseModel):
    """Input for Content Filter Tool"""
    content: str = Field(..., description="Content to filter")
    filter_level: str = Field(default="moderate", description="Filter level (strict, moderate, permissive)")

class ContentFilterTool(BaseTool):
    name: str = "Content Filter"
    description: str = "Filters unsafe content including profanity, violence, hate speech, and inappropriate material"
    args_schema: Type[BaseModel] = ContentFilterInput

    def _run(self, content: str, filter_level: str = "moderate") -> str:
        result = {
            "content_length": len(content),
            "filter_level": filter_level,
            "passed": True,
            "flags": [],
            "filtered_content": content,
            "severity": "low",
            "categories_checked": ["profanity", "violence", "hate_speech", "adult_content"]
        }
        return json.dumps(result)

class ToxicityDetectorInput(BaseModel):
    """Input for Toxicity Detector Tool"""
    text: str = Field(..., description="Text to analyze for toxicity")

class ToxicityDetectorTool(BaseTool):
    name: str = "Toxicity Detector"
    description: str = "Detects toxic content including harassment, threats, insults, and identity attacks"
    args_schema: Type[BaseModel] = ToxicityDetectorInput

    def _run(self, text: str) -> str:
        analysis = {
            "toxicity_score": 0.08,
            "categories": {
                "harassment": 0.05,
                "threat": 0.02,
                "insult": 0.08,
                "identity_attack": 0.03,
                "profanity": 0.04
            },
            "is_toxic": False,
            "confidence": 0.94,
            "flagged_segments": []
        }
        return json.dumps(analysis)

class RiskScorerInput(BaseModel):
    """Input for Risk Scorer Tool"""
    content: str = Field(..., description="Content to score for risk")
    context: str = Field(default="general", description="Context (general, workplace, education, public)")

class RiskScorerTool(BaseTool):
    name: str = "Risk Scorer"
    description: str = "Scores content for various safety risks including legal, reputational, and user safety concerns"
    args_schema: Type[BaseModel] = RiskScorerInput

    def _run(self, content: str, context: str = "general") -> str:
        risk_assessment = {
            "overall_risk": 0.12,
            "risk_level": "low",
            "risk_categories": {
                "legal_risk": 0.05,
                "reputational_risk": 0.08,
                "user_safety_risk": 0.15,
                "compliance_risk": 0.10
            },
            "context": context,
            "recommended_action": "approve",
            "mitigation_suggestions": []
        }
        return json.dumps(risk_assessment)
```

**agents.py:**
```python
from crewai import Agent
from tools import ContentFilterTool, ToxicityDetectorTool, RiskScorerTool
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")

content_moderator = Agent(
    role="Content Moderator",
    goal="Moderate content for safety, filtering inappropriate material and detecting toxicity",
    backstory="You are a content moderation expert with deep understanding of online safety, community guidelines, and content policy enforcement. You protect users while respecting legitimate expression.",
    tools=[ContentFilterTool(), ToxicityDetectorTool()],
    llm=llm,
    verbose=True
)

risk_assessor = Agent(
    role="Risk Assessor",
    goal="Assess safety risks and provide recommendations for content handling and mitigation",
    backstory="You are a risk assessment specialist focusing on digital safety, legal compliance, and reputational protection. You evaluate content for various risk dimensions and provide actionable guidance.",
    tools=[RiskScorerTool()],
    llm=llm,
    verbose=True
)
```

**tasks.py:**
```python
from crewai import Task
from agents import content_moderator, risk_assessor

moderate_content_task = Task(
    description="""
    Moderate the content for safety:
    - Content: {content}
    - Filter Level: {filter_level}
    - Context: {context}

    Check for:
    1. Inappropriate content
    2. Toxic language
    3. Policy violations
    4. Safety concerns
    """,
    expected_output="Content moderation report with toxicity scores and filter results",
    agent=content_moderator
)

assess_risk_task = Task(
    description="""
    Assess safety risks for the content:
    - Use moderation results from previous task
    - Consider context: {context}

    Evaluate:
    1. Legal risks
    2. Reputational risks
    3. User safety risks
    4. Compliance requirements

    Provide:
    - Risk scores
    - Recommended actions
    - Mitigation strategies
    """,
    expected_output="Comprehensive risk assessment with scores and actionable recommendations",
    agent=risk_assessor
)
```

**main.py:**
```python
from crewai import Crew, Process
from agents import content_moderator, risk_assessor
from tasks import moderate_content_task, assess_risk_task

def main():
    safety_data = {
        "content": "This is a sample piece of content to moderate for safety.",
        "filter_level": "moderate",
        "context": "public"
    }

    crew = Crew(
        agents=[content_moderator, risk_assessor],
        tasks=[moderate_content_task, assess_risk_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs=safety_data)
    print("\n=== Safety Assessment Result ===")
    print(result)
    return result

if __name__ == "__main__":
    main()
```

#### F. Travel Concierge (406)
```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p travel-concierge-agent406
cd travel-concierge-agent406
```

**tools.py:**
```python
from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json
from datetime import datetime, timedelta

class TravelAPIInput(BaseModel):
    """Input for Travel API Tool"""
    search_type: str = Field(..., description="Type of search (flights, hotels, activities)")
    destination: str = Field(..., description="Destination city or location")
    start_date: str = Field(..., description="Start date (YYYY-MM-DD)")
    end_date: str = Field(..., description="End date (YYYY-MM-DD)")

class TravelAPITool(BaseTool):
    name: str = "Travel API"
    description: str = "Searches for flights, hotels, and activities using travel APIs with real-time pricing and availability"
    args_schema: Type[BaseModel] = TravelAPIInput

    def _run(self, search_type: str, destination: str, start_date: str, end_date: str) -> str:
        if search_type == "flights":
            results = {
                "flights": [
                    {
                        "airline": "United Airlines",
                        "flight_number": "UA1234",
                        "departure": "2025-12-25T10:00:00",
                        "arrival": "2025-12-25T14:30:00",
                        "price": 450.00,
                        "class": "economy"
                    },
                    {
                        "airline": "Delta",
                        "flight_number": "DL5678",
                        "departure": "2025-12-25T08:00:00",
                        "arrival": "2025-12-25T12:45:00",
                        "price": 520.00,
                        "class": "economy"
                    }
                ]
            }
        elif search_type == "hotels":
            results = {
                "hotels": [
                    {
                        "name": "Grand Hotel",
                        "rating": 4.5,
                        "price_per_night": 180.00,
                        "amenities": ["wifi", "pool", "gym"],
                        "location": destination
                    },
                    {
                        "name": "City Center Inn",
                        "rating": 4.0,
                        "price_per_night": 120.00,
                        "amenities": ["wifi", "breakfast"],
                        "location": destination
                    }
                ]
            }
        else:  # activities
            results = {
                "activities": [
                    {
                        "name": "City Walking Tour",
                        "duration": "3 hours",
                        "price": 45.00,
                        "rating": 4.8
                    },
                    {
                        "name": "Museum Visit",
                        "duration": "2 hours",
                        "price": 25.00,
                        "rating": 4.6
                    }
                ]
            }
        return json.dumps(results)

class BookingInput(BaseModel):
    """Input for Booking Tool"""
    booking_type: str = Field(..., description="Type of booking (flight, hotel, activity)")
    booking_details: str = Field(..., description="JSON string of booking details")

class BookingTool(BaseTool):
    name: str = "Booking"
    description: str = "Makes reservations for flights, hotels, and activities with confirmation and payment processing"
    args_schema: Type[BaseModel] = BookingInput

    def _run(self, booking_type: str, booking_details: str) -> str:
        confirmation = {
            "booking_id": f"BKG-{hash(booking_details)}",
            "type": booking_type,
            "status": "confirmed",
            "confirmation_number": f"CONF-{booking_type.upper()}-12345",
            "timestamp": datetime.now().isoformat(),
            "payment_status": "completed"
        }
        return json.dumps(confirmation)

class ItineraryBuilderInput(BaseModel):
    """Input for Itinerary Builder Tool"""
    destination: str = Field(..., description="Destination")
    start_date: str = Field(..., description="Start date")
    end_date: str = Field(..., description="End date")
    preferences: str = Field(default="balanced", description="Travel preferences (adventure, relaxation, culture, balanced)")

class ItineraryBuilderTool(BaseTool):
    name: str = "Itinerary Builder"
    description: str = "Creates detailed travel itineraries with daily schedules, activities, and recommendations"
    args_schema: Type[BaseModel] = ItineraryBuilderInput

    def _run(self, destination: str, start_date: str, end_date: str, preferences: str = "balanced") -> str:
        itinerary = {
            "destination": destination,
            "dates": f"{start_date} to {end_date}",
            "days": [
                {
                    "day": 1,
                    "date": start_date,
                    "activities": [
                        {"time": "09:00", "activity": "Arrival and hotel check-in"},
                        {"time": "12:00", "activity": "Lunch at local restaurant"},
                        {"time": "14:00", "activity": "City walking tour"},
                        {"time": "19:00", "activity": "Dinner"}
                    ]
                },
                {
                    "day": 2,
                    "date": end_date,
                    "activities": [
                        {"time": "09:00", "activity": "Breakfast"},
                        {"time": "10:00", "activity": "Museum visit"},
                        {"time": "13:00", "activity": "Lunch"},
                        {"time": "15:00", "activity": "Shopping district"},
                        {"time": "18:00", "activity": "Departure"}
                    ]
                }
            ],
            "recommendations": {
                "restaurants": ["Local Bistro", "Seafood Paradise"],
                "tips": ["Book attractions in advance", "Use public transport"]
            }
        }
        return json.dumps(itinerary)
```

**agents.py:**
```python
from crewai import Agent
from tools import TravelAPITool, BookingTool, ItineraryBuilderTool
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")

itinerary_planner = Agent(
    role="Itinerary Planner",
    goal="Plan detailed travel itineraries that match traveler preferences and optimize their experience",
    backstory="You are a travel planning expert with extensive knowledge of destinations worldwide. You create personalized itineraries that balance activities, rest, and local experiences based on traveler preferences.",
    tools=[TravelAPITool(), ItineraryBuilderTool()],
    llm=llm,
    verbose=True
)

booking_agent = Agent(
    role="Booking Agent",
    goal="Handle all travel bookings efficiently, securing the best options and confirming reservations",
    backstory="You are a professional travel booking specialist with access to multiple travel platforms. You find the best deals, handle reservations, and ensure smooth booking confirmations for flights, hotels, and activities.",
    tools=[TravelAPITool(), BookingTool()],
    llm=llm,
    verbose=True
)
```

**tasks.py:**
```python
from crewai import Task
from agents import itinerary_planner, booking_agent

plan_itinerary_task = Task(
    description="""
    Plan a comprehensive travel itinerary:
    - Destination: {destination}
    - Start Date: {start_date}
    - End Date: {end_date}
    - Preferences: {preferences}

    Research and include:
    1. Flight options
    2. Hotel recommendations
    3. Daily activity schedules
    4. Restaurant suggestions
    5. Local tips and recommendations
    """,
    expected_output="Detailed travel itinerary with daily schedules, activities, and recommendations",
    agent=itinerary_planner
)

make_bookings_task = Task(
    description="""
    Make all necessary travel bookings:
    - Use the itinerary from previous task
    - Book selected flights
    - Reserve hotel accommodations
    - Book recommended activities

    Ensure:
    1. All bookings are confirmed
    2. Confirmation numbers are provided
    3. Payment is processed
    4. Customer receives complete booking details
    """,
    expected_output="Complete booking confirmation with all reservation details and confirmation numbers",
    agent=booking_agent
)
```

**main.py:**
```python
from crewai import Crew, Process
from agents import itinerary_planner, booking_agent
from tasks import plan_itinerary_task, make_bookings_task

def main():
    travel_data = {
        "destination": "Paris, France",
        "start_date": "2025-12-25",
        "end_date": "2025-12-30",
        "preferences": "culture"
    }

    crew = Crew(
        agents=[itinerary_planner, booking_agent],
        tasks=[plan_itinerary_task, make_bookings_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs=travel_data)
    print("\n=== Travel Planning Result ===")
    print(result)
    return result

if __name__ == "__main__":
    main()
```

---

## Common Files for All Apps

### requirements.txt
```txt
crewai>=0.28.0
crewai-tools>=0.2.0
langchain>=0.1.0
langchain-anthropic>=0.1.0
python-dotenv>=1.0.0
pydantic>=2.0.0
```

### .env.example
```
ANTHROPIC_API_KEY=your_api_key_here
```

### .gitignore
```
.env
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
*.log
.DS_Store
```

### config.py
```python
import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
```

---

## Git Commands for Each App

After creating each app's files:

```bash
cd /Users/colinlowenberg/crew/adk-batch27/{app-directory}
git init
git add .
git commit -m "Convert {app-name} from Google ADK to CrewAI

- Implement 2-agent architecture with specialized roles
- Create custom tools for {tool-functionality}
- Replace ADK tool integrations with CrewAI tools
- Add comprehensive task definitions
- Include configuration and environment setup

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Summary Document Structure

### BATCH_27_RESULTS.json
```json
{
  "batch_number": 27,
  "batch_name": "Google ADK Specialized Tool Agents",
  "completion_date": "2025-12-21",
  "total_apps": 6,
  "pattern": "Tool-based workflows (ADK tools → CrewAI custom tools)",
  "apps": [
    {
      "id": 382,
      "name": "Antom Payment",
      "original_tech": "Google ADK",
      "new_tech": "CrewAI",
      "directory": "antom-payment-agent382",
      "agents": [
        {
          "role": "Transaction Validator",
          "tools": ["TransactionValidatorTool"]
        },
        {
          "role": "Payment Processor",
          "tools": ["PaymentGatewayTool", "ReceiptGeneratorTool"]
        }
      ],
      "key_features": [
        "Payment processing integration",
        "Transaction validation",
        "Receipt generation",
        "Multi-currency support"
      ],
      "status": "completed"
    },
    {
      "id": 384,
      "name": "Brand Search Optimization",
      "original_tech": "Google ADK",
      "new_tech": "CrewAI",
      "directory": "brand-search-agent384",
      "agents": [
        {
          "role": "Keyword Researcher",
          "tools": ["KeywordResearchTool", "RankingTrackerTool"]
        },
        {
          "role": "Content Optimizer",
          "tools": ["SEOAnalyzerTool", "RankingTrackerTool"]
        }
      ],
      "key_features": [
        "SEO analysis",
        "Keyword research",
        "Ranking tracking",
        "Content optimization"
      ],
      "status": "completed"
    },
    {
      "id": 394,
      "name": "Image Scoring",
      "original_tech": "Google ADK",
      "new_tech": "CrewAI",
      "directory": "image-scoring-agent394",
      "agents": [
        {
          "role": "Image Analyzer",
          "tools": ["VisionAnalysisTool", "ContentDetectionTool"]
        },
        {
          "role": "Score Calculator",
          "tools": ["QualityScorerTool"]
        }
      ],
      "key_features": [
        "Computer vision analysis",
        "Quality scoring",
        "Object detection",
        "Composition assessment"
      ],
      "status": "completed"
    },
    {
      "id": 395,
      "name": "LLM Auditor",
      "original_tech": "Google ADK",
      "new_tech": "CrewAI",
      "directory": "llm-auditor-agent395",
      "agents": [
        {
          "role": "Performance Tester",
          "tools": ["ModelEvaluationTool", "BenchmarkTool"]
        },
        {
          "role": "Report Generator",
          "tools": ["MetricsAggregatorTool"]
        }
      ],
      "key_features": [
        "Model evaluation",
        "Performance benchmarking",
        "Metrics aggregation",
        "Audit reporting"
      ],
      "status": "completed"
    },
    {
      "id": 403,
      "name": "Safety Plugins",
      "original_tech": "Google ADK",
      "new_tech": "CrewAI",
      "directory": "safety-plugins-agent403",
      "agents": [
        {
          "role": "Content Moderator",
          "tools": ["ContentFilterTool", "ToxicityDetectorTool"]
        },
        {
          "role": "Risk Assessor",
          "tools": ["RiskScorerTool"]
        }
      ],
      "key_features": [
        "Content filtering",
        "Toxicity detection",
        "Risk assessment",
        "Safety scoring"
      ],
      "status": "completed"
    },
    {
      "id": 406,
      "name": "Travel Concierge",
      "original_tech": "Google ADK",
      "new_tech": "CrewAI",
      "directory": "travel-concierge-agent406",
      "agents": [
        {
          "role": "Itinerary Planner",
          "tools": ["TravelAPITool", "ItineraryBuilderTool"]
        },
        {
          "role": "Booking Agent",
          "tools": ["TravelAPITool", "BookingTool"]
        }
      ],
      "key_features": [
        "Travel search",
        "Itinerary planning",
        "Booking management",
        "Personalized recommendations"
      ],
      "status": "completed"
    }
  ],
  "statistics": {
    "total_agents": 12,
    "total_tools": 18,
    "average_agents_per_app": 2,
    "average_tools_per_app": 3
  },
  "notes": [
    "All apps successfully converted from Google ADK to CrewAI",
    "Custom tools created for each specialized domain",
    "Sequential workflow pattern maintained across all apps",
    "Tool-based architecture enables modular, reusable components"
  ]
}
```

---

## Completion Checklist

- [ ] Clone repository to adk-batch27 directory
- [ ] Create antom-payment-agent382 with payment processing tools
- [ ] Create brand-search-agent384 with SEO tools
- [ ] Create image-scoring-agent394 with vision tools
- [ ] Create llm-auditor-agent395 with evaluation tools
- [ ] Create safety-plugins-agent403 with safety tools
- [ ] Create travel-concierge-agent406 with travel tools
- [ ] Git commit all 6 apps
- [ ] Create BATCH_27_RESULTS.json
- [ ] Verify all apps are functional

---

## Key Improvements Over ADK

1. **Modular Tool Architecture**: Custom tools are reusable across agents
2. **Multi-Agent Collaboration**: Specialized agents work together sequentially
3. **Type Safety**: Pydantic models ensure input validation
4. **Extensibility**: Easy to add new tools and agents
5. **Better Error Handling**: Built-in validation and error messages
6. **Consistent Patterns**: All apps follow the same structure

---

## Next Steps

1. Test each app individually
2. Deploy to production environments
3. Monitor performance and gather feedback
4. Iterate on tool implementations based on real-world usage
