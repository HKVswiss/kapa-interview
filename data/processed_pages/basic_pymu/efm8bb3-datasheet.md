### **EFM8 Busy Bee Family** **EFM8BB3 Data Sheet**

The EFM8BB3, part of the Busy Bee family of MCUs, is a performance line of 8-bit microcontrollers with a comprehensive analog and digital feature set in small packages.

These devices offer state-of-the-art performance by integrating 12-bit ADC, internal
temperature sensor, and up to four 12-bit DACs into small packages, making them ideal for general purpose applications. With an efficient, pipelined 8051 core with maximum operating frequency at 50 MHz, various communication interfaces, and four channels of configurable logic, the EFM8BB3 family is optimal for many embedded applications.

EFM8BB3 applications include the following:


**KEY FEATURES**

 - Pipelined 8-bit 8051 MCU Core with
50 MHz operating frequency

 - Up to 29 multifunction I/O pins

 - One 12-bit/10-bit ADC

 - Four 12-bit DACs with synchronization
and PWM capabilities

 - Two low-current analog comparators with
built-in reference DACs

 - Internal temperature sensor

 - Internal 49 MHz and 24.5 MHz oscillators

accurate to ±2%

 - Four channels of Configurable Logic

 - 6-channel PWM / PCA

 - Six 16-bit general-purpose timers



- Consumer electronics

- Precision instrumentation

- Power management and control



- Industrial control and automation

- Smart sensors

- Automotive control


























**Lowest power mode with peripheral operational:**

**Normal** **Idle** **Suspend** **Snooze** **Shutdown**

**silabs.com** | Building a more connected world. **Copyright © 2024 by Silicon Laboratories** Rev. 1.5

EFM8BB3 Data Sheet

Feature List

**1. Feature List**

The EFM8BB3 device family are fully integrated, mixed-signal system-on-a-chip MCUs. Highlighted features are listed below.



- Core:

  - Pipelined CIP-51 Core

  - Fully compatible with standard 8051 instruction set

  - 70% of instructions execute in 1-2 clock cycles

  - 50 MHz maximum operating frequency

- Memory:

  - Up to 64 kB flash memory (63 kB user-accessible), in-system re-programmable from firmware in 512-byte sectors

  - Up to 4352 bytes RAM (including 256 bytes standard 8051
RAM and 4096 bytes on-chip XRAM)

- Power:

  - Internal LDO regulator for CPU core voltage

  - Power-on reset circuit and brownout detectors

- I/O: Up to 29 total multifunction I/O pins:

  - Up to 25 pins 5 V tolerant under bias

  - Selectable state retention through reset events

  - Flexible peripheral crossbar for peripheral routing

  - 5 mA source, 12.5 mA sink allows direct drive of LEDs

- Clock Sources:

  - Internal 49 MHz oscillator with accuracy of ±2%

  - Internal 24.5 MHz oscillator with ±2% accuracy

  - Internal 80 kHz low-frequency oscillator

  - External CMOS clock option (up to 25 MHz)

  - External crystal/RC oscillator option up to 25 MHz



- Analog:

  - 12/10-Bit Analog-to-Digital Converter (ADC)

  - Internal temperature sensor

  - 4 x 12-Bit Digital-to-Analog Converters (DAC)

  - 2 x Low-current analog comparators with adjustable refer
ence

- Communications and Digital Peripherals:

  - 2 x UART, up to 3 Mbaud

  - SPI™ Master / Slave, up to 12 Mbps

  - SMBus™/I2C™ Master / Slave, up to 400 kbps

  - I [2] C High-Speed Slave, up to 3.4 Mbps

  - 16-bit CRC unit, supporting automatic CRC of flash at 256byte boundaries

  - 4 Configurable Logic Units

- Timers/Counters and PWM:

  - 6-channel programmable counter array (PCA) supporting
PWM, capture/compare, and frequency output modes

  - 6 x 16-bit general-purpose timers

  - Independent watchdog timer, clocked from the low frequency oscillator

- On-Chip, Non-Intrusive Debugging

  - Full memory and register inspection

  - Four hardware breakpoints, single-stepping

- Pre-programmed UART bootloader

- Temperature range -40 to 85 ºC or -40 to 125 ºC

  - Available in commercial, industrial, and automotive variants


With on-chip power-on reset, voltage supply monitor, watchdog timer, and clock oscillator, the EFM8BB3 devices are truly standalone
system-on-a-chip solutions. The flash memory is reprogrammable in-circuit, providing nonvolatile data storage and allowing field upgrades of the firmware. The on-chip debugging interface (C2) allows non-intrusive (uses no on-chip resources), full speed, in-circuit
debugging using the production MCU installed in the final application. This debug logic supports inspection and modification of memory
and registers, setting breakpoints, single stepping, and run and halt commands. All analog and digital peripherals are fully functional
while debugging. Device operation is specified from 2.2 V up to a 3.6 V supply. Devices are AEC-Q100 qualified. Both G-grade and Igrade devices are available in 4x4 mm 32-pin QFN, 3x3 mm 24-pin QFN, 32-pin QFP, or 24-pin QSOP packages. A-grade and additional I-grade devices are available in 5x5 mm 32-pin QFN and 4x4 mm 24-pin QFN packages. All package options are lead-free and
RoHS compliant.

**silabs.com** | Building a more connected world. Rev. 1.5 | 2

EFM8BB3 Data Sheet
Ordering Information


**2. Ordering Information**


**Tape and Reel (Optional)**

**Package Type**

**Revision**

**Temperature Grade G (-40 to +85), I (-40 to +125), A (-40 to +125)**

**Flash Memory Size – 64 KB**

**Memory Type (Flash)**

**Family Feature Set**

**Busy Bee 3 Family**

**Silicon Labs EFM8 Product Line**

**Figure 2.1. EFM8BB3 Part Numbering**

All EFM8BB3 family members have the following features:

 - CIP-51 Core running up to 49 MHz

 - Three Internal Oscillators (49 MHz, 24.5 MHz and 80 kHz)

 - SMBus

 - I2C Slave

 - SPI

 - 2 UARTs

 - 6-Channel Programmable Counter Array (PWM, Clock Generation, Capture/Compare)

 - Six 16-bit Timers

 - Four Configurable Logic Units

 - 12-bit Analog-to-Digital Converter with integrated multiplexer, voltage reference, temperature sensor, channel sequencer, and directto-XRAM data transfer

 - Two Analog Comparators

 - 16-bit CRC Unit

 - AEC-Q100 qualified

 - Pre-loaded UART bootloader

In addition to these features, each part number in the EFM8BB3 family has a set of features that vary across the product line. The
product selection guide shows the features available on each family member.


**Table 2.1. Product Selection Guide**

|Ordering Part Number|Flash Memory (kB)|RAM (Bytes)|Digital Port I/Os (Total)|Voltage DACs|ADC0 Channels|Comparator 0 Inputs|Comparator 1 Inputs|Pb-free (RoHS Compliant)|Package|
|---|---|---|---|---|---|---|---|---|---|
|EFM8BB31F64G-D-QFN32|64|4352|29|4|20|10|9|Yes|QFN32-GI|
|EFM8BB31F64G-D-QFP32|64|4352|28|4|20|10|9|Yes|QFP32|
|EFM8BB31F64G-D-QFN24|64|4352|20|4|12|6|6|Yes|QFN24-GI|



**silabs.com** | Building a more connected world. Rev. 1.5 | 3

EFM8BB3 Data Sheet
Ordering Information

|Ordering Part Number|Flash Memory (kB)|RAM (Bytes)|Digital Port I/Os (Total)|Voltage DACs|ADC0 Channels|Comparator 0 Inputs|Comparator 1 Inputs|Pb-free (RoHS Compliant)|Package|
|---|---|---|---|---|---|---|---|---|---|
|EFM8BB31F64G-D-QSOP241|64|4352|21|4|13|6|7|Yes|QSOP24|
|EFM8BB31F32G-D-QFN32|32|2304|29|22|20|10|9|Yes|QFN32-GI|
|EFM8BB31F32G-D-QFP32|32|2304|28|22|20|10|9|Yes|QFP32|
|EFM8BB31F32G-D-QFN24|32|2304|20|22|12|6|6|Yes|QFN24-GI|
|EFM8BB31F32G-D-QSOP241|32|2304|21|22|13|6|7|Yes|QSOP24|
|EFM8BB31F16G-D-QFN32|16|2304|29|22|20|10|9|Yes|QFN32-GI|
|EFM8BB31F16G-D-QFP32|16|2304|28|22|20|10|9|Yes|QFP32|
|EFM8BB31F16G-D-QFN24|16|2304|20|22|12|6|6|Yes|QFN24-GI|
|EFM8BB31F16G-D-QSOP241|16|2304|21|22|13|6|7|Yes|QSOP24|
|EFM8BB31F64I-D-QFN32|64|4352|29|4|20|10|9|Yes|QFN32-GI|
|EFM8BB31F64I-D-QFP32|64|4352|28|4|20|10|9|Yes|QFP32|
|EFM8BB31F64I-D-QFN24|64|4352|20|4|12|6|6|Yes|QFN24-GI|
|EFM8BB31F64I-D-QSOP241|64|4352|21|4|13|6|7|Yes|QSOP24|
|EFM8BB31F64I-D-5QFN32|64|4352|29|4|20|10|9|Yes|QFN32-AI|
|EFM8BB31F64I-D-4QFN24|64|4352|20|4|12|6|6|Yes|QFN24-AI|
|EFM8BB31F32I-D-QFN32|32|2304|29|22|20|10|9|Yes|QFN32-GI|
|EFM8BB31F32I-D-QFP32|32|2304|28|22|20|10|9|Yes|QFP32|
|EFM8BB31F32I-D-QFN24|32|2304|20|22|12|6|6|Yes|QFN24-GI|
|EFM8BB31F32I-D-QSOP241|32|2304|21|22|13|6|7|Yes|QSOP24|
|EFM8BB31F32I-D-5QFN32|32|2304|29|22|20|10|9|Yes|QFN32-AI|
|EFM8BB31F32I-D-4QFN24|32|2304|20|22|12|6|6|Yes|QFN24-AI|
|EFM8BB31F16I-D-QFN32|16|2304|29|22|20|10|9|Yes|QFN32-GI|
|EFM8BB31F16I-D-QFP32|16|2304|28|22|20|10|9|Yes|QFP32|
|EFM8BB31F16I-D-QFN24|16|2304|20|22|12|6|6|Yes|QFN24-GI|
|EFM8BB31F16I-D-QSOP241|16|2304|21|22|13|6|7|Yes|QSOP24|
|EFM8BB31F16I-D-5QFN32|16|2304|29|22|20|10|9|Yes|QFN32-AI|
|EFM8BB31F16I-D-4QFN24|16|2304|20|22|12|6|6|Yes|QFN24-AI|
|EFM8BB31F64A-D-5QFN32|64|4352|29|4|20|10|9|Yes|QFN32-AI|
|EFM8BB31F64A-D-4QFN24|64|4352|20|4|12|6|6|Yes|QFN24-AI|
|EFM8BB31F32A-D-5QFN32|32|2304|29|22|20|10|9|Yes|QFN32-AI|



**silabs.com** | Building a more connected world. Rev. 1.5 | 4

EFM8BB3 Data Sheet
Ordering Information

|Ordering Part Number|Flash Memory (kB)|RAM (Bytes)|Digital Port I/Os (Total)|Voltage DACs|ADC0 Channels|Comparator 0 Inputs|Comparator 1 Inputs|Pb-free (RoHS Compliant)|Package|
|---|---|---|---|---|---|---|---|---|---|
|EFM8BB31F32A-D-4QFN24|32|2304|20|22|12|6|6|Yes|QFN24-AI|
|EFM8BB31F16A-D-5QFN32|16|2304|29|22|20|10|9|Yes|QFN32-AI|
|EFM8BB31F16A-D-4QFN24|16|2304|20|22|12|6|6|Yes|QFN24-AI|
|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|Note:<br>1. End of life.<br>2. DAC0 and DAC1 are enabled on devices with 2 DACs available.|



