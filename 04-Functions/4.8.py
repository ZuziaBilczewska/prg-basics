def time_string(hours, minutes, time_format):
    """Return a time as a string in either 24-hour or 12-hour format."""
    if not 0 <= hours <= 23:
        raise ValueError("hours must be between 0 and 23")
    if not 0 <= minutes <= 59:
        raise ValueError("minutes must be between 0 and 59")

    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    if time_format == '12':
        suffix = 'am' if hours < 12 else 'pm'
        hour_12 = hours % 12
        if hour_12 == 0:
            hour_12 = 12
        return f"{hour_12}:{minutes:02d}{suffix}"

    raise ValueError("time_format must be '24' or '12'")


# Tests
assert time_string(15, 38, '24') == '15:38'
assert time_string(8, 3, '24') == '08:03'
assert time_string(0, 5, '24') == '00:05'
assert time_string(11, 15, '12') == '11:15am'
assert time_string(0, 7, '12') == '12:07am'
assert time_string(7, 30, '12') == '7:30am'
assert time_string(12, 46, '12') == '12:46pm'
assert time_string(13, 10, '12') == '1:10pm'
assert time_string(19, 2, '12') == '7:02pm'

print("All tests passed.")
