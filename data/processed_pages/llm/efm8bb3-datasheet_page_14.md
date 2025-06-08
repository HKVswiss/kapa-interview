# EFM8BB3 Data Sheet - System Overview

## 3.7 Analog

### 12/10-Bit Analog-to-Digital Converter (ADC0)

The ADC is a successive-approximation-register (SAR) ADC with 12- and 10-bit modes, integrated track-and-hold, and a programmable window detector. It is fully configurable under software control via several registers and can measure different signals using the analog multiplexer. The voltage reference for the ADC is selectable between internal and external reference sources.

- Up to 20 external inputs
- Single-ended 12-bit and 10-bit modes
- Supports an output update rate of up to 350 ksps in 12-bit mode
- Channel sequencer logic with direct-to-XDATA output transfers
- Operation in a low power mode at lower conversion speeds
- Asynchronous hardware conversion trigger, selectable between software, external I/O, internal timer, and configurable logic sources
- Output data window comparator allows automatic range checking
- Support for output data accumulation
- Conversion complete and window compare interrupts supported
- Flexible output data formatting
- Includes a fully-internal fast-settling 1.65 V reference and an on-chip precision 2.4 / 1.2 V reference, with support for using the supply as the reference, an external reference, and signal ground
- Integrated temperature sensor

### 12-Bit Digital-to-Analog Converters (DAC0, DAC1, DAC2, DAC3)

The DAC modules are 12-bit Digital-to-Analog Converters with the capability to synchronize multiple outputs together. They are fully configurable under software control. The voltage reference for the DACs is selectable between internal and external reference sources.

- Voltage output with 12-bit performance
- Supports an update rate of 200 ksps
- Hardware conversion trigger, selectable between software, external I/O, internal timer, and configurable logic sources
- Outputs may be configured to persist through reset and maintain output state to avoid system disruption
- Multiple DAC outputs can be synchronized together
- DAC pairs (DAC0 and 1 or DAC2 and 3) support complementary output waveform generation
- Outputs may be switched between two levels according to the state of configurable logic / PWM input trigger
- Flexible input data formatting
- Supports references from internal supply, on-chip precision reference, or external VREF pin

---
*Page 15*