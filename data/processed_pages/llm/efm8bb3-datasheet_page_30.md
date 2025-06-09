# EFM8BB3 Data Sheet - Electrical Specifications

## 4.1.13 DACs

### Table 4.13. DACs

| Parameter                     | Symbol | Test Condition                                         | Min    | Typ           | Max   | Unit       |
|-------------------------------|--------|-------------------------------------------------------|--------|---------------|-------|------------|
| Output Voltage                | V_OUT  |                                                       | 0      | —             | V_DD  | V          |
| Output Current                | I_OUT  |                                                       | -2     | —             | 2     | mA         |
| Resolution                   | N_bits |                                                       | 12     | 12            | 12    | Bits       |
| Throughput Rate              | f_S    |                                                       | —      | —             | 200   | ksps       |
| Integral Nonlinearity        | INL    | DAC0 and DAC2, T = -40 °C to 125 °C (I-grade or A-grade parts only) | -11.5  | -1.77 / 1.56  | 11.5  | LSB        |
| Integral Nonlinearity        | INL    | DAC1 and DAC3, T = -40 °C to 125 °C (I-grade or A-grade parts only) | -13.5  | -2.73 / 1.11  | 13.5  | LSB        |
| Differential Nonlinearity    | DNL    |                                                       | -1     | —             | 1     | LSB        |
| Output Noise                 | V_NOISE| VREF = 2.4 V, f = 0.1 Hz to 300 kHz                   | —      | 110           | —     | µV RMS     |
| Slew Rate                   | SLEW   |                                                       | —      | ±1            | —     | V/µs       |
| Output Settling Time to 1% Full-scale | t_SETTLE | V change between 25% and 75% Full Scale             | —      | 2.6           | 5     | µs         |
| Power-on Time               | t_PWR  |                                                       | —      | —             | 10    | µs         |
| Voltage Reference Range     | V_REF  |                                                       | 1.15   | —             | V_DD  | V          |
| Power Supply Rejection Ratio| PSRR   | DC, V_OUT = 50% Full Scale                             | —      | 78            | —     | dB         |
| Total Harmonic Distortion   | THD    | V_OUT = 10 kHz sine wave, 10% to 90%                   | 54     | —             | —     | dB         |
| Offset Error                | E_OFF  | VREF = 2.4 V                                          | -8     | 0             | 8     | LSB        |
| Full-Scale Error            | E_FS   | VREF = 2.4 V                                          | -13    | ±5            | 13    | LSB        |
| External Load Impedance     | R_LOAD |                                                       | 2      | —             | —     | kΩ         |
| External Load Capacitance¹  | C_LOAD |                                                       | —      | —             | 100   | pF         |

> **Note:**
> 1. No minimum external load capacitance is required. However, under low loading conditions, it is possible for the DAC output to glitch during start-up. If smooth start-up is required, the minimum loading capacitance at the pin should be a minimum of 10 pF.

---

*silabs.com | Building a more connected world. Rev. 1.5 | Page 31*