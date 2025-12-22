from crewai import Task
from textwrap import dedent

class MarketingAgencyTasks:
    def conduct_market_research(self, agent, product, industry):
        return Task(
            description=dedent(f"""\
                Conduct comprehensive market research for:
                Product/Service: {product}
                Industry: {industry}

                Research and analyze:
                1. Market Size and Growth
                   - Current market size
                   - Growth trends and projections
                   - Market segmentation

                2. Target Audience
                   - Demographics
                   - Psychographics
                   - Pain points and needs
                   - Buying behavior

                3. Competitive Landscape
                   - Key competitors
                   - Market share distribution
                   - Competitor strengths and weaknesses
                   - Competitive positioning

                4. Market Trends
                   - Emerging trends
                   - Technology disruptions
                   - Regulatory changes
                   - Consumer preference shifts

                5. Opportunities and Threats
                   - Market gaps
                   - Entry barriers
                   - Risk factors

                Provide detailed findings with data and insights."""),
            agent=agent,
            expected_output="Comprehensive market research report with target audience profile, competitive analysis, and market opportunities"
        )

    def develop_brand_strategy(self, agent, product, market_research):
        return Task(
            description=dedent(f"""\
                Develop a comprehensive brand strategy for:
                Product/Service: {product}
                Market Research: {market_research}

                Create:
                1. Brand Positioning
                   - Unique value proposition
                   - Positioning statement
                   - Differentiation strategy
                   - Competitive advantages

                2. Brand Identity
                   - Brand personality
                   - Brand voice and tone
                   - Key brand attributes
                   - Brand values

                3. Messaging Framework
                   - Core message
                   - Supporting messages
                   - Proof points
                   - Key benefits

                4. Target Audience Strategy
                   - Primary audience segments
                   - Messaging for each segment
                   - Channel preferences

                Develop a cohesive brand strategy that resonates with the target audience."""),
            agent=agent,
            expected_output="Complete brand strategy with positioning, messaging framework, and audience targeting"
        )

    def create_content_calendar(self, agent, brand_strategy, channels, duration):
        return Task(
            description=dedent(f"""\
                Create a comprehensive content marketing calendar:
                Brand Strategy: {brand_strategy}
                Channels: {channels}
                Duration: {duration}

                Develop:
                1. Content Themes
                   - Monthly themes aligned with business goals
                   - Content pillars
                   - Seasonal considerations

                2. Content Mix
                   - Blog posts
                   - Social media content
                   - Email campaigns
                   - Video content
                   - Infographics
                   - Case studies

                3. Publishing Schedule
                   - Posting frequency per channel
                   - Optimal posting times
                   - Content distribution plan

                4. Content Ideas
                   - Specific content topics
                   - Headlines and hooks
                   - Call-to-action strategies

                Create a detailed, actionable content calendar."""),
            agent=agent,
            expected_output="Detailed content calendar with themes, content mix, and publishing schedule"
        )

    def optimize_for_search(self, agent, content, keywords):
        return Task(
            description=dedent(f"""\
                Optimize content for search engines:
                Content: {content}
                Target Keywords: {keywords}

                Perform:
                1. Keyword Optimization
                   - Primary keyword placement
                   - Secondary keyword integration
                   - Long-tail keyword opportunities
                   - Keyword density optimization

                2. On-Page SEO
                   - Title tag optimization
                   - Meta description
                   - Header tag structure (H1, H2, H3)
                   - URL structure
                   - Image alt text

                3. Content Enhancement
                   - Readability improvements
                   - Internal linking suggestions
                   - External linking strategy
                   - Content length optimization

                4. Technical SEO Recommendations
                   - Schema markup suggestions
                   - Mobile optimization notes
                   - Page speed considerations

                Provide optimized content and SEO recommendations."""),
            agent=agent,
            expected_output="SEO-optimized content with keyword integration and technical recommendations"
        )

    def create_campaign(self, agent, objective, budget, channels, timeline):
        return Task(
            description=dedent(f"""\
                Design a comprehensive marketing campaign:
                Objective: {objective}
                Budget: {budget}
                Channels: {channels}
                Timeline: {timeline}

                Develop:
                1. Campaign Strategy
                   - Campaign concept and theme
                   - Key messages
                   - Target audience segments
                   - Channel strategy

                2. Campaign Assets
                   - Ad copy variations
                   - Social media posts
                   - Email sequences
                   - Landing page content
                   - Creative briefs

                3. Budget Allocation
                   - Budget distribution by channel
                   - Resource allocation
                   - Timeline and milestones

                4. Success Metrics
                   - KPIs by channel
                   - Conversion goals
                   - ROI targets
                   - Tracking plan

                Create a comprehensive campaign plan ready for execution."""),
            agent=agent,
            expected_output="Complete campaign plan with strategy, assets, budget allocation, and success metrics"
        )

    def measure_and_report(self, agent, campaign_data, metrics):
        return Task(
            description=dedent(f"""\
                Analyze campaign performance and generate insights:
                Campaign Data: {campaign_data}
                Key Metrics: {metrics}

                Analyze:
                1. Performance Metrics
                   - Traffic and engagement
                   - Conversion rates
                   - Cost per acquisition
                   - Return on ad spend
                   - Click-through rates

                2. Channel Performance
                   - Performance by channel
                   - Best and worst performers
                   - Cross-channel attribution

                3. Audience Insights
                   - Demographic performance
                   - Behavioral patterns
                   - Engagement by segment

                4. Optimization Recommendations
                   - What's working well
                   - Areas for improvement
                   - A/B test suggestions
                   - Budget reallocation recommendations

                5. Executive Summary
                   - Key achievements
                   - Learnings
                   - Next steps

                Generate a comprehensive performance report with actionable insights."""),
            agent=agent,
            expected_output="Comprehensive marketing performance report with metrics, insights, and optimization recommendations"
        )
