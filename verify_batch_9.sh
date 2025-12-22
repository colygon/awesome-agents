#!/bin/bash
# Batch 9 Verification Script
# Verifies all 20 apps were properly upgraded with CrewAI

echo "=================================="
echo "BATCH 9 VERIFICATION REPORT"
echo "=================================="
echo ""

# Define batch 9 agent IDs
BATCH_9_AGENTS=(134 135 136 138 161 163 164 183 184 185 187 212 213 214 215 240 241 242 251 278)

# Counters
total=0
found=0
has_crewai=0
has_docs=0
has_git=0

echo "Checking 20 apps from Batch 9..."
echo ""

for agent_id in "${BATCH_9_AGENTS[@]}"; do
    total=$((total + 1))

    # Find directory with this agent ID
    dir=$(find /Users/colinlowenberg/crew -maxdepth 1 -type d -name "*-agent${agent_id}" | head -1)

    if [ -n "$dir" ]; then
        found=$((found + 1))
        app_name=$(basename "$dir")

        echo "[$total/20] Agent $agent_id: $app_name"

        # Check for crewai_agents directory
        if [ -d "$dir/crewai_agents" ]; then
            has_crewai=$((has_crewai + 1))

            # Count files in crewai_agents
            file_count=$(ls "$dir/crewai_agents" 2>/dev/null | wc -l)
            echo "  ✓ CrewAI agents directory ($file_count files)"

            # Check for required files
            if [ -f "$dir/crewai_agents/agents.py" ]; then
                echo "  ✓ agents.py"
            fi
            if [ -f "$dir/crewai_agents/tasks.py" ]; then
                echo "  ✓ tasks.py"
            fi
            if [ -f "$dir/crewai_agents/main.py" ]; then
                echo "  ✓ main.py"
            fi
        else
            echo "  ✗ Missing crewai_agents directory"
        fi

        # Check for documentation
        if [ -f "$dir/COMPLETION_REPORT.md" ] && [ -f "$dir/CREWAI_UPGRADE.md" ]; then
            has_docs=$((has_docs + 1))
            echo "  ✓ Documentation (COMPLETION_REPORT.md, CREWAI_UPGRADE.md)"
        else
            echo "  ✗ Missing documentation"
        fi

        # Check for requirements.txt with CrewAI
        if [ -f "$dir/requirements.txt" ]; then
            if grep -q "crewai>=0.86.0" "$dir/requirements.txt"; then
                echo "  ✓ requirements.txt (with CrewAI)"
            else
                echo "  ✗ requirements.txt (missing CrewAI)"
            fi
        fi

        # Check git status
        if [ -d "$dir/.git" ]; then
            has_git=$((has_git + 1))
            cd "$dir"
            current_branch=$(git branch --show-current 2>/dev/null)
            if [ "$current_branch" = "crewai-upgrade" ]; then
                echo "  ✓ Git repository (on crewai-upgrade branch)"
            else
                echo "  ⚠ Git repository (on $current_branch branch)"
            fi
            cd - > /dev/null
        else
            echo "  ✗ No git repository"
        fi

        echo ""
    else
        echo "[$total/20] Agent $agent_id: NOT FOUND"
        echo ""
    fi
done

echo "=================================="
echo "SUMMARY"
echo "=================================="
echo "Total apps expected:          20"
echo "Apps found:                   $found"
echo "Apps with CrewAI:            $has_crewai"
echo "Apps with documentation:     $has_docs"
echo "Apps with git repository:    $has_git"
echo ""

# Calculate success rate
success_rate=$(echo "scale=1; $found * 100 / 20" | bc)
echo "Success rate: $success_rate%"
echo ""

if [ $found -eq 20 ] && [ $has_crewai -eq 20 ] && [ $has_docs -eq 20 ]; then
    echo "✓ BATCH 9 VERIFICATION PASSED"
    exit 0
else
    echo "⚠ BATCH 9 VERIFICATION INCOMPLETE"
    exit 1
fi
