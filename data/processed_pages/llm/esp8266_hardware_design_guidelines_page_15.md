# ESP8266EX UART Swap and GPIO15 Isolation Circuit

After swapping, GPIO15 and GPIO13 of the ESP8266EX are connected respectively to MCU_RXD and MCU_TXD as swapped U0TXD and U0RXD for serial communication. For the reference design, see Figure 1-10b below.

## Figure 1-10b: ESP8266EX UART Swap Circuit

```
3.3V --- R1 (10K) --- MCU_TXD
                 |
             GPIO13_RX

GPIO15_TX --- MCU_RXD

GPIO5 --- R2 (100K) --- Q1 (switch transistor) --- GPIO15

R3 (10K), R4 (10K) connected to 3.3V and GND as needed

GND connections as shown
```

- GPIO15 is a strapping pin and must be at a low voltage level when the chip powers on.
- To prevent GPIO15 from being pulled up externally (which would cause the system to enter boot mode mistakenly), an isolation circuit is added.
- When the system powers on, Q1 is off by default, disconnecting GPIO15 from MCU_RXD.
- After the program starts running, GPIO5 can turn on Q1, connecting GPIO15 to MCU_RXD and enabling power-on isolation.

## Logic Level Considerations

- The ESP8266EX IO operates at 3.3 V logic level.
- When communicating serially with a 5 V CMOS logic system, an external level shifting circuit is required (see Figure 1-10c in the original document).

---

*Page 16*