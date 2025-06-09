# Page 12

## Text from PDF

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



## OCR Text

EFM8BB3 Data Sheet

System Overview

Timers (Timer 0, Timer 1, Timer 2, Timer 3, Timer 4, and Timer 5)

Several counter/timers are included in the device: two are 16-bit counter/timers compatible with those found in the standard 8051, and

the rest are 16-bit auto-reload timers for timing peripherals or for general purpose use. These timers can be used to measure time inter-

vals, count external events and generate periodic interrupt requests. Timer 0 and Timer 1 are nearly identical and have four primary

modes of operation. The other timers offer both 16-bit and split 8-bit timer functionality with auto-reload and capture capabilities.

Timer 0 and Timer 1 include the following features:

+ Standard 8051 timers, supporting backwards-compatibility with firmware and hardware.

* Clock sources include SYSCLK, SYSCLK divided by 12, 4, or 48, the External Clock divided by 8, or an external pin.

+ 8-bit auto-reload counter/timer mode

+ 13-bit counter/timer mode

+ 16-bit counter/timer mode

+ Dual 8-bit counter/timer mode (Timer 0)

Timer 2, Timer 3, Timer 4, and Timer 5 are 16-bit timers including the following features:

* Clock sources for all timers include SYSCLK, SYSCLK divided by 12, or the External Clock divided by 8

.

LFOSCO divided by 8 may be used to clock Timer 3 and Timer 4 in active or suspend/snooze power modes

.

Timer 4 is a low-power wake source, and can be chained together with Timer 3

.

16-bit auto-reload timer mode

.

Dual 8-bit auto-reload timer mode

.

External pin capture

.

LFOSCO capture

.

Comparator 0 capture

.

Configurable Logic output capture

Watchdog Timer (WDTO)

The device includes a programmable watchdog timer (WDT) running off the low-frequency oscillator. A WDT overflow forces the MCU

into the reset state. To prevent the reset, the WDT must be restarted by application software before overflow. If the system experiences

a software or hardware malfunction preventing the software from restarting the WDT, the WDT overflows and causes a reset. Following

a reset, the WDT is automatically enabled and running with the default maximum time interval. If needed, the WDT can be disabled by

system software or locked on to prevent accidental disabling. Once locked, the WDT cannot be disabled until the next system reset.

The state of the RST pin is unaffected by this reset.

The Watchdog Timer has the following features:

+ Programmable timeout interval

+ Runs from the low-frequency oscillator

+ Lock-out feature to prevent any modification until a system reset

3.6 Communications and Other Digital Peripherals

Universal Asynchronous Receiver/Transmitter (UARTO)

UARTO is an asynchronous, full duplex serial port offering modes 1 and 3 of the standard 8051 UART. Enhanced baud rate support

allows a wide range of clock sources to generate standard baud rates. Received data buffering allows UARTO to start reception of a

second incoming data byte before software has finished reading the previous data byte.

The UART module provides the following features:

+ Asynchronous transmissions and receptions.

+ Baud rates up to SYSCLK/2 (transmit) or SYSCLK/8 (receive).

+ 8-or 9-bit data.

+ Automatic start and stop generation.

+ Single-byte FIFO on transmit and receive.

silabs.com | Building a more connected world.

Rev. 1.5 | 12

## Tables

EFM8BB3 Data Sheet
System Overview
Timers (Timer 0, Timer 1, Timer 2, Timer 3, Timer 4, and Timer 5)
Several counter/timers are included in the device: two are 16-bit counter/timers compatible with those found in the standard 8051, and
the rest are 16-bit auto-reload timers for timing peripherals or for general purpose use. These timers can be used to measure time inter-
vals, count external events and generate periodic interrupt requests. Timer 0 and Timer 1 are nearly identical and have four primary
modes of operation. The other timers offer both 16-bit and split 8-bit timer functionality with auto-reload and capture capabilities.
Timer 0 and Timer 1 include the following features:
+ Standard 8051 timers, supporting backwards-compatibility with firmware and hardware.
* Clock sources include SYSCLK, SYSCLK divided by 12, 4, or 48, the External Clock divided by 8, or an external pin.
+ 8-bit auto-reload counter/timer mode
+ 13-bit counter/timer mode
+ 16-bit counter/timer mode
+ Dual 8-bit counter/timer mode (Timer 0)
Timer 2, Timer 3, Timer 4, and Timer 5 are 16-bit timers including the following features:
* Clock sources for all timers include SYSCLK, SYSCLK divided by 12, or the External Clock divided by 8
. LFOSCO divided by 8 may be used to clock Timer 3 and Timer 4 in active or suspend/snooze power modes
. Timer 4 is a low-power wake source, and can be chained together with Timer 3
. 16-bit auto-reload timer mode
. Dual 8-bit auto-reload timer mode
. External pin capture
. LFOSCO capture
. Comparator 0 capture
. Configurable Logic output capture
Watchdog Timer (WDTO)
The device includes a programmable watchdog timer (WDT) running off the low-frequency oscillator. A WDT overflow forces the MCU
into the reset state. To prevent the reset, the WDT must be restarted by application software before overflow. If the system experiences
a software or hardware malfunction preventing the software from restarting the WDT, the WDT overflows and causes a reset. Following
a reset, the WDT is automatically enabled and running with the default maximum time interval. If needed, the WDT can be disabled by
system software or locked on to prevent accidental disabling. Once locked, the WDT cannot be disabled until the next system reset.
The state of the RST pin is unaffected by this reset.
The Watchdog Timer has the following features:
+ Programmable timeout interval
+ Runs from the low-frequency oscillator
+ Lock-out feature to prevent any modification until a system reset
3.6 Communications and Other Digital Peripherals
Universal Asynchronous Receiver/Transmitter (UARTO)
UARTO is an asynchronous, full duplex serial port offering modes 1 and 3 of the standard 8051 UART. Enhanced baud rate support
allows a wide range of clock sources to generate standard baud rates. Received data buffering allows UARTO to start reception of a
second incoming data byte before software has finished reading the previous data byte.
The UART module provides the following features:
+ Asynchronous transmissions and receptions.
+ Baud rates up to SYSCLK/2 (transmit) or SYSCLK/8 (receive).
+ 8-or 9-bit data.
+ Automatic start and stop generation.
+ Single-byte FIFO on transmit and receive.
silabs.com | Building a more connected world. Rev. 1.5 | 12


---

