# About

Bambu Studio has the ability to export config settings. You can export filament settings, or actual printer nozzle settings.

Filament setting files have the `.bbsflmt` extension and printer nozzle settings have the `.bbscfg` extension.

Both are ZIP files: `Zip archive data, at least v2.0 to extract, compression method=deflate`

See the `misc_config` directory for examples of these.

# bbscfg

After extracting, you'll see this structure:

```
├── bundle_structure.json
├── filament
│   └── Bambu PLA Basic @BBL X1C - Max Strength.json
├── printer
│   └── Bambu Lab X1 Carbon 0.4 nozzle.json
└── process
    └── 0.20mm Strength @BBL X1C - Max Strength.json

4 directories, 4 files
```

`bundle_structure.json` is the metadata file. It has these fields:

```json
{
  "bundle_id": "2540517070_Bambu Lab X1 Carbon 0.4 nozzle_1711133062",
  "bundle_type": "printer config bundle",
  "filament_config": [
    "filament/Bambu PLA Basic @BBL X1C - Max Strength.json"
  ],
  "printer_config": [
    "printer/Bambu Lab X1 Carbon 0.4 nozzle.json"
  ],
  "printer_preset_name": "Bambu Lab X1 Carbon 0.4 nozzle",
  "process_config": [
    "process/0.20mm Strength @BBL X1C - Max Strength.json"
  ],
  "user_id": "2540517070",
  "user_name": "raleighlittles@gmail.com",
  "version": "01.08.04.06"
}
```

The json file under the filament directory looks like this:

```json
{
    "additional_cooling_fan_speed": [
        "0"
    ],
    "close_fan_the_first_x_layers": [
        "3"
    ],
    "filament_settings_id": [
        "Bambu PLA Basic @BBL X1C - Max Strength"
    ],
    "from": "User",
    "inherits": "Bambu PLA Basic @BBL X1C",
    "is_custom_defined": "0",
    "name": "Bambu PLA Basic @BBL X1C - Max Strength",
    "reduce_fan_stop_start_freq": [
        "0"
    ],
    "slow_down_min_speed": [
        "5"
    ],
    "version": "1.8.0.18"
}
```

The json file under the process directory looks like this:

```json
{
    "type": "machine",
    "name": "Bambu Lab X1 Carbon 0.4 nozzle",
    "inherits": "fdm_bbl_3dp_001_common",
    "from": "system",
    "setting_id": "GM001",
    "instantiation": "true",
    "nozzle_diameter": [
        "0.4"
    ],
    "printer_model": "Bambu Lab X1 Carbon",
    "printer_variant": "0.4",
    "bed_exclude_area": [
        "0x0",
        "18x0",
        "18x28",
        "0x28"
    ],
    "default_filament_profile": [
        "Bambu PLA Basic @BBL X1C"
    ],
    "default_print_profile": "0.20mm Standard @BBL X1C",
    "extruder_offset": [
        "0x2"
    ],
    "machine_load_filament_time": "29",
    "machine_unload_filament_time": "28",
    "scan_first_layer": "1",
    "upward_compatible_machine": [
        "Bambu Lab P1S 0.4 nozzle",
        "Bambu Lab P1P 0.4 nozzle",
        "Bambu Lab X1 0.4 nozzle",
        "Bambu Lab X1E 0.4 nozzle",
        "Bambu Lab A1 0.4 nozzle"
    ],
    "machine_start_gcode": "",
    "change_filament_gcode": ""
}
```

(the g code fields have been removed for the sake of brevity)

# bbsflmt

The structure looks like this:

```
├── BBL
│   └── Bambu PLA Basic @BBL X1C - Max Strength.json
└── bundle_structure.json

2 directories, 2 files
```

Just like the bbscfg files, there is a `bundle_structure.json` metadata file:

```json
{
  "bundle_id": "2540517070_Bambu PLA Basic_1711133078",
  "bundle_type": "filament config bundle",
  "filament_name": "Bambu PLA Basic",
  "printer_vendor": [
    {
      "filament_path": [
        "BBL/Bambu PLA Basic @BBL X1C - Max Strength.json"
      ],
      "vendor": "BBL"
    }
  ],
  "user_id": "2540517070",
  "user_name": "raleighlittles@gmail.com",
  "version": "01.08.04.06"
}
```

The json file under the BBL directory looks like this:

```json
{
    "additional_cooling_fan_speed": [
        "0"
    ],
    "close_fan_the_first_x_layers": [
        "3"
    ],
    "filament_settings_id": [
        "Bambu PLA Basic @BBL X1C - Max Strength"
    ],
    "from": "User",
    "inherits": "Bambu PLA Basic @BBL X1C",
    "is_custom_defined": "0",
    "name": "Bambu PLA Basic @BBL X1C - Max Strength",
    "reduce_fan_stop_start_freq": [
        "0"
    ],
    "slow_down_min_speed": [
        "5"
    ],
    "version": "1.8.0.18"
}
```

