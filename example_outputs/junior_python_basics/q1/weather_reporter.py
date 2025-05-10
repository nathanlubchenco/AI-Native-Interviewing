#!/usr/bin/env python3
"""
weather_reporter.py: Command-line tool to summarize temperatures per city.
"""
import argparse
import json
import sys
from typing import List, Dict

def parse_args(args=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize daily temperatures per city."
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Path to JSON input file."
    )
    return parser.parse_args(args)

def load_data(path: str) -> List[Dict]:
    """Load JSON data from the given file path."""
    with open(path, 'r') as f:
        return json.load(f)

def compute_stats(records: List[Dict]) -> Dict[str, Dict[str, float]]:
    """Compute average, min, and max temperatures per city."""
    temps_by_city: Dict[str, List[float]] = {}
    for rec in records:
        city = rec.get("city")
        temp = rec.get("temperature")
        if city is None or temp is None:
            continue
        temps_by_city.setdefault(city, []).append(temp)
    stats: Dict[str, Dict[str, float]] = {}
    for city, temps in temps_by_city.items():
        stats[city] = {
            "avg": sum(temps) / len(temps),
            "min": min(temps),
            "max": max(temps),
        }
    return stats

def format_table(stats: Dict[str, Dict[str, float]]) -> str:
    """Format the stats into a simple aligned table."""
    header = ["City", "Average", "Min", "Max"]
    rows = []
    for city, vals in sorted(stats.items()):
        rows.append([
            city,
            f"{vals['avg']:.2f}",
            f"{vals['min']:.2f}",
            f"{vals['max']:.2f}",
        ])
    # Determine column widths
    cols = list(zip(header, *rows)) if rows else [(h,) for h in header]
    widths = [max(len(str(x)) for x in col) for col in cols]
    # Build lines
    lines = []
    # Header
    lines.append("  ".join(header[i].ljust(widths[i]) for i in range(len(header))))
    # Separator
    lines.append("  ".join('-' * widths[i] for i in range(len(header))))
    # Rows
    for row in rows:
        lines.append("  ".join(row[i].ljust(widths[i]) for i in range(len(row))))
    return "\n".join(lines)

def main(args=None) -> None:
    parsed = parse_args(args)
    records = load_data(parsed.input)
    stats = compute_stats(records)
    table = format_table(stats)
    print(table)

if __name__ == "__main__":
    main()