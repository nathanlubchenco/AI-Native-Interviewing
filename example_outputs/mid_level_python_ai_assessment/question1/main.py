#!/usr/bin/env python3
import csv
import json
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="Process user activity logs CSV")
    parser.add_argument("input_csv", type=Path, help="Path to input CSV file")
    parser.add_argument("output_json", type=Path, help="Path to output JSON file")
    return parser.parse_args()

def process_csv(input_path):
    stats = {}
    with input_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                user = row["user_id"]
                timestamp = row["timestamp"]
                action = row["action"]
            except KeyError:
                continue
            stats.setdefault(user, []).append(action)
    result = {}
    for user, actions in stats.items():
        total = len(actions)
        days = {}
        for action in actions:
            days[action] = days.get(action, 0) + 1
        avg_per_day = total / len(days) if days else 0
        result[user] = {"total_actions": total, "average_per_day": avg_per_day}
    return result

def main():
    args = parse_args()
    result = process_csv(args.input_csv)
    with args.output_json.open("w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
