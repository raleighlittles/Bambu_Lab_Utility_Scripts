import binascii
import sys
import calendar
import struct
import pdb
import datetime

# locals
import helper


def decode_filament_sku(block_1_contents) -> str:
    """
    The SKU can be verified using the filament MSDS/reports (look under the 'Model' section in the PDF)
    """

    filament_sku = binascii.unhexlify(block_1_contents[0:12]).decode("unicode-escape").replace(
        "\x00", "")

    return f"Filament SKU: {filament_sku}"


def decode_filament_str_field(block_2_contents) -> str:

    # replace null bytes (0x00 in ASCII)
    return binascii.unhexlify(block_2_contents).decode("unicode-escape").replace(
        "\x00", "")


def decode_spool_weight(block_5_contents) -> str:

    # I was getting suspicious numbers (greater than 1000) when I ran this on the first dump in
    # the discord. If I used the bytes at index 9 and 10 (instead of 10 and 11, which is what
    # the documentation says), I got a reasonable number.
    # spool_weight_grams = int(block_5_contents[4*2 : 5*2 + 2], 16)
    spool_weight_grams = int(
        block_5_contents[5 * 2:5 * 2 + 2] + block_5_contents[4 * 2:4 * 2 + 2], 16)

    if spool_weight_grams < 1:
        raise ValueError(
            f"Error: spool weight is an invalid value ('{spool_weight_grams}'), please verify data is correct")

    spool_weight_kg = spool_weight_grams / 1000.0

    return f"Spool weight: {spool_weight_grams} g ({spool_weight_kg} kg)"


def decode_filament_color(block_5_contents) -> str:

    rgba = block_5_contents[0:3 * 2 + 2]

    red, green, blue, alpha = int(rgba[0:2],
                                  16), int(rgba[2:4],
                                           16), int(rgba[4:6],
                                                    16), int(rgba[6:8], 16)

    if all([channel == 0 for channel in [red, green, blue]]):
        return "Filament color: Black"

    elif all([channel == 0xFF for channel in [red, green, blue]]):
        return "Filament color: White"

    else:
        return f"Red: {red} Green: {green} Blue: {blue} Alpha: {alpha} | Raw: #{rgba[:-2]}"


def decode_filament_diameter(block_5_contents) -> str:

    filament_diameter_bytes_hex = block_5_contents[8 * 2:12 * 2]

    # 'f' for floating point, see https://docs.python.org/3/library/struct.html#format-characters
    filament_diameter_mm = struct.unpack(
        'f', bytes.fromhex(filament_diameter_bytes_hex))[0]

    return f"Filament diameter: {filament_diameter_mm} mm"


def decode_hotend_temperatures(block_6_contents) -> str:
    """

    """

    hotend_min_temp = int(
        block_6_contents[11 * 2: 11 * 2 + 2] + block_6_contents[10 * 2: 10 * 2 + 2], 16)

    hotend_max_temp = int(
        block_6_contents[9 * 2: 9 * 2 + 2] + block_6_contents[8 * 2: 8 * 2 + 2], 16)

    if hotend_min_temp == hotend_max_temp:
        return f"Hotend temperature: {hotend_min_temp}°C ({helper.convert_celsius_to_fahrenheit(hotend_min_temp)} °F)"

    else:
        return f"Hotend temperature range: {hotend_min_temp} — {hotend_max_temp} °C"


def decode_drying_instructions(block_6_contents) -> str:
    """

    """

    drying_temp = int(
        block_6_contents[1 * 2: 1 * 2 + 2] + block_6_contents[0 * 2: 0 * 2 + 2], 16)

    drying_time_h = int(
        block_6_contents[3 * 2: 3 * 2 + 2] + block_6_contents[2 * 2: 2 * 2 + 2], 16)

    return f"Drying temp: {drying_temp} °C ({helper.convert_celsius_to_fahrenheit(drying_temp)} °F) | Drying time: {drying_time_h} hours"


def decode_bed_plate_type(block_6_contents) -> str:
    """
    TODO The mapping of bed plate types to indices is not confirmed. The "Cool Plate" being 1 is a guess because its the default bed type for PLA
    and Bambu recommends using the Cool Plate for PLA, and for PETG, Bambu recommends the "Engineering Plate" which appears as value 2
    """

    output_str = ""

    bed_plate_type_raw = int(
        block_6_contents[5 * 2: 5 * 2 + 2] + block_6_contents[4 * 2: 4 * 2 + 2], 16)

    output_str += f"Bed plate type index = {bed_plate_type_raw} | Likeliest type: "

    if bed_plate_type_raw == 1:
        output_str += "PLA"

    elif bed_plate_type_raw == 2:
        output_str += "Engineering Plate"

    return output_str


def decode_bed_temperature(block_6_contents) -> str:

    bed_temperature = int(
        block_6_contents[9 * 2:9 * 2 + 2] + block_6_contents[8 * 2:8 * 2 + 2],
        16)

    return f"Bed temperature: {bed_temperature} °C ({helper.convert_celsius_to_fahrenheit(bed_temperature)} °F)"


def decode_xcam_info(block_8_contents) -> str:
    """
    TODO Figure out what this is
    """

    return f"X Cam info: {block_8_contents[0:12*2]}"


def decode_spool_width(block_10_contents) -> str:

    spool_width_mm = int(
        block_10_contents[5 * 2:5 * 2 + 2] +
        block_10_contents[4 * 2:4 * 2 + 2], 16) / 100

    return f"Spool width: {spool_width_mm} mm ({helper.convert_mm_to_inches(spool_width_mm)} inches)"


def decode_mfg_timestamps(block_12_contents, block_13_contents) -> str:

    long_mfg_timestamp = binascii.unhexlify(block_12_contents).decode(
        "unicode-escape")

    long_year, long_month, long_day, long_hour, long_minute = long_mfg_timestamp.split(
        "_")

    if int(long_month) > 12:
        raise ValueError(
            f"Error decoding long manufacturing timestamp -- invalid month '{long_month}'"
        )

    if int(long_day) > 31:
        raise ValueError(
            f"Error decoding long manufacturing timestamp -- invalid day '{long_day}'"
        )

    if int(long_hour) > 23:
        raise ValueError(
            f"Error decoding long manufacturing timestamp -- invalid hour '{long_hour}'"
        )

    if int(long_minute) > 59:
        raise ValueError(
            f"Error decoding long manufacturing timestamp -- invalid minute '{long_minute}'"
        )

    return f"Year: {long_year} | Month: {long_month} ({calendar.month_name[int(long_month)]}) | Day: {long_day} | Hour: {long_hour} | Minute: {long_minute}"


def decode_filament_length(block_14_contents) -> str:

    # for i in range(0, 32, 2):
    #     print(f"Index: {i/2} | Byte: {block_14_contents[i]}{block_14_contents[i+1]}")

    filament_length_m = int(
        block_14_contents[5 * 2:5 * 2 + 2] +
        block_14_contents[4 * 2:4 * 2 + 2], 16)

    return f"Filament length: {filament_length_m} m ({helper.convert_meters_to_ft(filament_length_m)} ft)"
