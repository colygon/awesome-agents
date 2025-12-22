#!/usr/bin/env python3
"""
Rapid analysis of all 179 remaining Streamlit apps in the gallery.
Categorizes them by upgrade pattern and complexity.
"""

import sqlite3
import json
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Connect to gallery database
db_path = "/Users/colinlowenberg/crew/streamlit-gallery-clone/apps.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all apps that don't have CrewAI yet
cursor.execute("""
    SELECT id, title, github_url, description, tags, category
    FROM apps
    WHERE has_crewai = 0 OR has_crewai IS NULL
    ORDER BY views DESC, watchers DESC
""")

apps = cursor.fetchall()
print(f"Found {len(apps)} apps to upgrade\n")

# Define upgrade patterns based on our successful agents
UPGRADE_PATTERNS = {
    "rag_replacement": {
        "keywords": ["pdf", "document", "chat", "qa", "question", "answer", "langchain", "embeddings", "vector"],
        "description": "Document Q&A apps - replace LangChain with CrewAI",
        "agents_needed": 3,
        "effort": "medium",
        "example": "talk-with-pdf, knowledge-gpt"
    },
    "dual_mode": {
        "keywords": ["generate", "create", "write", "email", "content", "text"],
        "description": "Content generation - add CrewAI version alongside original",
        "agents_needed": 3,
        "effort": "medium",
        "example": "email-generator"
    },
    "optional_insights": {
        "keywords": ["dashboard", "analytics", "visualization", "chart", "data", "leaderboard", "comparison"],
        "description": "Analytics/viz apps - add optional CrewAI insights",
        "agents_needed": 3,
        "effort": "low",
        "example": "llm-leaderboard"
    },
    "tool_integration": {
        "keywords": ["api", "scrape", "fetch", "search", "tool", "integration"],
        "description": "Tool-based apps - use CrewAI tools",
        "agents_needed": 2,
        "effort": "low",
        "example": "Use CrewAI's built-in tools"
    },
    "workflow_enhancement": {
        "keywords": ["workflow", "automation", "pipeline", "process"],
        "description": "Workflow apps - add CrewAI flows",
        "agents_needed": 3,
        "effort": "medium",
        "example": "Multi-step automation"
    },
    "simple_enhancement": {
        "keywords": [],  # Catch-all for simple apps
        "description": "Simple apps - add basic CrewAI feature",
        "agents_needed": 2,
        "effort": "low",
        "example": "Add AI insights or recommendations"
    }
}

def categorize_app(app_data):
    """Categorize an app by its upgrade pattern."""
    app_id, title, github_url, description, tags, category = app_data

    # Combine searchable text
    searchable = f"{title} {description} {tags or ''} {category or ''}".lower()

    # Score each pattern
    scores = {}
    for pattern_name, pattern in UPGRADE_PATTERNS.items():
        score = sum(1 for keyword in pattern["keywords"] if keyword in searchable)
        scores[pattern_name] = score

    # Pick highest scoring pattern (or simple_enhancement as default)
    best_pattern = max(scores.items(), key=lambda x: x[1])
    pattern_name = best_pattern[0] if best_pattern[1] > 0 else "simple_enhancement"

    return {
        "id": app_id,
        "title": title,
        "github_url": github_url,
        "description": description[:100] + "..." if description else "",
        "pattern": pattern_name,
        "pattern_info": UPGRADE_PATTERNS[pattern_name],
        "estimated_hours": {
            "low": 0.5,
            "medium": 1.5,
            "high": 3.0
        }[UPGRADE_PATTERNS[pattern_name]["effort"]]
    }

# Analyze all apps in parallel
print("Analyzing apps...")
categorized_apps = []
with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(categorize_app, app) for app in apps]
    for i, future in enumerate(as_completed(futures), 1):
        result = future.result()
        categorized_apps.append(result)
        if i % 10 == 0:
            print(f"  Analyzed {i}/{len(apps)} apps...")

# Sort by pattern and effort
categorized_apps.sort(key=lambda x: (x["pattern"], x["estimated_hours"]))

# Generate statistics
pattern_counts = {}
total_hours = 0
for app in categorized_apps:
    pattern = app["pattern"]
    pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
    total_hours += app["estimated_hours"]

# Output results
print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
print(f"\nTotal apps to upgrade: {len(categorized_apps)}")
print(f"Estimated total hours (sequential): {total_hours:.1f} hours")
print(f"Estimated time (20 parallel agents): {total_hours/20:.1f} hours")
print(f"\nBreakdown by pattern:")
for pattern, count in sorted(pattern_counts.items(), key=lambda x: -x[1]):
    pattern_info = UPGRADE_PATTERNS[pattern]
    print(f"  {pattern:25s}: {count:3d} apps ({pattern_info['effort']:6s} effort) - {pattern_info['description']}")

# Create batches for parallel execution
BATCH_SIZE = 20  # Process 20 apps at a time
batches = []
for i in range(0, len(categorized_apps), BATCH_SIZE):
    batch = categorized_apps[i:i+BATCH_SIZE]
    batches.append({
        "batch_number": len(batches) + 1,
        "apps": batch,
        "estimated_hours": sum(app["estimated_hours"] for app in batch)
    })

print(f"\n" + "="*80)
print(f"EXECUTION PLAN: {len(batches)} batches of {BATCH_SIZE} apps each")
print("="*80)
for i, batch in enumerate(batches[:5], 1):  # Show first 5 batches
    print(f"\nBatch {i}: {len(batch['apps'])} apps (~{batch['estimated_hours']:.1f} hours if sequential, ~{batch['estimated_hours']/20:.1f} hours parallel)")
    for app in batch['apps'][:3]:  # Show first 3 apps in batch
        print(f"  - {app['title'][:50]:50s} [{app['pattern']}]")
    if len(batch['apps']) > 3:
        print(f"  ... and {len(batch['apps']) - 3} more apps")

if len(batches) > 5:
    print(f"\n... and {len(batches) - 5} more batches")

# Save detailed analysis
output_path = "/Users/colinlowenberg/crew/MASS_UPGRADE_ANALYSIS.json"
with open(output_path, 'w') as f:
    json.dump({
        "total_apps": len(categorized_apps),
        "total_hours_sequential": total_hours,
        "total_hours_parallel": total_hours / 20,
        "pattern_counts": pattern_counts,
        "batches": batches,
        "apps": categorized_apps
    }, f, indent=2)

print(f"\n✅ Detailed analysis saved to: {output_path}")
print("\n" + "="*80)
print("NEXT STEP: Run parallel batch execution")
print("="*80)
print(f"\nCommand to start batch 1:")
print(f"  python3 /Users/colinlowenberg/crew/execute_batch.py 1")
print(f"\nOr to run ALL batches in parallel:")
print(f"  python3 /Users/colinlowenberg/crew/execute_all_batches.py")

conn.close()
