# EFM8BB3 Data Sheet

## 4.3 Absolute Maximum Ratings

Stresses above those listed in Table 4.21 Absolute Maximum Ratings may cause permanent damage to the device. This is a stress rating only and functional operation of the devices at those or any other conditions above those indicated in the operation listings of this specification is not implied. Exposure to maximum rating conditions for extended periods may affect device reliability. For more information on the available quality and reliability data, see the Quality and Reliability Monitor Report at [http://www.silabs.com/support/quality/pages/default.aspx](http://www.silabs.com/support/quality/pages/default.aspx).

### Table 4.21. Absolute Maximum Ratings

| Parameter                                                                                      | Symbol | Test Condition                                | Min    | Max    | Unit |
|-----------------------------------------------------------------------------------------------|--------|-----------------------------------------------|--------|--------|------|
| Ambient Temperature Under Bias                                                                | T_BIAS |                                               | -55    | 125    | °C   |
| Storage Temperature                                                                           | T_STG  |                                               | -65    | 150    | °C   |
| Voltage on VDD                                                                               | V_DD   |                                               | GND-0.3| 4.2    | V    |
| Voltage on VIO2                                                                              | V_IO   |                                               | GND-0.3| V_DD+0.3| V    |
| Voltage on I/O pins or RSTb, excluding P2.0-P2.3 (QFN24 and QSOP24) or P3.0-P3.3 (QFN32 and QFP32) | V_IN   | V_IO > 3.3 V                                  | GND-0.3| 5.8    | V    |
| Voltage on I/O pins or RSTb, excluding P2.0-P2.3 (QFN24 and QSOP24) or P3.0-P3.3 (QFN32 and QFP32) | V_IN   | V_IO < 3.3 V                                  | GND-0.3| V_IO+2.5| V    |
| Voltage on P2.0-P2.3 (QFN24 and QSOP24) or P3.0-P3.3 (QFN32 and QFP32)                        | V_IN   |                                               | GND-0.3| V_DD+0.3| V    |
| Total Current Sunk into Supply Pin                                                           | I_VDD  |                                               | —      | 200    | mA   |
| Total Current Sourced out of Ground Pin                                                      | I_GND  |                                               | 200    | —      | mA   |
| Current Sourced or Sunk by any I/O Pin or RSTb                                              | I_IO   |                                               | -100   | 100    | mA   |
| Operating Junction Temperature                                                              | T_J    | T = -40 °C to 85 °C                           | -40    | 105    | °C   |
| Operating Junction Temperature                                                              | T_J    | T = -40 °C to 125 °C (I-grade or A-grade parts only) | -40    | 130    | °C   |

**Notes:**

1. Exposure to maximum rating conditions for extended periods may affect device reliability.
2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.

---
*Page 40*