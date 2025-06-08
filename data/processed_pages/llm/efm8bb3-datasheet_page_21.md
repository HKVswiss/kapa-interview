# EFM8BB3 Data Sheet - Electrical Specifications

## Notes on Currents
1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increases supply current by the specified amount.
2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.
3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.
4. ADC0 power excludes internal reference supply current.
5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will depend on sampling rate.
6. DAC supply current for each enabled DA and not including external load on pin.
7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.

---

## 4.1.3 Reset and Supply Monitor

| Parameter                             | Symbol | Test Condition               | Min  | Typ  | Max  | Unit |
|-------------------------------------|--------|-----------------------------|------|------|------|------|
| VDD Supply Monitor Threshold        | V_VDDM |                             | 1.95 | 2.05 | 2.15 | V    |
| Power-On Reset (POR) Threshold      | V_POR  | Rising Voltage on VDD       | —    | 1.4  | —    | V    |
| Power-On Reset (POR) Threshold      | V_POR  | Falling Voltage on VDD      | 0.75 | —    | 1.36 | V    |
| VDD Ramp Time                       | t_RMP  | Time to V > 2.2 V_DD        | 10   | —    | —    | µs   |
| Reset Delay from POR                | t_POR  | Relative to V > V_DD_POR    | 3    | 10   | 31   | ms   |
| Reset Delay from non-POR source    | t_RST  | Time between release of reset source and code execution | — | 50 | — | µs |
| RST Low Time to Generate Reset     | t_RSTL |                             | 15   | —    | —    | µs   |
| Missing Clock Detector Response Time (final rising edge to reset) | t_MCD  | F >1 MHz_SYSCLK             | —    | 0.625| 1.2  | ms   |
| Missing Clock Detector Trigger Frequency | F_MCD  |                             | —    | 7.5  | 13.5 | kHz  |
| VDD Supply Monitor Turn-On Time    | t_MON  |                             | —    | 2    | —    | µs   |

---

*Source: silabs.com | Building a more connected world. Rev. 1.5 | Page 22*