#!/usr/bin/env python3
"""
Validate batches in MASS_UPGRADE_ANALYSIS.json to identify which contain
CrewAI built-in tools vs actual Streamlit apps requiring upgrade.
"""

import json
import sys
from collections import defaultdict

def validate_batches(filename):
    """Analyze batches and identify problematic ones."""

    with open(filename, 'r') as f:
        data = json.load(f)

    total_apps = data.get('total_apps', 0)
    batches = data.get('batches', [])

    print(f"Total apps in dataset: {total_apps}")
    print(f"Total batches: {len(batches)}\n")
    print("=" * 80)

    # Track statistics
    crewai_tools_count = 0
    crewai_examples_count = 0
    unique_repos_count = 0
    unique_repos = set()
    problematic_batches = []

    for batch in batches:
        batch_num = batch['batch_number']
        apps = batch.get('apps', [])

        # Analyze this batch
        repo_counts = defaultdict(int)
        crewai_tools_in_batch = 0
        crewai_examples_in_batch = 0

        for app in apps:
            github_url = app.get('github_url', '')
            repo_counts[github_url] += 1
            unique_repos.add(github_url)

            if 'crewAIInc/crewAI-tools' in github_url:
                crewai_tools_in_batch += 1
                crewai_tools_count += 1
            elif 'crewAIInc/crewAI-examples' in github_url:
                crewai_examples_in_batch += 1
                crewai_examples_count += 1

        total_in_batch = len(apps)

        # Check if batch is problematic
        is_problematic = False
        issue_type = None

        if crewai_tools_in_batch == total_in_batch:
            is_problematic = True
            issue_type = "ALL_CREWAI_TOOLS"
        elif crewai_tools_in_batch > 0:
            is_problematic = True
            issue_type = "MIXED_WITH_TOOLS"
        elif len(repo_counts) == 1:
            is_problematic = True
            issue_type = "SINGLE_REPO"

        # Print batch info
        print(f"Batch {batch_num}:")
        print(f"  Total apps: {total_in_batch}")
        print(f"  CrewAI tools: {crewai_tools_in_batch}")
        print(f"  CrewAI examples: {crewai_examples_in_batch}")
        print(f"  Unique repos: {len(repo_counts)}")

        if is_problematic:
            print(f"  STATUS: PROBLEMATIC ({issue_type})")
            problematic_batches.append({
                'batch': batch_num,
                'issue': issue_type,
                'total_apps': total_in_batch,
                'crewai_tools': crewai_tools_in_batch
            })
        else:
            print(f"  STATUS: OK")

        # Show top repositories
        if len(repo_counts) <= 3:
            print("  Repositories:")
            for repo, count in repo_counts.items():
                short_repo = repo.replace('https://github.com/', '')
                print(f"    - {short_repo}: {count} apps")

        print()

    # Summary
    print("=" * 80)
    print("\nSUMMARY:")
    print(f"Total unique repositories: {len(unique_repos)}")
    print(f"Apps pointing to crewAI-tools: {crewai_tools_count}")
    print(f"Apps pointing to crewAI-examples: {crewai_examples_count}")
    print(f"Problematic batches: {len(problematic_batches)}")

    if problematic_batches:
        print("\nPROBLEMATIC BATCHES DETAIL:")
        for item in problematic_batches:
            print(f"  Batch {item['batch']}: {item['issue']} "
                  f"({item['crewai_tools']}/{item['total_apps']} are tools)")

    # Pattern analysis
    print("\nPATTERN ANALYSIS:")
    pattern_counts = data.get('pattern_counts', {})
    for pattern, count in pattern_counts.items():
        print(f"  {pattern}: {count} apps")

    return {
        'total_batches': len(batches),
        'problematic_batches': problematic_batches,
        'crewai_tools_count': crewai_tools_count,
        'unique_repos': len(unique_repos)
    }

if __name__ == '__main__':
    filename = '/Users/colinlowenberg/crew/MASS_UPGRADE_ANALYSIS.json'
    results = validate_batches(filename)

    # Write results
    output_file = '/Users/colinlowenberg/crew/BATCH_VALIDATION_RESULTS.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults written to: {output_file}")
