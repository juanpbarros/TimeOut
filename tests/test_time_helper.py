import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.time_helper import add_minutes_to_time


def test_add_10_minutes_to_time():
    assert add_minutes_to_time("10:30", 10) == "10:40"


def test_add_1_hour_to_time():
    assert add_minutes_to_time("10:30", 60) == "11:30"


def test_add_minutes_wraps_to_next_day():
    assert add_minutes_to_time("23:50", 10) == "00:00"


def test_add_minutes_wraps_hour():
    assert add_minutes_to_time("10:55", 10) == "11:05"


def test_add_zero_minutes_keeps_same_time():
    assert add_minutes_to_time("18:20", 0) == "18:20"