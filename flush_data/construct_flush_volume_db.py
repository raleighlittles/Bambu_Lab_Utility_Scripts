import argparse
import os
import pandas


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Construct flush volume database")
    parser.add_argument("--input-directory", "-i", type=str, required=True, help="The path to where the flush data text files are stored")
    argparse_args = parser.parse_args()

    if not os.path.exists(argparse_args.input_directory):
        raise FileNotFoundError(f"The input directory {argparse_args.input_directory} does not exist.")
    
    files_in_dir = os.listdir(argparse_args.input_directory)
    flush_data_files = [f for f in files_in_dir if (f.startswith("flush_data_") and f.endswith(".txt"))]

    if len(flush_data_files) == 0:
        raise FileNotFoundError(f"No flush data files found in the directory {argparse_args.input_directory}.")
    
    flush_files_and_dataframes = dict()

    for flush_data_file in flush_data_files:
        flush_data_file_path = os.path.join(argparse_args.input_directory, flush_data_file)

        # Each flush_data_*.txt file starts with two header rows:
        # "colors"
        # <list of colors>
        flush_data_df = pandas.read_csv(flush_data_file_path, skiprows=2)

        flush_files_and_dataframes[flush_data_file] = flush_data_df

    print(f"[DEBUG] Creating database from {len(flush_files_and_dataframes)} flush data files")