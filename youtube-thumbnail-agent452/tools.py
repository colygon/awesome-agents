"""
Custom Tools for YouTube Thumbnail Analysis and Design
Provides image analysis, design suggestions, and competitor research
"""

from crewai_tools import BaseTool
from typing import Type, Optional
from pydantic import BaseModel, Field
import os
import requests
from langchain_openai import ChatOpenAI


class ImageAnalysisInput(BaseModel):
    """Input schema for ImageAnalysisTool"""
    image_url: str = Field(..., description="URL of the thumbnail image to analyze")
    analysis_type: str = Field(default="comprehensive", description="Type of analysis: comprehensive, quick, or competitive")


class ImageAnalysisTool(BaseTool):
    name: str = "Thumbnail Image Analyzer"
    description: str = """Analyzes thumbnail images to identify visual elements, design patterns,
    and effectiveness factors. Examines colors, composition, text, faces, and emotional triggers.
    Returns detailed analysis of what makes the thumbnail work or not work."""
    args_schema: Type[BaseModel] = ImageAnalysisInput

    def _run(self, image_url: str, analysis_type: str = "comprehensive") -> str:
        """
        Analyze a thumbnail image

        Args:
            image_url: URL of the image to analyze
            analysis_type: Depth of analysis

        Returns:
            Detailed analysis of the thumbnail
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

            prompt = f"""Analyze this YouTube thumbnail image: {image_url}

Analysis type: {analysis_type}

Provide detailed analysis of:

1. VISUAL ELEMENTS
   - Main subjects (people, objects, text)
   - Composition and layout
   - Use of space and focal points

2. COLOR & CONTRAST
   - Color palette and scheme
   - Contrast levels
   - Visual hierarchy
   - Background vs foreground

3. TEXT ANALYSIS
   - Text content and messaging
   - Font size and readability
   - Text placement and safety zones
   - Mobile readability

4. EMOTIONAL IMPACT
   - Facial expressions (if present)
   - Emotional triggers
   - Curiosity factors
   - Psychological hooks

5. TECHNICAL QUALITY
   - Image quality and resolution
   - Professional appearance
   - Brand consistency
   - Platform compliance

6. EFFECTIVENESS SCORE
   - Predicted click-through potential (1-10)
   - Strengths
   - Weaknesses
   - Improvement opportunities

Provide specific, actionable insights."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error analyzing thumbnail: {str(e)}"


class DesignSuggestionInput(BaseModel):
    """Input schema for DesignSuggestionTool"""
    video_topic: str = Field(..., description="Topic or title of the video")
    style: str = Field(default="engaging", description="Design style: engaging, professional, dramatic, playful")
    include_face: bool = Field(default=True, description="Whether to include a human face")


class DesignSuggestionTool(BaseTool):
    name: str = "Thumbnail Design Generator"
    description: str = """Generates detailed thumbnail design suggestions based on topic and style.
    Creates concepts with specific visual elements, colors, text, and composition recommendations.
    Optimized for YouTube's algorithm and viewer psychology."""
    args_schema: Type[BaseModel] = DesignSuggestionInput

    def _run(self, video_topic: str, style: str = "engaging", include_face: bool = True) -> str:
        """
        Generate thumbnail design suggestions

        Args:
            video_topic: Topic of the video
            style: Design style preference
            include_face: Whether to include a face

        Returns:
            Detailed design suggestions
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

            prompt = f"""Generate a detailed YouTube thumbnail design concept.

Video Topic: {video_topic}
Design Style: {style}
Include Human Face: {include_face}

Create a comprehensive design specification:

1. CONCEPT OVERVIEW
   - Core visual idea
   - Emotional hook
   - Curiosity trigger

2. VISUAL ELEMENTS
   - Main subject/image
   {f"- Facial expression and emotion" if include_face else ""}
   - Supporting visual elements
   - Background elements
   - Props or objects

3. COLOR SCHEME
   - Primary colors (with hex codes)
   - Accent colors
   - Background color/gradient
   - Contrast strategy

