"""
Custom Tools for Product Ad Generator
Provides specialized tools for ad creation and analysis
"""

from crewai_tools import BaseTool
from typing import Type, Dict, List
from pydantic import BaseModel, Field
import re


class AdCopyAnalyzerInput(BaseModel):
    """Input schema for AdCopyAnalyzerTool"""
    copy_text: str = Field(..., description="Ad copy text to analyze")


class AdCopyAnalyzerTool(BaseTool):
    name: str = "Ad Copy Analyzer"
    description: str = """Analyzes ad copy for readability, persuasion elements, and best practices.
    Provides metrics like reading level, power word count, and emotional triggers."""
    args_schema: Type[BaseModel] = AdCopyAnalyzerInput

    def _run(self, copy_text: str) -> str:
        """
        Analyze ad copy quality and effectiveness

        Args:
            copy_text: The ad copy to analyze

        Returns:
            Analysis report with metrics and recommendations
        """
        # Power words commonly used in advertising
        power_words = [
            'free', 'new', 'proven', 'guaranteed', 'exclusive', 'limited',
            'save', 'bonus', 'instant', 'now', 'discover', 'secret',
            'amazing', 'revolutionary', 'breakthrough', 'professional',
            'premium', 'ultimate', 'easy', 'simple', 'fast', 'best'
        ]

        # Action verbs
        action_verbs = [
            'get', 'buy', 'order', 'subscribe', 'download', 'join',
            'start', 'try', 'claim', 'unlock', 'access', 'discover',
            'learn', 'transform', 'boost', 'increase', 'improve'
        ]

        copy_lower = copy_text.lower()

        # Count metrics
        word_count = len(copy_text.split())
        char_count = len(copy_text)
        sentence_count = len([s for s in re.split(r'[.!?]+', copy_text) if s.strip()])

        power_word_count = sum(1 for word in power_words if word in copy_lower)
        action_verb_count = sum(1 for verb in action_verbs if verb in copy_lower)

        # Check for questions
        question_count = copy_text.count('?')

        # Check for numbers
        number_count = len(re.findall(r'\d+', copy_text))

        # Calculate average sentence length
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0

        analysis = f"""
Ad Copy Analysis Report
========================

Basic Metrics:
- Word Count: {word_count}
- Character Count: {char_count}
- Sentence Count: {sentence_count}
- Average Sentence Length: {avg_sentence_length:.1f} words

Persuasion Elements:
- Power Words: {power_word_count} (Good: 3-5, Excellent: 6+)
- Action Verbs: {action_verb_count} (Recommend: 2-3)
- Questions: {question_count} (Engagement technique)
- Numbers: {number_count} (Specificity and credibility)

Recommendations:
"""

        # Generate recommendations
        recommendations = []

        if word_count > 100:
            recommendations.append("- Consider shortening copy for better scanability (ideal: 50-100 words)")
        elif word_count < 30:
            recommendations.append("- Copy may be too brief to convey full value proposition")

        if avg_sentence_length > 20:
            recommendations.append("- Sentences are lengthy; break into shorter, punchier statements")

        if power_word_count < 3:
            recommendations.append("- Add more power words to increase emotional appeal")

        if action_verb_count < 1:
            recommendations.append("- Include strong action verbs to drive response")

        if number_count == 0:
            recommendations.append("- Add specific numbers/stats for credibility")

        if not recommendations:
            recommendations.append("- Copy meets best practice guidelines!")

        analysis += '\n'.join(recommendations)

        return analysis


class HeadlineGeneratorInput(BaseModel):
    """Input schema for HeadlineGeneratorTool"""
    product_name: str = Field(..., description="Name of the product")
    key_benefit: str = Field(..., description="Primary benefit or value proposition")


