from crewai import Agent
from textwrap import dedent
from tools import MarketResearchTools, ContentTools, AnalyticsTools

class MarketingAgencyAgents:
    def market_researcher(self):
        return Agent(
            role='Market Research Specialist',
            goal='Conduct comprehensive market research and competitor analysis',
            backstory=dedent("""\
                You are an expert market researcher with deep experience in
                analyzing market trends, consumer behavior, and competitive
                landscapes. You excel at gathering insights from multiple
                sources and identifying market opportunities. You understand
                how to segment audiences and analyze market dynamics."""),
            tools=[
                MarketResearchTools.research_market,
                MarketResearchTools.analyze_competitors,
                MarketResearchTools.identify_target_audience
            ],
            verbose=True,
            allow_delegation=False
        )

    def brand_strategist(self):
        return Agent(
            role='Brand Strategy Expert',
            goal='Develop comprehensive brand positioning and messaging strategies',
            backstory=dedent("""\
                You are a brand strategist with expertise in creating
                compelling brand identities and positioning. You understand
                how to differentiate brands in crowded markets and craft
                messages that resonate with target audiences. You excel at
                developing unique value propositions and brand narratives."""),
            tools=[
                MarketResearchTools.identify_target_audience,
                ContentTools.create_brand_message
            ],
            verbose=True,
            allow_delegation=False
        )

    def content_creator(self):
        return Agent(
            role='Content Marketing Specialist',
            goal='Create engaging marketing content across multiple channels',
            backstory=dedent("""\
                You are a creative content marketer who can write compelling
                copy for various channels - social media, blogs, emails, ads,
                and more. You understand content strategy, SEO, and how to
                create content that drives engagement and conversions. You
                adapt tone and style to match brand voice and audience."""),
            tools=[
                ContentTools.create_social_content,
                ContentTools.write_blog_post,
                ContentTools.create_email_campaign,
                ContentTools.generate_ad_copy
            ],
            verbose=True,
            allow_delegation=False
        )

    def seo_specialist(self):
        return Agent(
            role='SEO & Digital Marketing Expert',
            goal='Optimize content for search engines and digital channels',
            backstory=dedent("""\
                You are an SEO expert who understands search engine algorithms,
                keyword research, and content optimization. You know how to
                improve organic visibility and drive qualified traffic. You
                stay current with SEO best practices and algorithm updates."""),
            tools=[
                ContentTools.optimize_for_seo,
                AnalyticsTools.analyze_keywords
            ],
            verbose=True,
            allow_delegation=False
        )

    def campaign_manager(self):
        return Agent(
            role='Marketing Campaign Coordinator',
            goal='Orchestrate integrated marketing campaigns and measure performance',
            backstory=dedent("""\
                You are an experienced campaign manager who can coordinate
                multi-channel marketing campaigns. You understand campaign
                planning, execution, and measurement. You excel at setting
                KPIs, tracking performance, and optimizing campaigns for
                better results."""),
            tools=[
                AnalyticsTools.track_campaign_performance,
                AnalyticsTools.generate_marketing_report
            ],
            verbose=True,
            allow_delegation=False
        )
