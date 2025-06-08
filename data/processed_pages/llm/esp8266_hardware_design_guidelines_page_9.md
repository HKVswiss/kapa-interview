# ESP8266EX Overview

> **Note:** GPIO2, GPIO0, and MTDO are configurable on the PCB as the 3-bit strapping register that determines the booting mode and the SDIO timing mode.

## 1.4. Schematic Checklist

The highly-integrated design of the ESP8266EX reduces the number of components required. Besides the ESP8266EX chip itself, less than 10 resistors and capacitors, one crystal oscillator, and one SPI flash are needed to make a complete module with wireless communication capability.

The following is a detailed description of the ESP8266EX schematics and the layout design which ensures optimum functionality.

The complete circuit diagram of ESP8266EX is illustrated in Figure 1-3.

---

## Pin Description Table

| Pin Number | Pin Name  | Type | Description                                               |
|------------|-----------|------|-----------------------------------------------------------|
| 24         | GPIO5     | I/O  | General Purpose Input/Output                              |
| 25         | UORXD     | I/O  | UART Rx during flash programming; GPIO3                   |
| 26         | UOTXD     | I/O  | UART Tx during flash programming; GPIO1; SPI CS1          |
| 27         | XTAL_OUT  | O    | Connects to crystal oscillator output, can be used to provide BT clock input |
| 28         | XTAL_IN   | I    | Connects to crystal oscillator input                      |
| 29         | VDDD      | Power| Analog Power 2.5 V ~ 3.6 V                                |
| 30         | VDDA      | Power| Analog Power 2.5 V ~ 3.6 V                                |
| 31         | RES12K    | -    | Serial connection with a 12 kΩ resistor and connected to ground |
| 32         | EXT_RSTB  | I    | External reset signal (Low voltage level: Active)         |

---

*Page 10*