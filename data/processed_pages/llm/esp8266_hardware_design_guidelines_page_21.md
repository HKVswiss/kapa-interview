# ESP8266EX PCB Layout and Crystal Oscillator Design

## ESP8266EX Grounding

- The center ground pad at the bottom of the chip should be connected to the ground plane through at least 9 ground vias.

## Crystal Oscillator Design

- The crystal oscillator should be placed as close to the XTAL pins as possible without making the traces too long.
- The crystal cannot be placed too close to the chip to prevent interference; the recommended distance is 0.8 mm (see Figure 1-16 in the original document).
- It is good practice to use via stitching around the clock trace to ensure low ground-plane impedance.
- There should be no vias on the input and output traces; thus, the traces cannot cross layers.
- Input and output traces should not be routed over one another, even on different layers.
- Place the input and output bypass capacitors near the left or right side of the chip, not on the traces.
- Do not route high-frequency digital signal lines under the crystal oscillator; ideally, avoid routing any signal line underneath it.
- A larger copper area on the top layer around the crystal oscillator is beneficial.
- Avoid placing magnetic components nearby that may cause interference, such as power-switching converter components or unshielded inductors.

---

*Page 22*