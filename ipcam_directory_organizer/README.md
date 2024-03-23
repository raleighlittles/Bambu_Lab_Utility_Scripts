# About/Background

Python script for organizing the videos in the `ipcam` directory on the printer's microSD card.

Bambu Studio stores these videos for each print, but there is a short maximum video time (usually around 10 minutes). So for example, a 3 hour print will result in 18 videos, each sequentially named. This script will concatenate those videos together using [ffmpeg](https://ffmpeg.org/) so that you have a single video per print.

# Usage

```
usage: ipcam_directory_organizer.py [-h] -i INPUT_DIRECTORY

options:
  -h, --help            show this help message and exit
  -i INPUT_DIRECTORY, --input-directory INPUT_DIRECTORY
                        The directory to organize videos in

```