import argparse
import json
import os
import datetime
import requests
import random
import time


def download_image_from_url(image_url, image_filename):
    """
    https://stackoverflow.com/a/30229298/1576548
    """
    with open(image_filename, mode="wb") as img_file:

        resp = requests.get(image_url)

        if not resp.ok:
            print(f"ERROR! Failed to download image: {image_url}")

        for block in resp.iter_content(1024):
            img_file.write(block)

        # print(f"[DEBUG] Finished saving image '{image_filename}'. Filesize = {os.path.getsize(image_filename)} bytes")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Extract image paths from JSON file")
    parser.add_argument("-f", "--json-file", type=str,
                        help="Path to the JSON file. Should be called something like 'hms_action_<version>.json'", required=True)
    args = parser.parse_args()

    if not os.path.isfile(args.json_file):
        raise FileNotFoundError("ERROR! Can't find provided JSON file '{}'".format(args.json_file))

    with open(file=args.json_file, mode='r', encoding="utf-8") as hsm_action_file:
        json_data = json.load(hsm_action_file)
        last_updated_timestamp = json_data["t"]
        last_updated_date = datetime.datetime.fromtimestamp(
            last_updated_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        json_version = str(json_data["ver"])

        print(
            f"[DEBUG] JSON version: {json_version} | Last updated: {last_updated_date}")

        output_directory = "hms-images_" + json_version
        os.makedirs(output_directory, exist_ok=False)

        images_error_and_urls = {}
        image_key = "image"
        for data_elem_idx, data_elem in enumerate(json_data["data"]):

            if not image_key in data_elem:
                print(
                    f"[DEBUG] No image key found in data element idx {data_elem_idx}: {data_elem}")
                continue

            image_url = data_elem[image_key]

            if image_url == "":
                print(
                    f"[DEBUG] No URL found in data element idx {data_elem_idx}: {data_elem}")
                continue

            images_error_and_urls[data_elem["ecode"]] = image_url

        print(
            f"[DEBUG] Storing {len(images_error_and_urls)} images into {output_directory}")

        for error_code, image_url in images_error_and_urls.items():

            image_url_ext = os.path.splitext(image_url)[1]
            image_filename = f"{error_code}{image_url_ext}"

            image_filepath = os.path.join(output_directory, image_filename)

            download_image_from_url(image_url, image_filepath)

            # Sleep to avoid being rate-limited/throttled by their server
            time.sleep(random.uniform(1.0, 3.0))
