# EFM8BB3 Data Sheet

## Feature List

The EFM8BB3 device family are fully integrated, mixed-signal system-on-a-chip MCUs. Highlighted features are listed below.

### Core
- Pipelined CIP-51 Core
- Fully compatible with standard 8051 instruction set
- 70% of instructions execute in 1-2 clock cycles
- 50 MHz maximum operating frequency

### Memory
- Up to 64 kB flash memory (63 kB user-accessible), in-system re-programmable from firmware in 512-byte sectors
- Up to 4352 bytes RAM (including 256 bytes standard 8051 RAM and 4096 bytes on-chip XRAM)

### Power
- Internal LDO regulator for CPU core voltage
- Power-on reset circuit and brownout detectors

### I/O
- Up to 29 total multifunction I/O pins:
  - Up to 25 pins 5 V tolerant under bias
  - Selectable state retention through reset events
  - Flexible peripheral crossbar for peripheral routing
  - 5 mA source, 12.5 mA sink allows direct drive of LEDs

### Clock Sources
- Internal 49 MHz oscillator with accuracy of ±2%
- Internal 24.5 MHz oscillator with ±2% accuracy
- Internal 80 kHz low-frequency oscillator
- External CMOS clock option (up to 25 MHz)
- External crystal/RC oscillator option up to 25 MHz

### Analog
- 12/10-Bit Analog-to-Digital Converter (ADC)
- Internal temperature sensor
- 4 x 12-Bit Digital-to-Analog Converters (DAC)
- 2 x Low-current analog comparators with adjustable reference

### Communications and Digital Peripherals
- 2 x UART, up to 3 Mbaud
- SPI™ Master / Slave, up to 12 Mbps
- SMBus™/I2C™ Master / Slave, up to 400 kbps
- I2C High-Speed Slave, up to 3.4 Mbps
- 16-bit CRC unit, supporting automatic CRC of flash at 256-byte boundaries
- 4 Configurable Logic Units

### Timers/Counters and PWM
- 6-channel programmable counter array (PCA) supporting PWM, capture/compare, and frequency output modes
- 6 x 16-bit general-purpose timers
- Independent watchdog timer, clocked from the low frequency oscillator

### On-Chip, Non-Intrusive Debugging
- Full memory and register inspection
- Four hardware breakpoints, single-stepping

### Other Features
- Pre-programmed UART bootloader
- Temperature range -40 to 85 ºC or -40 to 125 ºC
- Available in commercial, industrial, and automotive variants

---

With on-chip power-on reset, voltage supply monitor, watchdog timer, and clock oscillator, the EFM8BB3 devices are truly standalone system-on-a-chip solutions. The flash memory is reprogrammable in-circuit, providing nonvolatile data storage and allowing field upgrades of the firmware. The on-chip debugging interface (C2) allows non-intrusive (uses no on-chip resources), full speed, in-circuit debugging using the production MCU installed in the final application. This debug logic supports inspection and modification of memory and registers, setting breakpoints, single stepping, and run and halt commands. All analog and digital peripherals are fully functional while debugging. Device operation is specified from 2.2 V up to a 3.6 V supply. Devices are AEC-Q100 qualified. Both G-grade and I-grade devices are available in 4x4 mm 32-pin QFN, 3x3 mm 24-pin QFN, 32-pin QFP, or 24-pin QSOP packages. A-grade and additional I-grade devices are available in 5x5 mm 32-pin QFN and 4x4 mm 24-pin QFN packages. All package options are lead-free and RoHS compliant.

---

*Page 2*