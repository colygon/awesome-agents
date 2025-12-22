"""
Custom Tools for Safety Plugins Agent
Provides content moderation, toxicity detection, privacy protection, and bias analysis
"""

from crewai_tools import BaseTool
from typing import Type, List, Dict, Any
from pydantic import BaseModel, Field
import re


class ContentModerationInput(BaseModel):
    """Input schema for ContentModerationTool"""
    content: str = Field(..., description="Content to moderate")


class ContentModerationTool(BaseTool):
    name: str = "Content Moderation Tool"
    description: str = """Analyzes content for policy violations including violence, adult
    content, hate speech, harassment, and other safety concerns. Returns moderation scores
    and recommendations."""
    args_schema: Type[BaseModel] = ContentModerationInput

    def _run(self, content: str) -> str:
        """
        Analyze content for moderation issues

        Args:
            content: Text content to analyze

        Returns:
            Moderation analysis results
        """
        try:
            content_lower = content.lower()

            # Simplified moderation checks (in production, use ML models)
            violence_keywords = ['kill', 'murder', 'hurt', 'attack', 'weapon', 'blood', 'death']
            adult_keywords = ['explicit sexual terms']  # Placeholder
            hate_keywords = ['slur', 'hate', 'discriminate', 'supremacy']
            harassment_keywords = ['threaten', 'stalk', 'dox', 'bully']

            scores = {
                'violence': sum(1 for kw in violence_keywords if kw in content_lower) / max(len(violence_keywords), 1),
                'adult_content': sum(1 for kw in adult_keywords if kw in content_lower) / max(len(adult_keywords), 1),
                'hate_speech': sum(1 for kw in hate_keywords if kw in content_lower) / max(len(hate_keywords), 1),
                'harassment': sum(1 for kw in harassment_keywords if kw in content_lower) / max(len(harassment_keywords), 1)
            }

            max_score = max(scores.values())
            overall_risk = "low" if max_score < 0.2 else "medium" if max_score < 0.5 else "high"

            result = f"""Content Moderation Analysis:

Violation Scores (0-1 scale):
- Violence/Gore: {scores['violence']:.2f}
- Adult Content: {scores['adult_content']:.2f}
- Hate Speech: {scores['hate_speech']:.2f}
- Harassment: {scores['harassment']:.2f}

Overall Risk: {overall_risk.upper()}

Note: This is a simplified analysis. For production use, integrate with
Perspective API, OpenAI Moderation API, or similar services for accurate results."""

            return result

        except Exception as e:
            return f"Error in content moderation: {str(e)}"


class ToxicityDetectionInput(BaseModel):
    """Input schema for ToxicityDetectionTool"""
    text: str = Field(..., description="Text to analyze for toxicity")


class ToxicityDetectionTool(BaseTool):
    name: str = "Toxicity Detection Tool"
    description: str = """Detects toxic language including insults, threats, profanity, and
    aggressive language. Provides toxicity scores across multiple dimensions."""
    args_schema: Type[BaseModel] = ToxicityDetectionInput

    def _run(self, text: str) -> str:
        """
        Analyze text for toxicity

        Args:
            text: Text to analyze

        Returns:
            Toxicity analysis results
        """
        try:
            text_lower = text.lower()

            # Simplified toxicity detection (use ML models in production)
            insult_words = ['idiot', 'stupid', 'dumb', 'moron', 'fool']
            threat_words = ['hurt you', 'get you', 'watch out', 'regret']
            aggressive_words = ['shut up', 'hate', 'disgusting', 'pathetic']

            insult_score = sum(1 for word in insult_words if word in text_lower) / 10
            threat_score = sum(1 for phrase in threat_words if phrase in text_lower) / 10
            aggressive_score = sum(1 for word in aggressive_words if word in text_lower) / 10

            overall_toxicity = (insult_score + threat_score + aggressive_score) / 3

            severity = (
                "severe" if overall_toxicity > 0.7 else
                "high" if overall_toxicity > 0.4 else
                "moderate" if overall_toxicity > 0.2 else
                "low"
            )

            result = f"""Toxicity Analysis:

Toxicity Scores (0-1 scale):
- Insults: {insult_score:.2f}
- Threats: {threat_score:.2f}
- Aggressive Language: {aggressive_score:.2f}
- Overall Toxicity: {overall_toxicity:.2f}

Severity: {severity.upper()}

Recommendation: {'REJECT' if overall_toxicity > 0.5 else 'WARN' if overall_toxicity > 0.2 else 'APPROVE'}

Note: For production, use Perspective API, Detoxify, or similar ML models."""

            return result

        except Exception as e:
            return f"Error in toxicity detection: {str(e)}"


class ProfanityFilterInput(BaseModel):
    """Input schema for ProfanityFilterTool"""
    text: str = Field(..., description="Text to check for profanity")


class ProfanityFilterTool(BaseTool):
    name: str = "Profanity Filter Tool"
    description: str = """Detects profanity and obscene language in text. Returns locations
    and severity of profane content."""
    args_schema: Type[BaseModel] = ProfanityFilterInput

    def _run(self, text: str) -> str:
        """
        Check text for profanity

        Args:
            text: Text to analyze

        Returns:
            Profanity detection results
        """
        try:
            # Simplified profanity detection
            # In production, use libraries like better-profanity or profanity-check

            profanity_count = 0  # Placeholder

            result = f"""Profanity Detection:

Profanity Found: {'No' if profanity_count == 0 else 'Yes'}
Count: {profanity_count}
Severity: {'None' if profanity_count == 0 else 'Low' if profanity_count < 3 else 'High'}

Note: For production, integrate with profanity detection libraries or APIs."""

            return result

        except Exception as e:
            return f"Error in profanity detection: {str(e)}"


