
import argparse
import os
import binascii
import pdb
import json


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument("-i", "--input-bin-file", help="Input bin file (to convert to JSON)", type=str, required=True)


    argparse_args = argparse_parser.parse_args()

    bin_file_path = argparse_args.input_bin_file

    if os.path.exists(bin_file_path):

        output_json_file_path = bin_file_path + ".json"

        bin_as_json_dict = dict()

        bin_as_json_dict["Created"] = str(__file__)
        bin_as_json_dict["FileType"] = "unknown"

        bin_as_json_dict["blocks"] = []

        with open(bin_file_path, mode='rb') as bin_file:

            fileContent = bin_file.read()

            file_content_hexed = binascii.b2a_hex(data=fileContent).decode("utf-8")

            bin_as_json_dict["blocks"] = dict()

            for block_idx in range(0, 64):

                #print("Block index = ", block_idx)
                
                bin_as_json_dict["blocks"][str(block_idx)] = str()

                for byte_idx in range(0, 32):

                    #print("Byte index: ", byte_idx)
                    #print("Reading byte in file", block_idx * 32 + byte_idx)

                    bin_as_json_dict["blocks"][str(block_idx)] += file_content_hexed[block_idx * 32 + byte_idx]

                
            with open(output_json_file_path, mode='w', encoding="utf-8") as output_json_file:

                print("Writing file to", output_json_file_path)
                json.dump(bin_as_json_dict, output_json_file, ensure_ascii=True, indent=4)

    else:
        raise FileNotFoundError(f"Error couldn't find bin file: '{bin_file_path}'")

                    

            