The A-grade (i.e. EFM8BB31F64A-C-5QFN32 or EFM8BB31F64A-C-4QFN24) devices receive full automotive quality production status, including AEC-Q100 qualification, registration with International Material Data System (IMDS), and Part Production Approval Proc[ess (PPAP) documentation. PPAP documentation is available at www.silabs.com with a registered and NDA approved user account.](http://www.silabs.com)

**silabs.com** | Building a more connected world. Rev. 1.5 | 5

**Table of Contents**

**1. Feature List .** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 2**

**2. Ordering Information** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 3**

**3. System Overview .** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 9**

3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

3.2 Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .10

3.3 I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .10

3.4 Clocking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .11

3.5 Counters/Timers and PWM . . . . . . . . . . . . . . . . . . . . . . . . . .11

3.6 Communications and Other Digital Peripherals . . . . . . . . . . . . . . . . . . .12

3.7 Analog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .15

3.8 Reset Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16

3.9 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16

3.10 Bootloader . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .17

**4. Electrical Specifications** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 19**

4.1 Electrical Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . .19

4.1.1 Recommended Operating Conditions . . . . . . . . . . . . . . . . . . . . .19
4.1.2 Power Consumption. . . . . . . . . . . . . . . . . . . . . . . . . . .20
4.1.3 Reset and Supply Monitor. . . . . . . . . . . . . . . . . . . . . . . . .22
4.1.4 Flash Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . .23
4.1.5 Power Management Timing . . . . . . . . . . . . . . . . . . . . . . . .23

4.1.6 Internal Oscillators . . . . . . . . . . . . . . . . . . . . . . . . . . .24

4.1.7 External Clock Input. . . . . . . . . . . . . . . . . . . . . . . . . . .24

4.1.8 External Oscillator . . . . . . . . . . . . . . . . . . . . . . . . . . .25

4.1.9 ADC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .26

4.1.10 Voltage Reference . . . . . . . . . . . . . . . . . . . . . . . . . . .29
4.1.11 Temperature Sensor . . . . . . . . . . . . . . . . . . . . . . . . . .30
4.1.12 1.8 V Internal LDO Voltage Regulator . . . . . . . . . . . . . . . . . . . .30

4.1.13 DACs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .31

4.1.14 Comparators . . . . . . . . . . . . . . . . . . . . . . . . . . . . .32
4.1.15 Configurable Logic . . . . . . . . . . . . . . . . . . . . . . . . . . .33

4.1.16 Port I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .34

4.1.17 SMBus. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .35

4.1.18 SPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .37

4.2 Thermal Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . .39

4.3 Absolute Maximum Ratings. . . . . . . . . . . . . . . . . . . . . . . . . .40

**5. Typical Connection Diagrams** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 41**

5.1 Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .41

5.2 Debug . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .42

5.3 Other Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . .42

**silabs.com** | Building a more connected world. Rev. 1.5 | 6

**6. Pin Definitions .** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **43**

6.1 EFM8BB3x-QFN32 and EFM8BB3x-5QFN32 Pin Definitions . . . . . . . . . . . . . .43

6.2 EFM8BB3x-QFP32 Pin Definitions . . . . . . . . . . . . . . . . . . . . . . .48

6.3 EFM8BB3x-QFN24 and EFM8BB3x-4QFN24 Pin Definitions . . . . . . . . . . . . . .53

6.4 EFM8BB3x-QSOP24 Pin Definitions. . . . . . . . . . . . . . . . . . . . . . .58

**7. QFN32-GI Package Specifications** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.63**

7.1 Package Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . .63

7.2 PCB Land Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . .65

7.3 Package Marking . . . . . . . . . . . . . . . . . . . . . . . . . . . . .66

**8. QFN32-AI Package Specifications** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.67**

8.1 Package Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . .67

8.2 PCB Land Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . .69

8.3 Package Marking . . . . . . . . . . . . . . . . . . . . . . . . . . . . .70

**9. QFP32 Package Specifications.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **71**

9.1 Package Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . .71

9.2 PCB Land Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . .73

9.3 Package Marking . . . . . . . . . . . . . . . . . . . . . . . . . . . . .74

**10. QFN24-GI Package Specifications** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 75**

10.1 Package Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . .75

10.2 PCB Land Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . .77

10.3 Package Marking. . . . . . . . . . . . . . . . . . . . . . . . . . . . .78

**11. QFN24-AI Package Specifications** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 79**

11.1 Package Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . .79

11.2 PCB Land Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . .81

11.3 Package Marking. . . . . . . . . . . . . . . . . . . . . . . . . . . . .82

**12. QSOP24 Package Specifications** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.83**

12.1 Package Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . .83

12.2 PCB Land Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . .85

12.3 Package Marking. . . . . . . . . . . . . . . . . . . . . . . . . . . . .86

**13. Revision History.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **87**

13.1 Revision 1.5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .87

13.2 Revision 1.4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .87

13.3 Revision 1.3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .87

13.4 Revision 1.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .87

13.5 Revision 1.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .88

13.6 Revision 1.01 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .88

**silabs.com** | Building a more connected world. Rev. 1.5 | 7

13.7 Revision 1.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .88

13.8 Revision 0.4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .88

13.9 Revision 0.3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .88

13.10 Revision 0.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .89

13.11 Revision 0.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .89

**silabs.com** | Building a more connected world. Rev. 1.5 | 8

**3. System Overview**

**3.1 Introduction**


EFM8BB3 Data Sheet

System Overview

VIO






C2CK/RSTb

VDD

GND





P2.n

P3.n


P0.n

P1.n







|Col1|CIP-51 8051 Controller Port I/O Configuration<br>Debug / Core<br>C2D<br>Programming Digital Peripherals<br>Hardware<br>UART0<br>64 KB ISP Flash<br>Program Memory UART1<br>Reset<br>Timers 0,<br>Power-On 1, 2, 3, 4, 5<br>Reset 256 Byte SRAM Port 0<br>6-ch PCA Priority Drivers<br>Crossbar<br>Supply I2C Slave Decoder<br>Monitor 4096 Byte XRAM<br>I2C /<br>SMBus Port 1<br>Drivers<br>SPI<br>Power<br>Net CRC<br>Independent SYSCLK<br>Voltage Watchdog Config. Port 2<br>Regulator Timer SFR Logic C Cro os ns trb oa lr Drivers<br>Bus Units (4)<br>System Clock<br>Configuration Analog Peripherals Port 3<br>Drivers<br>Low Freq. Internal Up to 4 12-<br>Oscillator Reference bit DACs<br>CMOS Clock VDD VREF<br>EXTCLK<br>Input<br>XTAL1 External Crystal / VDD<br>XTAL2 RC Oscillator 12/10- AMUX<br>bit ADC<br>49 MHz 2% Temp<br>Oscillator Sensor<br>24.5 MHz 2%<br>Oscillator + -+<br>-<br>2 Comparators|Col3|Col4|
|---|---|---|---|
||CIP-51 8051 Controller Port I/O Configuration<br>Debug / Core<br>C2D<br>Programming Digital Peripherals<br>Hardware<br>UART0<br>64 KB ISP Flash<br>Program Memory UART1<br>Reset<br>Timers 0,<br>Power-On 1, 2, 3, 4, 5<br>Reset 256 Byte SRAM Port 0<br>6-ch PCA Priority Drivers<br>Crossbar<br>Supply I2C Slave Decoder<br>Monitor 4096 Byte XRAM<br>I2C /<br>SMBus Port 1<br>Drivers<br>SPI<br>Power<br>Net CRC<br>Independent SYSCLK<br>Voltage Watchdog Config. Port 2<br>Regulator Timer SFR Logic C Cro os ns trb oa lr Drivers<br>Bus Units (4)<br>System Clock<br>Configuration Analog Peripherals Port 3<br>Drivers<br>Low Freq. Internal Up to 4 12-<br>Oscillator Reference bit DACs<br>CMOS Clock VDD VREF<br>EXTCLK<br>Input<br>XTAL1 External Crystal / VDD<br>XTAL2 RC Oscillator 12/10- AMUX<br>bit ADC<br>49 MHz 2% Temp<br>Oscillator Sensor<br>24.5 MHz 2%<br>Oscillator + -+<br>-<br>2 Comparators|||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||


**Figure 3.1. Detailed EFM8BB3 Block Diagram**

This section describes the EFM8BB3 family at a high level.

For more information on the device packages and pinout, electrical specifications, and typical connection diagrams, see the EFM8BB3
Data Sheet. For more information on each module including register definitions, see the EFM8BB3 Reference Manual. For more information on any errata, see the EFM8BB3 Errata.

**silabs.com** | Building a more connected world. Rev. 1.5 | 9

EFM8BB3 Data Sheet

System Overview

**3.2 Power**

All internal circuitry draws power from the VDD supply pin. External I/O pins are powered from the VIO supply voltage (or VDD on devices without a separate VIO connection), while most of the internal circuitry is supplied by an on-chip LDO regulator. Control over the
device power can be achieved by enabling/disabling individual peripherals as needed. Each analog peripheral can be disabled when
not in use and placed in low power mode. Digital peripherals, such as timers and serial buses, have their clocks gated off and draw little
power when they are not in use.

**Table 3.1. Power Modes**


|Power Mode|Details|Mode Entry|Wake-Up Sources|
|---|---|---|---|
|Normal|Core and all peripherals clocked and fully operational|||
|Idle|• Core halted<br>• All peripherals clocked and fully operational<br>• Code resumes execution on wake event|Set IDLE bit in PCON0|Any interrupt|
|Suspend|• Core and peripheral clocks halted<br>• HFOSC0 and HFOSC1 oscillators stopped<br>• Regulator in normal bias mode for fast wake<br>• Timer 3 and 4 may clock from LFOSC0<br>• Code resumes execution on wake event|1. Switch SYSCLK to<br>HFOSC0<br>2. Set SUSPEND bit in<br>PCON1|• Timer 4 Event<br>• SPI0 Activity<br>• I2C0 Slave Activity<br>• Port Match Event<br>• Comparator 0 Falling<br>Edge<br>• CLUn Interrupt-Enabled<br>Event|
|Stop|• All internal power nets shut down<br>• Pins retain state<br>• Exit on any reset source|1. Clear STOPCF bit in<br>REG0CN<br>2. Set STOP bit in<br>PCON0|Any reset source|
|Snooze|• Core and peripheral clocks halted<br>• HFOSC0 and HFOSC1 oscillators stopped<br>• Regulator in low bias current mode for energy sav-<br>ings<br>• Timer 3 and 4 may clock from LFOSC0<br>• Code resumes execution on wake event|1. Switch SYSCLK to<br>HFOSC0<br>2. Set SNOOZE bit in<br>PCON1|• Timer 4 Event<br>• SPI0 Activity<br>• I2C0 Slave Activity<br>• Port Match Event<br>• Comparator 0 Falling<br>Edge<br>• CLUn Interrupt-Enabled<br>Event|
|Shutdown|• All internal power nets shut down<br>• Pins retain state<br>• Exit on pin or power-on reset|1. Set STOPCF bit in<br>REG0CN<br>2. Set STOP bit in<br>PCON0|• RSTb pin reset<br>• Power-on reset|


**3.3 I/O**





Digital and analog resources are externally available on the device’s multi-purpose I/O pins. Port pins P0.0-P2.3 can be defined as general-purpose I/O (GPIO), assigned to one of the internal digital resources through the crossbar or dedicated channels, or assigned to an
analog function. Port pins P2.4 to P3.7 can be used as GPIO. Additionally, the C2 Interface Data signal (C2D) is shared with P3.0 or
P3.7, depending on the package option.

The port control block offers the following features:

 - Up to 29 multi-function I/O pins, supporting digital and analog functions.

 - Flexible priority crossbar decoder for digital peripheral assignment.

 - Two drive strength settings for each port.

 - State retention feature allows pins to retain configuration through most reset sources.

 - Two direct-pin interrupt sources with dedicated interrupt vectors (INT0 and INT1).

 - Up to 24 direct-pin interrupt sources with shared interrupt vector (Port Match).

**silabs.com** | Building a more connected world. Rev. 1.5 | 10

EFM8BB3 Data Sheet

System Overview

**3.4 Clocking**

The CPU core and peripheral subsystem may be clocked by both internal and external oscillator resources. By default, the system
clock comes up running from the 24.5 MHz oscillator divided by 8.

The clock control system offers the following features:

 - Provides clock to core and peripherals.

 - 24.5 MHz internal oscillator (HFOSC0), accurate to ±2% over supply and temperature corners.

 - 49 MHz internal oscillator (HFOSC1), accurate to ±2% over supply and temperature corners.

 - 80 kHz low-frequency oscillator (LFOSC0).

 - External RC, and CMOS clock options (EXTCLK and EXTOSC).

 - Clock divider with eight settings for flexible clock scaling:

  - Divide the selected clock source by 1, 2, 4, 8, 16, 32, 64, or 128.

  - HFOSC0 and HFOSC1 include 1.5x pre-scalers for further flexibility.

**3.5 Counters/Timers and PWM**

**Programmable Counter Array (PCA0)**

The programmable counter array (PCA) provides multiple channels of enhanced timer and PWM functionality while requiring less CPU
intervention than standard counter/timers. The PCA consists of a dedicated 16-bit counter/timer and one 16-bit capture/compare module for each channel. The counter/timer is driven by a programmable timebase that has flexible external and internal clocking options.
Each capture/compare module may be configured to operate independently in one of five modes: Edge-Triggered Capture, Software
Timer, High-Speed Output, Frequency Output, or Pulse-Width Modulated (PWM) Output. Each capture/compare module has its own
associated I/O line (CEXn) which is routed through the crossbar to port I/O when enabled.

 - 16-bit time base

 - Programmable clock divisor and clock source selection

 - Up to six independently-configurable channels

 - 8, 9, 10, 11 and 16-bit PWM modes (center or edge-aligned operation)

 - Output polarity control

 - Frequency output mode

 - Capture on rising, falling or any edge

 - Compare function for arbitrary waveform generation

 - Software timer (internal compare) mode

 - Can accept hardware “kill” signal from comparator 0 or comparator 1

**silabs.com** | Building a more connected world. Rev. 1.5 | 11

EFM8BB3 Data Sheet

System Overview

**Timers (Timer 0, Timer 1, Timer 2, Timer 3, Timer 4, and Timer 5)**

Several counter/timers are included in the device: two are 16-bit counter/timers compatible with those found in the standard 8051, and
the rest are 16-bit auto-reload timers for timing peripherals or for general purpose use. These timers can be used to measure time intervals, count external events and generate periodic interrupt requests. Timer 0 and Timer 1 are nearly identical and have four primary
modes of operation. The other timers offer both 16-bit and split 8-bit timer functionality with auto-reload and capture capabilities.

Timer 0 and Timer 1 include the following features:

 - Standard 8051 timers, supporting backwards-compatibility with firmware and hardware.

 - Clock sources include SYSCLK, SYSCLK divided by 12, 4, or 48, the External Clock divided by 8, or an external pin.

 - 8-bit auto-reload counter/timer mode

 - 13-bit counter/timer mode

 - 16-bit counter/timer mode

 - Dual 8-bit counter/timer mode (Timer 0)

Timer 2, Timer 3, Timer 4, and Timer 5 are 16-bit timers including the following features:

 - Clock sources for all timers include SYSCLK, SYSCLK divided by 12, or the External Clock divided by 8

 - LFOSC0 divided by 8 may be used to clock Timer 3 and Timer 4 in active or suspend/snooze power modes

 - Timer 4 is a low-power wake source, and can be chained together with Timer 3

 - 16-bit auto-reload timer mode

 - Dual 8-bit auto-reload timer mode

 - External pin capture

 - LFOSC0 capture

 - Comparator 0 capture

 - Configurable Logic output capture

**Watchdog Timer (WDT0)**

The device includes a programmable watchdog timer (WDT) running off the low-frequency oscillator. A WDT overflow forces the MCU
into the reset state. To prevent the reset, the WDT must be restarted by application software before overflow. If the system experiences
a software or hardware malfunction preventing the software from restarting the WDT, the WDT overflows and causes a reset. Following
a reset, the WDT is automatically enabled and running with the default maximum time interval. If needed, the WDT can be disabled by
system software or locked on to prevent accidental disabling. Once locked, the WDT cannot be disabled until the next system reset.
The state of the RST pin is unaffected by this reset.

The Watchdog Timer has the following features:

 - Programmable timeout interval

 - Runs from the low-frequency oscillator

 - Lock-out feature to prevent any modification until a system reset

**3.6 Communications and Other Digital Peripherals**

**Universal Asynchronous Receiver/Transmitter (UART0)**

UART0 is an asynchronous, full duplex serial port offering modes 1 and 3 of the standard 8051 UART. Enhanced baud rate support
allows a wide range of clock sources to generate standard baud rates. Received data buffering allows UART0 to start reception of a
second incoming data byte before software has finished reading the previous data byte.

The UART module provides the following features:

 - Asynchronous transmissions and receptions.

 - Baud rates up to SYSCLK/2 (transmit) or SYSCLK/8 (receive).

 - 8- or 9-bit data.

 - Automatic start and stop generation.

 - Single-byte FIFO on transmit and receive.

**silabs.com** | Building a more connected world. Rev. 1.5 | 12

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

**I2C Slave (I2CSLAVE0)**

The I2C Slave interface is a 2-wire, bidirectional serial bus that is compatible with the I2C Bus Specification 3.0. It is capable of transferring in high-speed mode (HS-mode) at speeds of up to 3.4 Mbps. Firmware can write to the I2C interface, and the I2C interface can
autonomously control the serial transfer of data. The interface also supports clock stretching for cases where the core may be temporarily prohibited from transmitting a byte or processing a received byte during an I2C transaction. This module operates only as an I2C
slave device.

The I2C module includes the following features:

 - Standard (up to 100 kbps), Fast (400 kbps), Fast Plus (1 Mbps), and High-speed (3.4 Mbps) transfer speeds

 - Support for slave mode only

 - Clock low extending (clock stretching) to interface with faster masters

 - Hardware support for 7-bit slave address recognition

 - Transmit and receive FIFOs (two byte) to help increase throughput in faster applications

 - Hardware support for multiple slave addresses with the option to save the matching address in the receive FIFO

**16-bit CRC (CRC0)**

The cyclic redundancy check (CRC) module performs a CRC using a 16-bit polynomial. CRC0 accepts a stream of 8-bit data and posts
the 16-bit result to an internal register. In addition to using the CRC block for data manipulation, hardware can automatically CRC the
flash contents of the device.

The CRC module is designed to provide hardware calculations for flash memory verification and communications protocols. The CRC
module supports the standard CCITT-16 16-bit polynomial (0x1021), and includes the following features:

 - Support for CCITT-16 polynomial

 - Byte-level bit reversal

 - Automatic CRC of flash contents on one or more 256-byte blocks

 - Initial seed selection of 0x0000 or 0xFFFF

**Configurable Logic Units (CLU0, CLU1, CLU2, and CLU3)**

The Configurable Logic block consists of multiple Configurable Logic Units (CLUs). CLUs are flexible logic functions which may be used
for a variety of digital functions, such as replacing system glue logic, aiding in the generation of special waveforms, or synchronizing
system event triggers.

 - Four configurable logic units (CLUs), with direct-pin and internal logic connections

 - Each unit supports 256 different combinatorial logic functions (AND, OR, XOR, muxing, etc.) and includes a clocked flip-flop for synchronous operations

 - Units may be operated synchronously or asynchronously

 - May be cascaded together to perform more complicated logic functions

 - Can operate in conjunction with serial peripherals such as UART and SPI or timing peripherals such as timers and PCA channels

 - Can be used to synchronize and trigger multiple on-chip resources (ADC, DAC, Timers, etc.)

 - Asynchronous output may be used to wake from low-power states

**silabs.com** | Building a more connected world. Rev. 1.5 | 14

EFM8BB3 Data Sheet

System Overview

**3.7 Analog**

**12/10-Bit Analog-to-Digital Converter (ADC0)**

The ADC is a successive-approximation-register (SAR) ADC with 12- and 10-bit modes, integrated track-and hold and a programmable
window detector. The ADC is fully configurable under software control via several registers. The ADC may be configured to measure
different signals using the analog multiplexer. The voltage reference for the ADC is selectable between internal and external reference

sources.

 - Up to 20 external inputs

 - Single-ended 12-bit and 10-bit modes

 - Supports an output update rate of up to 350 ksps in 12-bit mode

 - Channel sequencer logic with direct-to-XDATA output transfers

 - Operation in a low power mode at lower conversion speeds

 - Asynchronous hardware conversion trigger, selectable between software, external I/O and internal timer and configurable logic sour
ces

 - Output data window comparator allows automatic range checking

 - Support for output data accumulation

 - Conversion complete and window compare interrupts supported

 - Flexible output data formatting

 - Includes a fully-internal fast-settling 1.65 V reference and an on-chip precision 2.4 / 1.2 V reference, with support for using the supply as the reference, an external reference and signal ground

 - Integrated temperature sensor

**12-Bit Digital-to-Analog Converters (DAC0, DAC1, DAC2, DAC3)**

The DAC modules are 12-bit Digital-to-Analog Converters with the capability to synchronize multiple outputs together. The DACs are
fully configurable under software control. The voltage reference for the DACs is selectable between internal and external reference

sources.

 - Voltage output with 12-bit performance

 - Supports an update rate of 200 ksps

 - Hardware conversion trigger, selectable between software, external I/O and internal timer and configurable logic sources

 - Outputs may be configured to persist through reset and maintain output state to avoid system disruption

 - Multiple DAC outputs can be synchronized together

 - DAC pairs (DAC0 and 1 or DAC2 and 3) support complementary output waveform generation

 - Outputs may be switched between two levels according to state of configurable logic / PWM input trigger

 - Flexible input data formatting

 - Supports references from internal supply, on-chip precision reference, or external VREF pin

**silabs.com** | Building a more connected world. Rev. 1.5 | 15

EFM8BB3 Data Sheet

System Overview

**Low Current Comparators (CMP0, CMP1)**

An analog comparator is used to compare the voltage of two analog inputs, with a digital output indicating which input voltage is higher.
External input connections to device I/O pins and internal connections are available through separate multiplexers on the positive and
negative inputs. Hysteresis, response time, and current consumption may be programmed to suit the specific needs of the application.

The comparator includes the following features:

 - Up to 10 (CMP0) or 9 (CMP1) external positive inputs

 - Up to 10 (CMP0) or 9 (CMP1) external negative inputs

 - Additional input options:

  - Internal connection to LDO output

  - Direct connection to GND

  - Direct connection to VDD

  - Dedicated 6-bit reference DAC

 - Synchronous and asynchronous outputs can be routed to pins via crossbar

 - Programmable hysteresis between 0 and ±20 mV

 - Programmable response time

 - Interrupts generated on rising, falling, or both edges

 - PWM output kill feature

**3.8 Reset Sources**

Reset circuitry allows the controller to be easily placed in a predefined default condition. On entry to this reset state, the following occur:

 - The core halts program execution.

 - Module registers are initialized to their defined reset values unless the bits reset only with a power-on reset.

 - External port pins are forced to a known state.

 - Interrupts and timers are disabled.
All registers are reset to the predefined values noted in the register descriptions unless the bits only reset with a power-on reset. The
contents of RAM are unaffected during a reset; any previously stored data is preserved as long as power is not lost. By default, the Port
I/O latches are reset to 1 in open-drain mode, with weak pullups enabled during and after the reset. Optionally, firmware may configure
the port I/O, DAC outputs, and precision reference to maintain state through system resets other than power-on resets. For Supply
Monitor and power-on resets, the RSTb pin is driven low until the device exits the reset state. On exit from the reset state, the program
counter (PC) is reset, and the system clock defaults to an internal oscillator. The Watchdog Timer is enabled, and program execution
begins at location 0x0000.

Reset sources on the device include the following:

 - Power-on reset

 - External reset pin

 - Comparator reset

 - Software-triggered reset

 - Supply monitor reset (monitors VDD supply)

 - Watchdog timer reset

 - Missing clock detector reset

 - Flash error reset

**3.9 Debugging**

The EFM8BB3 devices include an on-chip Silicon Labs 2-Wire (C2) debug interface to allow flash programming and in-system debugging with the production part installed in the end application. The C2 interface uses a clock signal (C2CK) and a bi-directional C2 data
signal (C2D) to transfer information between the device and a host system. See the C2 Interface Specification for details on the C2
protocol.

**silabs.com** | Building a more connected world. Rev. 1.5 | 16

EFM8BB3 Data Sheet

System Overview

**3.10 Bootloader**

All devices come pre-programmed with a UART0 bootloader. This bootloader resides in the code security page, which is the last page
of code flash; it can be erased if it is not needed.

The byte before the Lock Byte is the Bootloader Signature Byte. Setting this byte to a value of 0xA5 indicates the presence of the bootloader in the system. Any other value in this location indicates that the bootloader is not present in flash.

When a bootloader is present, the device will jump to the bootloader vector after any reset, allowing the bootloader to run. The bootloader then determines if the device should stay in bootload mode or jump to the reset vector located at 0x0000. When the bootloader
is not present, the device will jump to the reset vector of 0x0000 after any reset.

Silicon Labs recommends the bootloader be disabled and the flash memory locked after the production programming step in applications where code security is a concern. More information about the factory bootloader protocol, usage, customization and best practices
can be found in *AN945: EFM8 Factory Bootloader User Guide* [. Application notes can be found on the Silicon Labs website (www.si-](http://www.silabs.com/8bit-appnotes)
[labs.com/8bit-appnotes) or within Simplicity Studio by using the [](http://www.silabs.com/8bit-appnotes) **Application Notes** ] tile.

0xFFFF



0xFFC0

0xFFBF

0xFC00

0xFBFF

0xFBFE

0xFBFD

0xFA00

0xF9FF




Bootloader Vector



0x0000
Reset Vector

**Figure 3.2. Flash Memory Map with Bootloader — 62.5 KB Devices**

**Table 3.2. Summary of Pins for Bootloader Communication**

|Bootloader|Pins for Bootload Communication|
|---|---|
|UART|TX – P0.4|
|UART|RX – P0.5|



**silabs.com** | Building a more connected world. Rev. 1.5 | 17

EFM8BB3 Data Sheet

System Overview

**Table 3.3. Summary of Pins for Bootload Mode Entry**

|Device Package|Pin for Bootload Mode Entry|
|---|---|
|all QFN32 packages|P3.7 / C2D|
|QFP32|P3.7 / C2D|
|all QFN24 packages|P3.0 / C2D|
|QSOP24|P3.0 / C2D|



**silabs.com** | Building a more connected world. Rev. 1.5 | 18

EFM8BB3 Data Sheet
Electrical Specifications

**4. Electrical Specifications**

**4.1 Electrical Characteristics**

All electrical parameters in all tables are specified under the conditions listed in Table 4.1 Recommended Operating Conditions on page
19, unless stated otherwise.

**4.1.1 Recommended Operating Conditions**

**Table 4.1. Recommended Operating Conditions**

|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Operating Supply Voltage on VDD|V<br>DD||2.2|—|3.6|V|
|Operating Supply Voltage on VIO2,|V<br>IO||2.2|—|V<br>DD|V|
|System Clock Frequency|f<br>SYSCLK||0|—|50|MHz|
|Operating Ambient Temperature|T<br>A|G-grade devices|–40|—|85|°C|
|Operating Ambient Temperature|T<br>A|I-grade or A-grade devices|-40|—|125|°C|
|Note:<br>1. All voltages with respect to GND<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.<br>3. I/O have reduced current drive/sink capabilities at lower VIO levels. See 4.1.16 Port I/O for additional information.|Note:<br>1. All voltages with respect to GND<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.<br>3. I/O have reduced current drive/sink capabilities at lower VIO levels. See 4.1.16 Port I/O for additional information.|Note:<br>1. All voltages with respect to GND<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.<br>3. I/O have reduced current drive/sink capabilities at lower VIO levels. See 4.1.16 Port I/O for additional information.|Note:<br>1. All voltages with respect to GND<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.<br>3. I/O have reduced current drive/sink capabilities at lower VIO levels. See 4.1.16 Port I/O for additional information.|Note:<br>1. All voltages with respect to GND<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.<br>3. I/O have reduced current drive/sink capabilities at lower VIO levels. See 4.1.16 Port I/O for additional information.|Note:<br>1. All voltages with respect to GND<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.<br>3. I/O have reduced current drive/sink capabilities at lower VIO levels. See 4.1.16 Port I/O for additional information.|Note:<br>1. All voltages with respect to GND<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.<br>3. I/O have reduced current drive/sink capabilities at lower VIO levels. See 4.1.16 Port I/O for additional information.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 19

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.2 Power Consumption**

**Table 4.2. Power Consumption**






|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 49 MHz (HFOSC1)2<br>SYSCLK|—|5|14.4|mA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 24.5 MHz (HFOSC0)2<br>SYSCLK|—|4.2|5|mA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 1.53 MHz (HFOSC0)2<br>SYSCLK|—|625|820|μA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 80 kHz3<br>SYSCLK|—|155|310|μA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 49 MHz (HFOSC1)2<br>SYSCLK|—|3.8|11.8|mA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 24.5 MHz (HFOSC0)2<br>SYSCLK|—|3.14|3.8|mA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 1.53 MHz (HFOSC0)2<br>SYSCLK|—|520|725|μA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 80 kHz3<br>SYSCLK|—|135|315|μA|
|Suspend Mode-Core halted and<br>high frequency clocks stopped,<br>Supply monitor off.|I<br>DD|LFO Running|—|125|320|μA|
|Suspend Mode-Core halted and<br>high frequency clocks stopped,<br>Supply monitor off.|I<br>DD|LFO Stopped|—|120|300|μA|
|Snooze Mode-Core halted and<br>high frequency clocks stopped.<br>Regulator in low-power state, Sup-<br>ply monitor off.|I<br>DD|LFO Running|—|23|190|μA|
|Snooze Mode-Core halted and<br>high frequency clocks stopped.<br>Regulator in low-power state, Sup-<br>ply monitor off.|I<br>DD|LFO Stopped|—|19|186|μA|
|Stop Mode—Core halted and all<br>clocks stopped,Internal LDO On,<br>Supply monitor off.|I<br>DD||—|120|300|μA|
|Shutdown Mode—Core halted and<br>all clocks stopped,Internal LDO<br>Off, Supply monitor off.|I<br>DD||—|0.2|0.91|μA|
|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 49 MHz (HFOSC1)2<br>SYSCLK|—|5|14.4|mA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 24.5 MHz (HFOSC0)2<br>SYSCLK|—|4.2|5.2|mA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 1.53 MHz (HFOSC0)2<br>SYSCLK|—|625|1280|μA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 80 kHz3<br>SYSCLK|—|155|765|μA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 49 MHz (HFOSC1)2<br>SYSCLK|—|3.8|11.8|mA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 24.5 MHz (HFOSC0)2<br>SYSCLK|—|3.14|4.1|mA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 1.53 MHz (HFOSC0)2<br>SYSCLK|—|520|1175|μA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 80 kHz3<br>SYSCLK|—|135|750|μA|
|Suspend Mode-Core halted and<br>high frequency clocks stopped,<br>Supply monitor off.|I<br>DD|LFO Running|—|125|775|μA|
|Suspend Mode-Core halted and<br>high frequency clocks stopped,<br>Supply monitor off.|I<br>DD|LFO Stopped|—|120|755|μA|


**silabs.com** | Building a more connected world. Rev. 1.5 | 20

EFM8BB3 Data Sheet
Electrical Specifications









|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Snooze Mode-Core halted and<br>high frequency clocks stopped.<br>Regulator in low-power state, Sup-<br>ply monitor off.|I<br>DD|LFO Running|—|23|615|μA|
|Snooze Mode-Core halted and<br>high frequency clocks stopped.<br>Regulator in low-power state, Sup-<br>ply monitor off.|I<br>DD|LFO Stopped|—|19|610|μA|
|Stop Mode—Core halted and all<br>clocks stopped,Internal LDO On,<br>Supply monitor off.|I<br>DD||—|120|740|μA|
|Shutdown Mode—Core halted and<br>all clocks stopped,Internal LDO<br>Off, Supply monitor off.|I<br>DD||—|0.2|4.5|μA|
|Analog Peripheral Supply Currents (-40 °C to +125 °C)|Analog Peripheral Supply Currents (-40 °C to +125 °C)|Analog Peripheral Supply Currents (-40 °C to +125 °C)|Analog Peripheral Supply Currents (-40 °C to +125 °C)|Analog Peripheral Supply Currents (-40 °C to +125 °C)|Analog Peripheral Supply Currents (-40 °C to +125 °C)|Analog Peripheral Supply Currents (-40 °C to +125 °C)|
|High-Frequency Oscillator 0|I<br>HFOSC0|Operating at 24.5 MHz,<br>T = 25 °C<br>A|—|120|135|μA|
|High-Frequency Oscillator 1|I<br>HFOSC1|Operating at 49 MHz,<br>T = 25 °C<br>A|—|770|1200|μA|
|Low-Frequency Oscillator|I<br>LFOSC|Operating at 80 kHz,<br>T = 25 °C<br>A|—|3.7|6|μA|
|ADC04|I<br>ADC|High Speed Mode<br>1 Msps, 10-bit conversions<br>Normal bias settings<br>V = 3.0 V<br>DD|—|1210|1600|μA|
|ADC04|I<br>ADC|Low Power Mode<br>350 ksps, 12-bit conversions<br>Low power bias settings<br>V = 3.0 V<br>DD|—|415|560|μA|
|Internal ADC0 Reference5|I<br>VREFFS|High Speed Mode|—|700|790|μA|
|Internal ADC0 Reference5|I<br>VREFFS|Low Power Mode|—|170|210|μA|
|On-chip Precision Reference|I<br>VREFP||—|75|—|µA|
|Temperature Sensor|I<br>TSENSE||—|68|120|μA|
|Digital-to-Analog Converters<br>(DAC0, DAC1, DAC2, DAC3)6|I<br>DAC||—|125|—|µA|
|Comparators (CMP0, CMP1)|I<br>CMP|CPMD = 11|—|0.5|—|μA|
|Comparators (CMP0, CMP1)|I<br>CMP|CPMD = 10|—|3|—|μA|
|Comparators (CMP0, CMP1)|I<br>CMP|CPMD = 01|—|10|—|μA|
|Comparators (CMP0, CMP1)|I<br>CMP|CPMD = 00|—|25|—|μA|
|Comparator Reference7|I<br>CPREF||—|24|—|μA|
|Voltage Supply Monitor (VMON0)|I<br>VMON||—|15|20|μA|


**silabs.com** | Building a more connected world. Rev. 1.5 | 21

EFM8BB3 Data Sheet
Electrical Specifications

|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|



**4.1.3 Reset and Supply Monitor**

**Table 4.3. Reset and Supply Monitor**







|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDD Supply Monitor Threshold|V<br>VDDM||1.95|2.05|2.15|V|
|Power-On Reset (POR) Threshold|V<br>POR|Rising Voltage on VDD|—|1.4|—|V|
|Power-On Reset (POR) Threshold|V<br>POR|Falling Voltage on VDD|0.75|—|1.36|V|
|VDD Ramp Time|t<br>RMP|Time to V > 2.2 V<br>DD|10|—|—|μs|
|Reset Delay from POR|t<br>POR|Relative to V > V<br>DD POR|3|10|31|ms|
|Reset Delay from non-POR source|t<br>RST|Time between release of reset<br>source and code execution|—|50|—|μs|
|RST Low Time to Generate Reset|t<br>RSTL||15|—|—|μs|
|Missing Clock Detector Response<br>Time (final rising edge to reset)|t<br>MCD|F >1 MHz<br>SYSCLK|—|0.625|1.2|ms|
|Missing Clock Detector Trigger<br>Frequency|F<br>MCD||—|7.5|13.5|kHz|
|VDD Supply Monitor Turn-On Time|t<br>MON||—|2|—|μs|


**silabs.com** | Building a more connected world. Rev. 1.5 | 22

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.4 Flash Memory**

**Table 4.4. Flash Memory**







|Parameter|Symbol|Test Condition|Min|Typ|Max|Units|
|---|---|---|---|---|---|---|
|Write Time1,2|t<br>WRITE|One Byte,<br>F = 24.5 MHz<br>SYSCLK|19|20|21|μs|
|Erase Time1,2|t<br>ERASE|One Page,<br>F = 24.5 MHz<br>SYSCLK|5.2|5.35|5.5|ms|
|V Voltage During Programming3<br>DD|V<br>PROG||2.2|—|3.6|V|
|Endurance (Write/Erase Cycles)|N<br>WE||20k|100k|—|Cycles|
|CRC Calculation Time|t<br>CRC|One 256-Byte Block<br>SYSCLK = 49 MHz|—|5.5|—|µs|
|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|


**4.1.5 Power Management Timing**

**Table 4.5. Power Management Timing**





|Parameter|Symbol|Test Condition|Min|Typ|Max|Units|
|---|---|---|---|---|---|---|
|Idle Mode Wake-up Time|t<br>IDLEWK||2|—|3|SYSCLKs|
|Suspend Mode Wake-up Time|t<br>SUS-<br>PENDWK|SYSCLK = HFOSC0<br>CLKDIV = 0x00|—|170|—|ns|
|Snooze Mode Wake-up Time|t<br>SLEEPWK|SYSCLK = HFOSC0<br>CLKDIV = 0x00|—|12|—|µs|


**silabs.com** | Building a more connected world. Rev. 1.5 | 23

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.6 Internal Oscillators**

**Table 4.6. Internal Oscillators**














|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|High Frequency Oscillator 0 (24.5 MHz)|High Frequency Oscillator 0 (24.5 MHz)|High Frequency Oscillator 0 (24.5 MHz)|High Frequency Oscillator 0 (24.5 MHz)|High Frequency Oscillator 0 (24.5 MHz)|High Frequency Oscillator 0 (24.5 MHz)|High Frequency Oscillator 0 (24.5 MHz)|
|Oscillator Frequency|f<br>HFOSC0|Full Temperature and Supply<br>Range|24|24.5|25|MHz|
|Power Supply Sensitivity|PSS<br>HFOS<br>C0|T = 25 °C<br>A|—|0.5|—|%/V|
|Temperature Sensitivity|TS<br>HFOSC0|V = 3.0 V<br>DD|—|40|—|ppm/°C|
|High Frequency Oscillator 1 (49 MHz)|High Frequency Oscillator 1 (49 MHz)|High Frequency Oscillator 1 (49 MHz)|High Frequency Oscillator 1 (49 MHz)|High Frequency Oscillator 1 (49 MHz)|High Frequency Oscillator 1 (49 MHz)|High Frequency Oscillator 1 (49 MHz)|
|Oscillator Frequency|f<br>HFOSC1|Full Temperature and Supply<br>Range|48.02|49|49.98|MHz|
|Power Supply Sensitivity|PSS<br>HFOS<br>C1|T = 25 °C<br>A|—|300|—|ppm/V|
|Temperature Sensitivity|TS<br>HFOSC1|V = 3.0 V<br>DD|—|103|—|ppm/°C|
|Low Frequency Oscillator (80 kHz)|Low Frequency Oscillator (80 kHz)|Low Frequency Oscillator (80 kHz)|Low Frequency Oscillator (80 kHz)|Low Frequency Oscillator (80 kHz)|Low Frequency Oscillator (80 kHz)|Low Frequency Oscillator (80 kHz)|
|Oscillator Frequency|f<br>LFOSC|Full Temperature and Supply<br>Range|75|80|85|kHz|
|Power Supply Sensitivity|PSS<br>LFOSC|T = 25 °C<br>A|—|0.05|—|%/V|
|Temperature Sensitivity|TS<br>LFOSC|V = 3.0 V<br>DD|—|65|—|ppm/°C|


**4.1.7 External Clock Input**

**Table 4.7. External Clock Input**



|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|External Input CMOS Clock<br>Frequency (at EXTCLK pin)|f<br>CMOS||0|—|50|MHz|
|External Input CMOS Clock High<br>Time|t<br>CMOSH||9|—|—|ns|
|External Input CMOS Clock Low<br>Time|t<br>CMOSL||9|—|—|ns|


**silabs.com** | Building a more connected world. Rev. 1.5 | 24

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.8 External Oscillator**

**Table 4.8. External Oscillator**



|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Crystal Frequency|f<br>XTAL||0.02|—|25|MHz|
|Crystal Drive Current|I<br>XTAL|XFCN = 000|—|0.5|—|μA|
|Crystal Drive Current|I<br>XTAL|XFCN = 001|—|1.5|—|μA|
|Crystal Drive Current|I<br>XTAL|XFCN = 010|—|4.8|—|μA|
|Crystal Drive Current|I<br>XTAL|XFCN = 011|—|14|—|μA|
|Crystal Drive Current|I<br>XTAL|XFCN = 100|—|40|—|μA|
|Crystal Drive Current|I<br>XTAL|XFCN = 101|—|120|—|μA|
|Crystal Drive Current|I<br>XTAL|XFCN = 110|—|550|—|μA|
|Crystal Drive Current|I<br>XTAL|XFCN = 111|—|2.6|—|mA|
|Frequency Range (resonators and<br>RC oscillators)|f<br>EXTOSC|XFCN = 000|0.02|—|25|kHz|
|Frequency Range (resonators and<br>RC oscillators)|f<br>EXTOSC|XFCN = 001|25|—|50|kHz|
|Frequency Range (resonators and<br>RC oscillators)|f<br>EXTOSC|XFCN = 010|50|—|100|kHz|
|Frequency Range (resonators and<br>RC oscillators)|f<br>EXTOSC|XFCN = 011|100|—|200|kHz|
|Frequency Range (resonators and<br>RC oscillators)|f<br>EXTOSC|XFCN = 100|200|—|400|kHz|
|Frequency Range (resonators and<br>RC oscillators)|f<br>EXTOSC|XFCN = 101|400|—|800|kHz|
|Frequency Range (resonators and<br>RC oscillators)|f<br>EXTOSC|XFCN = 110|800|—|1600|kHz|
|Frequency Range (resonators and<br>RC oscillators)|f<br>EXTOSC|XFCN = 111|1.6|—|3.2|MHz|


**silabs.com** | Building a more connected world. Rev. 1.5 | 25

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.9 ADC**

**Table 4.9. ADC**










|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Resolution|N<br>bits|12 Bit Mode|12|12|12|Bits|
|Resolution|N<br>bits|10 Bit Mode|10|10|10|Bits|
|Throughput Rate<br>(High Speed Mode)|f<br>S|10 Bit Mode|—|—|1.125|Msps|
|Throughput Rate<br>(Low Power Mode)|f<br>S|12 Bit Mode|—|—|340|ksps|
|Throughput Rate<br>(Low Power Mode)|f<br>S|10 Bit Mode|—|—|360|ksps|
|Tracking Time|t<br>TRK|High Speed Mode|230|—|—|ns|
|Tracking Time|t<br>TRK|Low Power Mode|450|—|—|ns|
|Power-On Time|t<br>PWR||1.2|—|—|μs|
|SAR Clock Frequency|f<br>SAR|High Speed Mode|—|—|18|MHz|
|SAR Clock Frequency|f<br>SAR|Low Power Mode|—|—|12.25|MHz|
|Conversion Time1|t<br>CNV|12-Bit Conversion,<br>SAR Clock = 6.125 MHz,<br>System Clock = 49 MHz|2.0|2.0|2.0|μs|
|Conversion Time1|t<br>CNV|10-Bit Conversion,<br>SAR Clock = 16.33 MHz,<br>System Clock = 49 MHz|0.658|0.658|0.658|μs|
|Sample/Hold Capacitor|C<br>SAR|Gain = 1|—|5.2|—|pF|
|Sample/Hold Capacitor|C<br>SAR|Gain = 0.75|—|3.9|—|pF|
|Sample/Hold Capacitor|C<br>SAR|Gain = 0.5|—|2.6|—|pF|
|Sample/Hold Capacitor|C<br>SAR|Gain = 0.25|—|1.3|—|pF|
|Input Pin Capacitance|C<br>IN||—|20|—|pF|
|Input Mux Impedance|R<br>MUX||—|550|—|Ω|
|Voltage Reference Range|V<br>REF||1|—|V<br>IO|V|
|Input Voltage Range2|V<br>IN||0|—|V /<br>REF<br>Gain|V|
|Power Supply Rejection Ratio|PSRR<br>ADC|At 1 kHz|—|66|—|dB|
|Power Supply Rejection Ratio|PSRR<br>ADC|At 1 MHz|—|43|—|dB|
|DC Performance|DC Performance|DC Performance|DC Performance|DC Performance|DC Performance|DC Performance|


**silabs.com** | Building a more connected world. Rev. 1.5 | 26

EFM8BB3 Data Sheet
Electrical Specifications














|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Integral Nonlinearity|INL|12 Bit Mode|-1.9|-0.35 / +1|1.9|LSB|
|Integral Nonlinearity|INL|10 Bit Mode<br>T = -40 °C to 85 °C<br>A|-0.6|±0.2|0.6|LSB|
|Integral Nonlinearity|INL|10 Bit Mode<br>T = -40 °C to 125 °C (I-grade or<br>A<br>A-grade parts only)|-0.7|±0.2|0.7|LSB|
|Differential Nonlinearity (Guaran-<br>teed Monotonic)|DNL|12 Bit Mode<br>T = -40 °C to 85 °C<br>A|-0.9|±0.3|0.9|LSB|
|Differential Nonlinearity (Guaran-<br>teed Monotonic)|DNL|12 Bit Mode<br>T = -40 °C to 125 °C (I-grade or<br>A<br>A-grade parts only)|-1.02|±0.3|1.02|LSB|
|Differential Nonlinearity (Guaran-<br>teed Monotonic)|DNL|10 Bit Mode|-0.5|±0.2|0.5|LSB|
|Offset Error3|E<br>OFF|12 Bit Mode<br>T = -40 °C to 85 °C<br>A|-2|0|2|LSB|
|Offset Error3|E<br>OFF|12 Bit Mode<br>T = -40 °C to 125 °C (I-grade or<br>A<br>A-grade parts only)|-3|0|3|LSB|
|Offset Error3|E<br>OFF|10 Bit Mode<br>T = -40 °C to 85 °C<br>A|-1|0|1|LSB|
|Offset Error3|E<br>OFF|10 Bit Mode<br>T = -40 °C to 125 °C (I-grade or<br>A<br>A-grade parts only)|-1|0|1.3|LSB|
|Offset Temperature Coefficient|TC<br>OFF||—|0.011|—|LSB/°C|
|Slope Error|E<br>M|12 Bit Mode<br>T = -40 °C to 85 °C<br>A|-2.5|—|2.5|LSB|
|Slope Error|E<br>M|12 Bit Mode<br>T = -40 °C to 125 °C (I-grade or<br>A<br>A-grade parts only)|-2.6|—|2.6|LSB|
|Slope Error|E<br>M|10 Bit Mode|-1.1|—|1.1|LSB|
|Dynamic Performance 10 kHz Sine Wave Input 1 dB below full scale, Max throughput, using AGND pin|Dynamic Performance 10 kHz Sine Wave Input 1 dB below full scale, Max throughput, using AGND pin|Dynamic Performance 10 kHz Sine Wave Input 1 dB below full scale, Max throughput, using AGND pin|Dynamic Performance 10 kHz Sine Wave Input 1 dB below full scale, Max throughput, using AGND pin|Dynamic Performance 10 kHz Sine Wave Input 1 dB below full scale, Max throughput, using AGND pin|Dynamic Performance 10 kHz Sine Wave Input 1 dB below full scale, Max throughput, using AGND pin|Dynamic Performance 10 kHz Sine Wave Input 1 dB below full scale, Max throughput, using AGND pin|
|Signal-to-Noise|SNR|12 Bit Mode|64|68|—|dB|
|Signal-to-Noise|SNR|10 Bit Mode|59|61|—|dB|
|Signal-to-Noise Plus Distortion|SNDR|12 Bit Mode|64|68|—|dB|
|Signal-to-Noise Plus Distortion|SNDR|10 Bit Mode|59|61|—|dB|
|Total Harmonic Distortion (Up to<br>5th Harmonic)|THD|12 Bit Mode|—|-72|—|dB|
|Total Harmonic Distortion (Up to<br>5th Harmonic)|THD|10 Bit Mode|—|-69|—|dB|
|Spurious-Free Dynamic Range|SFDR|12 Bit Mode|—|74|—|dB|
|Spurious-Free Dynamic Range|SFDR|10 Bit Mode|—|71|—|dB|


**silabs.com** | Building a more connected world. Rev. 1.5 | 27

EFM8BB3 Data Sheet
Electrical Specifications

|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Note:<br>1. Conversion Time does not include Tracking Time. Total Conversion Time is:<br>Total Conversion Time = [RPT x (ADTK + NUMBITS + 1) x T(SARCLK)] + (T(ADCCLK) x 4)<br>where RPT is the number of conversions represented by the ADRPT field and ADCCLK is the clock selected for the ADC.<br>2. Absolute input pin voltage is limited by the V supply.<br>IO<br>3. The offset is determined using curve fitting since the specification is measured using linear search where the intercept is always<br>positive.<br>4. Production test uses a 2.4 V external reference and external ground.|Note:<br>1. Conversion Time does not include Tracking Time. Total Conversion Time is:<br>Total Conversion Time = [RPT x (ADTK + NUMBITS + 1) x T(SARCLK)] + (T(ADCCLK) x 4)<br>where RPT is the number of conversions represented by the ADRPT field and ADCCLK is the clock selected for the ADC.<br>2. Absolute input pin voltage is limited by the V supply.<br>IO<br>3. The offset is determined using curve fitting since the specification is measured using linear search where the intercept is always<br>positive.<br>4. Production test uses a 2.4 V external reference and external ground.|Note:<br>1. Conversion Time does not include Tracking Time. Total Conversion Time is:<br>Total Conversion Time = [RPT x (ADTK + NUMBITS + 1) x T(SARCLK)] + (T(ADCCLK) x 4)<br>where RPT is the number of conversions represented by the ADRPT field and ADCCLK is the clock selected for the ADC.<br>2. Absolute input pin voltage is limited by the V supply.<br>IO<br>3. The offset is determined using curve fitting since the specification is measured using linear search where the intercept is always<br>positive.<br>4. Production test uses a 2.4 V external reference and external ground.|Note:<br>1. Conversion Time does not include Tracking Time. Total Conversion Time is:<br>Total Conversion Time = [RPT x (ADTK + NUMBITS + 1) x T(SARCLK)] + (T(ADCCLK) x 4)<br>where RPT is the number of conversions represented by the ADRPT field and ADCCLK is the clock selected for the ADC.<br>2. Absolute input pin voltage is limited by the V supply.<br>IO<br>3. The offset is determined using curve fitting since the specification is measured using linear search where the intercept is always<br>positive.<br>4. Production test uses a 2.4 V external reference and external ground.|Note:<br>1. Conversion Time does not include Tracking Time. Total Conversion Time is:<br>Total Conversion Time = [RPT x (ADTK + NUMBITS + 1) x T(SARCLK)] + (T(ADCCLK) x 4)<br>where RPT is the number of conversions represented by the ADRPT field and ADCCLK is the clock selected for the ADC.<br>2. Absolute input pin voltage is limited by the V supply.<br>IO<br>3. The offset is determined using curve fitting since the specification is measured using linear search where the intercept is always<br>positive.<br>4. Production test uses a 2.4 V external reference and external ground.|Note:<br>1. Conversion Time does not include Tracking Time. Total Conversion Time is:<br>Total Conversion Time = [RPT x (ADTK + NUMBITS + 1) x T(SARCLK)] + (T(ADCCLK) x 4)<br>where RPT is the number of conversions represented by the ADRPT field and ADCCLK is the clock selected for the ADC.<br>2. Absolute input pin voltage is limited by the V supply.<br>IO<br>3. The offset is determined using curve fitting since the specification is measured using linear search where the intercept is always<br>positive.<br>4. Production test uses a 2.4 V external reference and external ground.|Note:<br>1. Conversion Time does not include Tracking Time. Total Conversion Time is:<br>Total Conversion Time = [RPT x (ADTK + NUMBITS + 1) x T(SARCLK)] + (T(ADCCLK) x 4)<br>where RPT is the number of conversions represented by the ADRPT field and ADCCLK is the clock selected for the ADC.<br>2. Absolute input pin voltage is limited by the V supply.<br>IO<br>3. The offset is determined using curve fitting since the specification is measured using linear search where the intercept is always<br>positive.<br>4. Production test uses a 2.4 V external reference and external ground.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 28

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.10 Voltage Reference**

**Table 4.10. Voltage Reference**


















|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Internal Fast Settling Reference|Internal Fast Settling Reference|Internal Fast Settling Reference|Internal Fast Settling Reference|Internal Fast Settling Reference|Internal Fast Settling Reference|Internal Fast Settling Reference|
|Output Voltage<br>(Full Temperature and Supply<br>Range)|V<br>REFFS||1.62|1.65|1.68|V|
|Temperature Coefficient|TC<br>REFFS||—|50|—|ppm/°C|
|Turn-on Time|t<br>REFFS||—|—|1.5|μs|
|Power Supply Rejection|PSRR<br>REF<br>FS||—|400|—|ppm/V|
|On-chip Precision Reference|On-chip Precision Reference|On-chip Precision Reference|On-chip Precision Reference|On-chip Precision Reference|On-chip Precision Reference|On-chip Precision Reference|
|Valid Supply Range|V<br>DD|1.2 V Output|2.2|—|3.6|V|
|Valid Supply Range|V<br>DD|2.4 V Output|2.7|—|3.6|V|
|Output Voltage|V<br>REFP|1.2 V Output, V = 3.3 V, T = 25<br>DD<br>°C|1.195|1.2|1.205|V|
|Output Voltage|V<br>REFP|1.2 V Output|1.18|1.2|1.22|V|
|Output Voltage|V<br>REFP|2.4 V Output, V = 3.3 V, T = 25<br>DD<br>°C|2.39|2.4|2.41|V|
|Output Voltage|V<br>REFP|2.4 V Output|2.36|2.4|2.44|V|
|Turn-on Time, settling to 0.5 LSB|t<br>VREFP|4.7 µF tantalum + 0.1 µF ceramic<br>bypass on VREF pin|—|3|—|ms|
|Turn-on Time, settling to 0.5 LSB|t<br>VREFP|0.1 µF ceramic bypass on VREF<br>pin|—|100|—|µs|
|Load Regulation|LR<br>VREFP|VREF = 2.4 V, Load = 0 to 200 µA<br>to GND|—|8|—|µV/µA|
|Load Regulation|LR<br>VREFP|VREF = 1.2 V, Load = 0 to 200 µA<br>to GND|—|5|—|µV/µA|
|Load Capacitor|C<br>VREFP|Load = 0 to 200 µA to GND|0.1|—|—|µF|
|Short-circuit current|ISC<br>VREFP||—|—|8|mA|
|Power Supply Rejection|PSRR<br>VRE<br>FP||—|75|—|dB|
|External Reference|External Reference|External Reference|External Reference|External Reference|External Reference|External Reference|
|Input Current|I<br>EXTREF|ADC Sample Rate = 800 ksps;<br>VREF = 3.0 V|—|5|—|μA|


**silabs.com** | Building a more connected world. Rev. 1.5 | 29

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.11 Temperature Sensor**

**Table 4.11. Temperature Sensor**




|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Offset|V<br>OFF|T = 0 °C<br>A|—|751|—|mV|
|Offset Error1|E<br>OFF|T = 0 °C<br>A|—|19|—|mV|
|Slope|M||—|2.82|—|mV/°C|
|Slope Error1|E<br>M||—|29|—|μV/°C|
|Linearity|LIN|T = -40 °C to 85 °C|—|±0.4|—|°C|
|Linearity|LIN|T = -40 °C to 125 °C (I-grade or A-<br>grade parts only)|—|-0.6 to 1.2|—|°C|
|Turn-on Time|t<br>ON||—|3.5|—|μs|
|Note:<br>1. Represents one standard deviation from the mean.|Note:<br>1. Represents one standard deviation from the mean.|Note:<br>1. Represents one standard deviation from the mean.|Note:<br>1. Represents one standard deviation from the mean.|Note:<br>1. Represents one standard deviation from the mean.|Note:<br>1. Represents one standard deviation from the mean.|Note:<br>1. Represents one standard deviation from the mean.|


**4.1.12 1.8 V Internal LDO Voltage Regulator**

**Table 4.12. 1.8V Internal LDO Voltage Regulator**

|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Output Voltage|V<br>OUT_1.8V||1.79|1.84|1.88|V|



**silabs.com** | Building a more connected world. Rev. 1.5 | 30

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.13 DACs**

**Table 4.13. DACs**















|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Output Voltage|V<br>OUT||0|—|V<br>DD|V|
|Output Current|I<br>OUT||-2|—|2|mA|
|Resolution|N<br>bits||12|12|12|Bits|
|Throughput Rate|f<br>S||—|—|200|ksps|
|Integral Nonlinearity|INL|DAC0 and DAC2<br>T = -40 °C to 125 °C (I-grade or<br>A<br>A-grade parts only)|-11.5|-1.77 /<br>1.56|11.5|LSB|
|Integral Nonlinearity|INL|DAC1 and DAC3<br>T = -40 °C to 125 °C (I-grade or<br>A<br>A-grade parts only)|-13.5|-2.73 /<br>1.11|13.5|LSB|
|Differential Nonlinearity|DNL||-1|—|1|LSB|
|Output Noise|V<br>NOISE|VREF = 2.4 V<br>f = 0.1 Hz to 300 kHz<br>S|—|110|—|μV<br>RMS|
|Slew Rate|SLEW||—|±1|—|V/μs|
|Output Settling Time to 1% Full-<br>scale|t<br>SETTLE|V change between 25% and<br>OUT<br>75% Full Scale|—|2.6|5|μs|
|Power-on Time|t<br>PWR||—|—|10|μs|
|Voltage Reference Range|V<br>REF||1.15|—|V<br>DD|V|
|Power Supply Rejection Ratio|PSRR|DC, V = 50% Full Scale<br>OUT|—|78|—|dB|
|Total Harmonic Distortion|THD|V = 10 kHz sine wave, 10% to<br>OUT<br>90%|54|—|—|dB|
|Offset Error|E<br>OFF|VREF = 2.4 V|-8|0|8|LSB|
|Full-Scale Error|E<br>FS|VREF = 2.4 V|-13|±5|13|LSB|
|External Load Impedance|R<br>LOAD||2|—|—|kΩ|
|External Load Capacitance1|C<br>LOAD||—|—|100|pF|
|Note:<br>1. No minimum external load capacitance is required. However, under low loading conditions, it is possible for the DAC output to<br>glitch during start-up. If smooth start-up is required, the minimum loading capacitance at the pin should be a minimum of 10 pF.|Note:<br>1. No minimum external load capacitance is required. However, under low loading conditions, it is possible for the DAC output to<br>glitch during start-up. If smooth start-up is required, the minimum loading capacitance at the pin should be a minimum of 10 pF.|Note:<br>1. No minimum external load capacitance is required. However, under low loading conditions, it is possible for the DAC output to<br>glitch during start-up. If smooth start-up is required, the minimum loading capacitance at the pin should be a minimum of 10 pF.|Note:<br>1. No minimum external load capacitance is required. However, under low loading conditions, it is possible for the DAC output to<br>glitch during start-up. If smooth start-up is required, the minimum loading capacitance at the pin should be a minimum of 10 pF.|Note:<br>1. No minimum external load capacitance is required. However, under low loading conditions, it is possible for the DAC output to<br>glitch during start-up. If smooth start-up is required, the minimum loading capacitance at the pin should be a minimum of 10 pF.|Note:<br>1. No minimum external load capacitance is required. However, under low loading conditions, it is possible for the DAC output to<br>glitch during start-up. If smooth start-up is required, the minimum loading capacitance at the pin should be a minimum of 10 pF.|Note:<br>1. No minimum external load capacitance is required. However, under low loading conditions, it is possible for the DAC output to<br>glitch during start-up. If smooth start-up is required, the minimum loading capacitance at the pin should be a minimum of 10 pF.|


**silabs.com** | Building a more connected world. Rev. 1.5 | 31

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.14 Comparators**

**Table 4.14. Comparators**



|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Response Time, CPMD = 00<br>(Highest Speed)|t<br>RESP0|+100 mV Differential|—|100|—|ns|
|Response Time, CPMD = 00<br>(Highest Speed)|t<br>RESP0|-100 mV Differential|—|150|—|ns|
|Response Time, CPMD = 11 (Low-<br>est Power)|t<br>RESP3|+100 mV Differential|—|1.5|—|μs|
|Response Time, CPMD = 11 (Low-<br>est Power)|t<br>RESP3|-100 mV Differential|—|3.5|—|μs|
|Positive Hysteresis<br>Mode 0 (CPMD = 00)|HYS<br>CP+|CPHYP = 00|—|0.4|—|mV|
|Positive Hysteresis<br>Mode 0 (CPMD = 00)|HYS<br>CP+|CPHYP = 01|—|8|—|mV|
|Positive Hysteresis<br>Mode 0 (CPMD = 00)|HYS<br>CP+|CPHYP = 10|—|16|—|mV|
|Positive Hysteresis<br>Mode 0 (CPMD = 00)|HYS<br>CP+|CPHYP = 11|—|32|—|mV|
|Negative Hysteresis<br>Mode 0 (CPMD = 00)|HYS<br>CP-|CPHYN = 00|—|-0.4|—|mV|
|Negative Hysteresis<br>Mode 0 (CPMD = 00)|HYS<br>CP-|CPHYN = 01|—|-8|—|mV|
|Negative Hysteresis<br>Mode 0 (CPMD = 00)|HYS<br>CP-|CPHYN = 10|—|-16|—|mV|
|Negative Hysteresis<br>Mode 0 (CPMD = 00)|HYS<br>CP-|CPHYN = 11|—|-32|—|mV|
|Positive Hysteresis<br>Mode 1 (CPMD = 01)|HYS<br>CP+|CPHYP = 00|—|0.5|—|mV|
|Positive Hysteresis<br>Mode 1 (CPMD = 01)|HYS<br>CP+|CPHYP = 01|—|6|—|mV|
|Positive Hysteresis<br>Mode 1 (CPMD = 01)|HYS<br>CP+|CPHYP = 10|—|12|—|mV|
|Positive Hysteresis<br>Mode 1 (CPMD = 01)|HYS<br>CP+|CPHYP = 11|—|24|—|mV|
|Negative Hysteresis<br>Mode 1 (CPMD = 01)|HYS<br>CP-|CPHYN = 00|—|-0.5|—|mV|
|Negative Hysteresis<br>Mode 1 (CPMD = 01)|HYS<br>CP-|CPHYN = 01|—|-6|—|mV|
|Negative Hysteresis<br>Mode 1 (CPMD = 01)|HYS<br>CP-|CPHYN = 10|—|-12|—|mV|
|Negative Hysteresis<br>Mode 1 (CPMD = 01)|HYS<br>CP-|CPHYN = 11|—|-24|—|mV|
|Positive Hysteresis<br>Mode 2 (CPMD = 10)|HYS<br>CP+|CPHYP = 00|—|0.7|—|mV|
|Positive Hysteresis<br>Mode 2 (CPMD = 10)|HYS<br>CP+|CPHYP = 01|—|4.5|—|mV|
|Positive Hysteresis<br>Mode 2 (CPMD = 10)|HYS<br>CP+|CPHYP = 10|—|9|—|mV|
|Positive Hysteresis<br>Mode 2 (CPMD = 10)|HYS<br>CP+|CPHYP = 11|—|18|—|mV|
|Negative Hysteresis<br>Mode 2 (CPMD = 10)|HYS<br>CP-|CPHYN = 00|—|-0.6|—|mV|
|Negative Hysteresis<br>Mode 2 (CPMD = 10)|HYS<br>CP-|CPHYN = 01|—|-4.5|—|mV|
|Negative Hysteresis<br>Mode 2 (CPMD = 10)|HYS<br>CP-|CPHYN = 10|—|-9|—|mV|
|Negative Hysteresis<br>Mode 2 (CPMD = 10)|HYS<br>CP-|CPHYN = 11|—|-18|—|mV|
|Positive Hysteresis<br>Mode 3 (CPMD = 11)|HYS<br>CP+|CPHYP = 00|—|1.5|—|mV|
|Positive Hysteresis<br>Mode 3 (CPMD = 11)|HYS<br>CP+|CPHYP = 01|—|4|—|mV|
|Positive Hysteresis<br>Mode 3 (CPMD = 11)|HYS<br>CP+|CPHYP = 10|—|8|—|mV|
|Positive Hysteresis<br>Mode 3 (CPMD = 11)|HYS<br>CP+|CPHYP = 11|—|16|—|mV|


**silabs.com** | Building a more connected world. Rev. 1.5 | 32

EFM8BB3 Data Sheet
Electrical Specifications




|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Negative Hysteresis<br>Mode 3 (CPMD = 11)|HYS<br>CP-|CPHYN = 00|—|-1.5|—|mV|
|Negative Hysteresis<br>Mode 3 (CPMD = 11)|HYS<br>CP-|CPHYN = 01|—|-4|—|mV|
|Negative Hysteresis<br>Mode 3 (CPMD = 11)|HYS<br>CP-|CPHYN = 10|—|-8|—|mV|
|Negative Hysteresis<br>Mode 3 (CPMD = 11)|HYS<br>CP-|CPHYN = 11|—|-16|—|mV|
|Input Range (CP+ or CP-)|V<br>IN||-0.25|—|V +0.25<br>IO|V|
|Input Pin Capacitance|C<br>CP||—|7.5|—|pF|
|Internal Reference DAC Resolution|N<br>bits||6|6|6|bits|
|Common-Mode Rejection Ratio|CMRR<br>CP||—|70|—|dB|
|Power Supply Rejection Ratio|PSRR<br>CP||—|72|—|dB|
|Input Offset Voltage|V<br>OFF|T = 25 °C<br>A|-10|0|10|mV|
|Input Offset Tempco|TC<br>OFF||—|3.5|—|μV/°|


**4.1.15 Configurable Logic**

**Table 4.15. Configurable Logic**




|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Propagation Delay|t<br>DLY|Through single CLU<br>Using an external pin|—|—|35.3|ns|
|Propagation Delay|t<br>DLY|Through single CLU<br>Using an internal connection|—|3|—|ns|
|Clocking Frequency|F<br>CLK|1 or 2 CLUs Cascaded|—|—|73.5|MHz|
|Clocking Frequency|F<br>CLK|3 or 4 CLUs Cascaded|—|—|36.75|MHz|


**silabs.com** | Building a more connected world. Rev. 1.5 | 33

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.16 Port I/O**

**Table 4.16. Port I/O**





















|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Output High Voltage (High Drive)|V<br>OH|I = -7 mA, V ≥ 3.0 V<br>OH IO|V - 0.7<br>IO|—|—|V|
|Output High Voltage (High Drive)|V<br>OH|I = -3.3 mA, 2.2 V ≤ V < 3.0 V<br>OH IO<br>I = -1.8 mA, 1.71 V ≤ V < 2.2 V<br>OH IO|V x 0.8<br>IO|—|—|V|
|Output Low Voltage (High Drive)|V<br>OL|I = 13.5 mA, V ≥ 3.0 V<br>OL IO|—|—|0.6|V|
|Output Low Voltage (High Drive)|V<br>OL|I = 7 mA, 2.2 V ≤ V < 3.0 V<br>OL IO<br>I = 3.6 mA, 1.71 V ≤ V < 2.2 V<br>OL IO|—|—|V x 0.2<br>IO|V|
|Output High Voltage (Low Drive)|V<br>OH|I = -4.75 mA, V ≥ 3.0 V<br>OH IO|V - 0.7<br>IO|—|—|V|
|Output High Voltage (Low Drive)|V<br>OH|I = -2.25 mA, 2.2 V ≤ V < 3.0 V<br>OH IO<br>I = -1.2 mA, 1.71 V ≤ V < 2.2 V<br>OH IO|V x 0.8<br>IO|—|—|V|
|Output Low Voltage (Low Drive)|V<br>OL|I = 6.5 mA, V ≥ 3.0 V<br>OL IO|—|—|0.6|V|
|Output Low Voltage (Low Drive)|V<br>OL|I = 3.5 mA, 2.2 V ≤ V < 3.0 V<br>OL IO<br>I = 1.8 mA, 1.71 V ≤ V < 2.2 V<br>OL IO|—|—|V x 0.2<br>IO|V|
|Input High Voltage|V<br>IH||0.7 x<br>V<br>IO|—|—|V|
|Input Low Voltage|V<br>IL||—|—|0.3 x<br>V<br>IO|V|
|Pin Capacitance|C<br>IO||—|7|—|pF|
|Weak Pull-Up Current<br>(V = 0 V)<br>IN|I<br>PU|V = 3.6<br>DD|-30|-20|-10|μA|
|Input Leakage (Pullups off or Ana-<br>log)|I<br>LK|GND < V < V<br>IN IO<br>(G-grade and I-grade devices)|-1.1|—|4|μA|
|Input Leakage (Pullups off or Ana-<br>log)|I<br>LK|GND < V < V<br>IN IO<br>(A-grade devices only)|-1.1|—|1.1|μA|
|Input Leakage Current with V<br>IN<br>above V<br>IO|I<br>LK|V < V < V +2.5 V<br>IO IN IO<br>Any pin except P3.0, P3.1, P3.2, or<br>P3.3|0|5|150|μA|


**silabs.com** | Building a more connected world. Rev. 1.5 | 34

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.17 SMBus**

**Table 4.17. SMBus Peripheral Timing Performance (Master Mode)**







|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Standard Mode (100 kHz Class)|Standard Mode (100 kHz Class)|Standard Mode (100 kHz Class)|Standard Mode (100 kHz Class)|Standard Mode (100 kHz Class)|Standard Mode (100 kHz Class)|Standard Mode (100 kHz Class)|
|I2C Operating Frequency|f<br>I2C||0|—|702|kHz|
|SMBus Operating Frequency|f<br>SMB||401|—|702|kHz|
|Bus Free Time Between STOP and<br>START Conditions|t<br>BUF||9.4|—|—|µs|
|Hold Time After (Repeated)<br>START Condition|t<br>HD:STA||4.7|—|—|µs|
|Repeated START Condition Setup<br>Time|t<br>SU:STA||9.4|—|—|µs|
|STOP Condition Setup Time|t<br>SU:STO||9.4|—|—|µs|
|Data Hold Time|t<br>HD:DAT||2753|—|—|ns|
|Data Setup Time|t<br>SU:DAT||3003|—|—|ns|
|Detect Clock Low Timeout|t<br>TIMEOUT||25|—|—|ms|
|Clock Low Period|t<br>LOW||4.7|—|—|µs|
|Clock High Period|t<br>HIGH||9.4|—|504|µs|
|Fast Mode (400 kHz Class)|Fast Mode (400 kHz Class)|Fast Mode (400 kHz Class)|Fast Mode (400 kHz Class)|Fast Mode (400 kHz Class)|Fast Mode (400 kHz Class)|Fast Mode (400 kHz Class)|
|I2C Operating Frequency|f<br>I2C||0|—|2562|kHz|
|SMBus Operating Frequency|f<br>SMB||401|—|2562|kHz|
|Bus Free Time Between STOP and<br>START Conditions|t<br>BUF||2.6|—|—|µs|
|Hold Time After (Repeated)<br>START Condition|t<br>HD:STA||1.3|—|—|µs|
|Repeated START Condition Setup<br>Time|t<br>SU:STA||2.6|—|—|µs|
|STOP Condition Setup Time|t<br>SU:STO||2.6|—|—|µs|
|Data Hold Time|t<br>HD:DAT||2753|—|—|ns|
|Data Setup Time|t<br>SU:DAT||3003|—|—|ns|
|Detect Clock Low Timeout|t<br>TIMEOUT||25|—|—|ms|
|Clock Low Period|t<br>LOW||1.3|—|—|µs|
|Clock High Period|t<br>HIGH||2.6|—|504|µs|


**silabs.com** | Building a more connected world. Rev. 1.5 | 35

EFM8BB3 Data Sheet
Electrical Specifications

|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|



**Table 4.18. SMBus Peripheral Timing Formulas (Master Mode)**

|Parameter|Symbol|Clocks|
|---|---|---|
|SMBus Operating Frequency|f<br>SMB|f / 3<br>CSO|
|Bus Free Time Between STOP and START Conditions|t<br>BUF|2 / f<br>CSO|
|Hold Time After (Repeated) START Condition|t<br>HD:STA|1 / f<br>CSO|
|Repeated START Condition Setup Time|t<br>SU:STA|2 / f<br>CSO|
|STOP Condition Setup Time|t<br>SU:STO|2 / f<br>CSO|
|Clock Low Period|t<br>LOW|1 / f<br>CSO|
|Clock High Period|t<br>HIGH|2 / f<br>CSO|
|Note:<br>1. f is the SMBus peripheral clock source overflow frequency.<br>CSO|Note:<br>1. f is the SMBus peripheral clock source overflow frequency.<br>CSO|Note:<br>1. f is the SMBus peripheral clock source overflow frequency.<br>CSO|



V IH

SCL

V IL




SDA


V IH

V IL


|Col1|Col2|Col3|Col4|Col5|tLOW|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT||||||||||
|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT||||||||||||||
|||||||||||||||
||tBUF|||||||||||||


P S S P

**Figure 4.1. SMBus Peripheral Timing Diagram (Master Mode)**

**silabs.com** | Building a more connected world. Rev. 1.5 | 36

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.18 SPI**

**Table 4.19. SPI Timing Parameters**

|Parameter|Description|Min|Max|Units|
|---|---|---|---|---|
|Master Mode Timing|Master Mode Timing|Master Mode Timing|Master Mode Timing|Master Mode Timing|
|T<br>MCKH|SCK High Time|1 x T<br>SYSCLK|—|ns|
|T<br>MCKL|SCK Low Time|1 x T<br>SYSCLK|—|ns|
|T<br>MIS|MISO Valid to SCK Sample Edge|20|—|ns|
|T<br>MIH|SCK Sample Edge to MISO Change|5|—|ns|
|Slave Mode Timing|Slave Mode Timing|Slave Mode Timing|Slave Mode Timing|Slave Mode Timing|
|T<br>SE|NSS Falling to First SCK Edge|5|—|ns|
|T<br>SD|Last SCK Edge to NSS Rising|5|—|ns|
|T<br>SEZ|NSS Falling to MISO Valid|—|20|ns|
|T<br>SDZ|NSS Rising to MISO High-Z|—|20|ns|
|T<br>CKH|SCK High Time|40|—|ns|
|T<br>CKL|SCK Low Time|40|—|ns|
|T<br>SIS|MOSI Valid to SCK Sample Edge|20|—|ns|
|T<br>SIH|SCK Sample Edge to MOSI Change|5|—|ns|
|T<br>SOH|SCK Shift Edge to MISO Change|—|20|ns|
|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|



SCK*




MISO

MOSI

      - SCK is shown for CKPOL = 0. SCK is the opposite polarity for CKPOL = 1.

**Figure 4.2. SPI Master Timing (CKPHA = 0)**

**silabs.com** | Building a more connected world. Rev. 1.5 | 37

EFM8BB3 Data Sheet
Electrical Specifications


SCK*

MISO

MOSI






- SCK is shown for CKPOL = 0. SCK is the opposite polarity for CKPOL = 1.

**Figure 4.3. SPI Master Timing (CKPHA = 1)**

NSS





SCK*

MOSI

MISO







      - SCK is shown for CKPOL = 0. SCK is the opposite polarity for CKPOL = 1.

**Figure 4.4. SPI Slave Timing (CKPHA = 0)**

**silabs.com** | Building a more connected world. Rev. 1.5 | 38

EFM8BB3 Data Sheet
Electrical Specifications












      - SCK is shown for CKPOL = 0. SCK is the opposite polarity for CKPOL = 1.

**Figure 4.5. SPI Slave Timing (CKPHA = 1)**

**4.2 Thermal Conditions**

**Table 4.20. Thermal Conditions**

|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Thermal Resistance|θ<br>JA|QFN24-GI Packages|—|30|—|°C/W|
|Thermal Resistance|θ<br>JA|QFN24-AI Packages|—|TBD|—|°C/W|
|Thermal Resistance|θ<br>JA|QFN32-GI Packages|—|26|—|°C/W|
|Thermal Resistance|θ<br>JA|QFN32-AI Packages|—|TBD|—|°C/W|
|Thermal Resistance|θ<br>JA|QFP32 Packages|—|80|—|°C/W|
|Thermal Resistance|θ<br>JA|QSOP24 Packages|—|65|—|°C/W|
|Note:<br>1. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad.|Note:<br>1. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad.|Note:<br>1. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad.|Note:<br>1. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad.|Note:<br>1. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad.|Note:<br>1. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad.|Note:<br>1. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 39

EFM8BB3 Data Sheet
Electrical Specifications

**4.3 Absolute Maximum Ratings**

Stresses above those listed in Table 4.21 Absolute Maximum Ratings on page 40 may cause permanent damage to the device. This
is a stress rating only and functional operation of the devices at those or any other conditions above those indicated in the operation
listings of this specification is not implied. Exposure to maximum rating conditions for extended periods may affect device reliability. For
more information on the available quality and reliability data, see the Quality and Reliability Monitor Report at [http://www.silabs.com/](http://www.silabs.com/support/quality/pages/default.aspx)
[support/quality/pages/default.aspx.](http://www.silabs.com/support/quality/pages/default.aspx)

**Table 4.21. Absolute Maximum Ratings**









|Parameter|Symbol|Test Condition|Min|Max|Unit|
|---|---|---|---|---|---|
|Ambient Temperature Under Bias|T<br>BIAS||-55|125|°C|
|Storage Temperature|T<br>STG||-65|150|°C|
|Voltage on VDD|V<br>DD||GND-0.3|4.2|V|
|Voltage on VIO2|V<br>IO||GND-0.3|V +0.3<br>DD|V|
|Voltage on I/O pins or RSTb, excluding<br>P2.0-P2.3 (QFN24 and QSOP24) or<br>P3.0-P3.3 (QFN32 and QFP32)|V<br>IN|V > 3.3 V<br>IO|GND-0.3|5.8|V|
|Voltage on I/O pins or RSTb, excluding<br>P2.0-P2.3 (QFN24 and QSOP24) or<br>P3.0-P3.3 (QFN32 and QFP32)|V<br>IN|V < 3.3 V<br>IO|GND-0.3|V +2.5<br>IO|V|
|Voltage on P2.0-P2.3 (QFN24 and<br>QSOP24) or P3.0-P3.3 (QFN32 and<br>QFP32)|V<br>IN||GND-0.3|V +0.3<br>DD|V|
|Total Current Sunk into Supply Pin|I<br>VDD||—|200|mA|
|Total Current Sourced out of Ground<br>Pin|I<br>GND||200|—|mA|
|Current Sourced or Sunk by any I/O<br>Pin or RSTb|I<br>IO||-100|100|mA|
|Operating Junction Temperature|T<br>J|T = -40 °C to 85 °C<br>A|–40|105|°C|
|Operating Junction Temperature|T<br>J|T = -40 °C to 125 °C (I-grade or A-<br>A<br>grade parts only)|-40|130|°C|
|Note:<br>1. Exposure to maximum rating conditions for extended periods may affect device reliability.<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.|Note:<br>1. Exposure to maximum rating conditions for extended periods may affect device reliability.<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.|Note:<br>1. Exposure to maximum rating conditions for extended periods may affect device reliability.<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.|Note:<br>1. Exposure to maximum rating conditions for extended periods may affect device reliability.<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.|Note:<br>1. Exposure to maximum rating conditions for extended periods may affect device reliability.<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.|Note:<br>1. Exposure to maximum rating conditions for extended periods may affect device reliability.<br>2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.|


**silabs.com** | Building a more connected world. Rev. 1.5 | 40

EFM8BB3 Data Sheet
Typical Connection Diagrams

**5. Typical Connection Diagrams**

**5.1 Power**

Figure 5.1 Power Connection Diagram on page 41 shows a typical connection diagram for the power pins of the device.






4.7 µF and 0.1 µF bypass
capacitors required for
each power pin placed as
close to the pins as
possible.


**Figure 5.1. Power Connection Diagram**

**silabs.com** | Building a more connected world. Rev. 1.5 | 41

EFM8BB3 Data Sheet
Typical Connection Diagrams

**5.2 Debug**

The diagram below shows a typical connection diagram for the debug connections pins. The pin sharing resistors are only required if
the functionality on the C2D (a GPIO pin) and the C2CK (RSTb) is routed to external circuitry. For example, if the RSTb pin is connected to an external switch with debouncing filter or if the GPIO sharing with the C2D pin is connected to an external circuit, the pin sharing resistors and connections to the debug adapter must be placed on the hardware. Otherwise, these components and connections
can be omitted.

For more information on debug connections, see the example schematics and information available in *AN124: Pin Sharing Techniques*
*for the C2 Interface* [. Application notes can be found on the Silicon Labs website (http://www.silabs.com/8bit-appnotes) or in Simplicity](http://www.silabs.com/8bit-appnotes)
Studio.

VDD







**Figure 5.2. Debug Connection Diagram**

**5.3 Other Connections**

Other components or connections may be required to meet the system-level requirements. Application Note AN203: "8-bit MCU Printed
Circuit Board Design Notes" contains detailed information on these connections. Application Notes can be accessed on the Silicon
[Labs website (www.silabs.com/8bit-appnotes).](http://www.silabs.com/8bit-appnotes)

**silabs.com** | Building a more connected world. Rev. 1.5 | 42

EFM8BB3 Data Sheet

Pin Definitions


**6. Pin Definitions**

**6.1 EFM8BB3x-QFN32 and EFM8BB3x-5QFN32 Pin Definitions**


P1.1

P1.2


P1.6

P1.7

P2.0


P0.0

VIO

VDD

RSTb / C2CK

P3.7 / C2D

P3.4

P3.3

P3.2





P1.3

P1.4

P1.5





**Figure 6.1. EFM8BB3x-QFN32 (QFN32-GI) and EFM8BB3x-5QFN32 (QFN32-AI) Pinout**

**silabs.com** | Building a more connected world. Rev. 1.5 | 43

EFM8BB3 Data Sheet

Pin Definitions

**Table 6.1. Pin Definitions for EFM8BB3x-QFN32 (QFN32-GI) and EFM8BB3x-5QFN32 (QFN32-AI)**










|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|1|P0.0|Multifunction I/O|Yes|P0MAT.0<br>INT0.0<br>INT1.0<br>CLU0A.8<br>CLU2A.8<br>CLU3B.8|VREF|
|2|VIO|I/O Supply Power Input||||
|3|VDD|Supply Power Input||||
|4|RSTb /<br>C2CK|Active-low Reset /<br>C2 Debug Clock||||
|5|P3.7 /<br>C2D|Multifunction I/O /<br>C2 Debug Data||||
|6|P3.4|Multifunction I/O||||
|7|P3.3|Multifunction I/O|||DAC3|
|8|P3.2|Multifunction I/O|||DAC2|
|9|P3.1|Multifunction I/O|||DAC1|
|10|P3.0|Multifunction I/O|||DAC0|
|11|P2.6|Multifunction I/O|||ADC0.19<br>CMP1P.8<br>CMP1N.8|
|12|P2.5|Multifunction I/O||CLU3OUT|ADC0.18<br>CMP1P.7<br>CMP1N.7|
|13|P2.4|Multifunction I/O|||ADC0.17<br>CMP1P.6<br>CMP1N.6|
|14|P2.3|Multifunction I/O|Yes|P2MAT.3<br>CLU1B.15<br>CLU2B.15<br>CLU3A.15|ADC0.16<br>CMP1P.5<br>CMP1N.5|


**silabs.com** | Building a more connected world. Rev. 1.5 | 44

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|15|P2.2|Multifunction I/O|Yes|P2MAT.2<br>CLU2OUT<br>CLU1A.15<br>CLU2B.14<br>CLU3A.14|ADC0.15<br>CMP1P.4<br>CMP1N.4|
|16|P2.1|Multifunction I/O|Yes|P2MAT.1<br>I2C0_SCL<br>CLU1B.14<br>CLU2A.15<br>CLU3B.15|ADC0.14<br>CMP1P.3<br>CMP1N.3|
|17|P2.0|Multifunction I/O|Yes|P2MAT.0<br>I2C0_SDA<br>CLU1A.14<br>CLU2A.14<br>CLU3B.14|CMP1P.2<br>CMP1N.2|
|18|P1.7|Multifunction I/O|Yes|P1MAT.7<br>CLU0B.15<br>CLU1B.13<br>CLU2A.13|ADC0.13<br>CMP0P.9<br>CMP0N.9|
|19|P1.6|Multifunction I/O|Yes|P1MAT.6<br>CLU0A.15<br>CLU1B.12<br>CLU2A.12|ADC0.12|
|20|P1.5|Multifunction I/O|Yes|P1MAT.5<br>CLU0B.14<br>CLU1A.13<br>CLU2B.13|ADC0.11|
|21|P1.4|Multifunction I/O|Yes|P1MAT.4<br>CLU0A.14<br>CLU1A.12<br>CLU2B.12|ADC0.10|
|22|P1.3|Multifunction I/O|Yes|P1MAT.3<br>CLU0B.13<br>CLU1B.11<br>CLU2B.11<br>CLU3A.13|ADC0.9|


**silabs.com** | Building a more connected world. Rev. 1.5 | 45

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|23|P1.2|Multifunction I/O|Yes|P1MAT.2<br>CLU0A.13<br>CLU1A.11<br>CLU2B.10<br>CLU3A.12|ADC0.8<br>CMP0P.8<br>CMP0N.8|
|24|P1.1|Multifunction I/O|Yes|P1MAT.1<br>CLU0B.12<br>CLU1B.10<br>CLU2A.11<br>CLU3B.13|ADC0.7<br>CMP0P.7<br>CMP0N.7|
|25|P1.0|Multifunction I/O|Yes|P1MAT.0<br>CLU1OUT<br>CLU0A.12<br>CLU1A.10<br>CLU2A.10<br>CLU3B.12|ADC0.6<br>CMP0P.6<br>CMP0N.6<br>CMP1P.1<br>CMP1N.1|
|26|P0.7|Multifunction I/O|Yes|P0MAT.7<br>INT0.7<br>INT1.7<br>CLU0B.11<br>CLU1B.9<br>CLU3A.11|ADC0.5<br>CMP0P.5<br>CMP0N.5<br>CMP1P.0<br>CMP1N.0|
|27|P0.6|Multifunction I/O|Yes|P0MAT.6<br>CNVSTR<br>INT0.6<br>INT1.6<br>CLU0A.11<br>CLU1B.8<br>CLU3A.10|ADC0.4<br>CMP0P.4<br>CMP0N.4|


**silabs.com** | Building a more connected world. Rev. 1.5 | 46

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|28|P0.5|Multifunction I/O|Yes|P0MAT.5<br>INT0.5<br>INT1.5<br>UART0_RX<br>CLU0B.10<br>CLU1A.9<br>CLU3B.11|ADC0.3<br>CMP0P.3<br>CMP0N.3|
|29|P0.4|Multifunction I/O|Yes|P0MAT.4<br>INT0.4<br>INT1.4<br>UART0_TX<br>CLU0A.10<br>CLU1A.8<br>CLU3B.10|ADC0.2<br>CMP0P.2<br>CMP0N.2|
|30|P0.3|Multifunction I/O|Yes|P0MAT.3<br>EXTCLK<br>INT0.3<br>INT1.3<br>CLU0B.9<br>CLU2B.9<br>CLU3A.9|EXTOSC|
|31|P0.2|Multifunction I/O|Yes|P0MAT.2<br>INT0.2<br>INT1.2<br>CLU0OUT<br>CLU0A.9<br>CLU2B.8<br>CLU3A.8|ADC0.1<br>CMP0P.1<br>CMP0N.1|
|32|P0.1|Multifunction I/O|Yes|P0MAT.1<br>INT0.1<br>INT1.1<br>CLU0B.8<br>CLU2A.9<br>CLU3B.9|ADC0.0<br>CMP0P.0<br>CMP0N.0<br>AGND|
|Center|GND|Ground||||


**silabs.com** | Building a more connected world. Rev. 1.5 | 47

**6.2 EFM8BB3x-QFP32 Pin Definitions**

P0.0

GND

VIO

VDD

RSTb / C2CK

P3.7 / C2D

P3.3

P3.2



















EFM8BB3 Data Sheet

Pin Definitions

P1.1

P1.2

P1.3

P1.4

P1.5

P1.6

P1.7

P2.0



**Figure 6.2.  EFM8BB3x-QFP32 Pinout**

**Table 6.2. Pin Definitions for EFM8BB3x-QFP32**




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|1|P0.0|Multifunction I/O|Yes|P0MAT.0<br>INT0.0<br>INT1.0<br>CLU0A.8<br>CLU2A.8<br>CLU3B.8|VREF|
|2|GND|Ground||||
|3|VIO|I/O Supply Power Input||||
|4|VDD|Supply Power Input||||
|5|RSTb /<br>C2CK|Active-low Reset /<br>C2 Debug Clock||||


**silabs.com** | Building a more connected world. Rev. 1.5 | 48

EFM8BB3 Data Sheet

Pin Definitions








|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|6|P3.7 /<br>C2D|Multifunction I/O /<br>C2 Debug Data||||
|7|P3.3|Multifunction I/O|||DAC3|
|8|P3.2|Multifunction I/O|||DAC2|
|9|P3.1|Multifunction I/O|||DAC1|
|10|P3.0|Multifunction I/O|||DAC0|
|11|P2.6|Multifunction I/O|||ADC0.19<br>CMP1P.8<br>CMP1N.8|
|12|P2.5|Multifunction I/O||CLU3OUT|ADC0.18<br>CMP1P.7<br>CMP1N.7|
|13|P2.4|Multifunction I/O|||ADC0.17<br>CMP1P.6<br>CMP1N.6|
|14|P2.3|Multifunction I/O|Yes|P2MAT.3<br>CLU1B.15<br>CLU2B.15<br>CLU3A.15|ADC0.16<br>CMP1P.5<br>CMP1N.5|
|15|P2.2|Multifunction I/O|Yes|P2MAT.2<br>CLU2OUT<br>CLU1A.15<br>CLU2B.14<br>CLU3A.14|ADC0.15<br>CMP1P.4<br>CMP1N.4|
|16|P2.1|Multifunction I/O|Yes|P2MAT.1<br>I2C0_SCL<br>CLU1B.14<br>CLU2A.15<br>CLU3B.15|ADC0.14<br>CMP1P.3<br>CMP1N.3|
|17|P2.0|Multifunction I/O|Yes|P2MAT.0<br>I2C0_SDA<br>CLU1A.14<br>CLU2A.14<br>CLU3B.14|CMP1P.2<br>CMP1N.2|


**silabs.com** | Building a more connected world. Rev. 1.5 | 49

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|18|P1.7|Multifunction I/O|Yes|P1MAT.7<br>CLU0B.15<br>CLU1B.13<br>CLU2A.13|ADC0.13<br>CMP0P.9<br>CMP0N.9|
|19|P1.6|Multifunction I/O|Yes|P1MAT.6<br>CLU0A.15<br>CLU1B.12<br>CLU2A.12|ADC0.12|
|20|P1.5|Multifunction I/O|Yes|P1MAT.5<br>CLU0B.14<br>CLU1A.13<br>CLU2B.13|ADC0.11|
|21|P1.4|Multifunction I/O|Yes|P1MAT.4<br>CLU0A.14<br>CLU1A.12<br>CLU2B.12|ADC0.10|
|22|P1.3|Multifunction I/O|Yes|P1MAT.3<br>CLU0B.13<br>CLU1B.11<br>CLU2B.11<br>CLU3A.13|ADC0.9|
|23|P1.2|Multifunction I/O|Yes|P1MAT.2<br>CLU0A.13<br>CLU1A.11<br>CLU2B.10<br>CLU3A.12|ADC0.8<br>CMP0P.8<br>CMP0N.8|
|24|P1.1|Multifunction I/O|Yes|P1MAT.1<br>CLU0B.12<br>CLU1B.10<br>CLU2A.11<br>CLU3B.13|ADC0.7<br>CMP0P.7<br>CMP0N.7|


**silabs.com** | Building a more connected world. Rev. 1.5 | 50

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|25|P1.0|Multifunction I/O|Yes|P1MAT.0<br>CLU1OUT<br>CLU0A.12<br>CLU1A.10<br>CLU2A.10<br>CLU3B.12|ADC0.6<br>CMP0P.6<br>CMP0N.6<br>CMP1P.1<br>CMP1N.1|
|26|P0.7|Multifunction I/O|Yes|P0MAT.7<br>INT0.7<br>INT1.7<br>CLU0B.11<br>CLU1B.9<br>CLU3A.11|ADC0.5<br>CMP0P.5<br>CMP0N.5<br>CMP1P.0<br>CMP1N.0|
|27|P0.6|Multifunction I/O|Yes|P0MAT.6<br>CNVSTR<br>INT0.6<br>INT1.6<br>CLU0A.11<br>CLU1B.8<br>CLU3A.10|ADC0.4<br>CMP0P.4<br>CMP0N.4|
|28|P0.5|Multifunction I/O|Yes|P0MAT.5<br>INT0.5<br>INT1.5<br>UART0_RX<br>CLU0B.10<br>CLU1A.9<br>CLU3B.11|ADC0.3<br>CMP0P.3<br>CMP0N.3|
|29|P0.4|Multifunction I/O|Yes|P0MAT.4<br>INT0.4<br>INT1.4<br>UART0_TX<br>CLU0A.10<br>CLU1A.8<br>CLU3B.10|ADC0.2<br>CMP0P.2<br>CMP0N.2|


**silabs.com** | Building a more connected world. Rev. 1.5 | 51

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|30|P0.3|Multifunction I/O|Yes|P0MAT.3<br>EXTCLK<br>INT0.3<br>INT1.3<br>CLU0B.9<br>CLU2B.9<br>CLU3A.9|EXTOSC|
|31|P0.2|Multifunction I/O|Yes|P0MAT.2<br>INT0.2<br>INT1.2<br>CLU0OUT<br>CLU0A.9<br>CLU2B.8<br>CLU3A.8|ADC0.1<br>CMP0P.1<br>CMP0N.1|
|32|P0.1|Multifunction I/O|Yes|P0MAT.1<br>INT0.1<br>INT1.1<br>CLU0B.8<br>CLU2A.9<br>CLU3B.9|ADC0.0<br>CMP0P.0<br>CMP0N.0<br>AGND|


**silabs.com** | Building a more connected world. Rev. 1.5 | 52

EFM8BB3 Data Sheet

Pin Definitions


**6.3 EFM8BB3x-QFN24 and EFM8BB3x-4QFN24 Pin Definitions**


P0.7

P1.0


P1.1

P1.2

GND


P0.1

P0.0

GND

VDD / VIO

RSTb / C2CK









P2.3



P1.4



**Figure 6.3. EFM8BB3x-QFN24 (QFN24-GI) and EFM8BB3x-4QFN24 (QFN24-AI) Pinout**

**Table 6.3. Pin Definitions for EFM8BB3x-QFN24 (QFN24-GI) and EFM8BB3x-4QFN24 (QFN24-AI)**





|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|1|P0.1|Multifunction I/O|Yes|P0MAT.1<br>INT0.1<br>INT1.1<br>CLU0B.8<br>CLU2A.9<br>CLU3B.9|ADC0.0<br>CMP0P.0<br>CMP0N.0<br>AGND|


**silabs.com** | Building a more connected world. Rev. 1.5 | 53

EFM8BB3 Data Sheet

Pin Definitions







|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|2|P0.0|Multifunction I/O|Yes|P0MAT.0<br>INT0.0<br>INT1.0<br>CLU0A.8<br>CLU2A.8<br>CLU3B.8|VREF|
|3|GND|Ground||||
|4|VDD / VIO|Supply Power Input||||
|5|RSTb /<br>C2CK|Active-low Reset /<br>C2 Debug Clock||||
|6|P3.0 /<br>C2D|Multifunction I/O /<br>C2 Debug Data||||
|7|P2.3|Multifunction I/O|Yes|P2MAT.3<br>CLU1B.15<br>CLU2B.15<br>CLU3A.15|DAC3|
|8|P2.2|Multifunction I/O|Yes|P2MAT.2<br>CLU1A.15<br>CLU2B.14<br>CLU3A.14|DAC2|
|9|P2.1|Multifunction I/O|Yes|P2MAT.1<br>CLU1B.14<br>CLU2A.15<br>CLU3B.15|DAC1|
|10|P2.0|Multifunction I/O|Yes|P2MAT.0<br>CLU1A.14<br>CLU2A.14<br>CLU3B.14|DAC0|
|11|P1.6|Multifunction I/O|Yes|P1MAT.6<br>CLU3OUT<br>CLU0A.15<br>CLU1B.12<br>CLU2A.12|ADC0.11<br>CMP1P.5<br>CMP1N.5|


**silabs.com** | Building a more connected world. Rev. 1.5 | 54

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|12|P1.5|Multifunction I/O|Yes|P1MAT.5<br>CLU2OUT<br>CLU0B.14<br>CLU1A.13<br>CLU2B.13|ADC0.10<br>CMP1P.4<br>CMP1N.4|
|13|P1.4|Multifunction I/O|Yes|P1MAT.4<br>I2C0_SCL<br>CLU0A.14<br>CLU1A.12<br>CLU2B.12|ADC0.9<br>CMP1P.3<br>CMP1N.3|
|14|P1.3|Multifunction I/O|Yes|P1MAT.3<br>I2C0_SDA<br>CLU0B.13<br>CLU1B.11<br>CLU2B.11<br>CLU3A.13|CMP1P.2<br>CMP1N.2|
|15|GND|Ground||||
|16|P1.2|Multifunction I/O|Yes|P1MAT.2<br>CLU0A.13<br>CLU1A.11<br>CLU2B.10<br>CLU3A.12|ADC0.8|
|17|P1.1|Multifunction I/O|Yes|P1MAT.1<br>CLU0B.12<br>CLU1B.10<br>CLU2A.11<br>CLU3B.13|ADC0.7|
|18|P1.0|Multifunction I/O|Yes|P1MAT.0<br>CLU0A.12<br>CLU1A.10<br>CLU2A.10<br>CLU3B.12|ADC0.6|


**silabs.com** | Building a more connected world. Rev. 1.5 | 55

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|19|P0.7|Multifunction I/O|Yes|P0MAT.7<br>INT0.7<br>INT1.7<br>CLU1OUT<br>CLU0B.11<br>CLU1B.9<br>CLU3A.11|ADC0.5<br>CMP0P.5<br>CMP0N.5<br>CMP1P.1<br>CMP1N.1|
|20|P0.6|Multifunction I/O|Yes|P0MAT.6<br>CNVSTR<br>INT0.6<br>INT1.6<br>CLU0A.11<br>CLU1B.8<br>CLU3A.10|ADC0.4<br>CMP0P.4<br>CMP0N.4<br>CMP1P.0<br>CMP1N.0|
|21|P0.5|Multifunction I/O|Yes|P0MAT.5<br>INT0.5<br>INT1.5<br>UART0_RX<br>CLU0B.10<br>CLU1A.9<br>CLU3B.11|ADC0.3<br>CMP0P.3<br>CMP0N.3|
|22|P0.4|Multifunction I/O|Yes|P0MAT.4<br>INT0.4<br>INT1.4<br>UART0_TX<br>CLU0A.10<br>CLU1A.8<br>CLU3B.10|ADC0.2<br>CMP0P.2<br>CMP0N.2|
|23|P0.3|Multifunction I/O|Yes|P0MAT.3<br>EXTCLK<br>INT0.3<br>INT1.3<br>CLU0B.9<br>CLU2B.9<br>CLU3A.9|EXTOSC|


**silabs.com** | Building a more connected world. Rev. 1.5 | 56

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|24|P0.2|Multifunction I/O|Yes|P0MAT.2<br>INT0.2<br>INT1.2<br>CLU0OUT<br>CLU0A.9<br>CLU2B.8<br>CLU3A.8|ADC0.1<br>CMP0P.1<br>CMP0N.1|
|Center|GND|Ground||||


**silabs.com** | Building a more connected world. Rev. 1.5 | 57

**6.4 EFM8BB3x-QSOP24 Pin Definitions**

P0.3

P0.2

P0.1

P0.0

GND

VDD / VIO

RSTb / C2CK

P3.0 / C2D

P2.3

P2.2

P2.1

P2.0


EFM8BB3 Data Sheet

Pin Definitions



P0.4

P0.5

P0.6

P0.7

P1.0

P1.1

P1.2

P1.3

P1.4

P1.5

P1.6

P1.7



|Col1|24 pin QSOP<br>(Top View)|Col3|
|---|---|---|
|1|1|24|
||||
|2|2|23|
||||
|3|3|22|
||||
|4|4|21|
||||
|5|5|20|
||||
|6|6|19|
||||
|7|7|18|
||||
|8|8|17|
||||
|9|9|16|
||||
|10|10|15|
||||
|11|11|14|
||||
|12|12|13|
||||



**Figure 6.4.  EFM8BB3x-QSOP24 Pinout**

**Table 6.4. Pin Definitions for EFM8BB3x-QSOP24**


|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|1|P0.3|Multifunction I/O|Yes|P0MAT.3<br>EXTCLK<br>INT0.3<br>INT1.3<br>CLU0B.9<br>CLU2B.9<br>CLU3A.9|EXTOSC|


**silabs.com** | Building a more connected world. Rev. 1.5 | 58

EFM8BB3 Data Sheet

Pin Definitions







|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|2|P0.2|Multifunction I/O|Yes|P0MAT.2<br>INT0.2<br>INT1.2<br>CLU0OUT<br>CLU0A.9<br>CLU2B.8<br>CLU3A.8|ADC0.1<br>CMP0P.1<br>CMP0N.1|
|3|P0.1|Multifunction I/O|Yes|P0MAT.1<br>INT0.1<br>INT1.1<br>CLU0B.8<br>CLU2A.9<br>CLU3B.9|ADC0.0<br>CMP0P.0<br>CMP0N.0<br>AGND|
|4|P0.0|Multifunction I/O|Yes|P0MAT.0<br>INT0.0<br>INT1.0<br>CLU0A.8<br>CLU2A.8<br>CLU3B.8|VREF|
|5|GND|Ground||||
|6|VDD / VIO|Supply Power Input||||
|7|RSTb /<br>C2CK|Active-low Reset /<br>C2 Debug Clock||||
|8|P3.0 /<br>C2D|Multifunction I/O /<br>C2 Debug Data||||
|9|P2.3|Multifunction I/O|Yes|P2MAT.3<br>CLU1B.15<br>CLU2B.15<br>CLU3A.15|DAC3|
|10|P2.2|Multifunction I/O|Yes|P2MAT.2<br>CLU1A.15<br>CLU2B.14<br>CLU3A.14|DAC2|


**silabs.com** | Building a more connected world. Rev. 1.5 | 59

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|11|P2.1|Multifunction I/O|Yes|P2MAT.1<br>CLU1B.14<br>CLU2A.15<br>CLU3B.15|DAC1|
|12|P2.0|Multifunction I/O|Yes|P2MAT.0<br>CLU1A.14<br>CLU2A.14<br>CLU3B.14|DAC0|
|13|P1.7|Multifunction I/O|Yes|P1MAT.7<br>CLU0B.15<br>CLU1B.13<br>CLU2A.13|ADC0.12<br>CMP1P.6<br>CMP1N.6|
|14|P1.6|Multifunction I/O|Yes|P1MAT.6<br>CLU3OUT<br>CLU0A.15<br>CLU1B.12<br>CLU2A.12|ADC0.11<br>CMP1P.5<br>CMP1N.5|
|15|P1.5|Multifunction I/O|Yes|P1MAT.5<br>CLU2OUT<br>CLU0B.14<br>CLU1A.13<br>CLU2B.13|ADC0.10<br>CMP1P.4<br>CMP1N.4|
|16|P1.4|Multifunction I/O|Yes|P1MAT.4<br>I2C0_SCL<br>CLU0A.14<br>CLU1A.12<br>CLU2B.12|ADC0.9<br>CMP1P.3<br>CMP1N.3|
|17|P1.3|Multifunction I/O|Yes|P1MAT.3<br>I2C0_SDA<br>CLU0B.13<br>CLU1B.11<br>CLU2B.11<br>CLU3A.13|CMP1P.2<br>CMP1N.2|


**silabs.com** | Building a more connected world. Rev. 1.5 | 60

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|18|P1.2|Multifunction I/O|Yes|P1MAT.2<br>CLU0A.13<br>CLU1A.11<br>CLU2B.10<br>CLU3A.12|ADC0.8|
|19|P1.1|Multifunction I/O|Yes|P1MAT.1<br>CLU0B.12<br>CLU1B.10<br>CLU2A.11<br>CLU3B.13|ADC0.7|
|20|P1.0|Multifunction I/O|Yes|P1MAT.0<br>CLU0A.12<br>CLU1A.10<br>CLU2A.10<br>CLU3B.12|ADC0.6|
|21|P0.7|Multifunction I/O|Yes|P0MAT.7<br>INT0.7<br>INT1.7<br>CLU1OUT<br>CLU0B.11<br>CLU1B.9<br>CLU3A.11|ADC0.5<br>CMP0P.5<br>CMP0N.5<br>CMP1P.1<br>CMP1N.1|
|22|P0.6|Multifunction I/O|Yes|P0MAT.6<br>CNVSTR<br>INT0.6<br>INT1.6<br>CLU0A.11<br>CLU1B.8<br>CLU3A.10|ADC0.4<br>CMP0P.4<br>CMP0N.4<br>CMP1P.0<br>CMP1N.0|


**silabs.com** | Building a more connected world. Rev. 1.5 | 61

EFM8BB3 Data Sheet

Pin Definitions




|Pin<br>Number|Pin Name|Description|Crossbar Capability|Additional Digital<br>Functions|Analog Functions|
|---|---|---|---|---|---|
|23|P0.5|Multifunction I/O|Yes|P0MAT.5<br>INT0.5<br>INT1.5<br>UART0_RX<br>CLU0B.10<br>CLU1A.9<br>CLU3B.11|ADC0.3<br>CMP0P.3<br>CMP0N.3|
|24|P0.4|Multifunction I/O|Yes|P0MAT.4<br>INT0.4<br>INT1.4<br>UART0_TX<br>CLU0A.10<br>CLU1A.8<br>CLU3B.10|ADC0.2<br>CMP0P.2<br>CMP0N.2|


**silabs.com** | Building a more connected world. Rev. 1.5 | 62

EFM8BB3 Data Sheet
QFN32-GI Package Specifications

**7. QFN32-GI Package Specifications**

**7.1 Package Dimensions**

**Figure 7.1. Package Drawing**

**Table 7.1. Package Dimensions**

|Dimension|Min|Typ|Max|
|---|---|---|---|
|A|0.45|0.50|0.55|
|A1|0.00|0.035|0.05|
|b|0.15|0.20|0.25|
|D|4.00 BSC.|4.00 BSC.|4.00 BSC.|
|D2|2.80|2.90|3.00|
|e|0.40 BSC.|0.40 BSC.|0.40 BSC.|
|E|4.00 BSC.|4.00 BSC.|4.00 BSC.|
|E2|2.80|2.90|3.00|
|L|0.20|0.30|0.40|
|aaa|—|—|0.10|
|bbb|—|—|0.10|
|ccc|—|—|0.08|
|ddd|—|—|0.10|
|eee|—|—|0.10|
|ggg|—|—|0.05|



**silabs.com** | Building a more connected world. Rev. 1.5 | 63

EFM8BB3 Data Sheet
QFN32-GI Package Specifications

|Dimension|Min|Typ|Max|
|---|---|---|---|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC Solid State Outline MO-220.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020C specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC Solid State Outline MO-220.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020C specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC Solid State Outline MO-220.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020C specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC Solid State Outline MO-220.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020C specification for Small Body Components.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 64

EFM8BB3 Data Sheet
QFN32-GI Package Specifications

**7.2 PCB Land Pattern**

**Figure 7.2. PCB Land Pattern Drawing**

**Table 7.2. PCB Land Pattern Dimensions**

|Dimension|Min|Max|
|---|---|---|
|C1|—|4.10|
|C2|—|4.10|
|X1|—|0.2|
|X2|—|3.0|
|Y1|—|0.7|
|Y2|—|3.0|
|e|—|0.4|



**silabs.com** | Building a more connected world. Rev. 1.5 | 65

EFM8BB3 Data Sheet
QFN32-GI Package Specifications

|Dimension|Min|Max|
|---|---|---|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing is per the ANSI Y14.5M-1994 specification.<br>3. This Land Pattern Design is based on the IPC-7351 guidelines.<br>4. All dimensions shown are at Maximum Material Condition (MMC). Least Material Condition (LMC) is calculated based on a Fabri-<br>cation Allowance of 0.05mm.<br>5. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>6. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>7. The stencil thickness should be 0.125 mm (5 mils).<br>8. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>9. A 2 x 2 array of 1.10 mm square openings on a 1.30 mm pitch should be used for the center pad.<br>10. A No-Clean, Type-3 solder paste is recommended.<br>11. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing is per the ANSI Y14.5M-1994 specification.<br>3. This Land Pattern Design is based on the IPC-7351 guidelines.<br>4. All dimensions shown are at Maximum Material Condition (MMC). Least Material Condition (LMC) is calculated based on a Fabri-<br>cation Allowance of 0.05mm.<br>5. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>6. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>7. The stencil thickness should be 0.125 mm (5 mils).<br>8. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>9. A 2 x 2 array of 1.10 mm square openings on a 1.30 mm pitch should be used for the center pad.<br>10. A No-Clean, Type-3 solder paste is recommended.<br>11. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing is per the ANSI Y14.5M-1994 specification.<br>3. This Land Pattern Design is based on the IPC-7351 guidelines.<br>4. All dimensions shown are at Maximum Material Condition (MMC). Least Material Condition (LMC) is calculated based on a Fabri-<br>cation Allowance of 0.05mm.<br>5. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>6. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>7. The stencil thickness should be 0.125 mm (5 mils).<br>8. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>9. A 2 x 2 array of 1.10 mm square openings on a 1.30 mm pitch should be used for the center pad.<br>10. A No-Clean, Type-3 solder paste is recommended.<br>11. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**7.3 Package Marking**

**Figure 7.3. Package Marking**

The package marking consists of:

 - PPPPPPPP – The part number designation.

 - TTTTTT – A trace or manufacturing code.

 - YY – The last 2 digits of the assembly year.

 - WW – The 2-digit workweek when the device was assembled.

 - # – The device revision (A, B, etc.).

**silabs.com** | Building a more connected world. Rev. 1.5 | 66

EFM8BB3 Data Sheet
QFN32-AI Package Specifications

**8. QFN32-AI Package Specifications**

**8.1 Package Dimensions**

**Figure 8.1. Package Drawing**

**Table 8.1. Package Dimensions**

|Dimension|Min|Typ|Max|
|---|---|---|---|
|A|0.70|0.75|0.80|
|A1|0.00|0.02|0.05|
|b|0.20|0.25|0.30|
|D|5.00 BSC|5.00 BSC|5.00 BSC|
|D2|3.40|3.50|3.60|
|e|0.50 BSC|0.50 BSC|0.50 BSC|
|E|5.00 BSC|5.00 BSC|5.00 BSC|
|E2|3.40|3.50|3.60|
|L|0.30|0.40|0.50|
|aaa|0.10|0.10|0.10|
|bbb|0.10|0.10|0.10|
|ccc|0.08|0.08|0.08|
|ddd|0.10|0.10|0.10|



**silabs.com** | Building a more connected world. Rev. 1.5 | 67

EFM8BB3 Data Sheet
QFN32-AI Package Specifications

|Dimension|Min|Typ|Max|
|---|---|---|---|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 68

EFM8BB3 Data Sheet
QFN32-AI Package Specifications

**8.2 PCB Land Pattern**

**Figure 8.2. PCB Land Pattern Drawing**

**Table 8.2. PCB Land Pattern Dimensions**

|Dimension|mm|
|---|---|
|C1|4.90|
|C2|4.90|
|E|0.50|
|X1|0.30|
|Y1|0.85|
|X2|3.60|
|Y2|3.60|



**silabs.com** | Building a more connected world. Rev. 1.5 | 69

EFM8BB3 Data Sheet
QFN32-AI Package Specifications

|Dimension|mm|
|---|---|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This land pattern design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A 2x2 array of 0.9 mm square openings on 1.2 mm pitch should be used for the center ground pad.<br>8. A No-Clean, Type-3 solder paste is recommended.<br>9. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This land pattern design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A 2x2 array of 0.9 mm square openings on 1.2 mm pitch should be used for the center ground pad.<br>8. A No-Clean, Type-3 solder paste is recommended.<br>9. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**8.3 Package Marking**

**Figure 8.3. Package Marking**

The package marking consists of:

 - PPPPPPPP – The part number designation.

 - TTTTTT – A trace or manufacturing code.

 - YY – The last 2 digits of the assembly year.

 - WW – The 2-digit workweek when the device was assembled.

 - # – The device revision (A, B, etc.).

**silabs.com** | Building a more connected world. Rev. 1.5 | 70

EFM8BB3 Data Sheet
QFP32 Package Specifications

**9. QFP32 Package Specifications**

**9.1 Package Dimensions**

**Figure 9.1. Package Drawing**

**Table 9.1. Package Dimensions**

|Dimension|Min|Typ|Max|
|---|---|---|---|
|A|—|—|1.20|
|A1|0.05|—|0.15|
|A2|0.95|1.00|1.05|
|b|0.30|0.37|0.45|
|c|0.09|—|0.20|
|D|9.00 BSC|9.00 BSC|9.00 BSC|
|D1|7.00 BSC|7.00 BSC|7.00 BSC|
|e|0.80 BSC|0.80 BSC|0.80 BSC|
|E|9.00 BSC|9.00 BSC|9.00 BSC|



**silabs.com** | Building a more connected world. Rev. 1.5 | 71

EFM8BB3 Data Sheet
QFP32 Package Specifications

|Dimension|Min|Typ|Max|
|---|---|---|---|
|E1|7.00 BSC|7.00 BSC|7.00 BSC|
|L|0.50|0.60|0.70|
|aaa|0.20|0.20|0.20|
|bbb|0.20|0.20|0.20|
|ccc|0.10|0.10|0.10|
|ddd|0.20|0.20|0.20|
|theta|0°|3.5°|7°|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC outline MS-026.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC outline MS-026.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC outline MS-026.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC outline MS-026.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 72

EFM8BB3 Data Sheet
QFP32 Package Specifications

**9.2 PCB Land Pattern**

**Figure 9.2. PCB Land Pattern Drawing**

**Table 9.2. PCB Land Pattern Dimensions**

|Dimension|Min|Max|
|---|---|---|
|C1|8.40|8.50|
|C2|8.40|8.50|
|E|0.80 BSC|0.80 BSC|
|X1|0.55|0.55|
|Y1|1.5|1.5|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This Land Pattern Design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A No-Clean, Type-3 solder paste is recommended.<br>8. The recommended card reflow profile is per the JEDEC/IPC J-STD-020C specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This Land Pattern Design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A No-Clean, Type-3 solder paste is recommended.<br>8. The recommended card reflow profile is per the JEDEC/IPC J-STD-020C specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This Land Pattern Design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A No-Clean, Type-3 solder paste is recommended.<br>8. The recommended card reflow profile is per the JEDEC/IPC J-STD-020C specification for Small Body Components.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 73

EFM8BB3 Data Sheet
QFP32 Package Specifications


**9.3 Package Marking**



**Figure 9.3. Package Marking**

The package marking consists of:

 - PPPPPPPP – The part number designation.

 - TTTTTT – A trace or manufacturing code.

 - YY – The last 2 digits of the assembly year.

 - WW – The 2-digit workweek when the device was assembled.

 - # – The device revision (A, B, etc.).

**silabs.com** | Building a more connected world. Rev. 1.5 | 74

EFM8BB3 Data Sheet
QFN24-GI Package Specifications

**10. QFN24-GI Package Specifications**

**10.1 Package Dimensions**

**Figure 10.1. Package Drawing**

**silabs.com** | Building a more connected world. Rev. 1.5 | 75

EFM8BB3 Data Sheet
QFN24-GI Package Specifications

**Table 10.1. Package Dimensions**

|Dimension|Min|Typ|Max|
|---|---|---|---|
|A|0.8|0.85|0.9|
|A1|0.00|—|0.05|
|A2|—|0.65|—|
|A3|0.203 REF|0.203 REF|0.203 REF|
|b|0.15|0.2|0.25|
|b1|0.25|0.3|0.35|
|D|3.00 BSC|3.00 BSC|3.00 BSC|
|E|3.00 BSC|3.00 BSC|3.00 BSC|
|e|0.40 BSC|0.40 BSC|0.40 BSC|
|e1|0.45 BSC|0.45 BSC|0.45 BSC|
|J|1.60|1.70|1.80|
|K|1.60|1.70|1.80|
|L|0.35|0.40|0.45|
|L1|0.25|0.30|0.35|
|aaa|—|0.10|—|
|bbb|—|0.10|—|
|ccc|—|0.08|—|
|ddd|—|0.1|—|
|eee|—|0.1|—|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC Solid State Outline MO-248 but includes custom features which are toleranced per supplier<br>designation.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC Solid State Outline MO-248 but includes custom features which are toleranced per supplier<br>designation.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC Solid State Outline MO-248 but includes custom features which are toleranced per supplier<br>designation.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC Solid State Outline MO-248 but includes custom features which are toleranced per supplier<br>designation.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 76

**10.2 PCB Land Pattern**




EFM8BB3 Data Sheet
QFN24-GI Package Specifications




|c<br>X1<br>Y3<br>Y1<br>e<br>f Y2 C2<br>c<br>X2<br>C1|Col2|Col3|Col4|
|---|---|---|---|
|c<br>X1<br>Y3<br>Y1<br>e<br>f Y2 C2<br>c<br>X2<br>C1||||
|c||||
|c||||


**Figure 10.2. PCB Land Pattern Drawing**

**Table 10.2. PCB Land Pattern Dimensions**

|Dimension|Min|Max|
|---|---|---|
|C1|3.00|3.00|
|C2|3.00|3.00|
|e|0.4 REF|0.4 REF|
|X1|0.20|0.20|
|X2|1.80|1.80|
|Y1|0.80|0.80|
|Y2|1.80|1.80|
|Y3|0.4|0.4|
|f|2.50 REF|2.50 REF|



**silabs.com** | Building a more connected world. Rev. 1.5 | 77

EFM8BB3 Data Sheet
QFN24-GI Package Specifications

|Dimension|Min|Max|
|---|---|---|
|c|0.25|0.35|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing is per the ANSI Y14.5M-1994 specification.<br>3. This Land Pattern Design is based on the IPC-SM-782 guidelines.<br>4. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>5. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>6. The stencil thickness should be 0.125 mm (5 mils).<br>7. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>8. A 2 x 1 array of 0.7 mm x 1.6 mm openings on a 0.9 mm pitch should be used for the center pad.<br>9. A No-Clean, Type-3 solder paste is recommended.<br>10. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing is per the ANSI Y14.5M-1994 specification.<br>3. This Land Pattern Design is based on the IPC-SM-782 guidelines.<br>4. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>5. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>6. The stencil thickness should be 0.125 mm (5 mils).<br>7. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>8. A 2 x 1 array of 0.7 mm x 1.6 mm openings on a 0.9 mm pitch should be used for the center pad.<br>9. A No-Clean, Type-3 solder paste is recommended.<br>10. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing is per the ANSI Y14.5M-1994 specification.<br>3. This Land Pattern Design is based on the IPC-SM-782 guidelines.<br>4. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>5. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>6. The stencil thickness should be 0.125 mm (5 mils).<br>7. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>8. A 2 x 1 array of 0.7 mm x 1.6 mm openings on a 0.9 mm pitch should be used for the center pad.<br>9. A No-Clean, Type-3 solder paste is recommended.<br>10. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**10.3 Package Marking**



**Figure 10.3. Package Marking**

The package marking consists of:

 - PPPPPPPP – The part number designation.

 - TTTTTT – A trace or manufacturing code.

 - YY – The last 2 digits of the assembly year.

 - WW – The 2-digit workweek when the device was assembled.

 - # – The device revision (A, B, etc.).

**silabs.com** | Building a more connected world. Rev. 1.5 | 78

EFM8BB3 Data Sheet
QFN24-AI Package Specifications

**11. QFN24-AI Package Specifications**

**11.1 Package Dimensions**

**Figure 11.1. Package Drawing**

**Table 11.1. Package Dimensions**

|Dimension|Min|Typ|Max|
|---|---|---|---|
|A|0.70|0.75|0.80|
|A1|0.00|0.02|0.05|
|b|0.20|0.25|0.30|
|D|4.00 BSC|4.00 BSC|4.00 BSC|
|D2|2.35|2.45|2.55|
|e|0.50 BSC|0.50 BSC|0.50 BSC|
|E|4.00 BSC|4.00 BSC|4.00 BSC|
|E2|2.35|2.45|2.55|
|L|0.30|0.40|0.50|
|aaa|0.10|0.10|0.10|
|bbb|0.10|0.10|0.10|
|ccc|0.08|0.08|0.08|
|ddd|0.10|0.10|0.10|



**silabs.com** | Building a more connected world. Rev. 1.5 | 79

EFM8BB3 Data Sheet
QFN24-AI Package Specifications

|Dimension|Min|Typ|Max|
|---|---|---|---|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 80

EFM8BB3 Data Sheet
QFN24-AI Package Specifications


**11.2 PCB Land Pattern**

##### X1

**Figure 11.2. PCB Land Pattern Drawing**

**Table 11.2. PCB Land Pattern Dimensions**

|Dimension|Min|Max|
|---|---|---|
|C1|3.90|3.90|
|C2|3.90|3.90|
|E|0.50|0.50|
|X1|0.30|0.30|
|X2|2.55|2.55|
|Y1|0.85|0.85|
|Y2|2.55|2.55|



**silabs.com** | Building a more connected world. Rev. 1.5 | 81

EFM8BB3 Data Sheet
QFN24-AI Package Specifications

|Dimension|Min|Max|
|---|---|---|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This Land Pattern Design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A 2 x 2 array of 0.9 mm square openings on a 1.2 mm pitch should be used for the center pad.<br>8. A No-Clean, Type-3 solder paste is recommended.<br>9. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This Land Pattern Design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A 2 x 2 array of 0.9 mm square openings on a 1.2 mm pitch should be used for the center pad.<br>8. A No-Clean, Type-3 solder paste is recommended.<br>9. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This Land Pattern Design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A 2 x 2 array of 0.9 mm square openings on a 1.2 mm pitch should be used for the center pad.<br>8. A No-Clean, Type-3 solder paste is recommended.<br>9. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**11.3 Package Marking**



**Figure 11.3. Package Marking**

The package marking consists of:

 - PPPPPPPP – The part number designation.

 - TTTTTT – A trace or manufacturing code.

 - YY – The last 2 digits of the assembly year.

 - WW – The 2-digit workweek when the device was assembled.

 - # – The device revision (A, B, etc.).

**silabs.com** | Building a more connected world. Rev. 1.5 | 82

EFM8BB3 Data Sheet
QSOP24 Package Specifications

**12. QSOP24 Package Specifications**

**12.1 Package Dimensions**

**Figure 12.1. Package Drawing**

**Table 12.1. Package Dimensions**

|Dimension|Min|Typ|Max|
|---|---|---|---|
|A|—|—|1.75|
|A1|0.10|—|0.25|
|b|0.20|—|0.30|
|c|0.10|—|0.25|
|D|8.65 BSC|8.65 BSC|8.65 BSC|
|E|6.00 BSC|6.00 BSC|6.00 BSC|
|E1|3.90 BSC|3.90 BSC|3.90 BSC|
|e|0.635 BSC|0.635 BSC|0.635 BSC|
|L|0.40|—|1.27|



**silabs.com** | Building a more connected world. Rev. 1.5 | 83

EFM8BB3 Data Sheet
QSOP24 Package Specifications

|Dimension|Min|Typ|Max|
|---|---|---|---|
|theta|0º|—|8º|
|aaa|0.20|0.20|0.20|
|bbb|0.18|0.18|0.18|
|ccc|0.10|0.10|0.10|
|ddd|0.10|0.10|0.10|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC outline MO-137, variation AE.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC outline MO-137, variation AE.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC outline MO-137, variation AE.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.<br>3. This drawing conforms to JEDEC outline MO-137, variation AE.<br>4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 84

EFM8BB3 Data Sheet
QSOP24 Package Specifications

**12.2 PCB Land Pattern**

**Figure 12.2. PCB Land Pattern Drawing**

**Table 12.2. PCB Land Pattern Dimensions**

|Dimension|Min|Max|
|---|---|---|
|C|5.20|5.30|
|E|0.635 BSC|0.635 BSC|
|X|0.30|0.40|
|Y|1.50|1.60|
|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This land pattern design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A No-Clean, Type-3 solder paste is recommended.<br>8. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This land pattern design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A No-Clean, Type-3 solder paste is recommended.<br>8. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|Note:<br>1. All dimensions shown are in millimeters (mm) unless otherwise noted.<br>2. This land pattern design is based on the IPC-7351 guidelines.<br>3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm<br>minimum, all the way around the pad.<br>4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.<br>5. The stencil thickness should be 0.125 mm (5 mils).<br>6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.<br>7. A No-Clean, Type-3 solder paste is recommended.<br>8. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.|



**silabs.com** | Building a more connected world. Rev. 1.5 | 85

EFM8BB3 Data Sheet
QSOP24 Package Specifications


**12.3 Package Marking**



**Figure 12.3. Package Marking**

The package marking consists of:

 - PPPPPPPP – The part number designation.

 - TTTTTT – A trace or manufacturing code.

 - YY – The last 2 digits of the assembly year.

 - WW – The 2-digit workweek when the device was assembled.

 - # – The device revision (A, B, etc.).

**silabs.com** | Building a more connected world. Rev. 1.5 | 86

EFM8BB3 Data Sheet

Revision History

**13. Revision History**

**13.1 Revision 1.5**

March, 2024

 - Noted that all QSOP Package OPNs are EOL.

 - Added missing 4.1.18 SPI electrical specifications.

**13.2 Revision 1.4**

October, 2020

 - Updated ordering part numbers to revision D.

 - Restored crystal oscillator in 1. Feature List, Figure 3.1 Detailed EFM8BB3 Block Diagram on page 9, and 3.4 Clocking as it is again
available on revision D.

 - Restored crystal frequency and current specifications to Table 4.8 External Oscillator on page 25.

 - Added Input Leakage (Pullups off or Analog) current for A-grade devices and I- and G-grade devices in Table 4.16 Port I/O on page
34.

 - Corrected typos and made minor edits throughout the document.

**13.3 Revision 1.3**

December, 2018

 - Updated ordering part numbers to revision C.

 - Updated 1. Feature List, Figure 3.1 Detailed EFM8BB3 Block Diagram on page 9, and 3.4 Clocking to removed external crystal oscillator as clock source.

 - Updated Table 4.8 External Oscillator on page 25 for RC oscillator specifications.

 - Updated 3.1 Introduction to mention all device documentation.

 - Updated 4.1.1 Recommended Operating Conditions to remove the "GPIO levels are undefined whenever VIO is less than 1 V" note,
added a new minimum for VIO, and added a note referencing 4.1.16 Port I/O.

 - Updated 3.10 Bootloader recommendations for production programming.

 - Added more information about documentation to the 3.1 Introduction section.

 - Removed all references to XTAL and renamed it to EXTOSC.

**13.4 Revision 1.2**

June, 2017

 - Added A-grade devices and additional I-grade devices.

 - Added the packages for the A-grade and new I-grade devices (QFN24-AI and QFN32-AI).

 - Renamed the existing QFN24 and QFN32 packages to QFN24-GI and QFN32-GI.

 - Added a note to Table 4.2 Power Consumption on page 20 providing more information about the Comparator Reference specification.

**silabs.com** | Building a more connected world. Rev. 1.5 | 87

EFM8BB3 Data Sheet

Revision History

**13.5 Revision 1.1**

March, 2017

 - Added 4.1.12 1.8 V Internal LDO Voltage Regulator.

 - Updated the Integral Nonlinearity second row conditions to "DAC1 and DAC3" instead of "DAC0 and DAC3" in 4.1.13 DACs.

 - Fixed the Symbol and Test Condition values for Output Noise in 4.1.13 DACs.

 - Added a note to 4.1.9 ADC specifying the production test VREF and ground setup.

 - Added Output Voltage and Output Current specifications to 4.1.13 DACs.

 - Updated the language in 1. Feature List to clarify the package offerings for each of the different temperature grades.

 - Updated the minimum VIO displayed in Figure 5.1 Power Connection Diagram on page 41 to match the specification in 4.1.1 Recommended Operating Conditions.

 - Added a note to 3.1 Introduction referencing the Reference Manual.

 - Corrected the application note number for *AN124: Pin Sharing Techniques for the C2 Interface* in 5.2 Debug.

 - Adjusted the Data Hold and Data Setup Times in 4.1.17 SMBus and added a note referring to the DLYEXT bit.

**13.6 Revision 1.01**

October, 2016

 - Updated Figure 2.1 EFM8BB3 Part Numbering on page 3 to include the I-grade description.

 - Updated QFN24 center pad stencil description.

**13.7 Revision 1.0**

September, 2016

 - Filled in all TBD values in 4. Electrical Specifications.

 - Added a note regarding which DACs are available to Table 2.1 Product Selection Guide on page 3.

 - Added specifications for 4.1.17 SMBus.

 - Added bootloader pinout information to 3.10 Bootloader.

 - Added CRC Calculation Time to 4.1.4 Flash Memory.

**13.8 Revision 0.4**

May, 2016

 - Filled in TBD values for DAC Integral Nonlinearity in Table 4.13 DACs on page 31.

 - Added I-grade devices.

 - Adjusted the Total Current Sunk into Supply Pin and Total Current Sourced out of Ground Pin specifications in 4.3 Absolute Maximum Ratings.

 - Added Operating Junction Temperature specification to 4.3 Absolute Maximum Ratings.

**13.9 Revision 0.3**

February, 2016

 - Added EFM8831F16G-A-QFN24 to Table 2.1 Product Selection Guide on page 3.

 - Updated Figure 5.2 Debug Connection Diagram on page 42 to move the pull-up resistor on C2D / RSTb to after the series resistor
instead of before.

 - Added mention of the pre-programmed bootloader in 1. Feature List.

 - Added a reference to *AN945: EFM8 Factory Bootloader User Guide* in 3.10 Bootloader.

 - Updated all part numbers to revision B.

 - Adjusted C1, C2, X2, Y2, and Y1 maximums for 7.2 PCB Land Pattern.

 - Adjusted package markings for QFN32 and QSOP24 packages.

 - Filled in TBD minimum and maximum values for DAC Differential Nonlinearity in Table 4.13 DACs on page 31.

**silabs.com** | Building a more connected world. Rev. 1.5 | 88

EFM8BB3 Data Sheet

Revision History

**13.10 Revision 0.2**

September, 2017

 - Added information on the bootloader to 3.10 Bootloader.

 - Updated some characterization TBD values.

**13.11 Revision 0.1**

April, 2015

 - Initial release.

**silabs.com** | Building a more connected world. Rev. 1.5 | 89

**Disclaimer**

Silicon Labs intends to provide customers with the latest, accurate, and in-depth documentation of all peripherals and modules available for system and software implementers using or intending to use the Silicon Labs products. Characterization data, available modules and peripherals, memory sizes and memory addresses refer to each
specific device, and “Typical” parameters provided can and do vary in different applications. Application examples described herein are for illustrative purposes only. Silicon
Labs reserves the right to make changes without further notice to the product information, specifications, and descriptions herein, and does not give warranties as to the
accuracy or completeness of the included information. Without prior notification, Silicon Labs may update product firmware during the manufacturing process for security or
reliability reasons. Such changes will not alter the specifications or the performance of the product. Silicon Labs shall have no liability for the consequences of use of the information supplied in this document. This document does not imply or expressly grant any license to design or fabricate any integrated circuits. The products are not designed or
authorized to be used within any FDA Class III devices, applications for which FDA premarket approval is required or Life Support Systems without the specific written consent
of Silicon Labs. A “Life Support System” is any product or system intended to support or sustain life and/or health, which, if it fails, can be reasonably expected to result in
significant personal injury or death. Silicon Labs products are not designed or authorized for military applications. Silicon Labs products shall under no circumstances be used
in weapons of mass destruction including (but not limited to) nuclear, biological or chemical weapons, or missiles capable of delivering such weapons. Silicon Labs disclaims
all express and implied warranties and shall not be responsible or liable for any injuries or damages related to use of a Silicon Labs product in such unauthorized applications.
**Note: This content may contain offensive terminology that is now obsolete. Silicon Labs is replacing these terms with inclusive language wherever possible. For more**
**information, visit www.silabs.com/about-us/inclusive-lexicon-project**

**Trademark Information**

Silicon Laboratories Inc. [®], Silicon Laboratories [®], Silicon Labs [®], SiLabs [®] and the Silicon Labs logo [®], Bluegiga [®], Bluegiga Logo [®], EFM [®], EFM32 [®], EFR, Ember [®], Energy Micro, Energy
Micro logo and combinations thereof, “the world’s most energy friendly microcontrollers”, Redpine Signals [®], WiSeConnect, n-Link, ThreadArch [®], EZLink [®], EZRadio [®], EZRadioPRO [®],
Gecko [®], Gecko OS, Gecko OS Studio, Precision32 [®], Simplicity Studio [®], Telegesis, the Telegesis Logo [®], USBXpress [®], Zentri, the Zentri logo and Zentri DMS, Z-Wave [®], and others
are trademarks or registered trademarks of Silicon Labs. ARM, CORTEX, Cortex-M3 and THUMB are trademarks or registered trademarks of ARM Holdings. Keil is a registered
trademark of ARM Limited. Wi-Fi is a registered trademark of the Wi-Fi Alliance. All other products or brand names mentioned herein are trademarks of their respective holders.

**Silicon Laboratories Inc.**

**400 West Cesar Chavez**
**Austin, TX 78701**
**USA**

**www.silabs.com**

