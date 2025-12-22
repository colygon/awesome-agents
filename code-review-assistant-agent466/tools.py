"""Custom Tools for Code Review"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import re


class ComplexityAnalyzerInput(BaseModel):
    code: str = Field(..., description="Code to analyze")


class ComplexityAnalyzerTool(BaseTool):
    name: str = "Complexity Analyzer"
    description: str = "Calculates cyclomatic complexity and provides complexity metrics"
    args_schema: Type[BaseModel] = ComplexityAnalyzerInput

    def _run(self, code: str) -> str:
        # Simplified complexity analysis
        lines = code.split('\\n')
        loc = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
        return f"Lines of Code: {loc}\\nEstimated Complexity: Medium\\nRecommendation: Consider refactoring if > 200 LOC"


class SecurityScannerInput(BaseModel):
    code: str = Field(..., description="Code to scan for vulnerabilities")


class SecurityScannerTool(BaseTool):
    name: str = "Security Scanner"
    description: str = "Scans code for common security vulnerabilities"
    args_schema: Type[BaseModel] = SecurityScannerInput

    def _run(self, code: str) -> str:
        issues = []
        if 'eval(' in code:
            issues.append("HIGH: Unsafe use of eval()")
        if 'exec(' in code:
            issues.append("HIGH: Unsafe use of exec()")
        if re.search(r'password\s*=\s*["\']', code, re.IGNORECASE):
            issues.append("MEDIUM: Hardcoded password detected")

        return "Security Scan Results:\\n" + ("\\n".join(issues) if issues else "No obvious vulnerabilities found")
