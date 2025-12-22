"""
CrewAI Tasks for Podcast Transcript Analysis
Defines tasks for processing, analyzing, and optimizing podcast transcripts
"""

from crewai import Task
from textwrap import dedent


class PodcastTranscriptTasks:
    """Factory class for creating podcast transcript processing tasks"""

    def process_transcript(self, agent, transcript_text: str, speakers: list = None) -> Task:
        """
        Task: Clean and format raw transcript
        """
        speaker_info = ', '.join(speakers) if speakers else 'Auto-detect from transcript'

        return Task(
            description=dedent(f"""
                Process and clean the raw podcast transcript:

                Speakers: {speaker_info}

                Processing Requirements:
                1. Remove filler words (um, uh, like, you know, etc.)
                2. Fix punctuation and capitalization
                3. Segment speaker turns clearly
                4. Remove false starts and repetitions
                5. Format for readability
                6. Preserve meaning and context

                The cleaned transcript should:
                - Be grammatically correct
                - Have clear speaker labels
                - Flow naturally when read
                - Maintain the original conversation's intent
                - Be properly paragraphed by topic/speaker

                Return the processed transcript in a clean, readable format.
            """),
            agent=agent,
            expected_output='Cleaned and formatted transcript with proper speaker segmentation, '
                          'punctuation, and readability improvements'
        )

    def analyze_content(self, agent, episode_info: dict = None) -> Task:
        """
        Task: Analyze transcript content for themes and insights
        """
        return Task(
            description=dedent(f"""
                Analyze the podcast transcript content comprehensively:

                Episode Info: {episode_info if episode_info else 'To be extracted from transcript'}

                Analysis Areas:
                1. Main themes and topics discussed
                2. Key insights and takeaways
                3. Expert opinions and recommendations
                4. Data points and statistics mentioned
                5. Stories and anecdotes shared
                6. Debates or differing viewpoints
                7. Actionable advice given
                8. Resources or references mentioned

                For each theme:
                - Provide brief description
                - Note approximate portion of discussion
                - Highlight key insights
                - Identify related segments

                Create a comprehensive content breakdown that helps listeners understand
                what the episode covers and what value they'll gain.
            """),
            agent=agent,
            expected_output='Detailed content analysis with themes, key insights, takeaways, '
                          'and structured breakdown of discussion topics',
            context=[]
        )

    def create_summaries(self, agent, episode_info: dict = None) -> Task:
        """
        Task: Create multi-level summaries
        """
        return Task(
            description=dedent(f"""
                Create engaging summaries of the podcast episode at multiple levels:

                Episode: {episode_info.get('title', 'N/A') if episode_info else 'N/A'}

                Summary Levels Required:

                1. One-Liner (15-25 words)
                   - Ultra-concise hook for social media
                   - Captures core topic/value proposition

                2. Brief Summary (50-75 words)
                   - Quick overview for show notes
                   - Main topic and 2-3 key points
                   - Who should listen

                3. Standard Summary (150-200 words)
                   - Comprehensive overview
                   - Main themes and key insights
                   - Guest background (if applicable)
                   - Primary takeaways

                4. Detailed Summary (300-500 words)
                   - In-depth content overview
                   - All major topics and subtopics
                   - Key quotes and insights
                   - Actionable takeaways
                   - Resources mentioned

                Each summary should:
                - Be engaging and informative
                - Capture the episode's value
                - Use active voice
                - Include relevant keywords
                - Appeal to target audience
            """),
            agent=agent,
            expected_output='Four-tier summary package (one-liner, brief, standard, detailed) '
                          'optimized for different platforms and use cases',
            context=[]
        )

    def generate_timestamps(self, agent, transcript_segments: list = None) -> Task:
        """
        Task: Generate chapter markers and timestamps
        """
        return Task(
            description=dedent(f"""
                Generate chapter markers and timestamps for the podcast episode:

                Requirements:
                1. Identify natural topic transitions
                2. Create descriptive chapter titles
                3. Mark key moments and highlights
                4. Note when guests are introduced
                5. Flag important insights or revelations
                6. Mark sponsor/ad breaks (if present)

                Chapter Marker Guidelines:
                - Title should be concise and descriptive (5-8 words)
                - Average 5-10 chapters per hour of content
                - Balance granularity (not too many, not too few)
                - Use consistent naming format
                - Start with action words when appropriate

                Format:
                [00:00:00] Chapter Title - Brief description

                Also identify:
                - Best moments for social media clips
                - Quotable segments
                - Topic transition points
                - Guest introduction times

                Create a comprehensive timestamp guide that enhances navigation.
            """),
            agent=agent,
            expected_output='Complete chapter markers with timestamps, descriptions, and '
                          'highlights for easy episode navigation',
            context=[]
        )

    def extract_quotes(self, agent, quote_count: int = 10) -> Task:
        """
        Task: Extract memorable quotes and soundbites
        """
        return Task(
            description=dedent(f"""
                Extract the most compelling quotes and soundbites from the transcript:

                Target: {quote_count} top quotes

                Quote Selection Criteria:
                1. Memorability and impact
                2. Shareability on social media
                3. Captures key insights
                4. Standalone value (makes sense without context)
                5. Represents episode themes
                6. Quotable by nature

                For each quote provide:
                - The exact quote
                - Speaker attribution
                - Approximate timestamp
                - Context (1-2 sentences)
                - Suggested use (social, promotional, etc.)
                - Relevant hashtags or topics

                Quote Categories:
                - Inspirational/motivational
                - Educational/insightful
                - Controversial/thought-provoking
                - Actionable advice
                - Humorous/entertaining
                - Statistical/data-driven

                Format quotes for easy sharing across platforms.
            """),
            agent=agent,
            expected_output=f'Curated collection of {quote_count} memorable quotes with context, '
                          'attribution, and usage recommendations',
            context=[]
        )

    def optimize_for_seo(self, agent, episode_info: dict = None, target_keywords: list = None) -> Task:
        """
        Task: Create SEO-optimized metadata and show notes
        """
        keywords = ', '.join(target_keywords) if target_keywords else 'To be identified from content'

        return Task(
            description=dedent(f"""
                Create SEO-optimized metadata and show notes for the podcast episode:

                Episode: {episode_info.get('title', 'N/A') if episode_info else 'N/A'}
                Target Keywords: {keywords}

                Deliverables:

                1. SEO-Optimized Title
                   - Include primary keyword
                   - 60 characters or less
                   - Engaging and click-worthy
                   - Clear value proposition

                2. Meta Description (150-160 characters)
                   - Include primary and secondary keywords
                   - Compelling and accurate
                   - Call-to-action or hook

                3. Show Notes (300-500 words)
                   - Natural keyword integration
                   - Structured with headers
                   - Include episode highlights
                   - Links to resources mentioned
                   - Guest bio and links
                   - Timestamp links to chapters

                4. Tags and Categories
                   - Relevant topic tags (10-15)
                   - Platform categories
                   - Keyword phrases

                5. Social Media Descriptions
                   - Twitter/X (280 chars)
                   - LinkedIn (150 words)
                   - Instagram caption (125 words)

                SEO Best Practices:
                - Use keywords naturally
                - Front-load important information
                - Include internal links
                - Optimize for voice search
                - Consider question-based queries
                - Add structured data hints

                Create comprehensive, search-optimized content package.
            """),
            agent=agent,
            expected_output='Complete SEO package with optimized title, description, show notes, '
                          'tags, and platform-specific content',
            context=[]
        )

    def synthesize_episode_package(self, agent, episode_info: dict = None) -> Task:
        """
        Task: Synthesize all elements into complete episode package
        """
        return Task(
            description=dedent(f"""
                Synthesize all transcript analysis elements into a comprehensive episode package:

                Episode: {episode_info.get('title', 'N/A') if episode_info else 'N/A'}

                Compile and organize:

                1. Episode Overview
                   - Title and description
                   - Guest information
                   - Episode metadata
                   - Duration and format

                2. Content Summary
                   - Multi-level summaries
                   - Key themes and topics
                   - Main takeaways

                3. Navigation Aids
                   - Chapter markers with timestamps
                   - Topic index
                   - Highlight reel suggestions

                4. Promotional Assets
                   - Quotable soundbites
                   - Social media snippets
                   - Email newsletter content
                   - Blog post outline

                5. SEO and Discovery
                   - Optimized metadata
                   - Show notes
                   - Tags and categories
                   - Search keywords

                6. Resources and Links
                   - Mentioned resources
                   - Guest links
                   - Related episodes
                   - Call-to-action links

                7. Production Notes
                   - Audio quality observations
                   - Edit suggestions
                   - Content warnings (if any)

                Create a professional, ready-to-publish episode package.
            """),
            agent=agent,
            expected_output='Complete episode package with all assets, metadata, and content '
                          'ready for publication across platforms',
            context=[]
        )
