# ESP8266EX Analog Power Supply

## Overview

ESP8266EX has five analog power supply pins:
- Pin 1, Pin 3, Pin 4: Power supply for internal PA (Power Amplifier) and LNA (Low Noise Amplifier).
- Pin 29, Pin 30: Power supply for the internal PLL (Phase-Locked Loop).

The operating voltage for these analog power supply pins is **2.5 V to 3.6 V**.

## Important Notes

- The power supply channel might be damaged due to sudden current surges when ESP8266EX transmits analog signals.
- To protect the power supply channel, it is recommended to add an additional **10 µF capacitor** (package 0603 or 0805) in parallel with the existing 0.1 µF capacitor.
- ESP8266EX's EMC (Electromagnetic Compatibility) complies with FCC and CE requirements; therefore, ferrite beads are not necessary in the analog power-supply circuit.
- When using a single power supply, the recommended output current is **500 mA**.
- It is suggested to add an ESD (Electrostatic Discharge) protection tube at the power entrance.

## Figures

### Figure 1-4: ESP8266EX Digital Power Supply Pins

*(Diagram not included here)*

### Figure 1-5: ESP8266EX AVDD (Analog Power Supply) Circuit

*(Diagram not included here)*

---

*Page 12*