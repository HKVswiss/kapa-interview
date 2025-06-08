# EFM8BB3 Data Sheet

## System Overview

### 3.2 Power

All internal circuitry draws power from the VDD supply pin. External I/O pins are powered from the VIO supply voltage (or VDD on devices without a separate VIO connection), while most of the internal circuitry is supplied by an on-chip LDO regulator. Control over the device power can be achieved by enabling/disabling individual peripherals as needed. Each analog peripheral can be disabled when not in use and placed in low power mode. Digital peripherals, such as timers and serial buses, have their clocks gated off and draw little power when they are not in use.

### Table 3.1. Power Modes

| Power Mode | Details | Mode Entry | Wake-Up Sources |
|------------|---------|------------|-----------------|
| Normal | Core and all peripherals clocked and fully operational |  |  |
| Idle | • Core halted  
• All peripherals clocked and fully operational  
• Code resumes execution on wake event | Set IDLE bit in PCON0 | Any interrupt |
| Suspend | • Core and peripheral clocks halted  
• HFOSC0 and HFOSC1 oscillators stopped  
• Regulator in normal bias mode for fast wake  
• Timer 3 and 4 may clock from LFOSC0  
• Code resumes execution on wake event | 1. Switch SYSCLK to HFOSC0  
2. Set SUSPEND bit in PCON1 | • Timer 4 Event  
• SPI0 Activity  
• I2C0 Slave Activity  
• Port Match Event  
• Comparator 0 Falling Edge  
• CLUn Interrupt-Enabled Event |
| Stop | • All internal power nets shut down  
• Pins retain state  
• Exit on any reset source | 1. Clear STOPCF bit in REG0CN  
2. Set STOP bit in PCON0 | Any reset source |
| Snooze | • Core and peripheral clocks halted  
• HFOSC0 and HFOSC1 oscillators stopped  
• Regulator in low bias current mode for energy savings  
• Timer 3 and 4 may clock from LFOSC0  
• Code resumes execution on wake event | 1. Switch SYSCLK to HFOSC0  
2. Set SNOOZE bit in PCON1 | • Timer 4 Event  
• SPI0 Activity  
• I2C0 Slave Activity  
• Port Match Event  
• Comparator 0 Falling Edge  
• CLUn Interrupt-Enabled Event |
| Shutdown | • All internal power nets shut down  
• Pins retain state  
• Exit on pin or power-on reset | 1. Set STOPCF bit in REG0CN  
2. Set STOP bit in PCON0 | • RSTb pin reset  
• Power-on reset |

### 3.3 I/O

Digital and analog resources are externally available on the device’s multi-purpose I/O pins. Port pins P0.0-P2.3 can be defined as general-purpose I/O (GPIO), assigned to one of the internal digital resources through the crossbar or dedicated channels, or assigned to an analog function. Port pins P2.4 to P3.7 can be used as GPIO. Additionally, the C2 Interface Data signal (C2D) is shared with P3.0 or P3.7, depending on the package option.

The port control block offers the following features:

- Up to 29 multi-function I/O pins, supporting digital and analog functions.
- Flexible priority crossbar decoder for digital peripheral assignment.
- Two drive strength settings for each port.
- State retention feature allows pins to retain configuration through most reset sources.
- Two direct-pin interrupt sources with dedicated interrupt vectors (INT0 and INT1).
- Up to 24 direct-pin interrupt sources with shared interrupt vector (Port Match).

---

*Page 10*