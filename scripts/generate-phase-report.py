#!/usr/bin/env python3
"""
generate-phase-report.py

Reads the agile delivery process phase files in a project directory and
generates a structured delivery status report showing which sections are
complete, which contain placeholders, and which artefacts are present.

This is pseudocode demonstrating the pattern. Adapt paths and output
format for your specific project tooling.

Usage:
    python scripts/generate-phase-report.py [--project-dir PATH] [--phase PHASE]
    python scripts/generate-phase-report.py --project-dir .
    python scripts/generate-phase-report.py --project-dir . --phase 02

Output:
    Prints a structured report to stdout. Redirect to a file for archiving:
    python scripts/generate-phase-report.py > reports/phase-status-2026-07.md
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any


# ── Configuration ──────────────────────────────────────────────────────────

PHASE_FILES = {
    "01": ("01_Alignment.md", "Alignment"),
    "02": ("02_Discovery.md", "Discovery"),
    "03": ("03_Alpha.md", "Alpha"),
    "04": ("04_Beta.md", "Beta"),
    "05": ("05_Live.md", "Live"),
    "06": ("06_AI_Agent_Delivery.md", "AI Agent Delivery"),
}

REQUIRED_SECTIONS = [
    "What is",
    "What do you do",
    "What do you have at the end",
    "Staffing",
    "Checklist",
]

PLACEHOLDER_PATTERNS = [
    r'\[TBD\]',
    r'\*TBD\*',
    r'\[TBD:',
    r'\[Your ',
    r'\[insert ',
    r'\[describe ',
]

TEMPLATE_FILES = [
    "templates/phase-checklist-template.md",
    "templates/user-story-template.md",
    "templates/ai-evaluation-rubric-template.md",
    "templates/data-availability-matrix-template.md",
]


# ── Parsing ────────────────────────────────────────────────────────────────

def parse_phase_file(path: Path) -> dict[str, Any]:
    """Extract sections, placeholder count, and checklist status from a phase file."""
    if not path.exists():
        return {"exists": False}

    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    sections_found = []
    for section in REQUIRED_SECTIONS:
        if any(section.lower() in line.lower() for line in lines):
            sections_found.append(section)

    placeholder_count = sum(
        len(re.findall(pattern, content, re.IGNORECASE))
        for pattern in PLACEHOLDER_PATTERNS
    )

    checklist_items = [l for l in lines if l.strip().startswith("- [ ]")]
    checked_items = [l for l in lines if l.strip().startswith("- [x]") or l.strip().startswith("- [X]")]

    ai_notes = "AI/Agent Delivery Notes" in content or "AI/Agent" in content

    return {
        "exists": True,
        "line_count": len(lines),
        "sections_found": sections_found,
        "sections_missing": [s for s in REQUIRED_SECTIONS if s not in sections_found],
        "placeholder_count": placeholder_count,
        "checklist_total": len(checklist_items) + len(checked_items),
        "checklist_checked": len(checked_items),
        "has_ai_notes": ai_notes,
    }


def scan_templates(project_dir: Path) -> dict[str, bool]:
    """Check which template files are present."""
    return {tmpl: (project_dir / tmpl).exists() for tmpl in TEMPLATE_FILES}


# ── Reporting ──────────────────────────────────────────────────────────────

def status_icon(ok: bool) -> str:
    return "✓" if ok else "✗"


def render_phase_report(phase_id: str, filename: str, phase_name: str, data: dict[str, Any]) -> str:
    """Render a report block for a single phase."""
    lines = [f"\n## Phase {phase_id}: {phase_name} (`{filename}`)"] 

    if not data["exists"]:
        lines.append("  **STATUS: FILE NOT FOUND**")
        return "\n".join(lines)

    lines.append(f"  Lines: {data['line_count']}")

    # Sections
    lines.append("\n  ### Sections")
    for s in REQUIRED_SECTIONS:
        found = s in data["sections_found"]
        lines.append(f"  {status_icon(found)} {s}")

    # Placeholders
    lines.append("\n  ### Completeness")
    ph = data["placeholder_count"]
    lines.append(f"  {status_icon(ph == 0)} Placeholder text: {'none found' if ph == 0 else f'{ph} found — fill these in'}")

    # Checklist
    total = data["checklist_total"]
    checked = data["checklist_checked"]
    if total > 0:
        pct = int((checked / total) * 100)
        lines.append(f"  {status_icon(checked == total)} Checklist: {checked}/{total} items complete ({pct}%)")
    else:
        lines.append(f"  ✗ Checklist: no checklist items found — add a phase checklist")

    # AI notes
    lines.append(f"  {status_icon(data['has_ai_notes'])} AI/Agent delivery notes: {'present' if data['has_ai_notes'] else 'not found'}")

    return "\n".join(lines)


def render_full_report(project_dir: Path, phases_to_report: list[str]) -> str:
    """Render the complete delivery status report."""
    report_lines = [
        "# Delivery Status Report",
        f"\n**Project directory:** `{project_dir}`",
        f"**Generated:** [run date]",
        "\n---\n",
        "## Phase Status",
    ]

    issues = 0
    for phase_id in phases_to_report:
        if phase_id not in PHASE_FILES:
            continue
        filename, phase_name = PHASE_FILES[phase_id]
        data = parse_phase_file(project_dir / filename)
        report_lines.append(render_phase_report(phase_id, filename, phase_name, data))

        if not data.get("exists"):
            issues += 1
        elif data.get("placeholder_count", 0) > 0 or data.get("checklist_checked", 0) < data.get("checklist_total", 0):
            issues += 1

    # Templates
    report_lines.append("\n---\n\n## Templates")
    template_status = scan_templates(project_dir)
    for tmpl, present in template_status.items():
        report_lines.append(f"  {status_icon(present)} `{tmpl}`")

    # Summary
    report_lines.append("\n---\n\n## Summary")
    if issues == 0:
        report_lines.append("All checked phases are complete. Ready for phase gate review.")
    else:
        report_lines.append(f"{issues} phase(s) have incomplete sections or placeholder text. Resolve before phase gate review.")

    return "\n".join(report_lines)


# ── CLI ────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate agile delivery phase status report")
    parser.add_argument("--project-dir", default=".", help="Path to the delivery project directory")
    parser.add_argument("--phase", default="all", help="Phase to report on: all, 01, 02, 03, 04, 05, 06")
    args = parser.parse_args()

    project_dir = Path(args.project_dir).resolve()
    if not project_dir.is_dir():
        print(f"Error: directory not found: {project_dir}", file=sys.stderr)
        sys.exit(1)

    if args.phase == "all":
        phases = list(PHASE_FILES.keys())
    else:
        phases = [args.phase.zfill(2)]

    print(render_full_report(project_dir, phases))


if __name__ == "__main__":
    main()
