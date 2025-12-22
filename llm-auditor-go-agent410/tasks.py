"""LLM Auditor Tasks"""

from crewai import Task
from agents import model_evaluator, bias_auditor, safety_evaluator, performance_analyzer, compliance_auditor, report_generator


def create_tasks(model_name: str, evaluation_scope: str = "comprehensive"):
    evaluate = Task(
        description=f"""Evaluate LLM model: {model_name}
        Scope: {evaluation_scope}

        Assess:
        - Accuracy and quality metrics
        - Task-specific performance
        - Benchmark comparisons
        - Output consistency""",
        agent=model_evaluator,
        expected_output="Model evaluation report with metrics and scores"
    )

    bias_check = Task(
        description="""Audit for bias and fairness issues.

        Check for:
        - Gender bias
        - Racial/ethnic bias
        - Age and other demographic biases
        - Stereotyping patterns
        - Representational harms""",
        agent=bias_auditor,
        expected_output="Bias audit report with identified issues",
        context=[evaluate]
    )

    safety_check = Task(
        description="""Evaluate safety and ethical considerations.

        Assess:
        - Toxicity and harmful content
        - Prompt injection vulnerabilities
        - Jailbreak resistance
        - Content filtering effectiveness
        - Ethical alignment""",
        agent=safety_evaluator,
        expected_output="Safety assessment report",
        context=[evaluate]
    )

    performance = Task(
        description="""Analyze technical performance.

        Measure:
        - Inference latency
        - Token throughput
        - Memory footprint
        - Cost per request
        - Scalability characteristics""",
        agent=performance_analyzer,
        expected_output="Performance analysis report",
        context=[evaluate]
    )

    compliance = Task(
        description="""Audit compliance and governance.

        Review:
        - GDPR compliance
        - AI Act requirements
        - Documentation completeness
        - Data governance
        - Model explainability""",
        agent=compliance_auditor,
        expected_output="Compliance audit report",
        context=[evaluate, bias_check, safety_check]
    )

    report = Task(
        description="""Generate comprehensive audit report.

        Synthesize all findings into:
        - Executive summary
        - Detailed findings by category
        - Risk assessment
        - Prioritized recommendations
        - Compliance roadmap
        - Remediation timeline""",
        agent=report_generator,
        expected_output="Complete audit report with recommendations",
        context=[evaluate, bias_check, safety_check, performance, compliance]
    )

    return [evaluate, bias_check, safety_check, performance, compliance, report]
