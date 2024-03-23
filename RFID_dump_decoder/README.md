# About

Bambu Labs filament spools come with RFID tags that the AMS reads to determine which type of filament is being used.

You can decode these RFID tags using the [guide here](https://github.com/Bambu-Research-Group/RFID-Tag-Guide).

The output of that process is either a json or a bin file. This script decodes that into meaningful output, like this:

```
-------------------------------
Filament SKU: A00-A0
Filament type: 'PLA' (PLA Basic)
Spool weight: 250 g (0.25 kg)
Filament diameter: 1.75 mm
Red: 255 Green: 106 Blue: 19 Alpha: 255 | Raw: #ff6a13
Hotend temperature range: 190 — 230 °C
Bed temperature: 230 °C (446 °F)
Drying temp: 55 °C (131 °F) | Drying time: 8 hours
Bed plate type index = 1 | Likeliest type: PLA
Spool width: 66.25 mm (2.6 inches)
Year: 2023 | Month: 09 (September) | Day: 05 | Hour: 09 | Minute: 50
Filament length: 82 m (269 ft)
===============================
```

# Usage

```
usage: decode_rfid_tag_dump.py [-h] [-j INPUT_JSON_DUMP_FILE]

options:
  -h, --help            show this help message and exit
  -j INPUT_JSON_DUMP_FILE, --input-json-dump-file INPUT_JSON_DUMP_FILE
                        The input JSON file to decode

```