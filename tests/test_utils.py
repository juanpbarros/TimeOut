import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.utils import validate_time


def test_validate_time_valid():
    assert validate_time("12:30") is True


def test_validate_time_invalid_hour():
    assert validate_time("25:00") is False


def test_validate_time_invalid_minute():
    assert validate_time("12:99") is False


def test_validate_time_empty_string():
    assert validate_time("") is False


def test_validate_time_invalid_format():
    assert validate_time("abc") is False


def test_validate_time_trailing_colon():
    assert validate_time("12:") is False
