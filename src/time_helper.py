from datetime import datetime, timedelta


def add_minutes_to_time(time_str: str, minutes: int) -> str:
    if time_str:
        base_time = datetime.strptime(time_str, "%H:%M")
    else:
        base_time = datetime.now()

    new_time = base_time + timedelta(minutes=minutes)
    return new_time.strftime("%H:%M")