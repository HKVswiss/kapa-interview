EFM8BB3 Data Sheet
Electrical Specifications

**4.1.4 Flash Memory**

**Table 4.4. Flash Memory**







|Parameter|Symbol|Test Condition|Min|Typ|Max|Units|
|---|---|---|---|---|---|---|
|Write Time1,2|t<br>WRITE|One Byte,<br>F = 24.5 MHz<br>SYSCLK|19|20|21|μs|
|Erase Time1,2|t<br>ERASE|One Page,<br>F = 24.5 MHz<br>SYSCLK|5.2|5.35|5.5|ms|
|V Voltage During Programming3<br>DD|V<br>PROG||2.2|—|3.6|V|
|Endurance (Write/Erase Cycles)|N<br>WE||20k|100k|—|Cycles|
|CRC Calculation Time|t<br>CRC|One 256-Byte Block<br>SYSCLK = 49 MHz|—|5.5|—|µs|
|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|Note:<br>1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.<br>2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If<br>user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is<br>recommended to write the HFO0CAL register back to its reset value when writing or erasing flash.<br>3. Flash can be safely programmed at any voltage above the supply monitor threshold (V ).<br>VDDM<br>4. Data Retention Information is published in the Quarterly Quality and Reliability Report.|


**4.1.5 Power Management Timing**

**Table 4.5. Power Management Timing**





|Parameter|Symbol|Test Condition|Min|Typ|Max|Units|
|---|---|---|---|---|---|---|
|Idle Mode Wake-up Time|t<br>IDLEWK||2|—|3|SYSCLKs|
|Suspend Mode Wake-up Time|t<br>SUS-<br>PENDWK|SYSCLK = HFOSC0<br>CLKDIV = 0x00|—|170|—|ns|
|Snooze Mode Wake-up Time|t<br>SLEEPWK|SYSCLK = HFOSC0<br>CLKDIV = 0x00|—|12|—|µs|


**silabs.com** | Building a more connected world. Rev. 1.5 | 23



EFM8BB3 Data Sheet

Electrical Specifications

4.1.4 Flash Memory

Table 4.4. Flash Memory

Parameter

sy

Test Condition

Min

Typ

Max

Uni

Write Timet 2

{write

One Byte,

19

20

21

us

Fsyscik = 24.5 MHz

Erase Time’ 2

teRASE

One Page,

5.2

5.35

5.5

ms

Fsyscik = 24.5 MHz

Vpp Voltage During Programming? | Vproc

2.2

3.6

20k

100k

Endurance (Write/Erase Cycles)

Nwe

Cycles

CRC Calculation Time

tore

One 256-Byte Block

5.5

us

SYSCLK = 49 MHz

Note:

1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.

2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If

user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is

recommended to write the HFOOCAL register back to its reset value when writing or erasing flash.

3. Flash can be safely programmed at any voltage above the supply monitor threshold (Vvppm)-

4. Data Retention Information is published in the Quarterly Quality and Reliability Report.

4.1.5 Power Management Timing

Table 4.5. Power Management Timing

Parameter

Sy!

Test Condition

Typ

Max

Units

SYSCLKs

Idle Mode Wake-up Time

tiDLEwK

Suspend Mode Wake-up Time

tsus-

SYSCLK = HFOSCO

170

ns

PENDWK

CLKDIV = 0x00

Snooze Mode Wake-up Time

tsLEEPWK

SYSCLK = HFOSCO

12

us

CLKDIV = 0x00

silabs.com | Building a more connected world.

Rev. 1.5 | 23

EFM8BB3 Data Sheet
Electrical Specifications
4.1.4 Flash Memory
Table 4.4. Flash Memory
Parameter sy Test Condition Min Typ Max Uni
Write Timet 2 {write One Byte, 19 20 21 us
Fsyscik = 24.5 MHz
Erase Time’ 2 teRASE One Page, 5.2 5.35 5.5 ms
Fsyscik = 24.5 MHz
Vpp Voltage During Programming? | Vproc 2.2 3.6
20k 100k Endurance (Write/Erase Cycles) Nwe Cycles
CRC Calculation Time tore One 256-Byte Block 5.5 us
SYSCLK = 49 MHz
Note:
1. Does not include sequencing time before and after the write/erase operation, which may be multiple SYSCLK cycles.
2. The internal High-Frequency Oscillator 0 has a programmable output frequency, which is factory programmed to 24.5 MHz. If
user firmware adjusts the oscillator speed, it must be between 22 and 25 MHz during any flash write or erase operation. It is
recommended to write the HFOOCAL register back to its reset value when writing or erasing flash.
3. Flash can be safely programmed at any voltage above the supply monitor threshold (Vvppm)-
4. Data Retention Information is published in the Quarterly Quality and Reliability Report.
4.1.5 Power Management Timing
Table 4.5. Power Management Timing
Parameter Sy! Test Condition Typ Max Units
SYSCLKs Idle Mode Wake-up Time tiDLEwK
Suspend Mode Wake-up Time tsus- SYSCLK = HFOSCO 170 ns
PENDWK CLKDIV = 0x00
Snooze Mode Wake-up Time tsLEEPWK SYSCLK = HFOSCO 12 us
CLKDIV = 0x00
silabs.com | Building a more connected world. Rev. 1.5 | 23


---Page 23 

