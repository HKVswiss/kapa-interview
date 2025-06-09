# 2. ESP-LAUNCHER

There are multiple modules that can be connected to the ESP-LAUNCHER for testing and development through the 1.27 mm double-row pin headers (2-1-23) and 2.00 mm double-row pin headers (2-1-24).

> **Note:** Module pins should be connected to their corresponding pins on the board. Only one module at a time can be used.

## Table 2-2: ESP-LAUNCHER Interfaces

| Interface      | Description                                                                                         | Reference  |
|----------------|-------------------------------------------------------------------------------------------------|------------|
| HSPI           | Can interface SPI flash (Flash2), display screen, MCU, etc.                                      | (2-1-13)   |
| SDIO/SPI       | Can interface flash, host MCU, display screen, etc.                                              | (2-1-19)   |
| PWM            | Currently has four channels; users can extend channels as needed. Used to control LED lights, buzzers, relays, motors, etc. | (2-1-20)   |
| IR             | Infrared remote control interface implemented via software programming. Uses NEC coding, modulation, and demodulation. Carrier frequency is 38 KHz. | (2-1-24)   |
| ADC            | Used to test power supply voltage of VDD3P3 (pin 3 and pin 4) and input voltage of TOUT (pin 6). Also used in sensors. | (2-1-25)   |
| I2C            | Can interface sensors and display screens with 2.54 mm or 1.27 mm pin headers.                   | (2-1-21)   |
| UART           | UART0: UOTXD, UORXD, MTDO (UORTS), MTCK (UOCTS); UART1: GPIO2 (U1TXD). Can interface other UART devices.

- For firmware downloading: UOTXD + UORXD or GPIO2 + UORXD
- For communication: UART0 pins
- For debugging: UART1_TXD (GPIO2) can print debugging info.

By default, UART0 outputs some printed information when powered on. For sensitive applications, users can exchange UART pins during system initialization (swap UOTXD, UORXD with UORTS, UOCTS).

| Relay Control | Used to control the on/off switch of the relay in a smart plug terminal application, with an indicator light. | (2-1-15)   |

## Using SDIO/SPI Interfaces on ESP-LAUNCHER

To use the SDIO/SPI interfaces, follow these steps:

1. Move the 0R resistor at R85 to R9, then disable the flash on the ESP_Test Board.
2. Short-circuit the two lower pins on J3 with a jumper to enable HSPI flash.
3. Remove C8 (located next to the Reset key on the left of the PCB).

---

*Page 30*