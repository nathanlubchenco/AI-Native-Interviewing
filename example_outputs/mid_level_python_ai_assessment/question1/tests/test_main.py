import pytest
from pathlib import Path
from main import process_csv

def write_csv(tmp_path, lines):
    file = tmp_path / "input.csv"
    file.write_text("\n".join(lines))
    return file

def test_empty_file(tmp_path):
    csv_file = write_csv(tmp_path, ["user_id,timestamp,action"])
    result = process_csv(csv_file)
    assert result == {}

def test_malformed_rows(tmp_path):
    lines = ["user_id,timestamp,action", "1,2021-01-01,login", "2,2021-01-02"]
    csv_file = write_csv(tmp_path, lines)
    result = process_csv(csv_file)
    assert "1" in result and result["1"]["total_actions"] == 1

def test_summary_correct(tmp_path):
    lines = [
        "user_id,timestamp,action",
        "1,2021-01-01,login",
        "1,2021-01-01,logout",
        "1,2021-01-02,login"
    ]
    csv_file = write_csv(tmp_path, lines)
    result = process_csv(csv_file)
    assert result["1"]["total_actions"] == 3
    assert pytest.approx(result["1"]["average_per_day"]) == 1.5
