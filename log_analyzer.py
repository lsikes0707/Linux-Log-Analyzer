#!/usr/bin/env python3
"""
Simple Linux Log Analyzer

Parses log files and summarizes:
- Error counts
- Warning counts
- Most common log levels
- Recent log entries

Designed as a lightweight observability practice tool.
"""

import sys
from collections import Counter


def analyze_log(filepath):
    levels = Counter()
    recent_lines = []

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line_lower = line.lower()

                if "error" in line_lower:
                    levels["ERROR"] += 1
                elif "warn" in line_lower:
                    levels["WARNING"] += 1
                elif "info" in line_lower:
                    levels["INFO"] += 1

                recent_lines.append(line.strip())

        return levels, recent_lines[-10:]

    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)


def print_summary(levels, recent_lines):
    print("\n=== Log Summary ===")
    for level, count in levels.items():
        print(f"{level}: {count}")

    print("\n=== Recent Log Entries ===")
    for line in recent_lines:
        print(line)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    levels, recent_lines = analyze_log(logfile)
    print_summary(levels, recent_lines)
