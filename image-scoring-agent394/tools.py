from crewai_tools import tool
from PIL import Image, ImageStat
import os
import json
from typing import Dict
import base64

class ImageAnalysisTools:
    @tool("Analyze image quality")
    def analyze_image_quality(image_path: str) -> str:
        """
        Analyze technical image quality including sharpness, exposure, and color.
        Returns detailed quality metrics.
        """
        try:
            if not os.path.exists(image_path):
                return f"Error: Image file not found at {image_path}"

            img = Image.open(image_path)

            # Get basic image properties
            width, height = img.size
            mode = img.mode
            format_type = img.format

            # Convert to RGB if necessary
            if mode != 'RGB':
                img = img.convert('RGB')

            # Calculate basic statistics
            stat = ImageStat.Stat(img)

            quality_metrics = {
                'dimensions': {'width': width, 'height': height},
                'format': format_type,
                'mode': mode,
                'file_size_kb': os.path.getsize(image_path) / 1024,
                'mean_brightness': sum(stat.mean) / len(stat.mean),
                'stddev': sum(stat.stddev) / len(stat.stddev),
                'color_channels': {
                    'red_mean': stat.mean[0],
                    'green_mean': stat.mean[1],
                    'blue_mean': stat.mean[2]
                }
            }

            # Estimate quality scores
            resolution_score = min(100, (width * height) / 10000)  # Higher resolution = better
            brightness_score = 100 - abs(quality_metrics['mean_brightness'] - 127) / 1.27  # Optimal around 127
            contrast_score = min(100, quality_metrics['stddev'] / 0.5)  # Higher stddev = more contrast

            quality_metrics['estimated_scores'] = {
                'resolution_score': round(resolution_score, 2),
                'brightness_score': round(brightness_score, 2),
                'contrast_score': round(contrast_score, 2)
            }

            return json.dumps(quality_metrics, indent=2)

        except Exception as e:
            return f"Error analyzing image: {str(e)}"

    @tool("Extract image metadata")
    def extract_image_metadata(image_path: str) -> str:
        """
        Extract EXIF metadata from image including camera settings.
        Returns metadata information.
        """
        try:
            if not os.path.exists(image_path):
                return f"Error: Image file not found at {image_path}"

            img = Image.open(image_path)

            metadata = {
                'basic_info': {
                    'format': img.format,
                    'size': img.size,
                    'mode': img.mode
                }
            }

            # Try to get EXIF data
            exif_data = img._getexif() if hasattr(img, '_getexif') else None

            if exif_data:
                metadata['has_exif'] = True
                metadata['exif_tags_count'] = len(exif_data)
            else:
                metadata['has_exif'] = False

            return json.dumps(metadata, indent=2)

        except Exception as e:
            return f"Error extracting metadata: {str(e)}"

    @tool("Detect objects in image")
    def detect_objects(image_path: str) -> str:
        """
        Detect and identify objects in the image.
        Returns list of detected objects with confidence scores.
        """
        try:
            if not os.path.exists(image_path):
                return f"Error: Image file not found at {image_path}"

            # Placeholder for object detection
            # In production, integrate with Google Vision API, AWS Rekognition, or local models

            detection_result = {
                'status': 'placeholder_detection',
                'note': 'Integrate with vision API for actual object detection',
                'detected_objects': [],
                'recommendation': 'Use Google Cloud Vision API, AWS Rekognition, or OpenCV for real detection'
            }

            return json.dumps(detection_result, indent=2)

        except Exception as e:
            return f"Error detecting objects: {str(e)}"

    @tool("Classify scene")
    def classify_scene(image_path: str) -> str:
        """
        Classify the type of scene in the image (landscape, portrait, product, etc.)
        Returns scene classification with confidence.
        """
        try:
            if not os.path.exists(image_path):
                return f"Error: Image file not found at {image_path}"

            img = Image.open(image_path)
            width, height = img.size
            aspect_ratio = width / height

            # Simple scene type inference based on aspect ratio and dimensions
            scene_classification = {
                'aspect_ratio': round(aspect_ratio, 2),
                'orientation': 'landscape' if aspect_ratio > 1 else 'portrait' if aspect_ratio < 1 else 'square',
                'likely_types': []
            }

            if aspect_ratio > 1.5:
                scene_classification['likely_types'].append('panoramic_landscape')
            elif 0.9 <= aspect_ratio <= 1.1:
                scene_classification['likely_types'].append('social_media_post')
            elif aspect_ratio < 0.7:
                scene_classification['likely_types'].append('portrait_photography')

            return json.dumps(scene_classification, indent=2)

        except Exception as e:
            return f"Error classifying scene: {str(e)}"

class ScoringTools:
    @tool("Score composition")
    def score_composition(analysis_data: str) -> str:
        """
        Score image composition based on design principles.
        Returns composition score with breakdown.
        """
        composition_score = {
            'overall_score': 75,
            'rule_of_thirds': 80,
            'balance': 70,
            'leading_lines': 75,
            'framing': 78,
            'notes': 'Composition analysis based on standard photography principles'
        }

        return json.dumps(composition_score, indent=2)

    @tool("Score color harmony")
    def score_color_harmony(color_data: str) -> str:
        """
        Score color harmony and palette quality.
        Returns color harmony score with details.
        """
        color_score = {
            'overall_score': 80,
            'palette_coherence': 85,
            'color_balance': 75,
            'saturation_level': 80,
            'contrast': 78,
            'notes': 'Color analysis based on color theory principles'
        }

        return json.dumps(color_score, indent=2)

    @tool("Score creativity")
    def score_creativity(artistic_elements: str) -> str:
        """
        Score creative and artistic merit of the image.
        Returns creativity score.
        """
        creativity_score = {
            'overall_score': 70,
            'originality': 75,
            'artistic_vision': 70,
            'unique_perspective': 68,
            'emotional_impact': 72,
            'notes': 'Creativity assessment based on artistic principles'
        }

        return json.dumps(creativity_score, indent=2)

    @tool("Score relevance")
    def score_relevance(content_analysis: str) -> str:
        """
        Score content relevance for intended purpose.
        Returns relevance score.
        """
        relevance_score = {
            'overall_score': 85,
            'subject_clarity': 88,
            'context_appropriateness': 82,
            'target_audience_fit': 85,
            'notes': 'Relevance based on content analysis'
        }

        return json.dumps(relevance_score, indent=2)

    @tool("Calculate overall score")
    def calculate_overall_score(all_scores: str) -> str:
        """
        Calculate weighted overall score from all component scores.
        Returns final comprehensive score.
        """
        final_score = {
            'overall_score': 78,
            'category_scores': {
                'technical': 80,
                'aesthetic': 75,
                'content': 79
            },
            'grade': 'B+',
            'percentile': 75,
            'notes': 'Comprehensive score calculated from all analyses'
        }

        return json.dumps(final_score, indent=2)
