# EFM8BB3 Data Sheet - Electrical Specifications

| Parameter | Symbol | Test Condition | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| Snooze Mode - Core halted and high frequency clocks stopped. Regulator in low-power state, Supply monitor off. | I_DD | LFO Running | — | 23 | 615 | µA |
| Snooze Mode - Core halted and high frequency clocks stopped. Regulator in low-power state, Supply monitor off. | I_DD | LFO Stopped | — | 19 | 610 | µA |
| Stop Mode — Core halted and all clocks stopped, Internal LDO On, Supply monitor off. | I_DD | — | — | 120 | 740 | µA |
| Shutdown Mode — Core halted and all clocks stopped, Internal LDO Off, Supply monitor off. | I_DD | — | — | 0.2 | 4.5 | µA |
| **Analog Peripheral Supply Currents (-40 °C to +125 °C)** | | | | | | |
| High-Frequency Oscillator 0 | I_HFOSC0 | Operating at 24.5 MHz, T = 25 °C | — | 120 | 135 | µA |
| High-Frequency Oscillator 1 | I_HFOSC1 | Operating at 49 MHz, T = 25 °C | — | 770 | 1200 | µA |
| Low-Frequency Oscillator | I_LFOSC | Operating at 80 kHz, T = 25 °C | — | 3.7 | 6 | µA |
| ADC04 | I_ADC | High Speed Mode, 1 Msps, 10-bit conversions, Normal bias settings, V = 3.0 V | — | 1210 | 1600 | µA |
| ADC04 | I_ADC | Low Power Mode, 350 ksps, 12-bit conversions, Low power bias settings, V = 3.0 V | — | 415 | 560 | µA |
| Internal ADC0 Reference | I_VREFFS | High Speed Mode | — | 700 | 790 | µA |
| Internal ADC0 Reference | I_VREFFS | Low Power Mode | — | 170 | 210 | µA |
| On-chip Precision Reference | I_VREFP | — | — | 75 | — | µA |
| Temperature Sensor | I_TSENSE | — | — | 68 | 120 | µA |
| Digital-to-Analog Converters (DAC0, DAC1, DAC2, DAC3) | I_DAC | — | — | 125 | — | µA |
| Comparators (CMP0, CMP1) | I_CMP | CPMD = 11 | — | 0.5 | — | µA |
| Comparators (CMP0, CMP1) | I_CMP | CPMD = 10 | — | 3 | — | µA |
| Comparators (CMP0, CMP1) | I_CMP | CPMD = 01 | — | 10 | — | µA |
| Comparators (CMP0, CMP1) | I_CMP | CPMD = 00 | — | 25 | — | µA |
| Comparator Reference | I_CPREF | — | — | 24 | — | µA |
| Voltage Supply Monitor (VMON0) | I_VMON | — | — | 15 | 20 | µA |

---
*Page 21*