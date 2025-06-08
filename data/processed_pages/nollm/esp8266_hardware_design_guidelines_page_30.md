2. ESP-LAUNCHER

4. Remove R58 on the PCB and disconnect GPIO14 with the infrared transmitting tube;

5. Remove the pull-down resistor R29 of MTDO/IO15 (next to J11);

6. When downloading fifirmware, pull the IO15/CS at J11 to low level and toggle the

switch of GPIO0 inwards to enable UART Download mode;

7. When downloading is completed, release IO15/CS to enable SDIO Boot mode;

8. Connect SDIO/SPI at J5 to host for communication.
# 2.3. Schematics


2.3.1. Interfaces

























||Col2|Col3|
|---|---|---|
||||
|'<br>|'<br>|'<br>|

|Col1|Col2|Col3|� ��|
|---|---|---|---|
|||||
|||| (|
|||| |
|9|||)<br>9|










































Figure 2-2. ESP-LAUNCHER Interface

26/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10




Espressif



2. ESP-LAUNCHER

Remove R68 on the PCB and disconnect GPIO14 with the infrared transmitting tube;

Remove the pull-down resistor R29 of MTDO/IO15 (next to J11);

When downloading firmware, pull the 1O15/CS at J11 to low level and toggle the

switch of GPIOO inwards to enable UART Download mode;

When downloading is completed, release |015/CS to enable SDIO Boot mode;

Connect SDIO/SPI at J5 to host for communication.

2.3. Schematics

2.3.1

Interfaces

veus

GND vBUS

GND

GND

D+

D.

TONS

:

GND

Ne

ose

we

GND

us

Micro USB

EXT sv

20

vecio

TxD

>yrxo

GND vBUS

OR

BRAM

DM

16.

es

RXD

RXD

:

GND

GND

D+

3

OR.

DP.

15:

usBDP

USBDM

cTs#

RTs# Fy

SSRTs

Kors

One| GND

Ne

aT

> -2—+

ko

79

DIRE

1071

24

Debit

DSR#

10,

vops3

5V&USB-UART

his

28

27

‘osel

FT232RL

Rie

a

cn

‘enpeno [A

‘Osco

9 REELED

GND

R54

23

7X LED AR

oR

cusa1

cusso } 33

13

FOXCLED

UoRTS,

7

cuss2 1

Dit

3v30U"

cuss4

cuss 3

4

AN

Kors i=

BLUE LED

uF

32998

SAAS

GND

aI

vorxi

aaa

uoTxo >

K RxD

woRXt

GND

UORXO >)

>yTxo

DUE

14

CoN2

SAA

Js]

uooTs

pars

P1013

luocts.

1.Normal:use R1 R3 R5 R7

87

CON2

2. Swap: use R2 R4 R6 R8&

sy

(for cancelling log print when power on )

GPIO1S

UORTS.

3.Flow control: short J14 and J67

69

Cons

eno

‘vorxD

ol]

ORD

UART

‘OTS

ojo

WORTS

Figure 2-2. ESP-LAUNCHER Interface

26/32

Espressif

Submit Documentation Feedback

2024.10

2. ESP-LAUNCHER
Remove R68 on the PCB and disconnect GPIO14 with the infrared transmitting tube;
Remove the pull-down resistor R29 of MTDO/IO15 (next to J11);
When downloading firmware, pull the 1O15/CS at J11 to low level and toggle the
switch of GPIOO inwards to enable UART Download mode;
When downloading is completed, release |015/CS to enable SDIO Boot mode;
Connect SDIO/SPI at J5 to host for communication.
2.3. Schematics
2.3.1 Interfaces
veus GND vBUS
GND
GND
D+
D.
TONS
:
GND Ne
ose
we GND us
Micro USB
EXT
sv
20 vecio TxD >yrxo
GND vBUS OR
BRAM
DM 16. es RXD RXD :
GND
GND
D+
3
OR. DP. 15: usBDP
USBDM
cTs#
RTs# Fy SSRTs
Kors
One| GND Ne
aT > -2—+
ko
79 DIRE
1071 24 Debit
DSR# 10, vops3
5V&USB-UART
his
28
27 ‘osel FT232RL Rie a
cn ‘enpeno [A ‘Osco 9
REELED
GND R54 23 7X LED AR
oR cusa1
cusso
}
33
13
FOXCLED
UoRTS, 7 cuss2 1 Dit 3v30U"
cuss4
cuss 3 4
AN
Kors i=
BLUE LED
uF
32998
SAAS
GND
aI
vorxi
aaa
uoTxo > K RxD
woRXt GND UORXO >) >yTxo
DUE 14
CoN2
SAA
Js] uooTs pars P1013 luocts.
1.Normal:use R1 R3 R5 R7 87
CON2
2. Swap: use R2 R4 R6 R8&
sy (for cancelling log print when power on )
GPIO1S UORTS.
3.Flow control: short J14 and J67
69
Cons
eno
‘vorxD ol]
ORD UART
‘OTS ojo
WORTS
Figure 2-2. ESP-LAUNCHER Interface
26/32
Espressif Submit Documentation Feedback 2024.10


---Page 31 

