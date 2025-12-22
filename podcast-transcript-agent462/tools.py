"""
Custom Tools for Podcast Transcript Processing
Provides specialized tools for transcript analysis and processing
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import re
from collections import Counter


class FillerWordRemoverInput(BaseModel):
    """Input schema for FillerWordRemoverTool"""
    text: str = Field(..., description="Text to clean of filler words")


class FillerWordRemoverTool(BaseTool):
    name: str = "Filler Word Remover"
    description: str = """Removes common filler words and verbal tics from transcript text
    while preserving meaning and natural flow."""
    args_schema: Type[BaseModel] = FillerWordRemoverInput

    def _run(self, text: str) -> str:
        """Remove filler words from text"""
        filler_words = [
            r'\bum+\b', r'\buh+\b', r'\blike\b', r'\byou know\b', r'\bi mean\b',
            r'\bso+\b', r'\bactually\b', r'\bbasically\b', r'\bliterally\b',
            r'\bokay\b', r'\bright\b', r'\byeah\b', r'\byep\b', r'\bmhm\b',
            r'\bkind of\b', r'\bsort of\b'
        ]

        cleaned = text
        for filler in filler_words:
            cleaned = re.sub(filler, '', cleaned, flags=re.IGNORECASE)

        # Clean up extra spaces
        cleaned = re.sub(r'\s+', ' ', cleaned)
        cleaned = re.sub(r'\s+([.,!?])', r'\1', cleaned)

        return cleaned.strip()


class TimestampParserInput(BaseModel):
    """Input schema for TimestampParserTool"""
    transcript: str = Field(..., description="Transcript text with timestamps")


class TimestampParserTool(BaseTool):
    name: str = "Timestamp Parser"
    description: str = """Parses timestamps from transcript text and creates structured
    chapter markers."""
    args_schema: Type[BaseModel] = TimestampParserInput

    def _run(self, transcript: str) -> str:
        """Parse timestamps from transcript"""
        # Match common timestamp formats: [00:00:00], (00:00), 00:00:00, etc.
        timestamp_pattern = r'[\[\(]?(\d{1,2}:\d{2}(?::\d{2})?)[\]\)]?'

        timestamps = re.findall(timestamp_pattern, transcript)

        if not timestamps:
            return "No timestamps found in transcript"

        output = "Extracted Timestamps:\n" + "="*50 + "\n"
        for i, ts in enumerate(timestamps[:20], 1):  # Limit to 20
            output += f"{i}. {ts}\n"

        return output


class SpeakerDiarizationInput(BaseModel):
    """Input schema for SpeakerDiarizationTool"""
    transcript: str = Field(..., description="Transcript text")
    speakers: list = Field(default=[], description="List of speaker names")


class SpeakerDiarizationTool(BaseTool):
    name: str = "Speaker Diarization"
    description: str = """Identifies and labels different speakers in transcript text."""
    args_schema: Type[BaseModel] = SpeakerDiarizationInput

    def _run(self, transcript: str, speakers: list = None) -> str:
        """Identify speaker segments"""
        if not speakers:
            speakers = ["Speaker 1", "Speaker 2"]

        # Look for speaker patterns: "Speaker:" or "Speaker 1:" or "[Speaker]"
        speaker_pattern = r'^([A-Z][^:]+):\s*(.+)$'

        lines = transcript.split('\n')
        formatted = []

        for line in lines:
            match = re.match(speaker_pattern, line.strip())
            if match:
                speaker, text = match.groups()
                formatted.append(f"\n**{speaker}**: {text}")
            else:
                formatted.append(line)

        return '\n'.join(formatted)


class KeywordExtractorInput(BaseModel):
    """Input schema for KeywordExtractorTool"""
    text: str = Field(..., description="Text to extract keywords from")
    top_n: int = Field(default=15, description="Number of top keywords to extract")


class KeywordExtractorTool(BaseTool):
    name: str = "Keyword Extractor"
    description: str = """Extracts the most frequently mentioned keywords and phrases
    from transcript for SEO and tagging."""
    args_schema: Type[BaseModel] = KeywordExtractorInput

    def _run(self, text: str, top_n: int = 15) -> str:
        """Extract top keywords from text"""
        # Remove common stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
            'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
            'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these',
            'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which',
            'who', 'when', 'where', 'why', 'how', 'all', 'each', 'every', 'both',
            'few', 'more', 'most', 'other', 'some', 'such', 'than', 'too', 'very'
        }

        # Tokenize and clean
        words = re.findall(r'\b[a-z]{3,}\b', text.lower())
        words = [w for w in words if w not in stop_words]

        # Count frequency
        word_freq = Counter(words)
        top_keywords = word_freq.most_common(top_n)

        output = f"Top {top_n} Keywords:\n" + "="*50 + "\n"
        for i, (word, count) in enumerate(top_keywords, 1):
            output += f"{i}. {word} ({count} mentions)\n"

        return output


class ReadabilityAnalyzerInput(BaseModel):
    """Input schema for ReadabilityAnalyzerTool"""
    text: str = Field(..., description="Text to analyze for readability")


class ReadabilityAnalyzerTool(BaseTool):
    name: str = "Readability Analyzer"
    description: str = """Analyzes transcript readability and provides metrics like
    average sentence length, word complexity, and reading level."""
    args_schema: Type[BaseModel] = ReadabilityAnalyzerInput

    def _run(self, text: str) -> str:
        """Analyze text readability"""
        # Basic metrics
        words = re.findall(r'\b\w+\b', text)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s for s in sentences if s.strip()]

        word_count = len(words)
        sentence_count = len(sentences)
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0

        # Character count
        char_count = len(text)
        avg_word_length = sum(len(w) for w in words) / word_count if word_count > 0 else 0

        # Complex words (3+ syllables, simplified check)
        complex_words = [w for w in words if len(w) > 8]
        complex_word_ratio = len(complex_words) / word_count if word_count > 0 else 0

        output = f"""
Readability Analysis:
{'='*50}

Basic Metrics:
- Total Words: {word_count}
- Total Sentences: {sentence_count}
- Total Characters: {char_count}

Averages:
- Average Sentence Length: {avg_sentence_length:.1f} words
- Average Word Length: {avg_word_length:.1f} characters

Complexity:
- Complex Words: {len(complex_words)} ({complex_word_ratio*100:.1f}%)

Recommendations:
"""

        recommendations = []
        if avg_sentence_length > 20:
            recommendations.append("- Sentences are lengthy. Consider breaking into shorter segments.")
        if avg_sentence_length < 10:
            recommendations.append("- Sentences are very short. May sound choppy when read.")
        if complex_word_ratio > 0.15:
            recommendations.append("- High use of complex words. Simplify for better accessibility.")

        if not recommendations:
            recommendations.append("- Readability is good!")

        output += '\n'.join(recommendations)

        return output
