import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.input_formatter import format_time_input


def test_format_time_input_with_four_digits():
    assert format_time_input("1234") == "12:34"


def test_format_time_input_with_three_digits():
    assert format_time_input("123") == "12:3"


def test_format_time_input_with_two_digits():
    assert format_time_input("12") == "12:"


def test_format_time_input_with_one_digit():
    assert format_time_input("1") == "1"


def test_format_time_input_ignores_non_digits_and_truncates():
    assert format_time_input("1a2b3c4d5e") == "12:34"


def test_format_time_input_returns_empty_for_no_digits():
    assert format_time_input("ab:cd") == ""