"""
Safety Plugins Agent CrewAI Tasks
Defines the workflow for comprehensive safety analysis
"""

from crewai import Task
from agents import (
    content_moderator,
    toxicity_analyzer,
    sensitive_info_guardian,
    bias_detector,
    safety_coordinator
)


def create_tasks(content: str, context: dict = None):
    """
    Create tasks for safety analysis workflow

    Args:
        content: The content to analyze
        context: Additional context about the content (source, author, etc.)

    Returns:
        List of Task objects
    """

    if context is None:
        context = {}

    context_str = f"\nContext: {context}" if context else ""

    # Task 1: Toxicity Detection
    toxicity_task = Task(
        description=f"""Analyze the provided content for toxicity and offensive language.

        Content to analyze:
        \"\"\"{content}\"\"\"{context_str}

        Perform comprehensive toxicity analysis:
        1. Overall Toxicity Score (0-1 scale)
        2. Specific Toxicity Categories:
           - Insults and personal attacks
           - Threats (explicit or implicit)
           - Profanity and obscene language
           - Identity-based hate (racism, sexism, etc.)
           - Sexually explicit content
           - Aggressive or hostile tone
        3. Severity Assessment (low/moderate/high/severe)
        4. Context Considerations: Identify if toxic language is:
           - Quoted or being discussed
           - Part of educational content
           - Genuine harmful intent
        5. Specific Examples: Highlight problematic phrases

        Provide a detailed toxicity report with scores and recommendations.""",
        agent=toxicity_analyzer,
        expected_output="""A structured toxicity report containing:
        - Overall toxicity score (0-1)
        - Category-specific scores
        - Severity level
        - Context analysis
        - Highlighted problematic content
        - Recommendation (approve/warn/reject)"""
    )

    # Task 2: Content Moderation
    moderation_task = Task(
        description=f"""Review the content against content moderation policies.

        Content to review:
        \"\"\"{content}\"\"\"{context_str}

        Evaluate for policy violations:
        1. Violence and Gore: Graphic violence, self-harm, dangerous activities
        2. Adult Content: Sexual content, nudity, suggestive material
        3. Hate Speech: Content attacking groups based on protected characteristics
        4. Harassment: Bullying, stalking, doxxing
        5. Misinformation: Dangerous false claims (health, safety, etc.)
        6. Illegal Activities: Promotion of illegal acts
        7. Spam and Manipulation: Deceptive content, scams
        8. Copyright/Trademark: Potential IP violations

        For each category:
        - Violation detected? (yes/no)
        - Confidence level (low/medium/high)
        - Specific violations
        - Recommended action

        Provide a comprehensive moderation assessment.""",
        agent=content_moderator,
        expected_output="""A content moderation report containing:
        - Policy violation checklist with confidence levels
        - Specific violation details
        - Overall risk assessment
        - Recommended moderation action
        - Appeal considerations"""
    )

    # Task 3: Sensitive Information Detection
    privacy_task = Task(
        description=f"""Scan the content for sensitive personal information and privacy risks.

        Content to scan:
        \"\"\"{content}\"\"\"{context_str}

        Detect and classify sensitive information:
        1. Direct Identifiers:
           - Full names
           - Email addresses
           - Phone numbers
           - Physical addresses
           - Social Security Numbers
           - Government IDs
        2. Financial Information:
           - Credit card numbers
           - Bank account numbers
           - Financial records
        3. Health Information:
           - Medical records
           - Health conditions
           - Prescriptions
        4. Login Credentials:
           - Passwords
           - API keys
           - Access tokens
        5. Other Private Data:
           - Dates of birth
           - Biometric data
           - Location data

        For each detected item:
        - Type of information
        - Location in content
        - Privacy risk level
        - Recommended action (redact/mask/remove)

        Provide a privacy risk assessment.""",
        agent=sensitive_info_guardian,
        expected_output="""A privacy analysis report containing:
        - List of detected sensitive information with types
        - Privacy risk score
        - Specific locations of PII
        - Redaction recommendations
        - Compliance considerations (GDPR, CCPA, etc.)"""
    )

    # Task 4: Bias Detection
    bias_task = Task(
        description=f"""Analyze the content for bias, stereotypes, and fairness issues.

        Content to analyze:
        \"\"\"{content}\"\"\"{context_str}

        Examine for various forms of bias:
        1. Gender Bias: Stereotypes, unequal representation, gendered language
        2. Racial/Ethnic Bias: Stereotypes, discriminatory language, prejudice
        3. Age Bias: Ageism, generational stereotypes
        4. Religious Bias: Religious stereotypes or prejudice
        5. Disability Bias: Ableist language or stereotypes
        6. Socioeconomic Bias: Class-based stereotypes
        7. Other Biases: Sexual orientation, nationality, etc.

        Also evaluate:
        - Inclusive language usage
        - Representation and diversity
        - Fairness in comparisons or statements
        - Microaggressions
        - Implicit bias indicators

        For each identified issue:
        - Type of bias
        - Specific examples
        - Severity (minor/moderate/significant)
        - Suggestions for improvement

        Provide a bias and fairness assessment.""",
        agent=bias_detector,
        expected_output="""A bias analysis report containing:
        - Identified biases with specific examples
        - Severity assessments
        - Inclusive language score
        - Specific problematic phrases
        - Suggestions for more inclusive alternatives"""
    )

    # Task 5: Safety Coordination and Final Assessment
    coordination_task = Task(
        description=f"""Synthesize all safety analyses into a comprehensive safety assessment.

        Original Content:
        \"\"\"{content}\"\"\"{context_str}

        Based on the findings from:
        - Toxicity analysis
        - Content moderation review
        - Privacy/sensitive information scan
        - Bias detection

        Provide a unified safety assessment:
        1. Overall Safety Score (0-100, where 100 is completely safe)
        2. Critical Issues: List any severe problems requiring immediate action
        3. Moderate Issues: List concerns that should be addressed
        4. Minor Issues: List suggestions for improvement
        5. Safety Categories Summary:
           - Toxicity level
           - Content policy compliance
           - Privacy protection
           - Fairness and inclusion
        6. Final Recommendation:
           - APPROVE: Content is safe, no action needed
           - APPROVE_WITH_WARNING: Safe but include content warnings
           - FLAG_FOR_REVIEW: Manual review recommended
           - REJECT: Content violates policies, should not be published
           - MODIFY_REQUIRED: Content can be salvaged with specific changes
        7. Specific Actions: If modification or review needed, list specific steps
        8. Priority Level: urgent/high/medium/low

        Provide clear, actionable guidance for content handling.""",
        agent=safety_coordinator,
        expected_output="""A comprehensive safety assessment containing:
        - Overall safety score (0-100)
        - Categorized issues (critical/moderate/minor)
        - Safety dimensions summary
        - Clear final recommendation with rationale
        - Specific action items if needed
        - Priority level
        - Summary suitable for content creators/moderators""",
        context=[toxicity_task, moderation_task, privacy_task, bias_task]
    )

    return [toxicity_task, moderation_task, privacy_task, bias_task, coordination_task]
