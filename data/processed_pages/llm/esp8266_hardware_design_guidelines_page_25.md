# ESP8266EX Troubleshooting and Typical Applications

## 1. Troubleshooting

### 3. When ESP8266EX sends data packages, the power value is much higher or lower than the target power value, and the EVM is relatively poor.

**Analysis:**
- The disparity between the tested value and the target value may be due to signal reflection caused by impedance mismatch on the transmission line connecting the RF pin and the antenna.

**Solution:**
- Match the antenna’s impedance with the reserved π-type circuit on the RF trace, so that the resistance from the RF pin to the antenna approaches (39 - j6) Ω.

### 4. TX performance is not bad, but the Rx sensitivity is low.

**Analysis:**
- Good Tx performance indicates proper RF impedance matching.
- External coupling to the antenna can affect Rx performance. For example, crystal oscillator signal harmonics could couple to the antenna.
- If ESP8266EX serves as a slave device, other high-frequency interference sources on the board may affect Rx performance.

**Solution:**
- Keep the antenna away from crystal oscillators.
- Do not route high-frequency signal traces close to the RF trace.

## 2. Typical Application

### 2.1 UART to Wi-Fi Smart Device

The two UART interfaces are defined in the following table:

| Category | Pin Definition          | Function                         |
|----------|-------------------------|---------------------------------|
| UART0    | RXD (Pin 25), TXD (Pin 26) | Receive and transmit user data packages |
| UART1    | Print information (Pin 14), GPIO2 (U1TXD) | Print information               |

AT+ instructions and examples are provided here: [Espressif Support Documents](http://www.espressif.com/en/support/download/documents?keys=&field_type_tid%5B%5D=14)

Application example: ESP8266EX development board (see Chapter 2).

### 2.2 Sensor

ESP8266EX can be used for developing sensor products by using the I2C interface.

---

*Page 26*