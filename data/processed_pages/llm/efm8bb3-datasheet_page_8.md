# 3. System Overview

## 3.1 Introduction

**Figure 3.1. Detailed EFM8BB3 Block Diagram**

The EFM8BB3 family is based on the CIP-51 8051 Controller core and includes a variety of integrated peripherals and features:

- 64 KB ISP Flash Program Memory
- 256 Byte SRAM
- 4096 Byte XRAM
- UART0 and UART1
- Timers 0, 1, 2, 3, 4, 5
- 6-channel PCA Priority Drivers
- Crossbar
- I2C / SMBus Port 1 Drivers
- SPI
- Power and Voltage Regulator
- Independent SYSCLK
- Watchdog Timer
- SFR Logic
- Bus Units (4)
- Analog Peripherals including up to 4 12-bit DACs
- 12-bit ADC with AMUX
- Internal Low Frequency Oscillator
- External Crystal Oscillator (XTAL1, XTAL2)
- RC Oscillator
- Temperature Sensor
- Two Comparators

### Pin and Port Configuration
- Port 0, Port 1, Port 2, Port 3 with multiple I/O pins (P0.n, P1.n, P2.n, P3.n)
- Debug / Core interface (C2D, C2CK/RSTb)

### Clock Sources
- CMOS Clock Input
- External Crystal / RC Oscillator
- Internal Oscillators at 49 MHz and 24.5 MHz with 2% accuracy

This section provides a high-level overview of the EFM8BB3 family.

For more detailed information on device packages, pinout, electrical specifications, and typical connection diagrams, refer to the EFM8BB3 Data Sheet.

For detailed module descriptions including register definitions, see the EFM8BB3 Reference Manual.

For known errata, consult the EFM8BB3 Errata documentation.

---

*Page 9*