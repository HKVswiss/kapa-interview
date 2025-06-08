1. ESP8266EX




1.4.1.2. Analog Power Supply

|<br>gur| <br>e 1-||||||Col8|
|---|---|---|---|---|---|---|---|
|<br>gur| <br>e 1-||4.|E|SP|82|66EX Digital Power Supply Pins|


ESP8266EX has fifive analog pins for power supply, including Pin1, Pin3, Pin4 that are the
power supply for internal PA and LNA; and Pin29, Pin30 for the internal PLL. The operating
voltage for analog power supply pins is 2.5 V ~ 3.6 V.

Note that the power supply channel might be damaged due to the sudden increase of
current when ESP8266EX is transmitting analog signals. Therefore, an additional 10 μF
capacitor with a 0603 or 0805 package is needed to match the 0.1 μF capacitor.








|Col1|Col2|Col3|
|---|---|---|
|||$|









|Col1|Col2|Col3|Col4|�� �� �� �� �� ��|
|---|---|---|---|---|
|||||%#&  <br><br>%&<br><br><br>"<br>"<br>ts. There is no need to add ferrite|
||   <br> <br>Figure 1-5. ESP826|   <br> <br>Figure 1-5. ESP826|   <br> <br>Figure 1-5. ESP826|   <br> <br>Figure 1-5. ESP826|
||   <br> <br>Figure 1-5. ESP826|<br>!<br>6EX AVDD|||
||   <br> <br>Figure 1-5. ESP826|<br>!<br>6EX AVDD|||
|📖 Note:<br>• ESP8266EX’s EMC is in conformity with FCC and CE requirements. There is no need to add ferrite<br>beads in the analog power-supply circuit.<br>• When using a single power supply, the recommended output current is 500 mA.<br>• It is suggested that users add an ESD tube at the power entrance.||||ts. There is no need to add ferrite|


Espressif


7/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



1. ESP8266EX

unre

OU_UAIM_é

17

XPD_DCDC.

VDDPST

MID

VDDPST

MTCK

MTDO

GPIO2

GPIOO

GPIO4

ESP8266EX

U2

olole

12

13

14

15

16

VDD33.

Figure 1-4. ESP8266EX Digital Power Supply Pins

1.4.1.2. Analog Power Supply

ESP8266EX has five analog pins for power supply, including Pin1, Pin3, Pin4 that are the

power supply for internal PA and LNA; and Pin29, Pin3O for the internal PLL. The operating

voltage for analog power supply pins is 2.5 V ~ 3.6 V.

Note that the power supply channel might be damaged due to the sudden increase of

current when ESP8266EX is transmitting analog signals. Therefore, an additional 10 LF

capacitor with a 0603 or 0805 package is needed to match the 0.1 UF capacitor.

vDD33

+

--

ond |

ce

6]

8,

=

=

N

41UF]

1uF(NC)

R1

—

—

12K41%

vDD33

GND

GND

ent

fe)

C3]

ford

oot

32

31

30

29

OR

10uF]

0.1uF]

TBD(NC)

GND

VDDA

VDDD

GND

GND

GND

_f

RES12K

EXT_RSTB

ANTI

WIFI_ANT. C4, W~\AA\2.2nH

VDDA

NA

C4

VDD3P3

.

rs

VDD3P3

Figure 1-5. ESP8266EX AVDD

LU Note:

.

ESP8266EX's EMC is in conformity with FCC and CE requirements. There is no need to add ferrite

beads in the analog power-supply circuit.

When using a single power supply, the recommended output current is 500 mA.

It is suggested that users add an ESD tube at the power entrance.

7/32

Espressif

Submit Documentation Feedback

2024.10

1. ESP8266EX
unre OU_UAIM_é 17
XPD_DCDC. VDDPST
MID
VDDPST
MTCK MTDO GPIO2 GPIOO GPIO4
ESP8266EX U2
olole 12 13 14 15 16
VDD33.
Figure 1-4. ESP8266EX Digital Power Supply Pins
1.4.1.2. Analog Power Supply
ESP8266EX has five analog pins for power supply, including Pin1, Pin3, Pin4 that are the
power supply for internal PA and LNA; and Pin29, Pin3O for the internal PLL. The operating
voltage for analog power supply pins is 2.5 V ~ 3.6 V.
Note that the power supply channel might be damaged due to the sudden increase of
current when ESP8266EX is transmitting analog signals. Therefore, an additional 10 LF
capacitor with a 0603 or 0805 package is needed to match the 0.1 UF capacitor.
vDD33
+ -- ond |
ce
6]
8,
= = N
41UF] 1uF(NC)
R1
— — 12K41%
vDD33
GND GND
ent
fe) C3] ford
oot
32 31 30 29 OR
10uF] 0.1uF] TBD(NC)
GND VDDA VDDD
GND GND GND _f
RES12K EXT_RSTB
ANTI
WIFI_ANT. C4, W~\AA\2.2nH VDDA
NA
C4 VDD3P3
. rs VDD3P3
Figure 1-5. ESP8266EX AVDD
LU Note:
. ESP8266EX's EMC is in conformity with FCC and CE requirements. There is no need to add ferrite
beads in the analog power-supply circuit.
When using a single power supply, the recommended output current is 500 mA.
It is suggested that users add an ESD tube at the power entrance.
7/32
Espressif Submit Documentation Feedback 2024.10


---Page 12 

