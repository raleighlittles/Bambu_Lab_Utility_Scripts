#!/usr/bin/env bash


input_dir=$1

json_ext="*.json"

num_dump_files_found=$(find "$input_dir" -iname "$json_ext" | wc -l)

echo -e "$(date +'%Y-%m-%d')"

echo -e "Found $num_dump_files_found dump files! \n"

find "$input_dir" -iname "$json_ext" | while read json_file; do
    echo "Analyzing $json_file.."
    echo -e "\n"
    python3 decode_rfid_tag_dump.py --input-json-dump-file "$json_file"
    echo -e "\n\n"
done