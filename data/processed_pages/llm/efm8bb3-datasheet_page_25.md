# EFM8BB3 Data Sheet - Electrical Specifications

## 4.1.9 ADC

### Table 4.9. ADC Electrical Characteristics

| Parameter                  | Symbol  | Test Condition                                               | Min   | Typ   | Max    | Unit  |
|----------------------------|---------|--------------------------------------------------------------|-------|-------|--------|-------|
| Resolution                 | N bits  | 12 Bit Mode                                                  | 12    | 12    | 12     | Bits  |
| Resolution                 | N bits  | 10 Bit Mode                                                  | 10    | 10    | 10     | Bits  |
| Throughput Rate (High Speed Mode) | f S     | 10 Bit Mode                                                 | —     | —     | 1.125  | Msps  |
| Throughput Rate (Low Power Mode)  | f S     | 12 Bit Mode                                                 | —     | —     | 340    | ksps  |
| Throughput Rate (Low Power Mode)  | f S     | 10 Bit Mode                                                 | —     | —     | 360    | ksps  |
| Tracking Time              | t TRK   | High Speed Mode                                              | 230   | —     | —      | ns    |
| Tracking Time              | t TRK   | Low Power Mode                                              | 450   | —     | —      | ns    |
| Power-On Time              | t PWR   | —                                                            | 1.2   | —     | —      | μs    |
| SAR Clock Frequency        | f SAR   | High Speed Mode                                              | —     | —     | 18     | MHz   |
| SAR Clock Frequency        | f SAR   | Low Power Mode                                              | —     | —     | 12.25  | MHz   |
| Conversion Time            | t CNV   | 12-Bit Conversion, SAR Clock = 6.125 MHz, System Clock = 49 MHz | 2.0   | 2.0   | 2.0    | μs    |
| Conversion Time            | t CNV   | 10-Bit Conversion, SAR Clock = 16.33 MHz, System Clock = 49 MHz | 0.658 | 0.658 | 0.658  | μs    |
| Sample/Hold Capacitor      | C SAR   | Gain = 1                                                    | —     | 5.2   | —      | pF    |
| Sample/Hold Capacitor      | C SAR   | Gain = 0.75                                                 | —     | 3.9   | —      | pF    |
| Sample/Hold Capacitor      | C SAR   | Gain = 0.5                                                  | —     | 2.6   | —      | pF    |
| Sample/Hold Capacitor      | C SAR   | Gain = 0.25                                                 | —     | 1.3   | —      | pF    |
| Input Pin Capacitance      | C IN    | —                                                            | —     | 20    | —      | pF    |
| Input Mux Impedance        | R MUX   | —                                                            | —     | 550   | —      | Ω     |
| Voltage Reference Range    | V REF   | —                                                            | 1     | —     | V IO   | V     |
| Input Voltage Range        | V IN    | —                                                            | 0     | —     | V REF / Gain | V |
| Power Supply Rejection Ratio | PSRR ADC | At 1 kHz                                                  | —     | 66    | —      | dB    |
| Power Supply Rejection Ratio | PSRR ADC | At 1 MHz                                                  | —     | 43    | —      | dB    |

---

*Page 26*