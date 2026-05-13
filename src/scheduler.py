import subprocess
from datetime import datetime, timedelta


def calculate_seconds_until(target_time_str: str) -> int:
    now = datetime.now()
    target_time = datetime.strptime(target_time_str, "%H:%M")

    target_time = target_time.replace(
        year=now.year,
        month=now.month,
        day=now.day
    )

    if target_time <= now:
        target_time += timedelta(days=1)

    difference = target_time - now
    return int(difference.total_seconds())


def schedule_shutdown(target_time_str: str) -> int:
    seconds = calculate_seconds_until(target_time_str)
    result = subprocess.run(
        ["shutdown", "-s", "-t", str(seconds)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Failed to schedule shutdown: {result.stderr.strip()}"
        )
    return seconds


def cancel_shutdown() -> None:
    result = subprocess.run(
        ["shutdown", "-a"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Failed to cancel shutdown: {result.stderr.strip()}"
        )