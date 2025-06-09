# EFM8BB3 Data Sheet - Electrical Specifications

## 4.1.16 Port I/O

### Table 4.16. Port I/O

| Parameter                          | Symbol | Test Condition                                                                                  | Min          | Typ | Max          | Unit |
|----------------------------------|--------|-----------------------------------------------------------------------------------------------|--------------|-----|--------------|------|
| Output High Voltage (High Drive) | V_OH   | I = -7 mA, V_IO ≥ 3.0 V                                                                       | V_IO - 0.7   | —   | —            | V    |
|                                  |        | I = -3.3 mA, 2.2 V ≤ V_IO < 3.0 V                                                            | V_IO × 0.8   | —   | —            | V    |
|                                  |        | I = -1.8 mA, 1.71 V ≤ V_IO < 2.2 V                                                           | V_IO × 0.8   | —   | —            | V    |
| Output Low Voltage (High Drive)  | V_OL   | I = 13.5 mA, V_IO ≥ 3.0 V                                                                     | —            | —   | 0.6          | V    |
|                                  |        | I = 7 mA, 2.2 V ≤ V_IO < 3.0 V                                                               | —            | —   | V_IO × 0.2   | V    |
|                                  |        | I = 3.6 mA, 1.71 V ≤ V_IO < 2.2 V                                                            | —            | —   | V_IO × 0.2   | V    |
| Output High Voltage (Low Drive)  | V_OH   | I = -4.75 mA, V_IO ≥ 3.0 V                                                                    | V_IO - 0.7   | —   | —            | V    |
|                                  |        | I = -2.25 mA, 2.2 V ≤ V_IO < 3.0 V                                                           | V_IO × 0.8   | —   | —            | V    |
|                                  |        | I = -1.2 mA, 1.71 V ≤ V_IO < 2.2 V                                                           | V_IO × 0.8   | —   | —            | V    |
| Output Low Voltage (Low Drive)   | V_OL   | I = 6.5 mA, V_IO ≥ 3.0 V                                                                      | —            | —   | 0.6          | V    |
|                                  |        | I = 3.5 mA, 2.2 V ≤ V_IO < 3.0 V                                                             | —            | —   | V_IO × 0.2   | V    |
|                                  |        | I = 1.8 mA, 1.71 V ≤ V_IO < 2.2 V                                                            | —            | —   | V_IO × 0.2   | V    |
| Input High Voltage               | V_IH   | —                                                                                             | 0.7 × V_IO   | —   | —            | V    |
| Input Low Voltage                | V_IL   | —                                                                                             | —            | —   | 0.3 × V_IO   | V    |
| Pin Capacitance                 | C_IO   | —                                                                                             | —            | 7   | —            | pF   |
| Weak Pull-Up Current (V = 0 V)  | I_PU   | V = 3.6 V                                                                                     | -30          | -20 | -10          | µA   |
| Input Leakage (Pull-ups off or Analog) (G-grade and I-grade devices) | I_LK   | GND < V < V_IO                                                                              | -1.1         | —   | 4            | µA   |
| Input Leakage (Pull-ups off or Analog) (A-grade devices only)        | I_LK   | GND < V < V_IO                                                                              | -1.1         | —   | 1.1          | µA   |
| Input Leakage Current with V_IN above V_IO (Any pin except P3.0, P3.1, P3.2, or P3.3) | I_LK   | V_IO < V < V_IO + 2.5 V                                                                    | 0            | 5   | 150          | µA   |

---
*Page 34*