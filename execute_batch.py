#!/usr/bin/env python3
"""
Execute a single batch of apps using parallel CrewAI agents.
Each batch processes ~20 apps in parallel.

Usage: python3 execute_batch.py <batch_number>
"""

import sys
import json
import os
from pathlib import Path

# Get batch number from command line
if len(sys.argv) < 2:
    print("Usage: python3 execute_batch.py <batch_number>")
    sys.exit(1)

batch_num = int(sys.argv[1])

# Load analysis
analysis_path = "/Users/colinlowenberg/crew/MASS_UPGRADE_ANALYSIS.json"
with open(analysis_path, 'r') as f:
    analysis = json.load(f)

if batch_num < 1 or batch_num > len(analysis["batches"]):
    print(f"Error: Batch {batch_num} not found. Valid range: 1-{len(analysis['batches'])}")
    sys.exit(1)

batch = analysis["batches"][batch_num - 1]
apps = batch["apps"]

print(f"="*80)
print(f"BATCH {batch_num}: Processing {len(apps)} apps")
print(f"="*80)
print(f"Estimated time: {batch['estimated_hours']:.1f} hours sequential, {batch['estimated_hours']/20:.1f} hours parallel")
print()

# Create upgrade tasks for each app
upgrade_tasks = []
for app in apps:
    task = {
        "app_id": app["id"],
        "title": app["title"],
        "github_url": app["github_url"],
        "pattern": app["pattern"],
        "pattern_info": app["pattern_info"],
        "agent_prompt": f"""
Upgrade the Streamlit app "{app['title']}" to support CrewAI.

**App Details:**
- Title: {app['title']}
- GitHub: {app['github_url']}
- Description: {app['description']}

**Upgrade Pattern: {app['pattern']}**
{app['pattern_info']['description']}

**Instructions:**
1. Fork the repository to colygon/{app['github_url'].split('/')[-1]}
2. Clone it to /Users/colinlowenberg/crew/{app['title'].lower().replace(' ', '-')}-agent{app['id']}/
3. Implement {app['pattern_info']['agents_needed']} CrewAI agents
4. Create comprehensive documentation (COMPLETION_REPORT.md, CREWAI_UPGRADE.md)
5. Update requirements.txt with crewai>=0.86.0
6. Ensure backward compatibility (original functionality preserved)
7. Create git commit with proper attribution
8. Update gallery database: UPDATE apps SET has_crewai = 1 WHERE id = {app['id']};

**Reference Example:** {app['pattern_info']['example']}

**Deliverables:**
- Working CrewAI implementation
- Documentation files
- Git commit
- Updated gallery database
"""
    }
    upgrade_tasks.append(task)

# NOW: Instead of actually running agents (which would require Task tool),
# let's generate the execution plan for the user to run

print("EXECUTION PLAN:")
print("="*80)
print()
print("To execute this batch, you can:")
print()
print("Option 1: Use Claude Code Task tool to spawn agents in parallel")
print("Option 2: Run each app upgrade individually")
print("Option 3: Use CrewAI Flows to automate the entire batch")
print()
print("="*80)
print("APPS IN THIS BATCH:")
print("="*80)

for i, app in enumerate(apps, 1):
    print(f"\n{i}. {app['title']}")
    print(f"   Pattern: {app['pattern']}")
    print(f"   GitHub: {app['github_url']}")
    print(f"   Effort: {app['estimated_hours']:.1f} hours")
    print(f"   Agents: {app['pattern_info']['agents_needed']}")

print("\n" + "="*80)
print(f"Total apps in batch: {len(apps)}")
print(f"Total effort: {batch['estimated_hours']:.1f} hours sequential")
print(f"Parallel time: ~{batch['estimated_hours']/20:.1f} hours (with 20 parallel agents)")
print("="*80)

# Save batch execution file
batch_file = f"/Users/colinlowenberg/crew/BATCH_{batch_num}_APPS.json"
with open(batch_file, 'w') as f:
    json.dump({
        "batch_number": batch_num,
        "apps": apps,
        "tasks": upgrade_tasks
    }, f, indent=2)

print(f"\n✅ Batch configuration saved to: {batch_file}")
print(f"\nTo execute, run:")
print(f"  # Spawn {len(apps)} parallel agents to upgrade these apps")
