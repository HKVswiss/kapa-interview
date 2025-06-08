# ESP8266EX RF Design and Crystal Oscillators

## Figure 1-16. ESP8266EX Crystal Oscillators

## 1.6.3.3. RF Design

- The characteristic RF impedance is 50 Ω.
- The ground plane should be complete.
- The RF trace should be as short as possible with dense ground via stitching around it for isolation.
- The width of RF lines should be as short as possible and there should be dense vias stitched around.
- π-type matching circuitry should be reserved on the RF trace and placed close to the RF Pin2.
- The components of the π-matching network should be placed in the same direction (see Figure 1-17).
- There should be no vias for the RF trace.
- The RF trace should be routed at a 135° angle, or with circular arcs if trace bends are required.
- There should be no RF routing around the high-frequency signal lines.
- The RF antenna should be set away from high-frequency transmitting devices, such as crystal oscillators, DDR, and certain high frequency clocks (SDIO_CLK, etc.).
- USB ports, USB-to-UART signal chips, UART signal lines (including traces, vias, test points, headers, etc.) must be placed as far away from the antenna as possible.
- The UART signal line is packaged and ground shielding is added.
- For PCB onboard antenna design, please refer to Type-B version by Espressif.
- If there are power traces near the antenna, the power traces and antenna must be isolated with GND copper.

---

*Page 23*