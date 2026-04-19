def format_time_input(raw_value: str) -> str:
    digits_only = "".join(char for char in raw_value if char.isdigit())
    digits_only = digits_only[:4]

    if len(digits_only) >= 3:
        return f"{digits_only[:2]}:{digits_only[2:]}"
    if len(digits_only) == 2:
        return f"{digits_only}:"
    return digits_only