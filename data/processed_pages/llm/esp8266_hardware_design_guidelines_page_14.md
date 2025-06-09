# ESP8266EX RF, External Resistor, and UART Configuration

## 1.4.5. RF

The impedance of the ESP8266 PA output end is 39 + j6 Ω, so the matched impedance is 39 - j6 Ω (from antenna to the chip).

### Figure 1-8. ESP8266EX RF

| Pin/Signal           | Description             |
|---------------------|-------------------------|
| ANT1                | 50 ohm Impedance Control|
| RF_ANT              | RF antenna input        |
| LNA_IN              | Low Noise Amplifier input|
| VDDA                | Analog power supply     |
| LNA                 | Low Noise Amplifier     |
| VDD3P3              | 3.3V power supply       |
| VDD_RTC             | RTC power supply        |
| TOUT                | Touch sensor output     |
| CHIP_EN             | Chip enable             |
| XPD_DCDC            | DC-DC converter enable  |
| GND                 | Ground                  |


## 1.4.6. External Resistor 12K

An external ground resistor should be connected to the RES12K pin (Pin 31). The ground resistor requires high accuracy when controlling the bias current. An accuracy of 12K ± 1% is recommended.

### Figure 1-9. ESP8266EX External Resistor

| Pin/Signal | Description          |
|------------|----------------------|
| EXT_RSTB   | External reset input  |
| RES12K     | External 12K resistor |
| VinAna     | Analog voltage input  |


## 1.4.7. UART

Users need to connect a 499 Ω resistor to the U0TXD line in order to suppress the 80 MHz harmonics.

### Figure 1-10a. ESP8266EX UART

| Signal  | Description               |
|---------|---------------------------|
| U0TXD   | UART0 transmit data        |
| U0RXD   | UART0 receive data         |
| R2      | 499 Ω resistor connected to U0TXD line |

By default, UART0 will output some printed information when ESP8266EX is powered on. For applications sensitive to this feature, users can exchange the pins of UART (UART SWAP) during system initialization, that is, exchange U0TXD, U0RXD with U0RTS.

---

*Page 15*