# ESP8266EX Analog Power Supply

## Overview

ESP8266EX has five analog pins for power supply:
- Pin 1, Pin 3, Pin 4: Power supply for internal PA (Power Amplifier) and LNA (Low Noise Amplifier).
- Pin 29, Pin 30: Power supply for the internal PLL (Phase-Locked Loop).

The operating voltage for these analog power supply pins is **2.5 V to 3.6 V**.

## Important Notes

- The power supply channel might be damaged due to sudden current increases when ESP8266EX is transmitting analog signals.
- To protect the power supply channel, it is recommended to add an additional **10 µF capacitor** (package 0603 or 0805) in parallel with the existing **0.1 µF capacitor**.
- ESP8266EX's EMC (Electromagnetic Compatibility) complies with FCC and CE requirements, so there is no need to add ferrite beads in the analog power-supply circuit.
- When using a single power supply, the recommended output current is **500 mA**.
- It is suggested to add an ESD (Electrostatic Discharge) protection tube at the power entrance.

## Figures

### Figure 1-4. ESP8266EX Digital Power Supply Pins

(Refer to the original document for the detailed pin diagram.)

### Figure 1-5. ESP8266EX AVDD (Analog Power Supply) Circuit

```
VDD33
 + -- ond |
ce
6]
8,
= = N
41µF] 1µF (NC)
R1
— — 12K41%
vDD33
GND GND
...
10µF] 0.1µF] TBD (NC)
GND VDDA VDDD
GND GND GND _f
RES12K EXT_RSTB
ANTI
WIFI_ANT. C4, W~\AA\2.2nH VDDA
NA
C4 VDD3P3
. rs VDD3P3
```

(Refer to the original document for the complete circuit schematic.)

---

*Page 12*