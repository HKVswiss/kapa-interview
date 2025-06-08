# ESP8266EX Layout and RF Performance Guidelines

- The distance between the chip and noise sources should be maximized to decrease interference and reduce coupled noise.

- It is recommended to add a 100 Ω to 200 Ω series resistor to the six signal traces when ESP8266EX communicates with the CPU via SDIO. This helps to decrease the drive current, reduce interferences, and eliminate sequencing problems caused by inconsistent SDIO trace lengths.

- On-board PCB antennas are not recommended because they receive much interference and coupling noise, which negatively impacts RF performance. Instead, use an external antenna directed away from the PCB board via a cable to weaken high-frequency interference with Wi-Fi.

- High-frequency signal traces between the CPU and associated memory should be routed strictly according to DDR trace routing guidelines. CLK and data/address lines should be laid underground.

- The ground (GND) of the Wi-Fi circuit and that of other high-power devices should be separated and connected through wires if there are high-power components (e.g., motors) in the design.

- The antenna should be kept away from high-frequency noise sources such as LCD, HDMI, Camera Sensor, USB, etc.

## Typical Layout Problems and Solutions

### 1. Current ripple is not large, but RF Tx performance is poor.

**Analysis:**
- Ripple strongly impacts RF Tx performance.
- Ripple must be tested when ESP8266EX is in normal working mode.
- Ripple increases with higher power.
- Generally, ripple should be <80 mV when sending 11n MCS7 packets, and <120 mV when sending 11b packets.

**Solution:**
- Add a 10 µF filter capacitor to the source circuit branch (ESP8266EX AVDD pin).
- The 10 µF capacitor should be placed adjacent to the VDDA pin.

### 2. Power ripple is small, but RF Tx performance is poor.

**Analysis:**
- RF Tx performance can be affected by the crystal oscillator quality.
- Poor quality and large frequency offsets (more than ±40 ppm) of the crystal oscillator decrease RF Tx performance.
- The crystal oscillator clock may be corrupted by other interfering signals such as high-speed output or input signals.
- Sensitive or radiating components like inductors and antennas may also decrease RF performance.

**Solution:**
- (Not explicitly stated in the text, but implies improving crystal oscillator quality and minimizing interference.)

---

*Page 25*