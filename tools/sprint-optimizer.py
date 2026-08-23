#!/usr/bin/env python3
"""
Sprint Optimizer — 45-Day Study & Application Portal
Analyzes weak-area-tracker.md and progress-tracker.md to suggest next-day focus.
Optimized for 12-14h/day sprint: never suggests adding hours, only reallocating.
Usage: python sprint-optimizer.py --student AZRA|ELA|ELFIIN
"""
import re
from pathlib import Path

STUDENTS = {
    "AZRA": {"band_now": "5.0", "band_target": "6.5", "sat_now": 0, "sat_target": 1250},
    "ELA": {"band_now": "5.5", "band_target": "6.5", "sat_now": 0, "sat_target": 1300},
    "ELFIIN": {"band_now": "6.5", "band_target": "7.5", "sat_now": 0, "sat_target": 1350},
}

def parse_tracker(path: Path):
    reds = []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line in text.splitlines():
            if "| R |" in line or "|R|" in line or " R " in line:
                # Extract topic name between | |
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 3:
                    topic = parts[1] or parts[2]
                    if topic and topic not in ("Topic", "Domain", "#", ""):
                        reds.append(topic)
    except FileNotFoundError:
        pass
    return reds

def suggest(student: str, base: Path):
    weak = parse_tracker(base / student / "sat" / "weak-area-tracker.md")
    print(f"=== {student} Optimization Report ===")
    print(f"Band: {STUDENTS[student]['band_now']} -> {STUDENTS[student]['band_target']}")
    print(f"RED topics found: {len(weak)}")
    for t in weak[:5]:
        print(f"  - Focus: {t} (20 min warm-up + 45 min timed set tomorrow)")
    if len(weak) == 0:
        print("  No REDs — shift 30 min from strongest to newest topic for breadth.")
    print("Rule: never add hours. Reallocate from GREEN topics (two clean sets) to REDs.")
    print("Next check: Sunday 45-min review — update tracker, then re-run this tool.")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--student", choices=STUDENTS.keys(), default="AZRA")
    p.add_argument("--base", default=".")
    args = p.parse_args()
    suggest(args.student, Path(args.base))
