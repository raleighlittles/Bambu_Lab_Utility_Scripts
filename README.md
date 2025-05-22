# About

This repository contains a set of utility scripts centered around the Bambu Lab's 3D printer ecosystem.

The most important directories are:

1. `RFID_dump_decoder`, which provides a helper script for decoding the RFID tags on Bambu Lab's filament.

2. `ipcam_directory_organizer`, which provides a helper script for organizing the videos that the Bambu Labs print chamber cameras.

3. `build_plate_markers`, which provides scripts for generating and detecting build plate marker images, as well as the build plate markers by themselves.

4. `docs`, which provides general documentation (schematics/PDFs/etc) on different Bambu Labs parts.

Apart from that, I've also included several useful files that are included in the Bambu Studio installation. These directories are:

* `bambu-parts-stl` : STL models of different Bambu Labs parts, like the plates and hotend
* `calibration` : STL/3MF models that you can use to calibrate your printer when setting it up
* `cover_images` : The default 'profile' images for each printer. Helpful if you use any kind of home automation software and want your device's icon to match.
* `default-models` : The default 'test' models (STL only) that come pre-installed on the printer. These include the famous ['Benchy'](https://en.wikipedia.org/wiki/3DBenchy)
* `gcode` : The G-Code used to do loading and unloading of filament if you have an AMS
* `hms` : The "Health Management System" part of Bambu. Basically contains a list of known error codes and descriptions, plus images to diagnose/repair.
* `icons` : Icon pack of UI icons, that come installed with Bambu Studio. In this directory there is also a Rust script for decoding `icns` files that may be generally useful.
* `flush_data`: The flushing data presets, used by the printer when changing filament during a multi-filament print

Each directory has its own README.md with more info.
