import binascii
import sys
import calendar
import struct
import pdb

def decode_filament_str_field(block_contents) -> str:
    
    # replace null bytes (0x00 in ASCII)
    return  binascii.unhexlify(block_contents).decode('unicode-escape').replace("\x00", "")


def decode_spool_weight(block_5_contents) -> str:
    
    # I was getting suspicious numbers (greater than 1000) when I ran this on the first dump in
    # the discord. If I used the bytes at index 9 and 10 (instead of 10 and 11, which is what 
    # the documentation says), I got a reasonable number.
    #spool_weight_grams = int(block_5_contents[4*2 : 5*2 + 2], 16)
    spool_weight_grams = int(block_5_contents[5*2 : 5*2 + 2] + block_5_contents[4*2 : 4*2+2], 16)

    spool_weight_kg = spool_weight_grams / 1000.0

    return f"Spool weight: {spool_weight_grams} g ({spool_weight_kg} kg)"


def decode_filament_color(block_5_contents) -> str:

    rgba = block_5_contents[0 : 3*2 + 2]

    red, green, blue, alpha = int(rgba[0:2], 16), int(rgba[2:4], 16), int(rgba[4:6], 16), int(rgba[6:8], 16)

    if all([channel == 0 for channel in [red, green, blue]]):
        return "Filament color: Black"
    
    elif all([channel == 0xFF for channel in [red, green, blue]]):
        return "Filament color: White"
    
    else:
        return f"Red: {red} Green: {green} Blue: {blue} Alpha: {alpha} | Raw: #{rgba[:-2]}"
    

def decode_filament_diameter(block_5_contents) -> str:
    
    filament_diameter_bytes_hex = block_5_contents[8*2 : 12*2]

    # 'f' for floating point, see https://docs.python.org/3/library/struct.html#format-characters
    filament_diameter_mm = struct.unpack('f', bytes.fromhex(filament_diameter_bytes_hex))[0]

    return f"Filament diameter: {filament_diameter_mm} mm"


def decode_filament_care_instructions(block_6_contents) -> str:


    bed_temperature_c = int(block_6_contents[9*2:9*2+2] + block_6_contents[8*2:8*2+2], 16)
    bed_temperature_f = (bed_temperature_c * (9/5) + 32)

    return f"Bed temperature: {bed_temperature_c}°C ({bed_temperature_f} °F)"


def decode_spool_width(block_10_contents) -> str:
    
    # for i in range(0, 32, 2):
    #     print(f"Index: {i/2} | Byte: {block_10_contents[i]}{block_10_contents[i+1]}")

    spool_width_hundreds_mm = int(block_10_contents[5*2:5*2+2] + block_10_contents[4*2:4*2+2], 16)

    return f"Spool width: {spool_width_hundreds_mm / 100} mm"


def decode_mfg_timestamps(block_12_contents, block_13_contents) -> str:

    long_mfg_timestamp = binascii.unhexlify(block_12_contents).decode("unicode-escape")

    long_year, long_month, long_day, long_hour, long_minute = long_mfg_timestamp.split("_")

    if int(long_month) > 12:
        raise ValueError(f"Error decoding long manufacturing timestamp -- invalid month '{long_month}'")
    
    if int(long_day) > 31:
        raise ValueError(f"Error decoding long manufacturing timestamp -- invalid day '{long_day}'")
    
    if int(long_hour) > 23:
        raise ValueError(f"Error decoding long manufacturing timestamp -- invalid hour '{long_hour}'")
    
    if int(long_minute) > 59:
        raise ValueError(f"Error decoding long manufacturing timestamp -- invalid minute '{long_minute}'")

    return f"Year: {long_year} | Month: {long_month} ({calendar.month_name[int(long_month)]}) | Day: {long_day} | Hour: {long_hour} | Minute: {long_minute}"


def decode_filament_length(block_14_contents) -> str:

    # for i in range(0, 32, 2):
    #     print(f"Index: {i/2} | Byte: {block_14_contents[i]}{block_14_contents[i+1]}")

    filament_length_m = int(block_14_contents[5*2:5*2+2] + block_14_contents[4*2:4*2+2], 16)

    filament_length_ft = filament_length_m * 3.281

    return f"Filament length: {filament_length_m} m ({round(filament_length_ft, 2)} ft)"