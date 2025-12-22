# Image Scoring Agent - CrewAI Implementation

An intelligent image evaluation system powered by CrewAI that analyzes and scores images based on technical quality, aesthetic appeal, and content relevance.

## Overview

This CrewAI implementation provides comprehensive image scoring using a team of specialized agents that evaluate technical quality, aesthetic merit, and content classification to deliver detailed scoring reports.

## Agents

1. **Image Analysis Expert**: Evaluates technical quality (sharpness, exposure, color balance)
2. **Aesthetic Quality Evaluator**: Assesses composition, color harmony, and artistic merit
3. **Content Classification Specialist**: Identifies subjects, scenes, and content relevance
4. **Image Scoring Coordinator**: Compiles comprehensive scores and generates reports

## Features

- Technical quality analysis (sharpness, exposure, color)
- Aesthetic evaluation (composition, harmony, creativity)
- Content classification and object detection
- Customizable scoring criteria
- Batch processing support
- Detailed scoring reports with recommendations
- Multiple use case profiles (product, art, stock photo, etc.)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Required API keys:
- OpenAI API key (GPT-4 Vision recommended)
- Optional: Google Cloud Vision or AWS Rekognition for advanced analysis

## Usage

### Score a Single Image

```bash
python main.py /path/to/image.jpg general
```

### Batch Score Multiple Images

```bash
python main.py --batch /path/to/image/directory product
```

### Programmatic Usage

```python
from main import score_image

result = score_image('image.jpg', criteria='art')
print(result)
```

## Scoring Criteria

Available criteria profiles:
- `general`: All-purpose image evaluation
- `product`: Product photography standards
- `art`: Artistic and creative merit
- `stock_photo`: Stock photography requirements
- `social_media`: Social media optimization

## Scoring Components

### Technical Quality (0-100)
- Sharpness and focus
- Exposure and dynamic range
- Color accuracy
- Noise levels
- Resolution
- Compression artifacts

### Aesthetic Quality (0-100)
- Composition principles
- Color harmony
- Visual balance
- Lighting quality
- Emotional impact
- Creative merit

### Content Relevance (0-100)
- Subject clarity
- Scene classification
- Purpose alignment
- Target audience fit
- Context appropriateness

## Output Format

The system generates comprehensive reports including:
- Overall score (0-100)
- Category breakdowns (Technical, Aesthetic, Content)
- Detailed sub-scores for each criterion
- Strengths and weaknesses
- Improvement recommendations
- Use case suitability assessment

## Customization

Modify these files to customize behavior:
- `agents.py`: Adjust evaluation criteria and agent roles
- `tasks.py`: Modify scoring workflows
- `tools.py`: Add custom analysis tools or integrate vision APIs
- `main.py`: Change scoring logic or criteria profiles

## Advanced Features

### Integration with Vision APIs

For enhanced object detection and scene classification:

1. **Google Cloud Vision API**:
   - Set `GOOGLE_APPLICATION_CREDENTIALS` in .env
   - Uncomment Vision API integration in tools.py

2. **AWS Rekognition**:
   - Set AWS credentials in .env
   - Uncomment Rekognition integration in tools.py

### Custom Scoring Models

Create custom scoring criteria in `tasks.py`:

```python
custom_criteria = {
    'technical_weight': 0.4,
    'aesthetic_weight': 0.4,
    'content_weight': 0.2
}
```

## Example Use Cases

- Product photography quality control
- Stock photo evaluation
- Art competition judging
- Social media content optimization
- Real estate photography assessment
- E-commerce image quality assurance
- Photography portfolio review

## Notes

- Supports common image formats (JPG, PNG, GIF, BMP, WebP)
- Vision API integration enhances accuracy significantly
- Scores are relative to criteria profile
- Batch processing available for multiple images
- Results can be exported to JSON or CSV
