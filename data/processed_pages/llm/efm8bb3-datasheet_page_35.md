# EFM8BB3 Data Sheet - Electrical Specifications

## Notes
1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.
2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifications.
3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and hold times.
4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than 50 µs. I2C can support periods longer than 50 µs.

## Table 4.18. SMBus Peripheral Timing Formulas (Master Mode)

| Parameter                                   | Symbol  | Clocks   |
|---------------------------------------------|---------|----------|
| SMBus Operating Frequency                    | f_SMB   | f_CSO / 3|
| Bus Free Time Between STOP and START Conditions | t_BUF   | 2 / f_CSO|
| Hold Time After (Repeated) START Condition  | t_HD:STA | 1 / f_CSO|
| Repeated START Condition Setup Time          | t_SU:STA | 2 / f_CSO|
| STOP Condition Setup Time                     | t_SU:STO | 2 / f_CSO|
| Clock Low Period                              | t_LOW   | 1 / f_CSO|
| Clock High Period                             | t_HIGH  | 2 / f_CSO|

**Note:**
- f_CSO is the SMBus peripheral clock source overflow frequency.

## Figure 4.1. SMBus Peripheral Timing Diagram (Master Mode)

The timing diagram illustrates the relationship between signals SCL and SDA with respect to the timing parameters defined above, including t_HIGH, t_LOW, t_HD:STA, t_SU:STA, t_SU:STO, t_BUF, and others.

---
*Page 36*