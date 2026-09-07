# Bambu Lab Printer Capabilities Reference

This directory contains the machine capability definitions (`.json`) utilized across the Bambu Lab ecosystem (Bambu Studio, Bambu Handy, and cloud/local slicer integrations). These profiles define hardware specifications, thermal thresholds, kinematics, vision/sensing hardware, multi-material AMS support, and functional feature flags across firmware versions.

---

## Master Printer Capabilities Table

| JSON File | Model ID | Display Name | Series / Arch | Enclosed | Max Nozzle / Bed Temp | Active Chamber Heat | Extruders | Supported Modes | Auto Bed Leveling | Flow Calibration | Micro-LiDAR | AI Failure Monitoring | Camera Resolution | Onboard Print (No SD) | AMS Type |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [BL-P001.json](./BL-P001.json) | `BL-P001` | **Bambu Lab X1 Carbon** | `series_x1` (CoreXY) | Yes | 300°C / 110–120°C | No | 1 (Single) | FDM | Type 1 | Manual + LiDAR | Yes | Yes (First Layer + Spaghetti) | 720p & 1080p | Yes (eMMC) | Generic (AMS) |
| [BL-P002.json](./BL-P002.json) | `BL-P002` | **Bambu Lab X1** | `series_x1` (CoreXY) | Yes | 300°C / 110–120°C | No | 1 (Single) | FDM | Type 1 | Manual + LiDAR | Yes | Yes (First Layer + Spaghetti) | 720p & 1080p | Yes (eMMC) | Generic (AMS) |
| [C11.json](./C11.json) | `C11` | **Bambu Lab P1P** | `series_p1p` (CoreXY) | No (Open) | 300°C / 100°C | No | 1 (Single) | FDM | Type 1 | Extrusion Manual Cali | No | No | 720p (0.5 fps) | No (Requires SD) | Generic (AMS) |
| [C12.json](./C12.json) | `C12` | **Bambu Lab P1S** | `series_p1p` (CoreXY) | Yes | 300°C / 100°C | No | 1 (Single) | FDM | Type 1 | Extrusion Manual Cali | No | No | 720p (0.5 fps) | No (Requires SD) | Generic (AMS) |
| [C13.json](./C13.json) | `C13` | **Bambu Lab X1E** | `series_x1` (CoreXY) | Yes | 320°C / 110°C | Yes (Up to 60°C) | 1 (Single) | FDM | Type 1 | Manual + LiDAR | Yes | Yes (First Layer + Spaghetti) | 720p & 1080p | Yes (eMMC) | Generic (AMS) |
| [N1.json](./N1.json) | `N1` | **Bambu Lab A1 mini** | `series_n` (i3 Bed-Slinger) | No (Open) | 300°C / 80°C | No | 1 (Single) | FDM | Type 1 | Extrusion Cali (Sensor) | No | No | 720p | No (Requires SD) | `f1` (AMS lite) |
| [N2S.json](./N2S.json) | `N2S` | **Bambu Lab A1** | `series_n` (i3 Bed-Slinger) | No (Open) | 300°C / 100°C | No | 1 (Single) | FDM | Type 1 | Extrusion Cali (Sensor) | No | No | 720p | No (Requires SD) | `f1` (AMS lite) |
| [N7.json](./N7.json) | `N7` | **Bambu Lab P2S** | `series_x1` (CoreXY) | Yes | 300°C / 110°C | No (Duct recirculation) | 1 (Single) | FDM | Type 2 | Auto Flow Cali | No | Yes (Spaghetti/Failure) | 1080p | Yes | Generic (AMS) |
| [O1C.json](./O1C.json) | `O1C` | **Bambu Lab H2C** | `series_o` (CoreXY) | Yes | 350°C / 120°C | Yes (Up to 65°C) | 2 (Dual Toolhead) | FDM, Laser, Cut | Type 2 | Auto Flow Cali | No | Yes | 1080p | Yes | Generic (AMS) |
| [O1C2.json](./O1C2.json) | `O1C2` | **Bambu Lab H2C (V2)** | `series_o` (CoreXY) | Yes | 350°C / 120°C | Yes (Up to 65°C) | 2 (Dual Toolhead) | FDM, Laser, Cut | Type 2 | Auto Flow Cali | No | Yes | 1080p | Yes | Generic (AMS) |
| [O1D.json](./O1D.json) | `O1D` | **Bambu Lab H2D** | `series_o` (CoreXY) | Yes | 350°C / 120°C | Yes (Up to 65°C) | 2 (Dual Toolhead) | FDM, Laser, Cut | Type 2 | Auto Flow Cali | No | Yes | 1080p | Yes | Generic (AMS) |
| [O1E.json](./O1E.json) | `O1E` | **Bambu Lab H2D Pro** | `series_o` (CoreXY) | Yes | 350°C / 120°C | Yes (Up to 65°C) | 2 (Dual Toolhead) | FDM, Laser, Cut | Type 2 | Auto Flow Cali | No | Yes | 1080p | Yes | Generic (AMS) |
| [O1S.json](./O1S.json) | `O1S` | **Bambu Lab H2S** | `series_o` (CoreXY) | Yes | 350°C / 120°C | Yes (Up to 65°C) | 1 (Single) | FDM, Laser, Cut | Type 2 | Auto Flow Cali | No | Yes | 1080p | Yes | Generic (AMS) |

