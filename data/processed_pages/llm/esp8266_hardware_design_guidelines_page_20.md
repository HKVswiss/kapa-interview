# ESP8266EX Module Placement and Power Supply Design

## Recommended Module Positioning

As shown in Figure 1-13, the recommended positions for placing the ESP8266EX module on the base board are:

- **Position 3, 4:** Highly recommended
- **Position 1, 2, 5:** Not recommended

If the recommended positions are not suitable, ensure that the module is not covered by any metal shell. The antenna area of the module and the area extending 15 mm outside the antenna must be kept clear of copper, routing, and components, as illustrated in Figure 1-14.

### Figure 1-14: Keepout Zone for ESP8266EX Module's Antenna on the Base Board

```
Clearance: 15 mm around the antenna area
Base Board
```

## Standalone ESP8266EX Module

### 1.6.3.1 Power Supply Design

- The 3.3 V power lines should have a width greater than 15 mil and are highlighted in yellow in Figure 1-15.
- Before the power traces reach the analog power-supply pins (Pin 1, 3, 4, 28, 29), a 10 µF capacitor is required, which works in conjunction with a 0.1 µF capacitor.
- Both a C circuit and an L circuit should be added to the power supplies of Pin 3 and Pin 4.
- As shown in Figure 1-15:
  - C5 (10 µF capacitor) is placed near the 3.3 V stamp hole.
  - C7, L8, and another C7 are placed as close as possible to the analog power-supply pins.
- All decoupling capacitors should be placed close to the power pins.
- Ground vias should be added adjacent to the ground pins for the decoupling capacitors to ensure a short return path.
- Power lines should be routed on the third layer.
- When power lines reach the chipset pins, vias are needed to connect the power lines through layers to the pins on the top layer.
- The diameter of the via holes should exceed the width of the power lines, and the drill diameter should be 1.5 times the radius of the vias.

---

*Page 21*