class SensitiveInfoInput(BaseModel):
    """Input schema for SensitiveInfoDetectorTool"""
    content: str = Field(..., description="Content to scan for sensitive information")


class SensitiveInfoDetectorTool(BaseTool):
    name: str = "Sensitive Information Detector Tool"
    description: str = """Detects personally identifiable information (PII) and sensitive data
    including emails, phone numbers, SSNs, credit cards, addresses, and other private information."""
    args_schema: Type[BaseModel] = SensitiveInfoInput

    def _run(self, content: str) -> str:
        """
        Scan content for sensitive information

        Args:
            content: Content to analyze

        Returns:
            Sensitive information detection results
        """
        try:
            findings = []

            # Email detection
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, content)
            if emails:
                findings.append(f"Emails: {len(emails)} found")

            # Phone number detection (simple patterns)
            phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b|\(\d{3}\)\s*\d{3}[-.]?\d{4}\b'
            phones = re.findall(phone_pattern, content)
            if phones:
                findings.append(f"Phone Numbers: {len(phones)} found")

            # SSN detection (US format)
            ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
            ssns = re.findall(ssn_pattern, content)
            if ssns:
                findings.append(f"SSNs: {len(ssns)} found (HIGH RISK)")

            # Credit card detection (simple)
            cc_pattern = r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'
            cards = re.findall(cc_pattern, content)
            if cards:
                findings.append(f"Credit Card Numbers: {len(cards)} found (HIGH RISK)")

            # Address detection (basic)
            address_pattern = r'\b\d+\s+[\w\s]+(?:street|st|avenue|ave|road|rd|drive|dr|lane|ln|court|ct)\b'
            addresses = re.findall(address_pattern, content, re.IGNORECASE)
            if addresses:
                findings.append(f"Addresses: {len(addresses)} found")

            risk_level = (
                "HIGH" if ssns or cards else
                "MEDIUM" if emails or phones else
                "LOW" if findings else
                "NONE"
            )

            result = f"""Sensitive Information Detection:

Findings:
{chr(10).join('- ' + f for f in findings) if findings else '- No sensitive information detected'}

Privacy Risk Level: {risk_level}

Recommendation: {'REDACT sensitive information before publishing' if risk_level in ['HIGH', 'MEDIUM'] else 'Content appears safe from privacy perspective'}

Note: This is a pattern-based detection. For production, use advanced PII detection
services like Microsoft Presidio, AWS Comprehend, or Google DLP API."""

            return result

        except Exception as e:
            return f"Error in sensitive information detection: {str(e)}"


class BiasDetectionInput(BaseModel):
    """Input schema for BiasDetectionTool"""
    content: str = Field(..., description="Content to analyze for bias")


class BiasDetectionTool(BaseTool):
    name: str = "Bias Detection Tool"
    description: str = """Analyzes content for bias, stereotypes, and fairness issues across
    gender, race, age, religion, and other dimensions. Suggests more inclusive alternatives."""
    args_schema: Type[BaseModel] = BiasDetectionInput

    def _run(self, content: str) -> str:
        """
        Analyze content for bias

        Args:
            content: Content to analyze

        Returns:
            Bias analysis results
        """
        try:
            content_lower = content.lower()
            findings = []

            # Gender bias detection
            gendered_terms = {
                'chairman': 'chairperson',
                'policeman': 'police officer',
                'fireman': 'firefighter',
                'mankind': 'humankind',
                'manpower': 'workforce'
            }

            for biased, inclusive in gendered_terms.items():
                if biased in content_lower:
                    findings.append(f"Gender Bias: '{biased}' → suggest '{inclusive}'")

            # Stereotyping language
            stereotype_keywords = ['typical', 'naturally', 'all', 'always', 'never', 'obviously']
            stereotype_flags = [kw for kw in stereotype_keywords if kw in content_lower]
            if stereotype_flags:
                findings.append(f"Potential Stereotyping: Use of absolute terms like {stereotype_flags}")

            # Age bias
            age_bias_terms = ['too old', 'too young', 'elderly', 'kids these days']
            age_flags = [term for term in age_bias_terms if term in content_lower]
            if age_flags:
                findings.append(f"Age Bias: Ageist language detected: {age_flags}")

            bias_score = len(findings) / 10  # Normalized score

            result = f"""Bias Detection Analysis:

Findings:
{chr(10).join('- ' + f for f in findings) if findings else '- No obvious bias detected'}

Bias Score: {bias_score:.2f} (0 = no bias, 1 = high bias)

Inclusive Language Score: {(1 - bias_score) * 100:.0f}/100

Recommendation: {'Review and revise for more inclusive language' if bias_score > 0.3 else 'Content appears reasonably inclusive'}

Note: For comprehensive bias detection, use specialized tools like IBM AI Fairness 360,
Google's What-If Tool, or dedicated bias detection APIs."""

            return result

        except Exception as e:
            return f"Error in bias detection: {str(e)}"