4. TEXT OVERLAY
   - Main headline (exact wording, 3-6 words)
   - Font style recommendations
   - Font size (large for mobile)
   - Text placement and positioning
   - Text color and outline/shadow
   - Optional supporting text

5. COMPOSITION
   - Layout structure (rule of thirds, centered, etc.)
   - Focal point placement
   - Visual flow and eye path
   - Negative space usage

6. PSYCHOLOGICAL TRIGGERS
   - What emotion this evokes
   - Curiosity gap creation
   - Social proof elements
   - Urgency or scarcity (if applicable)

7. TECHNICAL SPECS
   - Dimensions: 1280x720px (16:9)
   - File format: JPG or PNG
   - Mobile optimization notes
   - Text safety zones

8. WHY THIS WORKS
   - Psychology behind the design
   - Target audience appeal
   - Competitive differentiation
   - Expected CTR impact

Provide specific, detailed recommendations that can be implemented."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error generating design: {str(e)}"


class CompetitorAnalysisInput(BaseModel):
    """Input schema for CompetitorAnalysisTool"""
    niche: str = Field(..., description="YouTube niche or topic area to analyze")
    num_results: int = Field(default=10, description="Number of thumbnails to analyze")


class CompetitorAnalysisTool(BaseTool):
    name: str = "Competitor Thumbnail Analyzer"
    description: str = """Analyzes competitor thumbnails in a specific niche. Identifies
    patterns, trends, and best practices from successful channels. Returns insights about
    what works in the niche and opportunities for differentiation."""
    args_schema: Type[BaseModel] = CompetitorAnalysisInput

    def _run(self, niche: str, num_results: int = 10) -> str:
        """
        Analyze competitor thumbnails in a niche

        Args:
            niche: YouTube niche to analyze
            num_results: Number of examples to find

        Returns:
            Analysis of competitor thumbnail strategies
        """
        try:
            # Check for search API
            serper_api_key = os.getenv("SERPER_API_KEY")

            if serper_api_key:
                # Search for popular videos in this niche
                url = "https://google.serper.dev/search"
                payload = {
                    "q": f"{niche} site:youtube.com",
                    "num": num_results
                }
                headers = {
                    "X-API-KEY": serper_api_key,
                    "Content-Type": "application/json"
                }

                response = requests.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    results = response.json()

                    # Analyze the results
                    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

                    analysis_prompt = f"""Based on these YouTube videos about {niche},
                    analyze the thumbnail patterns:

{results}

Identify:
1. Common visual patterns
2. Popular color schemes
3. Text styles and messaging
4. Emotional triggers used
5. What differentiates top performers
6. Opportunities for standing out

Provide actionable insights."""

                    analysis = llm.invoke(analysis_prompt)
                    return analysis.content

            # Fallback: Provide general niche insights
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

            prompt = f"""Analyze typical YouTube thumbnail strategies for the niche: {niche}

Based on general knowledge of successful YouTube channels in this niche, provide:

1. COMMON PATTERNS
   - Typical visual elements used
   - Popular color schemes
   - Common composition styles
   - Frequent text strategies

2. TOP PERFORMER STRATEGIES
   - What successful channels do differently
   - Unique visual signatures
   - Emotional triggers that work
   - Innovation in the niche

3. AUDIENCE EXPECTATIONS
   - What viewers expect to see
   - Trust signals required
   - Credibility indicators
   - Engagement triggers

4. TRENDS & EVOLUTION
   - How thumbnails in this niche have evolved
   - Current trending styles
   - Emerging patterns
   - Declining tropes to avoid

5. DIFFERENTIATION OPPORTUNITIES
   - Gaps in current thumbnail strategies
   - Underused but effective approaches
   - Ways to stand out
   - Innovation possibilities

6. PLATFORM-SPECIFIC CONSIDERATIONS
   - How this niche performs on YouTube
   - Algorithm considerations
   - Mobile vs desktop optimization
   - Accessibility needs

Provide specific, actionable insights for {niche} thumbnails."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error analyzing competitors: {str(e)}"
