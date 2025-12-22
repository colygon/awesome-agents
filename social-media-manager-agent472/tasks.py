from crewai import Task
from textwrap import dedent

class SocialMediaManagerTasks:
    def develop_content_strategy(self, agent, brand_info):
        return Task(
            description=dedent(f"""
                Develop a comprehensive social media content strategy for the brand:

                Brand Information:
                {brand_info}

                Your tasks:
                1. Analyze target audience demographics and preferences
                2. Identify key content themes and pillars
                3. Define content mix (promotional, educational, entertaining)
                4. Research trending topics and hashtags in the industry
                5. Create content guidelines and brand voice document
                6. Develop monthly content calendar framework

                Provide a detailed content strategy document.
            """),
            agent=agent,
            expected_output="Comprehensive content strategy with audience analysis, content themes, and calendar framework"
        )

    def create_social_posts(self, agent, campaign_details):
        return Task(
            description=dedent(f"""
                Create engaging social media posts for the campaign:

                Campaign Details:
                {campaign_details}

                Your tasks:
                1. Write compelling post copy for each platform
                2. Create attention-grabbing headlines
                3. Develop relevant hashtag sets
                4. Include clear calls-to-action
                5. Adapt messaging for different platforms (Instagram, Twitter, LinkedIn, Facebook)
                6. Create variations for A/B testing

                Provide complete post copy for all platforms.
            """),
            agent=agent,
            expected_output="Platform-specific social media posts with copy, hashtags, and CTAs ready for publishing"
        )

    def schedule_content(self, agent, content_calendar):
        return Task(
            description=dedent(f"""
                Create an optimized posting schedule for the content:

                Content Calendar:
                {content_calendar}

                Your tasks:
                1. Research optimal posting times for each platform
                2. Distribute content evenly across the week/month
                3. Schedule posts at peak engagement times
                4. Balance different content types throughout the schedule
                5. Set up recurring posts for evergreen content
                6. Create backup content for gaps

                Provide a detailed posting schedule with dates and times.
            """),
            agent=agent,
            expected_output="Optimized posting schedule with specific dates, times, and platform assignments for all content"
        )

    def track_performance(self, agent, campaign_id):
        return Task(
            description=dedent(f"""
                Track and analyze social media performance:

                Campaign ID: {campaign_id}

                Your tasks:
                1. Monitor engagement metrics (likes, comments, shares)
                2. Track reach and impressions across platforms
                3. Analyze click-through rates and conversions
                4. Identify top-performing content
                5. Monitor audience growth and demographics
                6. Compare performance against benchmarks

                Provide a comprehensive performance report.
            """),
            agent=agent,
            expected_output="Detailed analytics report with metrics, insights, and performance comparisons"
        )

    def generate_monthly_report(self, agent, account_data):
        return Task(
            description=dedent(f"""
                Generate a comprehensive monthly social media report:

                Account Data:
                {account_data}

                Your tasks:
                1. Summarize key metrics and performance trends
                2. Highlight top-performing posts and campaigns
                3. Analyze audience growth and engagement trends
                4. Identify opportunities for improvement
                5. Provide strategic recommendations for next month
                6. Create visualizations for key metrics

                Provide a complete monthly report with insights and recommendations.
            """),
            agent=agent,
            expected_output="Comprehensive monthly report with metrics, analysis, visualizations, and strategic recommendations"
        )
