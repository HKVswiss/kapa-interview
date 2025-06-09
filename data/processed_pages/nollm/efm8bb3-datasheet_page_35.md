# Page 36

## Text from PDF

EFM8BB3 Data Sheet
Electrical Specifications

|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|Note:<br>1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.<br>2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-<br>cations.<br>3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and<br>hold times.<br>4. SMBus has a maximum requirement of 50 µs for Clock High Period. Operating frequencies lower than 40 kHz will be longer than<br>50 µs. I2C can support periods longer than 50 µs.|



**Table 4.18. SMBus Peripheral Timing Formulas (Master Mode)**

|Parameter|Symbol|Clocks|
|---|---|---|
|SMBus Operating Frequency|f<br>SMB|f / 3<br>CSO|
|Bus Free Time Between STOP and START Conditions|t<br>BUF|2 / f<br>CSO|
|Hold Time After (Repeated) START Condition|t<br>HD:STA|1 / f<br>CSO|
|Repeated START Condition Setup Time|t<br>SU:STA|2 / f<br>CSO|
|STOP Condition Setup Time|t<br>SU:STO|2 / f<br>CSO|
|Clock Low Period|t<br>LOW|1 / f<br>CSO|
|Clock High Period|t<br>HIGH|2 / f<br>CSO|
|Note:<br>1. f is the SMBus peripheral clock source overflow frequency.<br>CSO|Note:<br>1. f is the SMBus peripheral clock source overflow frequency.<br>CSO|Note:<br>1. f is the SMBus peripheral clock source overflow frequency.<br>CSO|



V IH

SCL

V IL




SDA


V IH

V IL


|Col1|Col2|Col3|Col4|Col5|tLOW|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT||||||||||
|tHIGH<br>tHD:STA tHD:DAT tSU:STA tSU:STO<br>tSU:DAT||||||||||||||
|||||||||||||||
||tBUF|||||||||||||


P S S P

**Figure 4.1. SMBus Peripheral Timing Diagram (Master Mode)**

**silabs.com** | Building a more connected world. Rev. 1.5 | 36



## OCR Text

EFM8BB3 Data Sheet

Electrical Specifications

Parameter

Test Condition

Min

Max

Uni

sy

Typ

Note:

1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.

2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-

cations.

3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and

hold times.

4. SMBus has a maximum requirement of 50 us for Clock High Period. Operating frequencies lower than 40 kHz will be longer than

50 ys. I2C can support periods longer than 50 us.

Table 4.18. SMBus Peripheral Timing Formulas (Master Mode)

Parameter

Symbol

Clocks

SMBus Operating Frequency

fsme

foso/3

Bus Free Time Between STOP and START Conditions

tur

2/fcso

Hold Time After (Repeated) START Condition

tup:sTA

11 fceso.

Repeated START Condition Setup Time

tsu:sTA

2/fcso

STOP Condition Setup Time

tsu:sTo

2/fcso

Clock Low Period

tlow

11 fceso.

tHIGH

2/ fcso

Clock High Period

Note:

1. fcgo is the SMBus peripheral clock source overflow frequency.

Vin

—

a-----

ToaL-----

3

a------

TToaso| ------------[-7---------———

SCL

Vu

‘tac

bios

‘tio.

J

tous

tsusr

tsuoar

Vin

_-[-—

=

——

a

fe

——_

_----——

SDA

Vu

~-/L---

=

a-----

a---------

| |

---------

_--- 3.

tour

Figure 4.1. SMBus Peripheral Timing Diagram (Master Mode)

silabs.com | Building a more connected world.

Rev. 1.5 | 36

## Tables

EFM8BB3 Data Sheet
Electrical Specifications
Parameter Test Condition Min Max Uni sy Typ
Note:
1. The minimum SMBus frequency is limited by the maximum Clock High Period requirement of the SMBus specification.
2. The maximum I2C and SMBus frequencies are limited by the minimum Clock Low Period requirements of their respective specifi-
cations.
3. Data setup and hold timing at 40 MHz or lower with EXTHOLD set to 1. The DLYEXT bit can be used to adjust the data setup and
hold times.
4. SMBus has a maximum requirement of 50 us for Clock High Period. Operating frequencies lower than 40 kHz will be longer than
50 ys. I2C can support periods longer than 50 us.
Table 4.18. SMBus Peripheral Timing Formulas (Master Mode)
Parameter Symbol Clocks
SMBus Operating Frequency fsme foso/3
Bus Free Time Between STOP and START Conditions tur 2/fcso
Hold Time After (Repeated) START Condition tup:sTA 11 fceso.
Repeated START Condition Setup Time tsu:sTA 2/fcso
STOP Condition Setup Time tsu:sTo 2/fcso
Clock Low Period tlow 11 fceso.
tHIGH 2/ fcso Clock High Period
Note:
1. fcgo is the SMBus peripheral clock source overflow frequency.
Vin — a----- ToaL----- 3 a------ TToaso| ------------[-7---------———
SCL
Vu
‘tac bios ‘tio.
J
tous tsusr tsuoar
Vin _-[-— = —— a fe ——_ _----——
SDA
Vu ~-/L--- = a----- a--------- |
|
--------- _--- 3.
tour
Figure 4.1. SMBus Peripheral Timing Diagram (Master Mode)
silabs.com | Building a more connected world. Rev. 1.5 | 36


---

