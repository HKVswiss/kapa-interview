# EFM8BB3 Data Sheet - Electrical Specifications

## 4.1.4 Flash Memory

| Parameter                  | Symbol   | Test Condition                      | Min  | Typ  | Max  | Units |
|----------------------------|----------|-----------------------------------|------|------|------|-------|
| Write Time¹,²              | t_WRITE  | One Byte, F = 24.5 MHz SYSCLK     | 19   | 20   | 21   | µs    |
| Erase Time¹,²              | t_ERASE  | One Page, F = 24.5 MHz SYSCLK     | 5.2  | 5.35 | 5.5  | ms    |
| V Voltage During Programming³ | V_PROG   |                                   | 2.2  | —    | 3.6  | V     |
| Endurance (Write/Erase Cycles) | N_WE     |                                   | 20k  | 100k | —    | Cycles|
| CRC Calculation Time       | t_CRC    | One 256-Byte Block, SYSCLK = 49 MHz | —    | 5.5  | —    | µs    |

**Notes:**
1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.
2. The internal High-Frequency Oscillator 0 has a programmable output frequency, factory programmed to 24.5 MHz. If user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.
3. Flash can be safely programmed at any voltage above the supply monitor threshold (VDDM).
4. Data Retention Information is published in the Quarterly Quality and Reliability Report.

---

## 4.1.5 Power Management Timing

| Parameter               | Symbol    | Test Condition               | Min | Typ | Max | Units  |
|-------------------------|-----------|------------------------------|-----|-----|-----|--------|
| Idle Mode Wake-up Time  | t_IDLEWK  |                              | 2   | —   | 3   | SYSCLKs|
| Suspend Mode Wake-up Time | t_SUSPENDWK | SYSCLK = HFOSC0, CLKDIV = 0x00 | —   | 170 | —   | ns     |
| Snooze Mode Wake-up Time | t_SLEEPWK | SYSCLK = HFOSC0, CLKDIV = 0x00 | —   | 12  | —   | µs     |

---

*Page 23*