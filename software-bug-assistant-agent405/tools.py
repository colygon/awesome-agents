"""
Custom Tools for Software Bug Assistant
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import re


class BugDetectionInput(BaseModel):
    error_message: str = Field(..., description="Error message or bug description")


class BugDetectionTool(BaseTool):
    name: str = "Bug Detection Tool"
    description: str = "Analyzes error messages and symptoms to identify bug types and patterns"
    args_schema: Type[BaseModel] = BugDetectionInput

    def _run(self, error_message: str) -> str:
        bug_patterns = {
            'NullPointerException': 'Null Reference Error',
            'IndexError': 'Array Index Out of Bounds',
            'KeyError': 'Missing Dictionary Key',
            'TypeError': 'Type Mismatch Error',
            'ValueError': 'Invalid Value Error',
            'AttributeError': 'Missing Attribute/Method',
            'ConnectionError': 'Network/API Connection Issue',
            'TimeoutError': 'Operation Timeout',
            'MemoryError': 'Memory Overflow',
            'RecursionError': 'Stack Overflow'
        }

        detected = []
        for pattern, bug_type in bug_patterns.items():
            if pattern.lower() in error_message.lower():
                detected.append(bug_type)

        return f"Detected bug patterns: {', '.join(detected) if detected else 'Generic error - needs analysis'}"


class CodeAnalysisInput(BaseModel):
    code: str = Field(..., description="Code to analyze")


class CodeAnalysisTool(BaseTool):
    name: str = "Code Analysis Tool"
    description: str = "Analyzes code for potential issues, patterns, and quality"
    args_schema: Type[BaseModel] = CodeAnalysisInput

    def _run(self, code: str) -> str:
        issues = []
        if 'TODO' in code or 'FIXME' in code:
            issues.append("Contains TODO/FIXME markers")
        if code.count('try:') > code.count('except'):
            issues.append("Incomplete exception handling")
        if 'print(' in code and 'logging' not in code:
            issues.append("Using print statements instead of logging")

        return f"Code analysis results: {'; '.join(issues) if issues else 'No obvious issues detected'}"


class TestGeneratorInput(BaseModel):
    function_name: str = Field(..., description="Function to test")


class TestGeneratorTool(BaseTool):
    name: str = "Test Generator Tool"
    description: str = "Generates test case templates"
    args_schema: Type[BaseModel] = TestGeneratorInput

    def _run(self, function_name: str) -> str:
        template = f"""
def test_{function_name}_normal_case():
    # Test normal operation
    pass

def test_{function_name}_edge_cases():
    # Test boundary conditions
    pass

def test_{function_name}_error_handling():
    # Test error scenarios
    pass
"""
        return template


class DocumentationInput(BaseModel):
    content: str = Field(..., description="Content to document")


class DocumentationTool(BaseTool):
    name: str = "Documentation Tool"
    description: str = "Formats and structures documentation"
    args_schema: Type[BaseModel] = DocumentationInput

    def _run(self, content: str) -> str:
        return f"""# Bug Resolution Documentation

## Summary
{content}

## Next Steps
- Review proposed changes
- Run test suite
- Deploy fix
- Monitor for regressions
"""
