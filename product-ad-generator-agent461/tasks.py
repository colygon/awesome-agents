"""
CrewAI Tasks for Product Ad Generator
Defines tasks for market research, copywriting, design, and optimization
"""

from crewai import Task
from textwrap import dedent


class ProductAdTasks:
    """Factory class for creating product ad generation tasks"""

    def research_target_audience(self, agent, product_info: dict) -> Task:
        """
        Task: Research target audience and market positioning
        """
        return Task(
            description=dedent(f"""
                Conduct comprehensive market research for the product:

                Product Information:
                - Name: {product_info.get('name', 'N/A')}
                - Category: {product_info.get('category', 'N/A')}
                - Description: {product_info.get('description', 'N/A')}
                - Key Features: {product_info.get('features', 'N/A')}
                - Target Market: {product_info.get('target_market', 'General audience')}

                Research Areas:
                1. Target audience demographics and psychographics
                2. Customer pain points and desires
                3. Competitive landscape and positioning
                4. Market trends and opportunities
                5. Unique selling propositions (USPs)
                6. Key messaging angles

                Your analysis should:
                - Identify 2-3 primary customer personas
                - Highlight emotional and rational buying motivators
                - Assess competitive advantages
                - Recommend positioning strategy
                - Suggest messaging themes

                Provide actionable insights for ad creative development.
            """),
            agent=agent,
            expected_output='Detailed market research report with target audience analysis, '
                          'competitive positioning, USPs, and messaging recommendations'
        )

    def create_ad_copy(self, agent, product_info: dict, platform: str = "general") -> Task:
        """
        Task: Create compelling ad copy and headlines
        """
        return Task(
            description=dedent(f"""
                Create persuasive ad copy for the product:

                Product: {product_info.get('name', 'N/A')}
                Platform: {platform}

                Context from Market Research:
                (Will be provided by Market Research Specialist)

                Deliverables:
                1. 5 headline variations (attention-grabbing, benefit-focused)
                2. 3 body copy variations (short, medium, long form)
                3. 5 call-to-action (CTA) options
                4. Key selling points in bullet format
                5. Emotional hooks and power words

                Copy Guidelines:
                - Focus on benefits, not just features
                - Use persuasive language and emotional triggers
                - Create urgency where appropriate
                - Maintain brand voice (professional yet approachable)
                - Keep it clear, concise, and compelling
                - Include social proof elements if applicable

                Platform-Specific Requirements:
                - Social media: Concise, engaging, shareable
                - Search ads: Keyword-rich, direct response
                - Display ads: Visual-focused, brief copy
                - Email: Longer form, narrative-driven
            """),
            agent=agent,
            expected_output='Complete ad copy package with multiple headline and body copy variations, '
                          'CTAs, and selling points optimized for the target platform',
            context=[]  # Will be populated with research task
        )

    def design_visual_strategy(self, agent, product_info: dict, brand_guidelines: dict = None) -> Task:
        """
        Task: Design visual strategy and creative direction
        """
        brand_colors = brand_guidelines.get('colors', 'To be defined') if brand_guidelines else 'To be defined'
        brand_fonts = brand_guidelines.get('fonts', 'To be defined') if brand_guidelines else 'To be defined'

        return Task(
            description=dedent(f"""
                Develop comprehensive visual strategy for the product ad:

                Product: {product_info.get('name', 'N/A')}
                Brand Colors: {brand_colors}
                Brand Fonts: {brand_fonts}

                Context:
                (Market research and ad copy will inform visual direction)

                Visual Strategy Deliverables:
                1. Color palette recommendations
                   - Primary, secondary, accent colors
                   - Color psychology rationale
                   - Contrast and accessibility considerations

                2. Typography recommendations
                   - Headline fonts
                   - Body text fonts
                   - Font hierarchy and sizing

                3. Imagery and visual elements
                   - Photo/illustration style
                   - Image composition guidelines
                   - Product showcase approach
                   - Background treatments

                4. Layout and composition
                   - Visual hierarchy
                   - White space usage
                   - Element placement
                   - Mobile vs desktop considerations

                5. Design do's and don'ts
                   - Best practices for the platform
                   - Common pitfalls to avoid
                   - Accessibility guidelines

                Your recommendations should:
                - Align with brand identity
                - Support the messaging strategy
                - Follow platform best practices
                - Optimize for conversion
                - Stand out from competitors
            """),
            agent=agent,
            expected_output='Comprehensive visual design strategy with color palettes, typography, '
                          'imagery guidelines, layout recommendations, and design specifications',
            context=[]  # Will reference previous tasks
        )

    def evaluate_ad_performance(self, agent, product_info: dict) -> Task:
        """
        Task: Evaluate ad creative and provide optimization recommendations
        """
        return Task(
            description=dedent(f"""
                Evaluate the ad creative against best practices and provide optimization recommendations:

                Product: {product_info.get('name', 'N/A')}

                Review the following elements created by the team:
                - Market research and positioning
                - Ad copy and headlines
                - Visual design strategy

                Evaluation Criteria:
                1. Message clarity and impact
                   - Is the value proposition clear?
                   - Does it address customer pain points?
                   - Is the benefit immediately obvious?

                2. Persuasion and conversion potential
                   - Emotional appeal strength
                   - Credibility and trust signals
                   - Call-to-action effectiveness
                   - Urgency and scarcity elements

                3. Visual effectiveness
                   - Eye-catching and memorable
                   - Brand consistency
                   - Platform optimization
                   - Accessibility compliance

                4. Competitive differentiation
                   - Uniqueness vs. competitors
                   - USP prominence
                   - Positioning clarity

                5. Platform best practices
                   - Format compliance
                   - Character limits
                   - Technical specifications
                   - A/B testing recommendations

                Provide:
                - Strengths analysis
                - Areas for improvement
                - Specific optimization suggestions
                - A/B testing recommendations
                - Predicted performance metrics
            """),
            agent=agent,
            expected_output='Detailed performance evaluation with strengths, weaknesses, optimization '
                          'recommendations, and A/B testing suggestions',
            context=[]  # Will reference all previous tasks
        )

    def ensure_brand_alignment(self, agent, product_info: dict, brand_guidelines: dict = None) -> Task:
        """
        Task: Ensure brand alignment and consistency
        """
        return Task(
            description=dedent(f"""
                Review all ad creative elements for brand alignment and consistency:

                Product: {product_info.get('name', 'N/A')}
                Brand Guidelines: {brand_guidelines if brand_guidelines else 'Industry best practices'}

                Review Elements:
                - Market positioning
                - Messaging and tone
                - Visual design
                - Overall creative direction

                Brand Alignment Checklist:
                1. Brand Voice and Tone
                   - Consistent with brand personality?
                   - Appropriate language level?
                   - Tone matches brand values?

                2. Visual Identity
                   - Colors align with brand palette?
                   - Typography follows guidelines?
                   - Imagery style is on-brand?
                   - Logo usage is correct?

                3. Messaging Consistency
                   - Aligns with brand positioning?
                   - Supports brand story?
                   - Consistent with other campaigns?

                4. Value Proposition
                   - Emphasizes brand differentiators?
                   - Reinforces brand promise?
                   - Builds brand equity?

                5. Compliance and Guidelines
                   - Meets legal requirements?
                   - Follows industry regulations?
                   - Adheres to platform policies?

                Deliverables:
                - Brand alignment scorecard
                - Consistency recommendations
                - Guideline adherence report
                - Final approval recommendations
            """),
            agent=agent,
            expected_output='Brand alignment report with scorecard, consistency analysis, and '
                          'final recommendations for approval',
            context=[]  # Will reference all tasks
        )

    def synthesize_ad_campaign(self, agent, product_info: dict) -> Task:
        """
        Task: Synthesize all elements into final ad campaign package
        """
        return Task(
            description=dedent(f"""
                Synthesize all research, copy, design, and optimization insights into a
                comprehensive ad campaign package:

                Product: {product_info.get('name', 'N/A')}

                Compile and organize:
                1. Executive Summary
                   - Product overview
                   - Target audience snapshot
                   - Key messaging themes
                   - Creative strategy overview

                2. Final Ad Creative
                   - Recommended headline (primary)
                   - Recommended body copy (primary)
                   - Alternative variations
                   - Call-to-action

                3. Visual Specifications
                   - Color palette
                   - Typography
                   - Layout guidelines
                   - Image requirements

                4. Implementation Guide
                   - Platform-specific adaptations
                   - Technical specifications
                   - Asset requirements
                   - Launch recommendations

                5. Testing & Optimization Plan
                   - A/B test variations
                   - Success metrics
                   - Optimization timeline
                   - Performance benchmarks

                6. Next Steps
                   - Production requirements
                   - Review and approval process
                   - Launch timeline
                   - Monitoring plan

                Create a cohesive, actionable campaign package ready for production.
            """),
            agent=agent,
            expected_output='Complete ad campaign package with final creative, specifications, '
                          'implementation guide, and optimization plan',
            context=[]  # Will reference all previous tasks
        )
