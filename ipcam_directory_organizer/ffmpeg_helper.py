

def build_concat_demuxer_list(files_list, concat_demuxer_filename):

    print(
        f"[DEBUG] Adding {len(files_list)} files to file list '{concat_demuxer_filename}'")

    with open(concat_demuxer_filename, mode='w', encoding="utf-8") as concat_demuxer_file_obj:

        for filename in files_list:

            concat_demuxer_file_obj.write(f"file '{filename}' \n")
