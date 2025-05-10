import json
import sys
import pathlib

import pytest

# Ensure q1 directory is on path for imports
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from weather_reporter import main

def test_weather_reporter_simple(tmp_path, capsys):
    # Prepare sample data
    data = [
        {"city": "Alpha", "date": "2023-01-01", "temperature": 10},
        {"city": "Alpha", "date": "2023-01-02", "temperature": 12},
        {"city": "Beta",  "date": "2023-01-01", "temperature": 15},
    ]
    file = tmp_path / "temps.json"
    file.write_text(json.dumps(data))
    # Run main with the test JSON file
    main(["--input", str(file)])
    captured = capsys.readouterr()
    output = captured.out.strip().splitlines()
    # Check header present
    assert output[0].startswith("City")
    # Check data lines include cities
    joined = "\n".join(output)
    assert "Alpha" in joined
    assert "Beta" in joined