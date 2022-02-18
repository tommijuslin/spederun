def convert_to_ms(hours, minutes, seconds, ms):
    s = 1000 * seconds
    m = 60000 * minutes
    h = 3600000 * hours

    return h + m + s + ms

def format_time(ms):
    second_ms = divmod(ms, 1000)
    min_second = divmod(second_ms[0], 60)
    hour_min = divmod(min_second[0], 60)

    s = int(min_second[1])
    m = int(hour_min[1])
    h = int(hour_min[0])
    ms = int(second_ms[1])

    if s == 0 and m == 0 and h == 0:
        return f"{h}h {m}m {s}s {ms}ms"

    return f"{h}h {m}m {s}s"

def validate_time(time):
    if time == "":
        return 0
    elif int(time) < 0:
        return NEGATIVE

    return int(time)

def format_title(title):
    if len(title) < 35:
        return title

    return title[:35] + "..."
