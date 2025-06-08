# EFM8BB3 Data Sheet - Electrical Specifications

## 4.1.10 Voltage Reference

| Parameter                     | Symbol   | Test Condition                                | Min   | Typ   | Max   | Unit    |
|-------------------------------|----------|-----------------------------------------------|-------|-------|-------|---------|
| **Internal Fast Settling Reference** |          |                                               |       |       |       |         |
| Output Voltage (Full Temperature and Supply Range) | V_REFFS  |                                               | 1.62  | 1.65  | 1.68  | V       |
| Temperature Coefficient        | TC_REFFS |                                               | —     | 50    | —     | ppm/°C  |
| Turn-on Time                   | t_REFFS  |                                               | —     | —     | 1.5   | µs      |
| Power Supply Rejection         | PSRR_REF_FS |                                             | —     | 400   | —     | ppm/V   |
| **On-chip Precision Reference** |          |                                               |       |       |       |         |
| Valid Supply Range             | V_DD     | 1.2 V Output                                  | 2.2   | —     | 3.6   | V       |
| Valid Supply Range             | V_DD     | 2.4 V Output                                  | 2.7   | —     | 3.6   | V       |
| Output Voltage                | V_REFP   | 1.2 V Output, V_DD = 3.3 V, T = 25 °C         | 1.195 | 1.2   | 1.205 | V       |
| Output Voltage                | V_REFP   | 1.2 V Output                                  | 1.18  | 1.2   | 1.22  | V       |
| Output Voltage                | V_REFP   | 2.4 V Output, V_DD = 3.3 V, T = 25 °C         | 2.39  | 2.4   | 2.41  | V       |
| Output Voltage                | V_REFP   | 2.4 V Output                                  | 2.36  | 2.4   | 2.44  | V       |
| Turn-on Time, settling to 0.5 LSB | t_VREFP  | 4.7 µF tantalum + 0.1 µF ceramic bypass on VREF pin | —     | 3     | —     | ms      |
| Turn-on Time, settling to 0.5 LSB | t_VREFP  | 0.1 µF ceramic bypass on VREF pin             | —     | 100   | —     | µs      |
| Load Regulation               | LR_VREFP | VREF = 2.4 V, Load = 0 to 200 µA to GND      | —     | 8     | —     | µV/µA   |
| Load Regulation               | LR_VREFP | VREF = 1.2 V, Load = 0 to 200 µA to GND      | —     | 5     | —     | µV/µA   |
| Load Capacitor                | C_VREFP  | Load = 0 to 200 µA to GND                      | 0.1   | —     | —     | µF      |
| Short-circuit current         | ISC_VREFP|                                               | —     | —     | 8     | mA      |
| Power Supply Rejection        | PSRR_VREFP |                                              | —     | 75    | —     | dB      |
| **External Reference**         |          |                                               |       |       |       |         |
| Input Current                 | I_EXTREF | ADC Sample Rate = 800 ksps; VREF = 3.0 V      | —     | 5     | —     | µA      |

---

*Page 29*