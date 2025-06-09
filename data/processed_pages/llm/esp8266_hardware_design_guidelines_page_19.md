# ESP8266EX PCB Design and Module Positioning

## PCB Layer Recommendations

- **Third Layer (POWER layer):** Only power lines should be placed here. It is acceptable to place some signal lines under unavoidable circumstances.

- **Fourth Layer (BOTTOM layer):** Only signal lines can be laid. Placing components on this layer is not recommended.

### Two-layer PCB Design Suggestions

- **First Layer (TOP layer):** Used for signal traces and components.

- **Second Layer (BOTTOM layer):** Used for power traces. Placing any components on this layer is not recommended.

- Do not route any power or signal traces under or around the RF and crystal oscillator.

- Ensure a complete GND plane connected to the Ground Pad at the bottom of the chip.

## Positioning an ESP8266EX Module on a Base Board

When adopting an on-board design, pay attention to the layout of the module on the base board to minimize interference affecting the module's antenna performance.

- It is recommended that the PCB antenna area of the module be placed outside the base board.

- The module should be placed as close as possible to the edge of the base board so that the feed point of the antenna is closest to the board.

---

*Figure 1-13. ESP8266EX Module Antenna Position on Base Board*

---

*Page 20*