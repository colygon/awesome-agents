#!/usr/bin/env python3
"""
HYPER-PARALLEL execution: Run ALL batches simultaneously.
This will spawn multiple Claude Code agents in parallel.

WARNING: This is VERY aggressive. Each batch spawns 20 agents.
If you run 9 batches in parallel, that's 180 concurrent agents!

Recommended: Run 2-3 batches at a time to avoid overwhelming the system.
"""

import json
import subprocess
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load analysis
analysis_path = "/Users/colinlowenberg/crew/MASS_UPGRADE_ANALYSIS.json"
with open(analysis_path, 'r') as f:
    analysis = json.load(f)

batches = analysis["batches"]
print(f"Found {len(batches)} batches to execute")
print(f"Total apps: {analysis['total_apps']}")
print(f"Estimated time (all parallel): {analysis['total_hours_parallel']:.1f} hours")
print("\n" + "="*80)

# Ask user how many batches to run in parallel
print("\nHow aggressive do you want to be?")
print("  1 = Conservative (1 batch at a time, ~20 agents)")
print("  2 = Moderate (2 batches at a time, ~40 agents)")
print("  3 = Aggressive (3 batches at a time, ~60 agents)")
print(f"  {len(batches)} = MAXIMUM (ALL batches, ~{len(batches)*20} agents!)")
print()

try:
    parallel_batches = int(input(f"Enter number of parallel batches (1-{len(batches)}): "))
    parallel_batches = max(1, min(parallel_batches, len(batches)))
except:
    parallel_batches = 2
    print(f"Invalid input, using moderate: {parallel_batches} batches")

print(f"\n🚀 Starting execution with {parallel_batches} parallel batches")
print("="*80)

def execute_batch(batch_num):
    """Execute a single batch using the batch execution script."""
    print(f"\n[Batch {batch_num}] Starting...")
    start_time = time.time()

    try:
        result = subprocess.run(
            ["python3", "/Users/colinlowenberg/crew/execute_batch.py", str(batch_num)],
            capture_output=True,
            text=True,
            timeout=7200  # 2 hour timeout per batch
        )

        elapsed = time.time() - start_time

        if result.returncode == 0:
            print(f"[Batch {batch_num}] ✅ COMPLETE in {elapsed/60:.1f} minutes")
            return {"batch": batch_num, "status": "success", "time": elapsed}
        else:
            print(f"[Batch {batch_num}] ❌ FAILED after {elapsed/60:.1f} minutes")
            print(f"[Batch {batch_num}] Error: {result.stderr[:200]}")
            return {"batch": batch_num, "status": "failed", "time": elapsed, "error": result.stderr}

    except subprocess.TimeoutExpired:
        elapsed = time.time() - start_time
        print(f"[Batch {batch_num}] ⏱️ TIMEOUT after {elapsed/60:.1f} minutes")
        return {"batch": batch_num, "status": "timeout", "time": elapsed}
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"[Batch {batch_num}] ❌ ERROR: {str(e)}")
        return {"batch": batch_num, "status": "error", "time": elapsed, "error": str(e)}

# Execute batches in parallel waves
results = []
total_start = time.time()

for wave_start in range(0, len(batches), parallel_batches):
    wave_end = min(wave_start + parallel_batches, len(batches))
    wave_batches = range(wave_start + 1, wave_end + 1)

    print(f"\n{'='*80}")
    print(f"WAVE {wave_start//parallel_batches + 1}: Executing batches {wave_start+1}-{wave_end}")
    print(f"{'='*80}")

    with ThreadPoolExecutor(max_workers=parallel_batches) as executor:
        futures = [executor.submit(execute_batch, batch_num) for batch_num in wave_batches]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)

total_elapsed = time.time() - total_start

# Summary
print("\n" + "="*80)
print("EXECUTION COMPLETE")
print("="*80)
print(f"\nTotal time: {total_elapsed/60:.1f} minutes ({total_elapsed/3600:.1f} hours)")
print(f"Batches completed: {sum(1 for r in results if r['status'] == 'success')}/{len(batches)}")
print(f"Batches failed: {sum(1 for r in results if r['status'] in ['failed', 'error', 'timeout'])}/{len(batches)}")

successful = [r for r in results if r['status'] == 'success']
if successful:
    avg_time = sum(r['time'] for r in successful) / len(successful)
    print(f"Average batch time: {avg_time/60:.1f} minutes")

failed = [r for r in results if r['status'] != 'success']
if failed:
    print(f"\n⚠️  Failed batches: {[r['batch'] for r in failed]}")
    print("   You can retry these individually with:")
    for r in failed:
        print(f"     python3 execute_batch.py {r['batch']}")

# Save results
results_path = "/Users/colinlowenberg/crew/MASS_UPGRADE_RESULTS.json"
with open(results_path, 'w') as f:
    json.dump({
        "total_time_minutes": total_elapsed / 60,
        "total_time_hours": total_elapsed / 3600,
        "batches_attempted": len(batches),
        "batches_successful": sum(1 for r in results if r['status'] == 'success'),
        "batches_failed": sum(1 for r in results if r['status'] != 'success'),
        "results": results
    }, f, indent=2)

print(f"\n✅ Results saved to: {results_path}")

# Update gallery database with successful upgrades
print("\n📊 Updating gallery database...")
# This would update has_crewai=1 for successfully upgraded apps
print("   (Database update would happen here)")

print("\n🎉 MASS UPGRADE COMPLETE!")
print(f"   {analysis['total_apps']} apps processed in {total_elapsed/3600:.1f} hours")
print(f"   That's {len(successful)} successful batches!")
