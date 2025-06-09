# EFM8BB3 Data Sheet - Electrical Specifications

## 4.1.18 SPI

### Table 4.19. SPI Timing Parameters

| Parameter | Description                      | Min           | Max | Units |
|-----------|--------------------------------|---------------|-----|-------|
| **Master Mode Timing** |                        |               |     |       |
| T\_MCKH  | SCK High Time                  | 1 x T\_SYSCLK | —   | ns    |
| T\_MCKL  | SCK Low Time                   | 1 x T\_SYSCLK | —   | ns    |
| T\_MIS   | MISO Valid to SCK Sample Edge | 20            | —   | ns    |
| T\_MIH   | SCK Sample Edge to MISO Change| 5             | —   | ns    |
| **Slave Mode Timing** |                         |               |     |       |
| T\_SE    | NSS Falling to First SCK Edge  | 5             | —   | ns    |
| T\_SD    | Last SCK Edge to NSS Rising    | 5             | —   | ns    |
| T\_SEZ   | NSS Falling to MISO Valid      | —             | 20  | ns    |
| T\_SDZ   | NSS Rising to MISO High-Z      | —             | 20  | ns    |
| T\_CKH   | SCK High Time                  | 40            | —   | ns    |
| T\_CKL   | SCK Low Time                   | 40            | —   | ns    |
| T\_SIS   | MOSI Valid to SCK Sample Edge | 20            | —   | ns    |
| T\_SIH   | SCK Sample Edge to MOSI Change | 5             | —   | ns    |
| T\_SOH   | SCK Shift Edge to MISO Change | —             | 20  | ns    |

**Note:**
1. T is equal to one period of the device system clock (SYSCLK).

---

### Figure 4.2. SPI Master Timing (CKPHA = 0)

- SCK is shown for CKPOL = 0. SCK is the opposite polarity for CKPOL = 1.

---

*Page 37*