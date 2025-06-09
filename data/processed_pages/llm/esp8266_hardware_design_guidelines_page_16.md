# ESP8266EX UART Voltage-level Switch Circuit

![UART Voltage-level Switch circuit](Figure_1-10c_UART_Voltage-level_Switch_circuit.png)  
*Figure 1-10c. UART Voltage-level Switch circuit*

## Circuit Components and Connections

| Component | Value |
|-----------|-------|
| Rt        | 10K   |
| R2        | 10K   |
| R3        | 40K   |
| Ra        | 10K   |
| Rs        | 100K  |
| Ré        | 10K   |
| Rt (second) | 10K |
| Other     | 33    |

## Pins

- MCU_TXD
- MCU_RXD
- GPIO13_RX
- GPIO15_TX
- GPIOS
- GND

## Notice

- When using GPIO13 and GPIO15 as serial communication pins, please pay attention to the direction of sending and receiving information. They need to be connected correctly to MCU UART pins.
- When using the AT firmware, the UART GPIO is already configured (refer to [Hardware Connection](https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp8266/Get_Started/Hardware_connection.html)). It is recommended to use the default configuration.

---
*Page 17*