# ESP8266EX RF, External Resistor, and UART Configuration

## 1.4.5. RF

The impedance of the ESP8266 PA output end is 39 + j6 Ω, so the matched impedance is 39 - j6 Ω (from antenna to the chip).

### RF Pin Description and Connections

| Pin | Description           |
|------|-----------------------|
| ANT1 | 50 ohm Impedance Control |
| 1    | RF_ANT                |
| 2    | LNA_IN                |
| 3    | TBD                   |
| 4    | C1, C2                |
| 5    | PCB_ANT               |
| 6    | TBD                   |
| 7    | GND                   |
| 8    | GND                   |

| Power and Control Pins |
|-----------------------|
| VDDA                  |
| LNA                   |
| VDD3P3                |
| VDD_RTC               |
| TOUT                  |
| CHIP_EN               |
| XPD_DCDC              |

*Figure 1-8. ESP8266EX RF*

---

## 1.4.6. External Resistor 12K

An external ground resistor should be connected to the RES12K pin (Pin 31). The ground resistor requires high accuracy when controlling the bias current. An accuracy of 12K ± 1% is recommended.

| Pin | Description |
|------|-------------|
| RES12K (Pin 31) | Connect external 12K resistor |

*Figure 1-9. ESP8266EX External Resistor*

---

## 1.4.7. UART

Users need to connect a 499 Ω resistor to the U0TXD line in order to suppress the 80 MHz harmonics.

| UART Pin | Description |
|----------|-------------|
| U0TXD    | UART0 Transmit Data (connect 499 Ω resistor) |
| U0RXD    | UART0 Receive Data |

*Figure 1-10a. ESP8266EX UART*

By default, UART0 will output some printed information when ESP8266EX is powered on. For applications sensitive to this feature, users can exchange the pins of UART (UART SWAP) during system initialization, that is, exchange U0TXD, U0RXD with U0RTS.

---

*Page 15*