class HeadlineGeneratorTool(BaseTool):
    name: str = "Headline Generator"
    description: str = """Generates multiple headline variations using proven copywriting formulas
    like How-To, Question, Number, Negative, and Benefit-focused templates."""
    args_schema: Type[BaseModel] = HeadlineGeneratorInput

    def _run(self, product_name: str, key_benefit: str) -> str:
        """
        Generate headline variations using proven formulas

        Args:
            product_name: Name of the product
            key_benefit: Primary benefit

        Returns:
            List of headline variations
        """
        headlines = []

        # Formula 1: How-To
        headlines.append(f"How to {key_benefit} with {product_name}")

        # Formula 2: Question
        headlines.append(f"Want to {key_benefit}?")

        # Formula 3: Number-based
        headlines.append(f"5 Ways {product_name} Helps You {key_benefit}")

        # Formula 4: Negative angle
        headlines.append(f"Stop Struggling to {key_benefit}")

        # Formula 5: Direct benefit
        headlines.append(f"{key_benefit} - Made Simple with {product_name}")

        # Formula 6: Urgency
        headlines.append(f"Limited Time: {key_benefit} Starts Now")

        # Formula 7: Social proof
        headlines.append(f"Join Thousands Who {key_benefit} with {product_name}")

        # Formula 8: Result-focused
        headlines.append(f"Finally: {key_benefit} in Just Minutes")

        output = "Generated Headline Variations:\n" + "="*50 + "\n\n"

        for i, headline in enumerate(headlines, 1):
            output += f"{i}. {headline}\n"

        output += "\n" + "="*50 + "\n"
        output += "Tips:\n"
        output += "- Test 3-5 variations to find the best performer\n"
        output += "- Keep headlines under 60 characters for display ads\n"
        output += "- Include the primary keyword for search ads\n"
        output += "- Use title case for better readability\n"

        return output


class ColorPsychologyInput(BaseModel):
    """Input schema for ColorPsychologyTool"""
    industry: str = Field(..., description="Industry or product category")
    emotion: str = Field(..., description="Desired emotional response")


class ColorPsychologyTool(BaseTool):
    name: str = "Color Psychology Advisor"
    description: str = """Recommends color schemes based on color psychology principles,
    industry standards, and desired emotional responses."""
    args_schema: Type[BaseModel] = ColorPsychologyInput

    def _run(self, industry: str, emotion: str) -> str:
        """
        Recommend colors based on psychology and industry

        Args:
            industry: Product industry or category
            emotion: Desired emotional response

        Returns:
            Color recommendations with psychology rationale
        """
        # Color psychology database
        color_emotions = {
            'trust': ['Blue', 'Navy', 'Teal'],
            'excitement': ['Red', 'Orange', 'Yellow'],
            'calm': ['Blue', 'Green', 'Lavender'],
            'luxury': ['Purple', 'Gold', 'Black'],
            'energy': ['Red', 'Orange', 'Bright Yellow'],
            'nature': ['Green', 'Brown', 'Earth tones'],
            'creativity': ['Purple', 'Pink', 'Bright colors'],
            'security': ['Blue', 'Gray', 'Dark Green'],
            'happiness': ['Yellow', 'Orange', 'Light colors'],
            'sophistication': ['Black', 'Charcoal', 'Deep Purple']
        }

        # Industry-specific recommendations
        industry_colors = {
            'technology': ['Blue', 'Gray', 'White'],
            'healthcare': ['Blue', 'Green', 'White'],
            'food': ['Red', 'Yellow', 'Orange'],
            'finance': ['Blue', 'Green', 'Gray'],
            'fashion': ['Black', 'White', 'Bold accents'],
            'eco': ['Green', 'Brown', 'Earth tones'],
            'children': ['Bright primary colors', 'Rainbow'],
            'luxury': ['Gold', 'Black', 'Deep Purple']
        }

        emotion_lower = emotion.lower()
        industry_lower = industry.lower()

        # Find matching colors
        recommended_colors = []
        for key, colors in color_emotions.items():
            if key in emotion_lower:
                recommended_colors.extend(colors)

        industry_match = []
        for key, colors in industry_colors.items():
            if key in industry_lower:
                industry_match.extend(colors)

        output = f"""
Color Psychology Recommendations
=================================

Target Emotion: {emotion}
Industry: {industry}

Recommended Color Palette:
"""

        if recommended_colors:
            output += "\nEmotion-Based Colors:\n"
            for color in set(recommended_colors[:3]):
                output += f"  - {color}\n"

        if industry_match:
            output += "\nIndustry-Standard Colors:\n"
            for color in set(industry_match[:3]):
                output += f"  - {color}\n"

        output += """
Color Psychology Principles:
- Blue: Trust, security, professionalism, calm
- Red: Energy, urgency, excitement, passion
- Green: Nature, health, growth, wealth
- Yellow: Optimism, clarity, warmth, caution
- Purple: Luxury, creativity, wisdom, royalty
- Orange: Enthusiasm, creativity, success, energy
- Black: Sophistication, luxury, power, elegance
- White: Purity, simplicity, cleanliness, space

Best Practices:
- Use 2-3 primary colors maximum
- Ensure sufficient contrast for readability (WCAG AA: 4.5:1)
- Consider cultural color associations for global campaigns
- Test color combinations for accessibility (colorblind-friendly)
- Align with brand guidelines while optimizing for response
"""

        return output