---

## Detailed Capability Breakdown

### 1. Thermal & Motion Architecture

* **X1 Series (`BL-P001`, `BL-P002`, `C13`)**: Enclosed CoreXY chassis. The X1E (`C13`) adds active chamber heating up to 60°C and a higher nozzle limit (320°C) with an ethernet chip (`rv2166`).
* **P1 Series (`C11`, `C12`)**: CoreXY chassis. P1P is open-frame; P1S is enclosed with a chamber fan. Both cap the heated bed at 100°C.
* **A1 Series (`N1`, `N2S`)**: Open-frame `i3` Cartesian bed-slingers. Bed limits are 80°C (A1 mini) and 100°C (A1).
* **P2S (`N7`)**: Enclosed CoreXY with an advanced dual-air duct system:
  * **Cooling mode**: `Left(Aux)` + `Right(Aux)` for PLA/TPU.
  * **Heating mode**: `Left(Aux)` + `Right(Filter)` internal air recirculation & filtering for PETG/ABS/ASA/PC/PA.
* **H2 Series (`O1C`, `O1C2`, `O1D`, `O1E`, `O1S`)**: High-temperature multi-function CoreXY platforms reaching 350°C nozzle and 120°C bed, with active chamber heating editable between 0–65°C (`support_chamber_temp_switch_heating: 40°C`).

---

### 2. Calibration, Probing & AI Computer Vision

| Printer Family / Model | Bed Leveling | Micro-LiDAR | Auto Flow Calibration | Nozzle Offset Cali | Clump Position Cali | Spool / Nozzle Wrapping Detect | Step Loss Auto-Recovery | Plate Marker Detection |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **X1 / X1C / X1E** | Type 1 | Yes | Manual / LiDAR | N/A | No | No | Yes | Type 1 (AprilTag / ArUco) |
| **P1P / P1S** | Type 1 | No | Manual Extrusion | N/A | No | No | Yes | None |
| **A1 mini / A1** | Type 1 | No | Nozzle Pressure Sensor | N/A | No | No | Yes | None |
| **P2S (N7)** | Type 2 | No | Yes (Integrated Auto) | No | Yes | Yes | Yes | Type 2 |
| **H2C / H2D / H2D Pro** | Type 2 | No | Yes (Multi-Extruder) | Yes (Dual Nozzle) | No | Yes | Yes | Type 2 |
| **H2S** | Type 2 | No | Yes (Single Extruder) | No (Single Nozzle) | No | Yes | Yes | Type 2 |

---

### 3. Ecosystem & Multi-Material Capabilities

* **AMS Compatibility**:
  * **Generic AMS (Enclosed 4-slot)**: Supported on X1, X1C, X1E, P1P, P1S, P2S, and all H2 printers (`use_ams_type: "generic"`). Includes humidity sensor reading and external spool mixed printing.
  * **AMS lite (Open 4-spool rotary)**: Supported exclusively on A1 mini and A1 (`use_ams_type: "f1"`). Features air print / tangle detection (`air_print_detection_position: "ams_setting"`).
* **Audio & Melodies**:
  * Only the A1 and A1 mini feature an internal speaker/piezo system for prompt audio and startup/completion melodies (`support_prompt_sound: true`).
* **Active Motor Noise Calibration**:
  * Only the A1 and A1 mini include `support_motor_noise_cali: true`.
* **Multi-Toolhead & Multi-Mode (Laser & Blade Cutting)**:
  * The **H2 Series** (`series_o`) are 3-in-1 machines supporting `fdm`, `laser`, and `cut`. They include 2D laser processing profiles supporting 10W and 40W laser modules (`2D.laser.power: [10, 40]`).
  * The `O1C`, `O1C2`, `O1D`, and `O1E` feature dual extruders (`['ext_image_o_right', 'ext_image_o_left']`), dual nozzle offset calibration, and left-extruder TPU checks.
  * The `O1S` is the single-extruder variant (`ext_image_o1s`).

---

### 4. Storage & Network Security

* **Direct Printing / Storage**:
  * X1, X1C, X1E, P2S, and H2 series support `support_print_without_sd: true` and `support_save_remote_print_file_to_storage: true` via internal eMMC/flash storage.
  * P1P, P1S, A1 mini, and A1 require an external MicroSD card for local print caching (`ftp_folder: "sdcard/"`).
* **Security & Network**:
  * X1E, P2S, and all H2 series have `support_ssl_for_mqtt: true` and `support_tunnel_mqtt: true` for encrypted and enterprise MQTT communication.

