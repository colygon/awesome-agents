"""Custom Tools for Java Bug Assistant"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class JavaBugDetectionInput(BaseModel):
    error: str = Field(..., description="Java error or exception")


class JavaBugDetectionTool(BaseTool):
    name: str = "Java Bug Detection Tool"
    description: str = "Detects common Java exceptions and issues"
    args_schema: Type[BaseModel] = JavaBugDetectionInput

    def _run(self, error: str) -> str:
        java_patterns = {
            'NullPointerException': 'Null reference in Java',
            'ConcurrentModificationException': 'Collection modified during iteration',
            'OutOfMemoryError': 'JVM heap exhausted',
            'ClassCastException': 'Invalid type cast',
            'IllegalArgumentException': 'Invalid method argument',
            'SQLException': 'Database operation failed'
        }
        detected = [v for k, v in java_patterns.items() if k in error]
        return f"Java issues detected: {', '.join(detected) if detected else 'Unknown'}"


class JavaCodeAnalysisInput(BaseModel):
    code: str = Field(..., description="Java code to analyze")


class JavaCodeAnalysisTool(BaseTool):
    name: str = "Java Code Analysis Tool"
    description: str = "Analyzes Java code for quality and patterns"
    args_schema: Type[BaseModel] = JavaCodeAnalysisInput

    def _run(self, code: str) -> str:
        issues = []
        if 'System.out.println' in code:
            issues.append("Use logging framework instead of System.out")
        if 'catch (Exception e)' in code:
            issues.append("Catching generic Exception - be more specific")
        return f"Java analysis: {'; '.join(issues) if issues else 'Code looks good'}"


class JavaTestGeneratorInput(BaseModel):
    method: str = Field(..., description="Java method to test")


class JavaTestGeneratorTool(BaseTool):
    name: str = "Java Test Generator Tool"
    description: str = "Generates JUnit 5 test templates"
    args_schema: Type[BaseModel] = JavaTestGeneratorInput

    def _run(self, method: str) -> str:
        return f"""
@Test
void test{method}() {{
    // Arrange
    // Act
    // Assert
    assertNotNull(result);
}}
"""
