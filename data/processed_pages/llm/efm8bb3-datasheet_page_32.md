# EFM8BB3 Data Sheet - Electrical Specifications

| Parameter                     | Symbol  | Test Condition           | Min   | Typ   | Max    | Unit |
|-------------------------------|---------|--------------------------|-------|-------|--------|------|
| Negative Hysteresis Mode 3 (CPMD = 11) | HYS CP- | CPHYN = 00               | —     | -1.5  | —      | mV   |
|                               |         | CPHYN = 01               | —     | -4    | —      | mV   |
|                               |         | CPHYN = 10               | —     | -8    | —      | mV   |
|                               |         | CPHYN = 11               | —     | -16   | —      | mV   |
| Input Range (CP+ or CP-)       | V_IN    |                          | -0.25 | —     | V_IO+0.25 | V    |
| Input Pin Capacitance          | C_CP    |                          | —     | 7.5   | —      | pF   |
| Internal Reference DAC Resolution | N bits |                          | 6     | 6     | 6      | bits |
| Common-Mode Rejection Ratio    | CMRR_CP |                          | —     | 70    | —      | dB   |
| Power Supply Rejection Ratio   | PSRR_CP |                          | —     | 72    | —      | dB   |
| Input Offset Voltage           | V_OFF   | T = 25 °C, A             | -10   | 0     | 10     | mV   |
| Input Offset Tempco            | TC_OFF  |                          | —     | 3.5   | —      | μV/°C |

## 4.1.15 Configurable Logic

| Parameter           | Symbol | Test Condition           | Min | Typ  | Max   | Unit |
|---------------------|--------|--------------------------|-----|------|-------|------|
| Propagation Delay   | t_DLY  | Through single CLU using an external pin | —   | —    | 35.3  | ns   |
| Propagation Delay   | t_DLY  | Through single CLU using an internal connection | —   | 3    | —     | ns   |
| Clocking Frequency  | F_CLK  | 1 or 2 CLUs Cascaded     | —   | —    | 73.5  | MHz  |
| Clocking Frequency  | F_CLK  | 3 or 4 CLUs Cascaded     | —   | —    | 36.75 | MHz  |

---
*Page 33*