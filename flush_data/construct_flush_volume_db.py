import argparse
import os
import pandas
import pdb
import sqlite3

def check_flush_data_symmetry(flush_data_df):
    """
    Check if the flush data is symmetric, i.e., if flush_data_df["src"] -> flush_data_df["dst"]
    is equal to flush_data_df["dst"] -> flush_data_df["src"].
    """
    # Create a new dataframe with the reversed src and dst columns
    reversed_df = flush_data_df.copy()
    reversed_df[["src", "dst"]] = flush_data_df[["dst", "src"]]

    # Check if the two dataframes are equal
    return pandas.DataFrame.equals(flush_data_df, reversed_df)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Construct flush volume database")
    parser.add_argument("--input-directory", "-i", type=str, required=True,
                        help="The path to where the flush data text files are stored")
    argparse_args = parser.parse_args()

    if not os.path.exists(argparse_args.input_directory):
        raise FileNotFoundError(
            f"The input directory {argparse_args.input_directory} does not exist.")

    files_in_dir = os.listdir(argparse_args.input_directory)
    flush_data_files = [f for f in files_in_dir if (
        f.startswith("flush_data_") and f.endswith(".txt"))]

    if len(flush_data_files) == 0:
        raise FileNotFoundError(
            f"No flush data files found in the directory {argparse_args.input_directory}.")

    flush_files_and_dataframes = dict()
    expected_num_rows = 0

    for flush_data_file in flush_data_files:
        flush_data_file_path = os.path.join(
            argparse_args.input_directory, flush_data_file)

        # Each flush_data_*.txt file starts with two header rows:
        # "colors"
        # <list of colors>
        flush_data_df = pandas.read_csv(flush_data_file_path, skiprows=2, sep=" ")
        expected_num_rows += flush_data_df.shape[0]

        flush_files_and_dataframes[flush_data_file] = flush_data_df

    print(
        f"[DEBUG] Creating database from {len(flush_files_and_dataframes)} flush data files, {expected_num_rows} expected rows")

    # Create a single dataframe from all flush data files
    combined_df = pandas.concat(
        flush_files_and_dataframes.values(), ignore_index=True)
    combined_df = pandas.DataFrame.drop_duplicates(
        combined_df, ignore_index=True)
    
    # Now store that combined dataframe into a database file
    db_conn = sqlite3.connect("flush_volume.db")
    db_cursor = db_conn.cursor()

    db_cursor.execute("""CREATE TABLE IF NOT EXISTS flush_volume (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      src_color TEXT,
                      dst_color TEXT,
                      flush_volume_mm3 INTEGER)""")
    
    for index, row in combined_df.iterrows():
        # Insert each row into the database
        db_cursor.execute("INSERT INTO flush_volume (src_color, dst_color, flush_volume_mm3) VALUES (?, ?, ?)",
                          (row["src"], row["dst"], row["flush"]))

    db_conn.commit()
    db_conn.close()

    print(f"[DEBUG] Created database with {len(combined_df)} rows (size {os.path.getsize('flush_volume.db')} bytes)")
    