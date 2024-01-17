

def convert_celsius_to_fahrenheit(celsius_temp: int) -> int:

    return int((celsius_temp * (9/5)) + 32)


def convert_meters_to_ft(length_m: int) -> int:

    return int(length_m * 3.281)


def convert_mm_to_inches(length_mm) -> int:

    return round(length_mm / 25.4, 1)
