

def get_basename(video_filename):

    parsed_video_filename_fields = parse_video_filename(video_filename)

    return f"{parsed_video_filename_fields.get('prefix')}_{parsed_video_filename_fields.get('timestamp')}"


def get_index(video_filename):

    parse_video_filename_fields = parse_video_filename(video_filename)

    return int(parse_video_filename_fields.get("index"))


def parse_video_filename(video_filename):
    """
    A video filename looks like: "ipcam-record.2024-02-25_21-35-33.482.mp4"
    """

    common_prefix, timestamp, current_idx, mp4_extension = video_filename.split(
        ".")

    # sanity check
    if common_prefix != "ipcam-record" or mp4_extension != "mp4":
        raise ValueError(
            f"Filename '{video_filename}' does not appear to be formatted correctly")

    return {"prefix": common_prefix, "timestamp": timestamp, "index": current_idx}
