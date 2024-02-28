import argparse
import os
import subprocess

# locals
import ffmpeg_helper
import video_filename_helper


def combine_videos_from_sequences(directory, video_sequences):

    print(f"[DEBUG] Creating '{len(video_sequences)}' videos from sequences")

    for video_sequence_idx, video_sequence in enumerate(video_sequences):

        concat_demuxer_filename = f"{video_sequence_idx}_ffmpeg_demuxer.txt"

        ffmpeg_helper.build_concat_demuxer_list([os.path.join(
            directory, video_filename) for video_filename in video_sequence], concat_demuxer_filename)

        ffmpeg_concat_videos_cmd = f"""ffmpeg -f concat -safe 0 -i {concat_demuxer_filename} -c copy '{video_filename_helper.get_basename(video_sequence[0])}.mp4' """

        subprocess.run(ffmpeg_concat_videos_cmd,
                       shell=True, stdout=subprocess.PIPE)

        # cleanup
        os.remove(concat_demuxer_filename)


def group_ipcam_videos(directory):

    all_videos = sorted([filename for filename in os.listdir(
        directory) if filename.endswith(".mp4")])

    print(
        f"[DEBUG] '{len(all_videos)}' videos found in directory '{directory}'")

    video_sequences = list()

    current_video_sequence = list()

    initial_conditions, previous_idx = True, -1

    for video_filename in all_videos:

        # As long as the index keeps going up, keep adding it to the current sequence
        # once the index goes back to zero (OR a lower number), then stop, and start a new sequence

        current_idx = video_filename_helper.get_index(video_filename)

        # print(
        #    f"[DEBUG] Analyzing element with index: '{current_idx}' and previous index '{previous_idx}'")

        # You're at the first element
        if initial_conditions:
            current_video_sequence.append(video_filename)
            initial_conditions = False
            previous_idx = current_idx

        else:
            # The count is rising, so add the current video
            if (previous_idx + 1) == current_idx:
                current_video_sequence.append(video_filename)
                previous_idx = current_idx

            else:  # either the count reset or an element was skipped, in either case, stop incrementing the chain
                video_sequences.append(current_video_sequence)
                print(
                    f"[DEBUG] Finished sequence of length '{len(current_video_sequence)}'")
                current_video_sequence = list()
                previous_idx = current_idx

        # end for loop

    return [sequence for sequence in video_sequences if len(sequence) > 1]


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument(
        "-i", "--input-directory", help="The directory to organize videos in", type=str, required=True)

    argparse_args = argparse_parser.parse_args()

    ipcam_dir = argparse_args.input_directory

    if os.path.exists(ipcam_dir):

        video_sequences = group_ipcam_videos(ipcam_dir)
        combine_videos_from_sequences(ipcam_dir, video_sequences)

    else:
        raise FileNotFoundError(f"ERROR: Can't find directory '{ipcam_dir}'")
