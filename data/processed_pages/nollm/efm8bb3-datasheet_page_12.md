EFM8BB3 Data Sheet

System Overview

**Universal Asynchronous Receiver/Transmitter (UART1)**

UART1 is an asynchronous, full duplex serial port offering a variety of data formatting options. A dedicated baud rate generator with a
16-bit timer and selectable prescaler is included, which can generate a wide range of baud rates. A received data FIFO allows UART1
to receive multiple bytes before data is lost and an overflow occurs.

UART1 provides the following features:

 - Asynchronous transmissions and receptions

 - Dedicated baud rate generator supports baud rates up to SYSCLK/2 (transmit) or SYSCLK/8 (receive)

 - 5, 6, 7, 8, or 9 bit data

 - Automatic start and stop generation

 - Automatic parity generation and checking

 - Single-byte buffer on transmit and receive

 - Auto-baud detection

 - LIN break and sync field detection

 - CTS / RTS hardware flow control

**Serial Peripheral Interface (SPI0)**

The serial peripheral interface (SPI) module provides access to a flexible, full-duplex synchronous serial bus. The SPI can operate as a
main (clock driver) or secondary (clock receiver) interface in both 3-wire or 4-wire modes, and supports multiple main/secondary devices on a single SPI bus. The chip-select (NSS) signal can be configured as an input to select the SPI in secondary mode, or to disable
main mode operation in an environment with multiple main interfaces, avoiding contention on the SPI bus when more than one main
device attempts simultaneous data transfers. NSS can also be configured as a firmware-controlled chip-select output in main inferface
mode, or disabled to reduce the number of pins required. Additional general purpose port I/O pins can be used to select multiple secondary devices.

 - Supports 3- or 4-wire main or secondary modes

 - Supports external clock frequencies up to 12 Mbps in main or secondary mode

 - Support for all clock phase and polarity modes

 - 8-bit programmable clock rate (main)

 - Programmable receive timeout (secondary)

 - Two byte FIFO on transmit and receive

 - Can operate in suspend or snooze modes and wake the CPU on reception of a byte

 - Support for multiple mains on the same data lines

**System Management Bus / I2C (SMB0)**

The SMBus I/O interface is a two-wire, bi-directional serial bus. The SMBus is compliant with the System Management Bus Specification, version 1.1, and compatible with the I [2] C serial bus.

The SMBus module includes the following features:

 - Standard (up to 100 kbps) and Fast (400 kbps) transfer speeds

 - Support for leader, follower, and multi-leader modes

 - Hardware synchronization and arbitration for multi-leader mode

 - Clock low extending (clock stretching) to interface with faster leader devices

 - Hardware support for 7-bit follower and general call address recognition

 - Firmware support for 10-bit follower address decoding

 - Ability to inhibit all follower states

 - Programmable data setup/hold times

 - Transmit and receive FIFOs (one byte) to help increase throughput in faster applications

**silabs.com** | Building a more connected world. Rev. 1.5 | 13



EFM8BB3 Data Sheet

System Overview

Universal Asynchronous Receiver/Transmitter (UART1)

UART1 is an asynchronous, full duplex serial port offering a variety of data formatting options. A dedicated baud rate generator with a

16-bit timer and selectable prescaler is included, which can generate a wide range of baud rates. A received data FIFO allows UART1

to receive multiple bytes before data is lost and an overflow occurs.

UART1 provides the following features:

.

Asynchronous transmissions and receptions

.

Dedicated baud rate generator supports baud rates up to SYSCLK/2 (transmit) or SYSCLK/8 (receive)

.

5, 6, 7, 8, or 9 bit data

.

Automatic start and stop generation

.

Automatic parity generation and checking

.

Single-byte buffer on transmit and receive

.

Auto-baud detection

.

LIN break and sync field detection

.

CTS /RTS hardware flow control

Serial Peripheral Interface (SPIO)

The serial peripheral interface (SPI) module provides access to a flexible, full-duplex synchronous serial bus. The SPI can operate as a

main (clock driver) or secondary (clock receiver) interface in both 3-wire or 4-wire modes, and supports multiple main/secondary devi-

ces on a single SPI bus. The chip-select (NSS) signal can be configured as an input to select the SPI in secondary mode, or to disable

main mode operation in an environment with multiple main interfaces, avoiding contention on the SPI bus when more than one main