class CTAOptimizerInput(BaseModel):
    """Input schema for CTAOptimizerTool"""
    cta_text: str = Field(..., description="Call-to-action text to optimize")
    goal: str = Field(..., description="Campaign goal (e.g., purchase, signup, download)")


class CTAOptimizerTool(BaseTool):
    name: str = "CTA Optimizer"
    description: str = """Analyzes and optimizes call-to-action text for maximum conversion,
    providing variations based on proven CTA best practices."""
    args_schema: Type[BaseModel] = CTAOptimizerInput

    def _run(self, cta_text: str, goal: str) -> str:
        """
        Optimize CTA text for conversions

        Args:
            cta_text: Original CTA text
            goal: Campaign goal

        Returns:
            Optimized CTA variations with rationale
        """
        goal_lower = goal.lower()

        # Goal-specific CTA templates
        cta_templates = {
            'purchase': [
                'Buy Now',
                'Shop Now',
                'Get Yours Today',
                'Add to Cart',
                'Order Now'
            ],
            'signup': [
                'Sign Up Free',
                'Get Started',
                'Join Now',
                'Create Account',
                'Start Free Trial'
            ],
            'download': [
                'Download Now',
                'Get Your Free Guide',
                'Claim Your Copy',
                'Download Free',
                'Get Instant Access'
            ],
            'learn': [
                'Learn More',
                'Discover How',
                'See How It Works',
                'Find Out More',
                'Explore Solutions'
            ],
            'contact': [
                'Get in Touch',
                'Contact Us Today',
                'Request a Quote',
                'Schedule a Call',
                'Talk to an Expert'
            ]
        }

        # Find matching templates
        suggestions = []
        for key, ctas in cta_templates.items():
            if key in goal_lower:
                suggestions = ctas
                break

        if not suggestions:
            suggestions = cta_templates.get('learn', [])

        output = f"""
CTA Optimization Report
========================

Original CTA: "{cta_text}"
Goal: {goal}

Optimized Variations:
"""

        for i, cta in enumerate(suggestions, 1):
            output += f"{i}. {cta}\n"

        output += """
CTA Best Practices:
- Use action verbs (Get, Start, Join, Discover, Try)
- Create urgency ("Now", "Today", "Limited Time")
- Emphasize value ("Free", "Save", "Exclusive")
- Keep it short (2-5 words ideal)
- Be specific about the action
- Use first-person for higher conversion ("Get My Free Trial")
- Consider adding benefit ("Start Saving Today")
- Test button color contrast (high visibility)
- Make it stand out visually

A/B Testing Recommendations:
1. Test urgent vs. non-urgent versions
2. Compare first-person vs. second-person
3. Try with/without benefit statement
4. Test different action verbs
5. Experiment with button size and color

Conversion Tips:
- Place CTA above the fold
- Repeat CTA if page is long
- Use white space around button
- Make button large enough to tap easily (mobile)
- Reduce friction (minimize form fields)
"""

        return output
