#!/usr/bin/env python
from crewai import Crew, Process
from agents import LLMAuditorAgents
from tasks import LLMAuditorTasks
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def audit_llm(model_name: str = "gpt-3.5-turbo", audit_scope: str = "comprehensive"):
    """
    Conduct a comprehensive audit of a language model.

    Args:
        model_name: Name of the model to audit (e.g., 'gpt-3.5-turbo', 'gpt-4')
        audit_scope: Scope of audit ('comprehensive', 'safety', 'bias', 'performance')
    """
    print(f"\n{'='*60}")
    print(f"LLM Audit Starting")
    print(f"Model: {model_name}")
    print(f"Scope: {audit_scope}")
    print(f"{'='*60}\n")

    # Initialize agents and tasks
    agents = LLMAuditorAgents()
    tasks = LLMAuditorTasks()

    # Create agents
    prompt_engineer = agents.prompt_engineer()
    response_evaluator = agents.response_evaluator()
    bias_detector = agents.bias_detector()
    security_auditor = agents.security_auditor()
    audit_coordinator = agents.audit_coordinator()

    # Create tasks
    test_design_task = tasks.design_test_suite(
        agent=prompt_engineer,
        model_name=model_name,
        audit_scope=audit_scope
    )

    test_execution_task = tasks.execute_tests(
        agent=response_evaluator,
        test_suite="Execute comprehensive test suite",
        model_name=model_name
    )

    evaluation_task = tasks.evaluate_responses(
        agent=response_evaluator,
        test_results="Evaluate all test responses"
    )

    bias_detection_task = tasks.detect_biases(
        agent=bias_detector,
        test_results="Analyze responses for bias"
    )

    security_task = tasks.assess_security(
        agent=security_auditor,
        test_results="Assess security vulnerabilities"
    )

    report_task = tasks.compile_audit_report(
        agent=audit_coordinator,
        model_name=model_name,
        evaluation="Compile evaluation results",
        bias_analysis="Include bias analysis",
        security_assessment="Include security assessment"
    )

    # Create crew
    crew = Crew(
        agents=[
            prompt_engineer,
            response_evaluator,
            bias_detector,
            security_auditor,
            audit_coordinator
        ],
        tasks=[
            test_design_task,
            test_execution_task,
            evaluation_task,
            bias_detection_task,
            security_task,
            report_task
        ],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print(f"\n{'='*60}")
    print("LLM Audit Complete!")
    print(f"{'='*60}\n")
    print(result)

    # Save report
    output_file = f"llm_audit_{model_name.replace('/', '_')}_{audit_scope}.txt"
    with open(output_file, 'w') as f:
        f.write(str(result))
    print(f"\nAudit report saved to: {output_file}")

    return result

def compare_models(models: list, audit_scope: str = "comprehensive"):
    """
    Compare multiple language models through auditing.
    """
    results = {}
    for model in models:
        print(f"\n{'='*60}")
        print(f"Auditing model: {model}")
        print(f"{'='*60}\n")
        results[model] = audit_llm(model, audit_scope)

    # Generate comparison report
    print(f"\n{'='*60}")
    print("Model Comparison Summary")
    print(f"{'='*60}\n")
    for model, result in results.items():
        print(f"\nModel: {model}")
        print(f"Result: {result[:200]}...")  # Print first 200 chars

    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single model: python main.py <model_name> [audit_scope]")
        print("  Compare:      python main.py --compare model1,model2,model3 [audit_scope]")
        print("\nAudit scope options: comprehensive, safety, bias, performance")
        print("\nExamples:")
        print("  python main.py gpt-3.5-turbo comprehensive")
        print("  python main.py --compare gpt-3.5-turbo,gpt-4 safety")
        sys.exit(1)

    if sys.argv[1] == "--compare":
        if len(sys.argv) < 3:
            print("Error: Model list required for comparison")
            sys.exit(1)
        models = sys.argv[2].split(',')
        audit_scope = sys.argv[3] if len(sys.argv) > 3 else "comprehensive"
        compare_models(models, audit_scope)
    else:
        model_name = sys.argv[1]
        audit_scope = sys.argv[2] if len(sys.argv) > 2 else "comprehensive"
        audit_llm(model_name, audit_scope)
