"""
Custom Tools for Project Management
Provides project planning, task breakdown, and risk analysis capabilities
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class ProjectPlanInput(BaseModel):
    """Input schema for ProjectPlannerTool"""
    project_details: str = Field(..., description="Project details and requirements")


class ProjectPlannerTool(BaseTool):
    name: str = "Project Planner Tool"
    description: str = """Creates comprehensive project plans including scope, objectives,
    stakeholders, and methodology recommendations. Returns structured project charter."""
    args_schema: Type[BaseModel] = ProjectPlanInput

    def _run(self, project_details: str) -> str:
        """
        Create project plan from requirements

        Args:
            project_details: Project information

        Returns:
            Comprehensive project plan
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

            prompt = f"""Create a comprehensive project plan based on these details:

{project_details}

Provide:

1. PROJECT CHARTER:
   - Project name and brief description
   - Business justification (why this project?)
   - SMART objectives (Specific, Measurable, Achievable, Relevant, Time-bound)
   - Success criteria (how to measure success)
   - High-level requirements

2. SCOPE DEFINITION:
   - In-scope: What will be delivered
   - Out-of-scope: What will NOT be included
   - Acceptance criteria
   - Assumptions
   - Constraints

3. STAKEHOLDER ANALYSIS:
   - Identify key stakeholders (roles)
   - Stakeholder interests
   - Influence level (High/Medium/Low)
   - Engagement strategy

4. METHODOLOGY RECOMMENDATION:
   - Recommend Agile, Waterfall, or Hybrid
   - Justify the choice
   - Suggest iteration/sprint structure if Agile
   - Recommend ceremonies (standups, reviews, etc.)

5. HIGH-LEVEL PHASES:
   - Identify 4-6 major phases
   - Phase objectives
   - Key deliverables per phase
   - Estimated duration

Make recommendations specific and actionable."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error creating project plan: {str(e)}"


class TaskBreakdownInput(BaseModel):
    """Input schema for TaskBreakdownTool"""
    project_plan: str = Field(..., description="Project plan to break down into tasks")
    complexity: str = Field(default="medium", description="Project complexity: low, medium, or high")


class TaskBreakdownTool(BaseTool):
    name: str = "Task Breakdown Tool"
    description: str = """Creates Work Breakdown Structure (WBS) with detailed tasks,
    dependencies, and estimates. Returns hierarchical task structure."""
    args_schema: Type[BaseModel] = TaskBreakdownInput

    def _run(self, project_plan: str, complexity: str = "medium") -> str:
        """
        Break down project into detailed tasks

        Args:
            project_plan: Project plan information
            complexity: Project complexity level

        Returns:
            Work Breakdown Structure
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)

            # Adjust number of tasks based on complexity
            task_count = {"low": 30, "medium": 60, "high": 100}.get(complexity, 60)

            prompt = f"""Create a detailed Work Breakdown Structure (WBS) for this project:

{project_plan}

Project complexity: {complexity}

Create approximately {task_count} tasks organized hierarchically:

STRUCTURE:
Level 1: Major Deliverables/Phases (5-8)
Level 2: Components (15-25)
Level 3: Detailed Tasks (30-70)
Level 4: Sub-tasks if needed

FOR EACH TASK:
- Task ID (e.g., 1.1.1)
- Task Name (clear, action-oriented)
- Description (specific what needs to be done)
- Estimated Effort (hours or days)
- Required Skills (e.g., Frontend Dev, UX Designer, DevOps)
- Dependencies (Task IDs this depends on)
- Priority (Critical/High/Medium/Low)
- Deliverable/Output

TASK CATEGORIES:
- Planning & Setup (5-10%)
- Design & Architecture (10-15%)
- Development/Implementation (50-60%)
- Testing & QA (15-20%)
- Documentation (5-10%)
- Deployment & Launch (5-10%)

CRITICAL PATH:
- Identify tasks on critical path
- Note parallel work opportunities
- Flag potential bottlenecks

Make tasks:
- Specific and actionable
- Right-sized (1-5 days each)
- Measurable (clear done criteria)"""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error creating task breakdown: {str(e)}"


class RiskAnalysisInput(BaseModel):
    """Input schema for RiskAnalysisTool"""
    project_info: str = Field(..., description="Project information for risk analysis")


class RiskAnalysisTool(BaseTool):
    name: str = "Risk Analysis Tool"
    description: str = """Identifies and assesses project risks. Provides mitigation
    strategies and risk register. Returns comprehensive risk analysis."""
    args_schema: Type[BaseModel] = RiskAnalysisInput

    def _run(self, project_info: str) -> str:
        """
        Conduct risk analysis for project

        Args:
            project_info: Project details

        Returns:
            Risk analysis and mitigation strategies
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

            prompt = f"""Conduct comprehensive risk analysis for this project:

{project_info}

Identify 25-30 potential risks across categories:

RISK CATEGORIES:
1. Technical Risks (8-10):
   - Technology choices
   - Integration challenges
   - Performance/scalability
   - Technical debt
   - Security vulnerabilities

2. Resource Risks (5-7):
   - Team availability
   - Skill gaps
   - Key person dependencies
   - Contractor/vendor risks
   - Budget constraints

3. Schedule Risks (5-7):
   - Estimation errors
   - Dependency delays
   - Scope creep
   - Approval delays
   - Testing bottlenecks

4. External Risks (4-6):
   - Vendor dependencies
   - Regulatory changes
   - Market conditions
   - Third-party integrations
   - Customer availability

5. Quality Risks (3-5):
   - Defect rates
   - Performance issues
   - User acceptance
   - Compatibility problems

FOR EACH RISK:
- Risk ID and Name
- Category
- Description (what could go wrong)
- Probability (Low=1/Medium=2/High=3)
- Impact (Low=1/Medium=2/High=3)
- Risk Score (Probability × Impact)
- Timing (when it might occur)

RISK PRIORITIZATION:
- Critical (Score 6-9): Immediate mitigation needed
- Important (Score 3-6): Develop mitigation plan
- Monitor (Score 1-3): Watch for triggers

MITIGATION STRATEGIES:
For top 15 risks provide:
- Prevention actions (reduce probability)
- Mitigation actions (reduce impact)
- Contingency plan (if risk materializes)
- Owner (who manages this risk)
- Cost/time for mitigation

RISK MONITORING:
- Key risk indicators
- Monitoring frequency
- Escalation triggers"""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error analyzing risks: {str(e)}"
