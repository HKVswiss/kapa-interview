# EFM8BB3 Data Sheet

## 4.1.2 Power Consumption

### Table 4.2. Power Consumption

| Parameter | Symbol | Test Condition | Min | Typ | Max | Unit |
|-----------|--------|----------------|-----|-----|-----|------|
| **Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)** | | | | | | |
| Normal Mode - Full speed with code executing from flash | I_DD | F = 49 MHz (HFOSC1) SYSCLK | — | 5 | 14.4 | mA |
| Normal Mode - Full speed with code executing from flash | I_DD | F = 24.5 MHz (HFOSC0) SYSCLK | — | 4.2 | 5 | mA |
| Normal Mode - Full speed with code executing from flash | I_DD | F = 1.53 MHz (HFOSC0) SYSCLK | — | 625 | 820 | µA |
| Normal Mode - Full speed with code executing from flash | I_DD | F = 80 kHz SYSCLK | — | 155 | 310 | µA |
| Idle Mode - Core halted with peripherals running | I_DD | F = 49 MHz (HFOSC1) SYSCLK | — | 3.8 | 11.8 | mA |
| Idle Mode - Core halted with peripherals running | I_DD | F = 24.5 MHz (HFOSC0) SYSCLK | — | 3.14 | 3.8 | mA |
| Idle Mode - Core halted with peripherals running | I_DD | F = 1.53 MHz (HFOSC0) SYSCLK | — | 520 | 725 | µA |
| Idle Mode - Core halted with peripherals running | I_DD | F = 80 kHz SYSCLK | — | 135 | 315 | µA |
| Suspend Mode - Core halted and high frequency clocks stopped, Supply monitor off | I_DD | LFO Running | — | 125 | 320 | µA |
| Suspend Mode - Core halted and high frequency clocks stopped, Supply monitor off | I_DD | LFO Stopped | — | 120 | 300 | µA |
| Snooze Mode - Core halted and high frequency clocks stopped. Regulator in low-power state, Supply monitor off | I_DD | LFO Running | — | 23 | 190 | µA |
| Snooze Mode - Core halted and high frequency clocks stopped. Regulator in low-power state, Supply monitor off | I_DD | LFO Stopped | — | 19 | 186 | µA |
| Stop Mode - Core halted and all clocks stopped, Internal LDO On, Supply monitor off | I_DD | — | — | 120 | 300 | µA |
| Shutdown Mode - Core halted and all clocks stopped, Internal LDO Off, Supply monitor off | I_DD | — | — | 0.2 | 0.91 | µA |

| **Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)** | | | | | | |
| Normal Mode - Full speed with code executing from flash | I_DD | F = 49 MHz (HFOSC1) SYSCLK | — | 5 | 14.4 | mA |
| Normal Mode - Full speed with code executing from flash | I_DD | F = 24.5 MHz (HFOSC0) SYSCLK | — | 4.2 | 5.2 | mA |
| Normal Mode - Full speed with code executing from flash | I_DD | F = 1.53 MHz (HFOSC0) SYSCLK | — | 625 | 1280 | µA |
| Normal Mode - Full speed with code executing from flash | I_DD | F = 80 kHz SYSCLK | — | 155 | 765 | µA |
| Idle Mode - Core halted with peripherals running | I_DD | F = 49 MHz (HFOSC1) SYSCLK | — | 3.8 | 11.8 | mA |
| Idle Mode - Core halted with peripherals running | I_DD | F = 24.5 MHz (HFOSC0) SYSCLK | — | 3.14 | 4.1 | mA |
| Idle Mode - Core halted with peripherals running | I_DD | F = 1.53 MHz (HFOSC0) SYSCLK | — | 520 | 1175 | µA |
| Idle Mode - Core halted with peripherals running | I_DD | F = 80 kHz SYSCLK | — | 135 | 750 | µA |
| Suspend Mode - Core halted and high frequency clocks stopped, Supply monitor off | I_DD | LFO Running | — | 125 | 775 | µA |
| Suspend Mode - Core halted and high frequency clocks stopped, Supply monitor off | I_DD | LFO Stopped | — | 120 | 755 | µA |

---

*Page 20*