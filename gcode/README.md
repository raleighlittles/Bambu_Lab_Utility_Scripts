# About

Contains the default [G-code](https://en.wikipedia.org/wiki/G-code) implementation for AMS.

The actual code is in the files, below is an annotated version for each.

On Windows, you can get these files from this directory:
```
C:\Users\%USERNAME%\AppData\Roaming\BambuStudio\printers
```

# Code

## Load

```gcode
M620 S[next_extruder]    ; Activate extruder [next_extruder] (custom command, machine-specific)
M106 S255                ; Set fan speed to full (255 = 100%)
M104 S250                ; Set hotend temperature to 250°C, without waiting
M17 S                    ; Enable all stepper motors (some firmware-specific variant)
M17 X0.5 Y0.5            ; Set current for X and Y stepper motors to 50% (firmware-dependent)
G91                      ; Set to **relative positioning**
G1 Y-5 F1200             ; Move Y axis by -5mm at 1200 mm/min
G1 Z3                    ; Move Z axis up by 3mm
G90                      ; Set back to **absolute positioning**
G28 X                    ; Home X axis
M17 R                    ; Enable 'R' stepper motor
G1 X70 F21000            ; Move to X=70 at 21000 mm/min (very fast)
G1 Y245                  ; Move to Y=245
G1 Y265 F3000            ; Move to Y=265 at 3000 mm/min
G4                       ; Dwell (pause) for default time (often 0 ms)
M106 S0                  ; Turn off fan
M109 S250                ; Set hotend to 250°C **and wait until it reaches the temperature**
G1 X90                   ; Move to X=90
G1 Y255                  ; Move to Y=255
G1 X120                  ; Move to X=120
G1 X20 Y50 F21000        ; Move to X=20, Y=50 at 21000 mm/min
G1 Y-3                   ; Move to Y=-3 (relative move if previous G91 active)
T[next_extruder]         ; Switch to extruder [next_extruder]
G1 X54                   ; Move to X=54
G1 Y265                  ; Move to Y=265
G92 E0                   ; Reset extruder position to 0
G1 E40 F180              ; Extrude 40mm of filament at 180 mm/min
G4                       ; Dwell
M104 S[new_filament_temp]; Set hotend to [new_filament_temp], don't wait
G1 X70 F15000            ; Move to X=70 at 15000 mm/min
G1 X76                   ; Move to X=76
G1 X65                   ; Move to X=65
G1 X76                   ; Move to X=76
G1 X65                   ; Move to X=65
G1 X90 F3000             ; Move to X=90 at 3000 mm/min
G1 Y255                  ; Move to Y=255
G1 X100                  ; Move to X=100
G1 Y265                  ; Move to Y=265
G1 X70 F10000            ; Move to X=70 at 10000 mm/min
G1 X100 F5000            ; Move to X=100 at 5000 mm/min
G1 X70 F10000            ; Move to X=70 at 10000 mm/min
G1 X100 F5000            ; Move to X=100 at 5000 mm/min
G1 X165 F12000           ; Move to X=165 at 12000 mm/min
G1 Y245                  ; Move to Y=245
G1 X70                   ; Move to X=70
G1 Y265 F3000            ; Move to Y=265 at 3000 mm/min
G91                      ; Set to **relative positioning**
G1 Z-3 F1200             ; Move Z down by 3mm
G90                      ; Set back to **absolute positioning**
M621 S[next_extruder]    ; Custom: likely finalize extruder [next_extruder] configuration
```

## Unload

```gcode
M620 S255              ; Custom command — likely activate or prepare extruder 255 (machine-specific)
M106 P1 S255           ; Set fan 1 to full speed (255 = 100%)
M104 S250              ; Set hotend temperature to 250°C, don't wait
M17 S                  ; Enable all stepper motors (possibly firmware-specific variant)
M17 X0.5 Y0.5          ; Set current for X and Y stepper motors to 50% (machine/firmware-dependent)
G91                    ; Set to **relative positioning mode**
G1 Y-5 F3000           ; Move Y axis -5mm at 3000 mm/min
G1 Z3 F1200            ; Move Z axis up by 3mm at 1200 mm/min
G90                    ; Return to **absolute positioning mode**
G28 X                  ; Home the X axis
M17 R                  ; Custom or machine-specific motor-related command (could be 'reset' or 'release')
G1 X70 F21000          ; Move to X=70 at 21000 mm/min (very fast)
G1 Y245                ; Move to Y=245
G1 Y265 F3000          ; Move to Y=265 at 3000 mm/min
G4                     ; Dwell (pause) — default duration or firmware-specific
M106 P1 S0             ; Turn off fan 1
M109 S250              ; Set hotend to 250°C **and wait until it reaches that temperature**
G1 X90 F3000           ; Move to X=90 at 3000 mm/min
G1 Y255 F4000          ; Move to Y=255 at 4000 mm/min
G1 X100 F5000          ; Move to X=100 at 5000 mm/min
G1 X120 F21000         ; Move to X=120 at 21000 mm/min
G1 X20 Y50             ; Move to X=20 and Y=50 (using absolute positioning)
G1 Y-3                 ; Move to Y=-3 (if in absolute, odd move — if relative, move Y down 3mm)
T255                   ; Tool/extruder change to tool 255 (possibly a custom tool index)
G4                     ; Dwell (pause)
M104 S0                ; Set hotend temperature to 0°C (turn it off)
G1 X70 F3000           ; Move to X=70 at 3000 mm/min
G91                    ; Switch to **relative positioning**
G1 Z-3 F1200           ; Move Z down by 3mm at 1200 mm/min
G90                    ; Switch back to **absolute positioning**
M621 S255              ; Custom command — likely finalize or deactivate extruder 255 (machine-specific)
```