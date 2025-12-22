#!/usr/bin/env python
from crewai import Crew, Process
from agents import ImageScoringAgents
from tasks import ImageScoringTasks
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def score_image(image_path: str, criteria: str = "general"):
    """
    Score an image using a team of specialized agents.

    Args:
        image_path: Path to the image file
        criteria: Scoring criteria (e.g., 'general', 'product', 'art', 'stock_photo')
    """
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return None

    print(f"\n{'='*60}")
    print(f"Scoring Image: {os.path.basename(image_path)}")
    print(f"Criteria: {criteria}")
    print(f"{'='*60}\n")

    # Initialize agents and tasks
    agents = ImageScoringAgents()
    tasks = ImageScoringTasks()

    # Create agents
    image_analyzer = agents.image_analyzer()
    aesthetic_evaluator = agents.aesthetic_evaluator()
    content_classifier = agents.content_classifier()
    scoring_coordinator = agents.scoring_coordinator()

    # Create tasks
    technical_task = tasks.analyze_technical_quality(
        agent=image_analyzer,
        image_path=image_path
    )

    aesthetic_task = tasks.evaluate_aesthetics(
        agent=aesthetic_evaluator,
        image_path=image_path
    )

    content_task = tasks.classify_content(
        agent=content_classifier,
        image_path=image_path
    )

    final_score_task = tasks.calculate_final_score(
        agent=scoring_coordinator,
        technical_analysis="Technical analysis results",
        aesthetic_evaluation="Aesthetic evaluation results",
        content_classification="Content classification results",
        criteria=criteria
    )

    # Create crew
    crew = Crew(
        agents=[
            image_analyzer,
            aesthetic_evaluator,
            content_classifier,
            scoring_coordinator
        ],
        tasks=[
            technical_task,
            aesthetic_task,
            content_task,
            final_score_task
        ],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print(f"\n{'='*60}")
    print("Image Scoring Complete!")
    print(f"{'='*60}\n")
    print(result)

    return result

def score_batch(image_directory: str, criteria: str = "general"):
    """
    Score multiple images in a directory.
    """
    if not os.path.exists(image_directory):
        print(f"Error: Directory not found at {image_directory}")
        return None

    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    image_files = [
        f for f in os.listdir(image_directory)
        if os.path.splitext(f)[1].lower() in image_extensions
    ]

    if not image_files:
        print(f"No image files found in {image_directory}")
        return None

    results = {}
    for image_file in image_files:
        image_path = os.path.join(image_directory, image_file)
        print(f"\nProcessing: {image_file}")
        result = score_image(image_path, criteria)
        results[image_file] = result

    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single image: python main.py <image_path> [criteria]")
        print("  Batch mode:   python main.py --batch <directory_path> [criteria]")
        print("\nCriteria options: general, product, art, stock_photo, social_media")
        sys.exit(1)

    if sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("Error: Directory path required for batch mode")
            sys.exit(1)
        directory = sys.argv[2]
        criteria = sys.argv[3] if len(sys.argv) > 3 else "general"
        score_batch(directory, criteria)
    else:
        image_path = sys.argv[1]
        criteria = sys.argv[2] if len(sys.argv) > 2 else "general"
        score_image(image_path, criteria)
