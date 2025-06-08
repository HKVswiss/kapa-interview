# EFM8BB3 Data Sheet - Electrical Specifications

## 4.1.17 SMBus

### Table 4.17. SMBus Peripheral Timing Performance (Master Mode)

| Parameter                                   | Symbol   | Test Condition | Min  | Typ  | Max  | Unit |
|---------------------------------------------|----------|----------------|------|------|------|------|
| **Standard Mode (100 kHz Class)**           |          |                |      |      |      |      |
| I2C Operating Frequency                      | f_I2C    |                | 0    | —    | 702  | kHz  |
| SMBus Operating Frequency                    | f_SMB    |                | 401  | —    | 702  | kHz  |
| Bus Free Time Between STOP and START Conditions | t_BUF    |                | 9.4  | —    | —    | µs   |
| Hold Time After (Repeated) START Condition  | t_HD:STA |                | 4.7  | —    | —    | µs   |
| Repeated START Condition Setup Time          | t_SU:STA |                | 9.4  | —    | —    | µs   |
| STOP Condition Setup Time                     | t_SU:STO |                | 9.4  | —    | —    | µs   |
| Data Hold Time                                | t_HD:DAT |                | 2753 | —    | —    | ns   |
| Data Setup Time                               | t_SU:DAT |                | 3003 | —    | —    | ns   |
| Detect Clock Low Timeout                       | t_TIMEOUT|                | 25   | —    | —    | ms   |
| Clock Low Period                              | t_LOW    |                | 4.7  | —    | —    | µs   |
| Clock High Period                             | t_HIGH   |                | 9.4  | —    | 504  | µs   |

| **Fast Mode (400 kHz Class)**                 |          |                |      |      |      |      |
| I2C Operating Frequency                      | f_I2C    |                | 0    | —    | 2562 | kHz  |
| SMBus Operating Frequency                    | f_SMB    |                | 401  | —    | 2562 | kHz  |
| Bus Free Time Between STOP and START Conditions | t_BUF    |                | 2.6  | —    | —    | µs   |
| Hold Time After (Repeated) START Condition  | t_HD:STA |                | 1.3  | —    | —    | µs   |
| Repeated START Condition Setup Time          | t_SU:STA |                | 2.6  | —    | —    | µs   |
| STOP Condition Setup Time                     | t_SU:STO |                | 2.6  | —    | —    | µs   |
| Data Hold Time                                | t_HD:DAT |                | 2753 | —    | —    | ns   |
| Data Setup Time                               | t_SU:DAT |                | 3003 | —    | —    | ns   |
| Detect Clock Low Timeout                       | t_TIMEOUT|                | 25   | —    | —    | ms   |
| Clock Low Period                              | t_LOW    |                | 1.3  | —    | —    | µs   |
| Clock High Period                             | t_HIGH   |                | 2.6  | —    | 504  | µs   |

---
*Page 35*