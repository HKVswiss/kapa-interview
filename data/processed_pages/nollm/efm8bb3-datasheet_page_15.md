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

Low Current Comparators (CMP0, CMP1)

An analog comparator is used to compare the voltage of two analog inputs, with a digital output indicating which input voltage is higher.

External input connections to device I/O pins and internal connections are available through separate multiplexers on the positive and

negative inputs. Hysteresis, response time, and current consumption may be programmed to suit the specific needs of the application.

The comparator includes the following features:

+ Up to 10 (CMPO) or 9 (CMP1) external positive inputs

+ Up to 10 (CMPO) or 9 (CMP1) external negative inputs

+ Additional input options:

+ Internal connection to LDO output

+ Direct connection to GND

+ Direct connection to VDD

+ Dedicated 6-bit reference DAC

+ Synchronous and asynchronous outputs can be routed to pins via crossbar

+ Programmable hysteresis between 0 and +20 mV

+ Programmable response time

+ Interrupts generated on rising, falling, or both edges

+ PWM output kill feature

3.8 Reset Sources

Reset circuitry allows the controller to be easily placed in a predefined default condition. On entry to this reset state, the following occur:

+ The core halts program execution.

+ Module registers are initialized to their defined reset values unless the bits reset only with a power-on reset.

+ External port pins are forced to a known state.

* Interrupts and timers are disabled.

All registers are reset to the predefined values noted in the register descriptions unless the bits only reset with a power-on reset. The

contents of RAM are unaffected during a reset; any previously stored data is preserved as long as power is not lost. By default, the Port

\/O latches are reset to 1 in open-drain mode, with weak pullups enabled during and after the reset. Optionally, firmware may configure

the port I/O, DAC outputs, and precision reference to maintain state through system resets other than power-on resets. For Supply

Monitor and power-on resets, the RSTb pin is driven low until the device exits the reset state. On exit from the reset state, the program

counter (PC) is reset, and the system clock defaults to an internal oscillator. The Watchdog Timer is enabled, and program execution

begins at location 0x0000.

Reset sources on the device include the following:

+ Power-on reset

.

External reset pin

.

Comparator reset

.

Software-triggered reset

.

Supply monitor reset (monitors VDD supply)

.

Watchdog timer reset

.

Missing clock detector reset

.

Flash error reset

3.9 Debugging

The EFM8BB3 devices include an on-chip Silicon Labs 2-Wire (C2) debug interface to allow flash programming and in-system debug-

ging with the production part installed in the end application. The C2 interface uses a clock signal (C2CK) and a bi-directional C2 data

signal (C2D) to transfer information between the device and a host system. See the C2 Interface Specification for details on the C2

protocol.

silabs.com | Building a more connected world.

Rev. 1.5 | 16

EFM8BB3 Data Sheet
System Overview
Low Current Comparators (CMP0, CMP1)
An analog comparator is used to compare the voltage of two analog inputs, with a digital output indicating which input voltage is higher.
External input connections to device I/O pins and internal connections are available through separate multiplexers on the positive and
negative inputs. Hysteresis, response time, and current consumption may be programmed to suit the specific needs of the application.
The comparator includes the following features:
+ Up to 10 (CMPO) or 9 (CMP1) external positive inputs
+ Up to 10 (CMPO) or 9 (CMP1) external negative inputs
+ Additional input options:
+ Internal connection to LDO output
+ Direct connection to GND
+ Direct connection to VDD
+ Dedicated 6-bit reference DAC
+ Synchronous and asynchronous outputs can be routed to pins via crossbar
+ Programmable hysteresis between 0 and +20 mV
+ Programmable response time
+ Interrupts generated on rising, falling, or both edges
+ PWM output kill feature
3.8 Reset Sources
Reset circuitry allows the controller to be easily placed in a predefined default condition. On entry to this reset state, the following occur:
+ The core halts program execution.
+ Module registers are initialized to their defined reset values unless the bits reset only with a power-on reset.
+ External port pins are forced to a known state.
* Interrupts and timers are disabled.
All registers are reset to the predefined values noted in the register descriptions unless the bits only reset with a power-on reset. The
contents of RAM are unaffected during a reset; any previously stored data is preserved as long as power is not lost. By default, the Port
\/O latches are reset to 1 in open-drain mode, with weak pullups enabled during and after the reset. Optionally, firmware may configure
the port I/O, DAC outputs, and precision reference to maintain state through system resets other than power-on resets. For Supply
Monitor and power-on resets, the RSTb pin is driven low until the device exits the reset state. On exit from the reset state, the program
counter (PC) is reset, and the system clock defaults to an internal oscillator. The Watchdog Timer is enabled, and program execution
begins at location 0x0000.
Reset sources on the device include the following:
+ Power-on reset
. External reset pin
. Comparator reset
. Software-triggered reset
. Supply monitor reset (monitors VDD supply)
. Watchdog timer reset
. Missing clock detector reset
. Flash error reset
3.9 Debugging
The EFM8BB3 devices include an on-chip Silicon Labs 2-Wire (C2) debug interface to allow flash programming and in-system debug-
ging with the production part installed in the end application. The C2 interface uses a clock signal (C2CK) and a bi-directional C2 data
signal (C2D) to transfer information between the device and a host system. See the C2 Interface Specification for details on the C2
protocol.
silabs.com | Building a more connected world. Rev. 1.5 | 16


---Page 16 

