# 2. ESP-LAUNCHER

There are multiple modules that can be connected to the ESP-LAUNCHER for testing and development, through the 1.27mm double-row pin headers (2-1-23) and 2.00 mm double-row pin headers (2-1-24).

Please note that module pins should be connected to their corresponding pins on the board. Besides, only one module at a time can be used.

## Table 2-2: ESP-LAUNCHER Interfaces

| Interface       | Description                                                                                      | Reference  |
|-----------------|--------------------------------------------------------------------------------------------------|------------|
| HSPI            | Can interface SPI flash (Flash2), display screen, MCU, etc.                                      | (2-1-13)   |
| SDIO/SPI        | Can interface flash, host MCU, display screen, etc.                                             | (2-1-19)   |
| PWM             | Currently has four channels; can be extended. Used to control LED lights, buzzers, relays, motors, etc. | (2-1-20)   |
| IR              | Infrared remote control interface implemented via software programming. Uses NEC coding, modulation, and demodulation. Carrier frequency is 38 KHz. | (2-1-24)   |
| ADC             | Used to test power supply voltage of VDD3P3 (pin3 and pin4) and input voltage of TOUT (pin6). Also used in sensors. | (2-1-25)   |
| I2C             | Can interface sensors and display screens with 2.54 mm or 1.27 mm pin headers.                   | (2-1-21)   |
| UART0 / UART1   | UART0: UOTXD, UORXD, MTDO (UORTS), MTCK (UOCTS); UART1: GPIO2 (U1TXD). Used to interface other UART devices. | (2-1-5)    |
| Relay control   | Controls the on-and-off switch of the relay in a smart plug terminal application, with an indicator light. | (2-1-15)   |

### Notes on UART usage:
- For firmware downloading: use UOTXD + UORXD or GPIO2 + UORXD.
- For communication: UART0 uses UOTXD, UORXD, MTDO (UORTS), MTCK (UOCTS).
- For debugging: UART1_TXD (GPIO2) can print debugging information.
- By default, UART0 outputs some printed information when powered on. To avoid this, users can exchange UART pins during system initialization (swap UOTXD, UORXD with UORTS, UOCTS).

### Hardware configuration for SDIO/SPI interfaces on ESP-LAUNCHER:
1. Move the 0R resistor at R85 to R9, then disable the flash on the ESP_Test Board.
2. Short-circuit the two lower pins on J3 with a jumper to enable HSPI flash.
3. Remove capacitor C8 (located next to the Reset key on the left of the PCB).

### Additional hardware notes:
- Resistors R1, R3, R5, R7 should not be mounted with other components.
- Resistors R2, R4, R6, R8 can be mounted with other components.
- Jumpers J14 and J67 should be shorted.

---

*Page 30*