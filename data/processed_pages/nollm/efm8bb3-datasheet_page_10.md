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

3.4 Clocking

The CPU core and peripheral subsystem may be clocked by both internal and external oscillator resources. By default, the system

clock comes up running from the 24.5 MHz oscillator divided by 8.

The clock control system offers the following features:

+ Provides clock to core and peripherals.

* 24.5 MHz internal oscillator (HFOSCO), accurate to +2% over supply and temperature corners.

* 49 MHz internal oscillator (HFOSC1), accurate to +2% over supply and temperature corners.

* 80 kHz low-frequency oscillator (LFOSCO).

+ External RC, and CMOS clock options (EXTCLK and EXTOSC).

* Clock divider with eight settings for flexible clock scaling:

* Divide the selected clock source by 1, 2, 4, 8, 16, 32, 64, or 128.

+ HFOSCO and HFOSC1 include 1.5x pre-scalers for further flexibility.

3.5 Counters/Timers and PWM

Programmable Counter Array (PCAO)

The programmable counter array (PCA) provides multiple channels of enhanced timer and PWM functionality while requiring less CPU

intervention than standard counter/timers. The PCA consists of a dedicated 16-bit counter/timer and one 16-bit capture/compare mod-

ule for each channel. The counter/timer is driven by a programmable timebase that has flexible external and internal clocking options.

Each capture/compare module may be configured to operate independently in one of five modes: Edge-Triggered Capture, Software

Timer, High-Speed Output, Frequency Output, or Pulse-Width Modulated (PWM) Output. Each capture/compare module has its own

associated I/O line (CEXn) which is routed through the crossbar to port I/O when enabled.

+ 16-bit time base

.

Programmable clock divisor and clock source selection

.

Up to six independently-configurable channels

.

8, 9, 10, 11 and 16-bit PWM modes (center or edge-aligned operation)

.

Output polarity control

.

Frequency output mode

.

Capture on rising, falling or any edge

.

Compare function for arbitrary waveform generation

.

Software timer (internal compare) mode

.

Can accept hardware “kill” signal from comparator 0 or comparator 1

silabs.com | Building a more connected world.

Rev. 1.5 | 11

EFM8BB3 Data Sheet
System Overview
3.4 Clocking
The CPU core and peripheral subsystem may be clocked by both internal and external oscillator resources. By default, the system
clock comes up running from the 24.5 MHz oscillator divided by 8.
The clock control system offers the following features:
+ Provides clock to core and peripherals.
* 24.5 MHz internal oscillator (HFOSCO), accurate to +2% over supply and temperature corners.
* 49 MHz internal oscillator (HFOSC1), accurate to +2% over supply and temperature corners.
* 80 kHz low-frequency oscillator (LFOSCO).
+ External RC, and CMOS clock options (EXTCLK and EXTOSC).
* Clock divider with eight settings for flexible clock scaling:
* Divide the selected clock source by 1, 2, 4, 8, 16, 32, 64, or 128.
+ HFOSCO and HFOSC1 include 1.5x pre-scalers for further flexibility.
3.5 Counters/Timers and PWM
Programmable Counter Array (PCAO)
The programmable counter array (PCA) provides multiple channels of enhanced timer and PWM functionality while requiring less CPU
intervention than standard counter/timers. The PCA consists of a dedicated 16-bit counter/timer and one 16-bit capture/compare mod-
ule for each channel. The counter/timer is driven by a programmable timebase that has flexible external and internal clocking options.
Each capture/compare module may be configured to operate independently in one of five modes: Edge-Triggered Capture, Software
Timer, High-Speed Output, Frequency Output, or Pulse-Width Modulated (PWM) Output. Each capture/compare module has its own
associated I/O line (CEXn) which is routed through the crossbar to port I/O when enabled.
+ 16-bit time base
. Programmable clock divisor and clock source selection
. Up to six independently-configurable channels
. 8, 9, 10, 11 and 16-bit PWM modes (center or edge-aligned operation)
. Output polarity control
. Frequency output mode
. Capture on rising, falling or any edge
. Compare function for arbitrary waveform generation
. Software timer (internal compare) mode
. Can accept hardware “kill” signal from comparator 0 or comparator 1
silabs.com | Building a more connected world. Rev. 1.5 | 11


---Page 11 

