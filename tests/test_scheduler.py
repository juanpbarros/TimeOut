import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.scheduler import calculate_seconds_until


def test_calculate_seconds_until_returns_positive_integer():
    seconds = calculate_seconds_until("23:59")
    assert isinstance(seconds, int)
    assert seconds > 0