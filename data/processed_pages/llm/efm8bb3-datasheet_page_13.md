# EFM8BB3 Data Sheet - System Overview

## I2C Slave (I2CSLAVE0)

The I2C Slave interface is a 2-wire, bidirectional serial bus compatible with the I2C Bus Specification 3.0. It supports high-speed mode (HS-mode) at speeds up to 3.4 Mbps. Firmware can write to the I2C interface, which can autonomously control serial data transfer. The interface supports clock stretching to handle cases where the core is temporarily unable to transmit or process a byte during an I2C transaction. This module operates only as an I2C slave device.

**Features:**

- Standard (up to 100 kbps), Fast (400 kbps), Fast Plus (1 Mbps), and High-speed (3.4 Mbps) transfer speeds
- Support for slave mode only
- Clock low extending (clock stretching) to interface with faster masters
- Hardware support for 7-bit slave address recognition
- Transmit and receive FIFOs (two bytes) to increase throughput in faster applications
- Hardware support for multiple slave addresses with option to save matching address in the receive FIFO

## 16-bit CRC (CRC0)

The cyclic redundancy check (CRC) module performs CRC using a 16-bit polynomial. CRC0 accepts a stream of 8-bit data and posts the 16-bit result to an internal register. It can also automatically CRC the flash contents of the device.

The CRC module is designed for hardware calculations for flash memory verification and communication protocols. It supports the standard CCITT-16 16-bit polynomial (0x1021).

**Features:**

- Support for CCITT-16 polynomial
- Byte-level bit reversal
- Automatic CRC of flash contents on one or more 256-byte blocks
- Initial seed selection of 0x0000 or 0xFFFF

## Configurable Logic Units (CLU0, CLU1, CLU2, and CLU3)

The Configurable Logic block consists of multiple Configurable Logic Units (CLUs) that provide flexible logic functions for various digital functions such as replacing system glue logic, generating special waveforms, or synchronizing system event triggers.

**Features:**

- Four configurable logic units with direct-pin and internal logic connections
- Each unit supports 256 different combinatorial logic functions (AND, OR, XOR, muxing, etc.) and includes a clocked flip-flop for synchronous operations
- Units may operate synchronously or asynchronously
- Units can be cascaded to perform more complex logic functions
- Can operate with serial peripherals (UART, SPI) or timing peripherals (timers, PCA channels)
- Can synchronize and trigger multiple on-chip resources (ADC, DAC, Timers, etc.)
- Asynchronous output can be used to wake from low-power states

---

*Page 14*