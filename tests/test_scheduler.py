import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.scheduler import calculate_seconds_until


def test_calculate_seconds_until_returns_positive_integer():
    seconds = calculate_seconds_until("23:59")

    assert isinstance(seconds, int)
    assert seconds > 0


def test_calculate_seconds_until_returns_value_within_one_day():
    seconds = calculate_seconds_until("23:59")

    assert seconds <= 86400


def test_calculate_seconds_until_invalid_hour():
    with pytest.raises(ValueError):
        calculate_seconds_until("25:00")


def test_calculate_seconds_until_invalid_minute():
    with pytest.raises(ValueError):
        calculate_seconds_until("23:99")


def test_calculate_seconds_until_invalid_text():
    with pytest.raises(ValueError):
        calculate_seconds_until("abc")