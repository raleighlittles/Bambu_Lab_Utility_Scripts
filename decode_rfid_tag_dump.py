import argparse
import json
import os
import pdb

import decoder

def decode_rfid_dump(json_file_obj):

    rfid_dump_data = json.load(json_file_obj)

    rfid_blocks = rfid_dump_data["blocks"]
    

    # Block 1
    tray_info_index = rfid_blocks["1"][0:8]
    print(f"Tray info index: {tray_info_index}")

    # Block 2
    filament_type = decoder.decode_filament_str_field(rfid_blocks["2"])

    # Block 4
    filament_description = decoder.decode_filament_str_field(rfid_blocks["4"])

    print(f"Filament type: '{filament_type}' ({filament_description})")

    
    # for i in range(0, 32, 2):
    #     print(f"Index: {i/2} | Byte: {(rfid_blocks['5'])[i]}{(rfid_blocks['5'])[i+1]}")

    # pdb.set_trace()

    print(decoder.decode_spool_weight(rfid_blocks["5"]))

    print(decoder.decode_filament_diameter(rfid_blocks["5"]))

    print(decoder.decode_filament_color(rfid_blocks["5"]))

    print(decoder.decode_filament_care_instructions(rfid_blocks["6"]))

    print(f"Tray UID: {rfid_blocks['9']}")

    print(decoder.decode_spool_width(rfid_blocks["10"]))

    print(decoder.decode_mfg_timestamps(rfid_blocks["12"], rfid_blocks["13"]))

    print(decoder.decode_filament_length(rfid_blocks["14"]))


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument("-j", "--input-json-dump-file", type=str, required=True, help="The input JSON file to decode")

    argparse_args = argparse_parser.parse_args()

    json_filepath = argparse_args.input_json_dump_file

    if os.path.exists(json_filepath):

        with open(json_filepath, 'r') as json_file_obj:

            decode_rfid_dump(json_file_obj)
