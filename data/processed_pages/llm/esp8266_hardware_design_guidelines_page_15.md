# ESP8266EX UART Swap and GPIO15 Isolation Circuit

GPIO15 and GPIO13 of the ESP8266EX are used for UART serial communication. After swapping, GPIO15 and GPIO13 will be connected respectively to MCU_RXD and MCU_TXD as swapped U0TXD and U0RXD signals. For the reference design, see Figure 1-10b.

## GPIO15 Boot Mode Isolation

GPIO15 is a strapping pin that must be held at a low voltage level when the chip powers on. To prevent GPIO15 from being pulled up externally (which would cause the system to mistakenly enter boot mode), an isolation circuit is implemented.

- When the system powers on, transistor Q1 is switched off by default, effectively disconnecting GPIO15 from MCU_RXD.
- After the program starts running, Q1 can be turned on by GPIO5, connecting GPIO15 to MCU_RXD and enabling normal operation.

This design ensures power-on isolation of GPIO15.

## Logic Level Considerations

The ESP8266EX IO operates at 3.3 V logic level. When communicating serially with a 5 V CMOS logic system, an external level shifting circuit is required (see Figure 1-10c).

---

### Figure 1-10b: ESP8266EX UART Swap Circuit

| Component | Value/Connection |
|-----------|------------------|
| R1        | 10K              |
| R2        | 100K             |
| R3        | 10K              |
| R4        | 10K              |
| GPIO5     | Control Q1       |
| GPIO13    | MCU_TXD (RX)     |
| GPIO15    | MCU_RXD (TX)     |
| Power     | 3.3 V            |
| Ground    | GND              |

*Note: The table summarizes resistor values and key connections in the UART swap and isolation circuit.*

---

*Page 16*