from crewai import Agent
from textwrap import dedent
from tools import ImageAnalysisTools, ScoringTools

class ImageScoringAgents:
    def image_analyzer(self):
        return Agent(
            role='Image Analysis Expert',
            goal='Analyze images for technical quality, composition, and visual elements',
            backstory=dedent("""\
                You are an expert in image analysis with deep knowledge of
                photography, composition, and visual design. You can evaluate
                technical aspects like exposure, focus, color balance, and
                composition principles. You understand what makes an image
                visually appealing and technically sound."""),
            tools=[
                ImageAnalysisTools.analyze_image_quality,
                ImageAnalysisTools.extract_image_metadata,
                ImageAnalysisTools.detect_objects
            ],
            verbose=True,
            allow_delegation=False
        )

    def aesthetic_evaluator(self):
        return Agent(
            role='Aesthetic Quality Evaluator',
            goal='Assess the aesthetic appeal and artistic merit of images',
            backstory=dedent("""\
                You are an art critic and aesthetics expert who understands
                visual appeal, artistic composition, and design principles.
                You can evaluate color harmony, balance, rule of thirds,
                leading lines, and other compositional elements. You appreciate
                both technical excellence and creative expression."""),
            tools=[
                ScoringTools.score_composition,
                ScoringTools.score_color_harmony,
                ScoringTools.score_creativity
            ],
            verbose=True,
            allow_delegation=False
        )

    def content_classifier(self):
        return Agent(
            role='Content Classification Specialist',
            goal='Classify image content and identify key subjects and themes',
            backstory=dedent("""\
                You are an expert in visual content classification and
                understanding. You can identify objects, scenes, activities,
                and themes in images. You understand context and can categorize
                images based on their content, purpose, and subject matter."""),
            tools=[
                ImageAnalysisTools.detect_objects,
                ImageAnalysisTools.classify_scene,
                ScoringTools.score_relevance
            ],
            verbose=True,
            allow_delegation=False
        )

    def scoring_coordinator(self):
        return Agent(
            role='Image Scoring Coordinator',
            goal='Compile comprehensive image scores and generate detailed reports',
            backstory=dedent("""\
                You are an expert in evaluation metrics and scoring systems.
                You can synthesize multiple assessment criteria into a
                comprehensive scoring framework. You understand how to weight
                different factors and present scores in clear, actionable ways."""),
            tools=[ScoringTools.calculate_overall_score],
            verbose=True,
            allow_delegation=False
        )
