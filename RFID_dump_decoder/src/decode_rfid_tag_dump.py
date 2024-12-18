import argparse
import json
import os

import decoder


def decode_rfid_dump(json_file_obj):

    rfid_dump_data = json.load(json_file_obj)

    rfid_blocks = rfid_dump_data["blocks"]

    print("-------------------------------")

    # Prints the whole dump out to the console (debug only)
    # print("-----------------------------")
    # for values in rfid_blocks.values():
    #     print(values)
    # print("-----------------------------")

    # Prints an entire block out, byte by byte

    # print("=====================")
    # for i in range(0, 32, 2):
    #     print(f"Index: {i/2} | Byte: {(rfid_blocks['6'])[i]}{(rfid_blocks['6'])[i+1]}")
    # print("=====================")

    # Block 1
    print(decoder.decode_filament_sku(rfid_blocks['1']))

    # Block 2
    filament_type = decoder.decode_filament_str_field(rfid_blocks['2'])

    # Block 4
    filament_description = decoder.decode_filament_str_field(rfid_blocks['4'])

    print(f"Filament type: '{filament_type}' ({filament_description})")

    print(decoder.decode_spool_weight(rfid_blocks['5']))

    print(decoder.decode_filament_diameter(rfid_blocks['5']))

    print(decoder.decode_filament_color(rfid_blocks["5"]))

    print(decoder.decode_hotend_temperatures(rfid_blocks['6']))

    print(decoder.decode_bed_temperature(rfid_blocks['6']))

    print(decoder.decode_drying_instructions(rfid_blocks['6']))

    print(decoder.decode_bed_plate_type(rfid_blocks['6']))

    print(decoder.decode_xcam_info(rfid_blocks['8']))

    print(f"Tray UID: {rfid_blocks['9']}")

    print(decoder.decode_spool_width(rfid_blocks["10"]))


    print(decoder.decode_mfg_timestamps(rfid_blocks["12"], rfid_blocks["13"]))


    print(decoder.decode_filament_length(rfid_blocks["14"]))
    
    print("===============================")


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument("-j",
                                 "--input-json-dump-file",
                                 type=str,
                                 required=False,
                                 help="The input JSON file to decode")
    

    argparse_args = argparse_parser.parse_args()

    json_filepath = argparse_args.input_json_dump_file

    if os.path.exists(json_filepath):

        with open(json_filepath, mode='r') as json_file_obj:

            try:
                decode_rfid_dump(json_file_obj)
                
            except ValueError as e:
                print(f"Error extracting data from JSON file '{json_file_obj.name}': {e}")

    else:
        raise FileNotFoundError(f"Error: JSON file '{json_filepath}' could not be found")
