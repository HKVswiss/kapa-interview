# ESP8266EX Layout and RF Performance Guidelines

- The distance between the chip and noise sources should be maximized to decrease interference and reduce coupled noise.

- It is recommended to add a 100 Ω to 200 Ω series resistor to the six signal traces when ESP8266EX communicates with the CPU via SDIO. This reduces drive current, minimizes interference, and eliminates sequencing problems caused by inconsistent SDIO trace lengths.

- On-board PCB antennas are not recommended due to high interference and coupling noise affecting RF performance. Use an external antenna connected via a cable and directed away from the PCB to reduce high-frequency interference with Wi-Fi.

- High-frequency signal traces between the CPU and associated memory should follow strict routing guidelines (refer to DDR trace routing guidelines). Clock (CLK) and data/address lines should be routed underground.

- The ground (GND) of the Wi-Fi circuit should be separated from that of other high-power devices (e.g., motors) and connected through wires to avoid interference.

- Keep the antenna away from high-frequency noise sources such as LCD, HDMI, Camera Sensor, USB, etc.

## Typical Layout Problems and Solutions

### 1. Current ripple is not large, but RF Tx performance is poor.

**Analysis:**
- Ripple strongly impacts RF Tx performance.
- Ripple should be measured during normal operation.
- Ripple increases with power.
- Recommended ripple limits:
  - < 80 mV when sending 11n MCS7 packets
  - < 120 mV when sending 11b packets

**Solution:**
- Add a 10 µF filter capacitor adjacent to the ESP8266EX AVDD (VDDA) pin on the power source branch.

### 2. Power ripple is small, but RF Tx performance is poor.

**Analysis:**
- RF Tx performance can be affected by the crystal oscillator quality.
- Poor quality crystals or frequency offsets greater than ±40 ppm degrade RF Tx.
- Crystal oscillator clock may be corrupted by interfering signals (e.g., high-speed I/O).
- Sensitive or radiating components (inductors, antennas) nearby can also reduce RF performance.

**Solution:**
- Use a high-quality crystal oscillator with minimal frequency offset.
- Minimize interference from other signals and components near the crystal.

---

*Page 25*