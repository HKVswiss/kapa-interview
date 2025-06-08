# ESP-LAUNCHER

1. Remove R58 on the PCB and disconnect GPIO14 from the infrared transmitting tube.
2. Remove the pull-down resistor R29 of MTDO/IO15 (next to J11).
3. When downloading firmware, pull IO15/CS at J11 to low level and toggle the switch of GPIO0 inwards to enable UART Download mode.
4. When downloading is completed, release IO15/CS to enable SDIO Boot mode.
5. Connect SDIO/SPI at J5 to host for communication.

## 2.3 Schematics

### 2.3.1 Interfaces

Below is the ESP-LAUNCHER interface schematic and pin connections:

| Signal | Description |
|--------|-------------|
| GND    | Ground      |
| vBUS   | USB Power   |
| D+     | USB Data+   |
| D-     | USB Data-   |
| TxD    | UART Transmit |
| RxD    | UART Receive |
| RTS#   | Request To Send |
| CTS#   | Clear To Send |
| 5V USB-UART | USB to UART 5V power |

Additional notes:

- Normal mode uses resistors R1, R3, R5, R7, R8.
- Swap mode uses resistors R2, R4, R6, R8 (for cancelling log print when power on).
- Flow control: short J14 and J67.

### Figure 2-2. ESP-LAUNCHER Interface

![ESP-LAUNCHER Interface](Figure_2-2_ESP-LAUNCHER_Interface.png)

---

*Page 31*