device attempts simultaneous data transfers. NSS can also be configured as a firmware-controlled chip-select output in main inferface

mode, or disabled to reduce the number of pins required. Additional general purpose port I/O pins can be used to select multiple secon-

dary devices.

+ Supports 3- or 4-wire main or secondary modes

.

Supports external clock frequencies up to 12 Mbps in main or secondary mode

.

Support for all clock phase and polarity modes

.

8-bit programmable clock rate (main)

.

Programmable receive timeout (secondary)

.

Two byte FIFO on transmit and receive

.

Can operate in suspend or snooze modes and wake the CPU on reception of a byte

.

Support for multiple mains on the same data lines

System Management Bus / I2C (SMBO)

The SMBus 1/O interface is a two-wire, bi-directional serial bus. The SMBus is compliant with the System Management Bus Specifica-

tion, version 1.1, and compatible with the I2C serial bus.

The SMBus module includes the following features:

.

Standard (up to 100 kbps) and Fast (400 kbps) transfer speeds

.

Support for leader, follower, and multi-leader modes

.

Hardware synchronization and arbitration for multi-leader mode

.

Clock low extending (clock stretching) to interface with faster leader devices

.

Hardware support for 7-bit follower and general call address recognition

.

Firmware support for 10-bit follower address decoding

.

Ability to inhibit all follower states

.

Programmable data setup/hold times

.

Transmit and receive FIFOs (one byte) to help increase throughput in faster applications

silabs.com | Building a more connected world.

Rev. 1.5 | 13

EFM8BB3 Data Sheet
System Overview
Universal Asynchronous Receiver/Transmitter (UART1)
UART1 is an asynchronous, full duplex serial port offering a variety of data formatting options. A dedicated baud rate generator with a
16-bit timer and selectable prescaler is included, which can generate a wide range of baud rates. A received data FIFO allows UART1
to receive multiple bytes before data is lost and an overflow occurs.
UART1 provides the following features:
. Asynchronous transmissions and receptions
. Dedicated baud rate generator supports baud rates up to SYSCLK/2 (transmit) or SYSCLK/8 (receive)
. 5, 6, 7, 8, or 9 bit data
. Automatic start and stop generation
. Automatic parity generation and checking
. Single-byte buffer on transmit and receive
. Auto-baud detection
. LIN break and sync field detection
. CTS /RTS hardware flow control
Serial Peripheral Interface (SPIO)
The serial peripheral interface (SPI) module provides access to a flexible, full-duplex synchronous serial bus. The SPI can operate as a
main (clock driver) or secondary (clock receiver) interface in both 3-wire or 4-wire modes, and supports multiple main/secondary devi-
ces on a single SPI bus. The chip-select (NSS) signal can be configured as an input to select the SPI in secondary mode, or to disable
main mode operation in an environment with multiple main interfaces, avoiding contention on the SPI bus when more than one main
device attempts simultaneous data transfers. NSS can also be configured as a firmware-controlled chip-select output in main inferface
mode, or disabled to reduce the number of pins required. Additional general purpose port I/O pins can be used to select multiple secon-
dary devices.
+ Supports 3- or 4-wire main or secondary modes
. Supports external clock frequencies up to 12 Mbps in main or secondary mode
. Support for all clock phase and polarity modes
. 8-bit programmable clock rate (main)
. Programmable receive timeout (secondary)
. Two byte FIFO on transmit and receive
. Can operate in suspend or snooze modes and wake the CPU on reception of a byte
. Support for multiple mains on the same data lines
System Management Bus / I2C (SMBO)
The SMBus 1/O interface is a two-wire, bi-directional serial bus. The SMBus is compliant with the System Management Bus Specifica-
tion, version 1.1, and compatible with the I2C serial bus.
The SMBus module includes the following features:
. Standard (up to 100 kbps) and Fast (400 kbps) transfer speeds
. Support for leader, follower, and multi-leader modes
. Hardware synchronization and arbitration for multi-leader mode
. Clock low extending (clock stretching) to interface with faster leader devices
. Hardware support for 7-bit follower and general call address recognition
. Firmware support for 10-bit follower address decoding
. Ability to inhibit all follower states
. Programmable data setup/hold times
. Transmit and receive FIFOs (one byte) to help increase throughput in faster applications
silabs.com | Building a more connected world. Rev. 1.5 | 13


---Page 13 

