from crewai import Task
from textwrap import dedent

class ImageScoringTasks:
    def analyze_technical_quality(self, agent, image_path):
        return Task(
            description=dedent(f"""\
                Analyze the technical quality of the image:
                Image Path: {image_path}

                Evaluate the following technical aspects:
                1. Sharpness and focus quality
                2. Exposure (brightness, highlights, shadows)
                3. Color accuracy and white balance
                4. Noise and grain levels
                5. Resolution and clarity
                6. Compression artifacts
                7. Technical metadata (ISO, aperture, shutter speed if available)

                Provide detailed scores (0-100) for each technical aspect with explanations."""),
            agent=agent,
            expected_output="Technical quality analysis with scores and detailed explanations for each aspect"
        )

    def evaluate_aesthetics(self, agent, image_path):
        return Task(
            description=dedent(f"""\
                Evaluate the aesthetic quality and artistic merit:
                Image Path: {image_path}

                Assess the following aesthetic elements:
                1. Composition (rule of thirds, symmetry, balance)
                2. Color harmony and palette
                3. Visual interest and focal points
                4. Lighting quality and direction
                5. Depth and dimensionality
                6. Emotional impact
                7. Creative and artistic value

                Provide scores (0-100) for each aesthetic element with detailed reasoning."""),
            agent=agent,
            expected_output="Aesthetic evaluation with scores and detailed reasoning for each element"
        )

    def classify_content(self, agent, image_path):
        return Task(
            description=dedent(f"""\
                Classify and analyze the image content:
                Image Path: {image_path}

                Identify and categorize:
                1. Main subjects and objects
                2. Scene type (landscape, portrait, product, etc.)
                3. Activities or actions depicted
                4. Setting and environment
                5. Mood and atmosphere
                6. Intended purpose or use case
                7. Target audience relevance

                Provide content classification with confidence scores."""),
            agent=agent,
            expected_output="Content classification report with identified subjects, scene type, and relevance scores"
        )

    def calculate_final_score(self, agent, technical_analysis, aesthetic_evaluation, content_classification, criteria):
        return Task(
            description=dedent(f"""\
                Compile all analyses into a comprehensive image score:

                Technical Analysis: {technical_analysis}
                Aesthetic Evaluation: {aesthetic_evaluation}
                Content Classification: {content_classification}
                Scoring Criteria: {criteria}

                Generate a final comprehensive report including:
                1. Overall Score (0-100)
                2. Category Breakdowns:
                   - Technical Quality Score
                   - Aesthetic Score
                   - Content Relevance Score
                3. Strengths and Weaknesses
                4. Detailed scoring breakdown by criteria
                5. Recommendations for improvement
                6. Comparison to scoring criteria/standards
                7. Use case suitability assessment

                Apply appropriate weighting based on the scoring criteria."""),
            agent=agent,
            expected_output="Comprehensive scoring report with overall score, category breakdowns, and detailed recommendations"
        )
