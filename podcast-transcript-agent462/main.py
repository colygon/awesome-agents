"""
Podcast Transcript Analyzer - CrewAI Implementation
Main execution file for processing and analyzing podcast transcripts
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import PodcastTranscriptAgents
from tasks import PodcastTranscriptTasks

load_dotenv()


def analyze_podcast_transcript(
    transcript_text: str,
    episode_info: dict = None,
    speakers: list = None,
    target_keywords: list = None
) -> str:
    """
    Analyze podcast transcript and generate complete episode package

    Args:
        transcript_text: Raw or processed transcript text
        episode_info: Dict with title, guest, date, etc.
        speakers: List of speaker names
        target_keywords: SEO keywords to target

    Returns:
        Complete episode package as string
    """

    print(f"\n{'='*70}")
    print(f"Podcast Transcript Analyzer - CrewAI Edition")
    print(f"{'='*70}\n")

    agents = PodcastTranscriptAgents()
    tasks_factory = PodcastTranscriptTasks()

    # Create agents
    processor = agents.transcript_processor()
    analyzer = agents.content_analyzer()
    summarizer = agents.summarizer()
    timestamper = agents.timestamp_generator()
    quote_extractor = agents.quote_extractor()
    seo_optimizer = agents.seo_optimizer()

    # Create tasks
    process_task = tasks_factory.process_transcript(processor, transcript_text, speakers)
    analyze_task = tasks_factory.analyze_content(analyzer, episode_info)
    analyze_task.context = [process_task]

    summary_task = tasks_factory.create_summaries(summarizer, episode_info)
    summary_task.context = [process_task, analyze_task]

    timestamp_task = tasks_factory.generate_timestamps(timestamper)
    timestamp_task.context = [process_task]

    quote_task = tasks_factory.extract_quotes(quote_extractor, quote_count=10)
    quote_task.context = [process_task]

    seo_task = tasks_factory.optimize_for_seo(seo_optimizer, episode_info, target_keywords)
    seo_task.context = [analyze_task, summary_task]

    synthesis_task = tasks_factory.synthesize_episode_package(seo_optimizer, episode_info)
    synthesis_task.context = [process_task, analyze_task, summary_task,
                              timestamp_task, quote_task, seo_task]

    # Create crew
    crew = Crew(
        agents=[processor, analyzer, summarizer, timestamper, quote_extractor, seo_optimizer],
        tasks=[process_task, analyze_task, summary_task, timestamp_task,
               quote_task, seo_task, synthesis_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result


def main():
    """Example usage"""

    sample_transcript = """
    [00:00:00] Host: Welcome back to the Tech Innovators Podcast. Today we have Sarah Chen,
    CEO of CloudScale AI. Sarah, thanks for joining us.

    [00:00:15] Sarah: Thanks for having me. Excited to be here.

    [00:00:18] Host: So, your company has been making waves in the AI infrastructure space.
    Can you tell us about what you're building?

    [00:00:25] Sarah: Absolutely. We're building the next generation of AI training infrastructure.
    The key insight we had was that current cloud platforms weren't optimized for the unique
    demands of large language model training...
    """

    episode_info = {
        'title': 'Building AI Infrastructure at Scale with Sarah Chen',
        'guest': 'Sarah Chen, CEO of CloudScale AI',
        'date': '2025-01-15',
        'duration': '45 minutes'
    }

    speakers = ['Host', 'Sarah']
    target_keywords = ['AI infrastructure', 'cloud computing', 'machine learning', 'scalability']

    result = analyze_podcast_transcript(
        transcript_text=sample_transcript,
        episode_info=episode_info,
        speakers=speakers,
        target_keywords=target_keywords
    )

    print("\n" + "="*70)
    print("EPISODE PACKAGE")
    print("="*70 + "\n")
    print(result)


if __name__ == "__main__":
    main()
