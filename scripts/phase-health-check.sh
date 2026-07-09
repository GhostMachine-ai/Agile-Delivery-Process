#!/usr/bin/env bash
# phase-health-check.sh
#
# Inspects a delivery project repository and reports on which agile delivery
# process artefacts are present, missing, or incomplete.
#
# Usage:
#   ./scripts/phase-health-check.sh [PATH_TO_PROJECT]
#   ./scripts/phase-health-check.sh .               # run in current directory
#   ./scripts/phase-health-check.sh ~/my-project    # run in specified directory
#
# What it checks:
#   - Presence of phase files (01–06)
#   - TBD or placeholder sections remaining in phase files
#   - Presence of templates directory and required templates
#   - Presence of checklists or filled-out templates
#   - AI/agent delivery supplement if project is AI-tagged

set -euo pipefail

PROJECT_DIR="${1:-.}"
PASS=0
WARN=0
FAIL=0

green() { printf '\033[0;32m[OK]     \033[0m %s\n' "$1"; ((PASS++)) || true; }
yellow() { printf '\033[0;33m[WARN]   \033[0m %s\n' "$1"; ((WARN++)) || true; }
red() { printf '\033[0;31m[MISSING]\033[0m %s\n' "$1"; ((FAIL++)) || true; }

echo ""
echo "======================================================"
echo "  Agile Delivery Process — Health Check"
echo "======================================================"
echo "  Project: $PROJECT_DIR"
echo "  Date:    $(date '+%Y-%m-%d')"
echo "======================================================"
echo ""

# ── Phase Files ───────────────────────────────────────────
echo "Phase Files"
echo "-----------"

PHASES=(
  "01_Alignment.md:Alignment"
  "02_Discovery.md:Discovery"
  "03_Alpha.md:Alpha"
  "04_Beta.md:Beta"
  "05_Live.md:Live"
)

for entry in "${PHASES[@]}"; do
  file="${entry%%:*}"
  name="${entry##*:}"
  path="$PROJECT_DIR/$file"

  if [ -f "$path" ]; then
    green "$file — $name"

    # Check for TBD placeholders
    tbd_count=$(grep -c '\[TBD\]\|\[TBD:\]\|\*TBD\*' "$path" 2>/dev/null || true)
    if [ "$tbd_count" -gt 0 ]; then
      yellow "  $tbd_count TBD section(s) found in $file — fill these in"
    fi

    # Check for empty staffing section
    if ! grep -q "Staffing" "$path" 2>/dev/null; then
      yellow "  No 'Staffing the Team' section found in $file"
    fi

    # Check for checklist
    if ! grep -q '^\- \[' "$path" 2>/dev/null; then
      yellow "  No checklist items found in $file — consider adding a phase checklist"
    fi
  else
    red "$file — $name (not found)"
  fi
done

# ── AI Supplement ─────────────────────────────────────────
echo ""
echo "AI/Agent Delivery Supplement"
echo "----------------------------"

if [ -f "$PROJECT_DIR/06_AI_Agent_Delivery.md" ]; then
  green "06_AI_Agent_Delivery.md — AI delivery supplement present"
else
  yellow "06_AI_Agent_Delivery.md — not found (add if building AI-powered features)"
fi

# ── Templates ─────────────────────────────────────────────
echo ""
echo "Templates"
echo "---------"

TEMPLATES=(
  "templates/phase-checklist-template.md:Phase Gate Checklist Template"
  "templates/user-story-template.md:User Story Template"
  "templates/ai-evaluation-rubric-template.md:AI Evaluation Rubric Template"
  "templates/data-availability-matrix-template.md:Data Availability Matrix Template"
)

for entry in "${TEMPLATES[@]}"; do
  file="${entry%%:*}"
  name="${entry##*:}"
  if [ -f "$PROJECT_DIR/$file" ]; then
    green "$file — $name"
  else
    yellow "$file — $name (not found; copy from agile-delivery-process repo templates/)"
  fi
done

# ── Scripts ───────────────────────────────────────────────
echo ""
echo "Automation Scripts"
echo "------------------"

SCRIPTS=(
  "scripts/phase-health-check.sh:This health check script"
  "scripts/generate-phase-report.py:Phase gap analysis report generator"
)

for entry in "${SCRIPTS[@]}"; do
  file="${entry%%:*}"
  name="${entry##*:}"
  if [ -f "$PROJECT_DIR/$file" ]; then
    green "$file — $name"
  else
    yellow "$file — $name (optional; available in agile-delivery-process repo scripts/)"
  fi
done

# ── Summary ───────────────────────────────────────────────
echo ""
echo "======================================================"
echo "  Summary"
echo "======================================================"
printf "  \033[0;32m[OK]    \033[0m %d item(s) passing\n" "$PASS"
printf "  \033[0;33m[WARN]  \033[0m %d item(s) need attention\n" "$WARN"
printf "  \033[0;31m[MISS]  \033[0m %d item(s) missing\n" "$FAIL"
echo ""

if [ "$FAIL" -gt 0 ]; then
  echo "  Action: resolve MISSING items before phase gate review."
  exit 1
elif [ "$WARN" -gt 0 ]; then
  echo "  Action: review WARN items — they may block phase advancement."
  exit 0
else
  echo "  All checks passed."
  exit 0
fi
