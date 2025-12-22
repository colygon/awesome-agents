# LLM Auditor Agent - CrewAI Implementation

A comprehensive AI auditing system powered by CrewAI that evaluates language models for performance, safety, bias, and security vulnerabilities.

## Overview

This CrewAI implementation provides systematic auditing of language models using specialized agents that test accuracy, detect biases, assess security, and generate comprehensive audit reports.

## Agents

1. **Prompt Engineering Specialist**: Designs comprehensive test prompts across multiple categories
2. **LLM Response Evaluator**: Evaluates responses for accuracy, quality, and helpfulness
3. **Bias Detection Specialist**: Identifies biases and fairness issues in outputs
4. **AI Security Auditor**: Assesses security risks and vulnerabilities
5. **LLM Audit Coordinator**: Compiles comprehensive audit reports and recommendations

## Features

- Multi-dimensional LLM evaluation
- Automated test suite generation
- Factual accuracy testing
- Bias and fairness analysis
- Security vulnerability assessment
- Safety guardrail testing
- Robustness evaluation (prompt injection, adversarial inputs)
- Comprehensive audit reporting
- Model comparison capabilities

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
- OpenAI API key (to audit OpenAI models)
- Optional: Google API key (to audit Gemini), Anthropic key (to audit Claude)

## Usage

### Audit a Single Model

```bash
python main.py gpt-3.5-turbo comprehensive
```

### Audit with Specific Scope

```bash
python main.py gpt-4 safety
python main.py gpt-3.5-turbo bias
python main.py gpt-4 performance
```

### Compare Multiple Models

```bash
python main.py --compare gpt-3.5-turbo,gpt-4 comprehensive
```

### Programmatic Usage

```python
from main import audit_llm

result = audit_llm('gpt-3.5-turbo', 'comprehensive')
print(result)
```

## Audit Scopes

- **comprehensive**: Full audit covering all dimensions
- **safety**: Focus on safety and harmful content
- **bias**: Focus on bias and fairness issues
- **performance**: Focus on accuracy and quality

## Test Categories

### 1. Factual Accuracy
- General knowledge questions
- Domain-specific queries
- Common misconceptions
- Temporal reasoning

### 2. Reasoning & Logic
- Mathematical reasoning
- Logical puzzles
- Causal reasoning
- Problem-solving

### 3. Safety & Ethics
- Harmful content requests
- Safety guardrail testing
- Privacy handling
- Ethical scenarios

### 4. Bias & Fairness
- Demographic bias tests
- Stereotyping detection
- Cultural bias assessment
- Representation analysis

### 5. Security & Robustness
- Prompt injection attempts
- Jailbreaking tests
- Adversarial inputs
- Consistency checks

## Output

The system generates a comprehensive audit report including:

### Executive Summary
- Overall assessment score
- Key findings
- Critical issues
- Risk rating

### Performance Evaluation
- Accuracy scores by category
- Strengths and weaknesses
- Response quality metrics
- Comparison to benchmarks

### Bias & Fairness Assessment
- Identified biases with examples
- Fairness metrics
- Representation issues
- Demographic analysis

### Security & Safety Analysis
- Vulnerability assessment
- Safety guardrail effectiveness
- Prompt injection resistance
- Risk severity ratings

### Recommendations
- Improvement suggestions
- Deployment considerations
- Mitigation strategies
- Best practices

## Customization

Modify these files to customize behavior:
- `agents.py`: Adjust agent roles and evaluation criteria
- `tasks.py`: Modify audit workflow and test categories
- `tools.py`: Add custom tests or integrate additional APIs
- `main.py`: Change audit orchestration or comparison logic

## Example Use Cases

- Pre-deployment model validation
- Responsible AI compliance
- Model performance benchmarking
- Security risk assessment
- Bias auditing for fairness
- Comparing model versions
- Regulatory compliance testing
- Third-party model evaluation

## Advanced Features

### Custom Test Suites

Add custom test categories in `tools.py`:

```python
custom_tests = {
    'domain_specific': [
        "Your custom test prompts here"
    ]
}
```

### Integration with Other Models

Extend `tools.py` to support additional model providers:

```python
# Add support for Anthropic Claude
from anthropic import Anthropic

# Add support for Google Gemini
import google.generativeai as genai
```

### Automated Reporting

Configure automatic report generation and storage:

```python
OUTPUT_DIRECTORY=./audit_results
SAVE_RESULTS=true
```

## Metrics & Scoring

All evaluations use 0-100 scoring with the following grades:
- 90-100: A (Excellent)
- 80-89: B (Good)
- 70-79: C (Acceptable)
- 60-69: D (Needs Improvement)
- Below 60: F (Failing)

## Notes

- Requires API access to models being audited
- Test execution time varies by model and scope
- Results saved to timestamped files
- Comparison mode generates comparative analysis
- Extensible framework for custom evaluations
- Supports batch testing for efficiency
