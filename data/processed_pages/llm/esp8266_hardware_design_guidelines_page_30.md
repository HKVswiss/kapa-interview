# 2. ESP-LAUNCHER

1. Remove R68 on the PCB and disconnect GPIO14 from the infrared transmitting tube.
2. Remove the pull-down resistor R29 of MTDO/IO15 (next to J11).
3. When downloading firmware, pull IO15/CS at J11 to low level and toggle the switch of GPIO0 inwards to enable UART Download mode.
4. When downloading is completed, release IO15/CS to enable SDIO Boot mode.
5. Connect SDIO/SPI at J5 to host for communication.

## 2.3. Schematics

### 2.3.1 Interfaces

The ESP-LAUNCHER interface includes connections for USB, UART, and control signals. Key signals and components include:

- GND, vBUS, D+, D- lines for USB interface
- Micro USB connector
- UART signals: TxD, RxD, RTS, CTS
- Control signals: GPIO0, IO15/CS, MTDO/IO15
- LEDs: Blue LED, Fox LED, 7X LED
- Resistors and jumpers for configuration:
  - Use R1, R3, R5, R7 for normal operation
  - Use R2, R4, R6, R8 for swap (to cancel log print when power on)
  - Short J14 and J67 for flow control

### Notes:
- The interface uses an FT232RL USB-UART bridge chip.
- The schematic includes various test points and connectors (e.g., CON2).

---
*Figure 2-2. ESP-LAUNCHER Interface*

*Page 31 of 32*