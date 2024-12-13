#!/usr/bin/env bash


input_dir=$1

num_dump_files_found_cmd="find $input_dir \( -iname "*.bin" -or -iname "*.json" \)"

num_dump_files_found=$(eval $num_dump_files_found_cmd | wc -l)

echo -e "$(date +'%Y-%m-%d')"

echo -e "Found $num_dump_files_found dump files! \n"

find "$input_dir" -iname "*.json" | while read json_file; do
    echo "Analyzing $json_file.."
    echo -e "\n"
    python3 src/decode_rfid_tag_dump.py --input-json-dump-file "$json_file"
    echo -e "\n\n"
done

find "$input_dir" -iname "*.bin" | while read bin_file; do

    python3 src/generate_json_from_bin.py --input-bin-file "$bin_file" 1> /dev/null 2> /dev/null
    converted_json_filename="$bin_file".json

    if test -f "$converted_json_filename"; then
        echo "Analyzing $bin_file.."
        echo -e "\n"
        python3 src/decode_rfid_tag_dump.py --input-json-dump-file $bin_file.json
    fi
    
    echo -e "\n\n"
done