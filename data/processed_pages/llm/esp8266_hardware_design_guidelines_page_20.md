# ESP8266EX Module Placement and Power Supply Design

## Module Placement Recommendations

As shown in Figure 1-13, the recommended positions for the ESP8266EX module on the base board are:

- **Position 3, 4:** Highly recommended
- **Position 1, 2, 5:** Not recommended

If the recommended positions are not suitable, ensure that the module is not covered by any metal shell. The antenna area of the module and the area extending 15 mm outside the antenna must be kept clear of copper, routing, and components, as illustrated in Figure 1-14.

### Figure 1-14: Keepout Zone for ESP8266EX Module's Antenna on the Base Board

```
Clearance: 15 mm around antenna area

Base Board

[No copper, routing, or components within this zone]
```

## Standalone ESP8266EX Module

### 1.6.3.1 Power Supply Design

- The 3.3 V power lines (highlighted in yellow in Figure 1-15) should have a width greater than 15 mil.
- Before power traces reach the analog power-supply pins (Pin 1, 3, 4, 28, 29), a 10 µF capacitor is required, which works in conjunction with a 0.1 µF capacitor.
- A C circuit and an L circuit should be added to the power supplies of Pin 3 and Pin 4.
- Capacitor C5 (10 µF) is placed near the 3.3 V stamp hole.
- Capacitors C7, L8, and C7 are placed as close as possible to the analog power-supply pins.
- All decoupling capacitors should be placed close to the power pins.
- Ground vias should be added adjacent to the ground pins for the decoupling capacitors to ensure a short return path.
- Power lines should be routed on the third layer.
- When power lines reach the chipset pins, vias are needed to connect the power lines through layers to the pins on the TOP layer.
- The diameter of the via holes should exceed the width of the power lines, and the drill diameter should be 1.5 times the radius of the vias.

---

*Page 21*