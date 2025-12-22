"""
LLM Auditor Go - CrewAI Implementation
Original: Go ADK, Migrated to Python CrewAI
"""

from crewai import Agent
from tools import ModelEvaluationTool, BiasDetectionTool, PerformanceAnalysisTool

# Model Evaluator Agent
model_evaluator = Agent(
    role="LLM Model Evaluation Specialist",
    goal="Evaluate LLM model performance across various metrics and benchmarks",
    backstory="""You are an expert in evaluating language models. You understand
    metrics like perplexity, BLEU, ROUGE, accuracy, F1 score, and human evaluation
    criteria. You can assess models across different tasks and domains.""",
    verbose=True,
    allow_delegation=False,
    tools=[ModelEvaluationTool(), PerformanceAnalysisTool()]
)

# Bias Auditor Agent
bias_auditor = Agent(
    role="AI Bias and Fairness Auditor",
    goal="Detect and analyze bias in LLM outputs and training data",
    backstory="""You are a specialist in AI fairness and bias detection. You identify
    biases related to gender, race, age, religion, and other protected characteristics.
    You understand representational and allocational harms in AI systems.""",
    verbose=True,
    allow_delegation=False,
    tools=[BiasDetectionTool()]
)

# Safety Evaluator Agent
safety_evaluator = Agent(
    role="AI Safety and Ethics Evaluator",
    goal="Assess LLM safety, toxicity, and ethical considerations",
    backstory="""You evaluate AI systems for safety concerns including toxicity,
    harmful content generation, prompt injection vulnerabilities, and ethical
    implications. You ensure models meet safety standards.""",
    verbose=True,
    allow_delegation=False
)

# Performance Analyzer Agent
performance_analyzer = Agent(
    role="LLM Performance Analyst",
    goal="Analyze model performance, latency, throughput, and resource usage",
    backstory="""You analyze technical performance metrics including inference speed,
    token throughput, memory usage, and cost efficiency. You identify bottlenecks
    and optimization opportunities.""",
    verbose=True,
    allow_delegation=False,
    tools=[PerformanceAnalysisTool()]
)

# Compliance Auditor Agent
compliance_auditor = Agent(
    role="AI Compliance and Governance Specialist",
    goal="Ensure LLM compliance with regulations and best practices",
    backstory="""You ensure AI systems comply with regulations like GDPR, AI Act,
    and industry standards. You audit documentation, data handling, and model
    governance practices.""",
    verbose=True,
    allow_delegation=False
)

# Report Generator Agent
report_generator = Agent(
    role="AI Audit Report Specialist",
    goal="Create comprehensive audit reports with findings and recommendations",
    backstory="""You synthesize technical audit findings into clear, actionable
    reports for technical and non-technical stakeholders. You provide prioritized
    recommendations and compliance roadmaps.""",
    verbose=True,
    allow_delegation=True
)
