# Page 21

## Text from PDF

1. ESP8266EX

Note:

*As is shown in Figure 1-13, the recommended position of ESP8266EX module on the base board should be:*

*•*
*Position 3, 4: Highly recommended;*

*•* *Position 1, 2, 5: Not recommended.*

If the positions recommended are not suitable, please make sure that the module is not
covered by any metal shell. The antenna area of the module and the area 15 mm outside
the antenna should be kept clean, (namely no copper, routing, components on it) as shown
in Figure 1-14:




Figure 1-14. Keepout Zone for ESP8266EX Module's Antenna on the Base Board

1.6.3. Standalone ESP8266EX Module

1.6.3.1. Power Supply Design

The 3.3 V power lines are highlighted in yellow in Figure 1-15. The width of the power lines
should be greater than 15 mil.

Before power traces reach the analog power-supply pins (Pin1, 3, 4, 28, 29), a 10 μF
capacitor is required, which can work in conjunction with the 0.1 μF capacitor. A C circuit
and an L circuit should be added to the power supplies of Pin3 and Pin4. As Figure 1-15
shows, C5 (10 μF capacitor) is placed by the 3.3V stamp hole; C7, L3 and C7 are placed
as close as possible to the analog power-supply pin. Note that all decoupling capacitors
should be placed close to the power pin, and ground vias should be added adjacent to the
ground pin for the decoupling capacitors to ensure a short return path.

Power lines should be placed on the third layer. When the power lines reach the pins of the
chipset, vias are needed so that the power lines can go through the layers and connect to
the pins of the chipset on the TOP layer. The diameter of the via holes should exceed the
width of the power lines and the diameter of the drill should be 1.5 times that of the radius
of the vias.


Espressif


16/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



## OCR Text

1. ESP8266EX

LU Note:

As is shown in Figure 1-13, the recommended position of ESP8266EX module on the base board should be:

.

Position 3, 4: Highly recommended;

.

Position 1, 2, 5: Not recommended.

If the positions recommended are not suitable, please make sure that the module is not

covered by any metal shell. The antenna area of the module and the area 15 mm outside

the antenna should be kept clean, (namely no copper, routing, components on it) as shown

in Figure 1-14:

Clearance

15mm

|

15mm,

15mm

Base Board

[=|

Figure 1-14. Keepout Zone for ESP8266EX Module's Antenna on the Base Board

1.6.3. Standalone ESP8266EX Module

1.6.3.1. Power Supply Design

The 3.3 V power lines are highlighted in yellow in Figure 1-15. The width of the power lines

should be greater than 15 mil.

Before power traces reach the analog power-supply pins (Pin1, 3, 4, 28, 29), a 10 UF

capacitor is required, which can work in conjunction with the 0.1 UF capacitor. A C circuit

and an L circuit should be added to the power supplies of Pin3 and Pin4. As Figure 1-15

shows, C5 (10 uF capacitor) is placed by the 3.3V stamp hole; C7, L8 and C7 are placed

as close as possible to the analog power-supply pin. Note that all decoupling capacitors

should be placed close to the power pin, and ground vias should be added adjacent to the

ground pin for the decoupling capacitors to ensure a short return path.

Power lines should be placed on the third layer. When the power lines reach the pins of the

chipset, vias are needed so that the power lines can go through the layers and connect to

the pins of the chipset on the TOP layer. The diameter of the via holes should exceed the

width of the power lines and the diameter of the drill should be 1.5 times that of the radius

of the vias.

16/32

Submit Documentation Feedback

2024.10

Espressif

## Tables

1. ESP8266EX
LU Note:
As is shown in Figure 1-13, the recommended position of ESP8266EX module on the base board should be:
. Position 3, 4: Highly recommended;
. Position 1, 2, 5: Not recommended.
If the positions recommended are not suitable, please make sure that the module is not
covered by any metal shell. The antenna area of the module and the area 15 mm outside
the antenna should be kept clean, (namely no copper, routing, components on it) as shown
in Figure 1-14:
Clearance
15mm
|
15mm,
15mm Base Board
[=|
Figure 1-14. Keepout Zone for ESP8266EX Module's Antenna on the Base Board
1.6.3. Standalone ESP8266EX Module
1.6.3.1. Power Supply Design
The 3.3 V power lines are highlighted in yellow in Figure 1-15. The width of the power lines
should be greater than 15 mil.
Before power traces reach the analog power-supply pins (Pin1, 3, 4, 28, 29), a 10 UF
capacitor is required, which can work in conjunction with the 0.1 UF capacitor. A C circuit
and an L circuit should be added to the power supplies of Pin3 and Pin4. As Figure 1-15
shows, C5 (10 uF capacitor) is placed by the 3.3V stamp hole; C7, L8 and C7 are placed
as close as possible to the analog power-supply pin. Note that all decoupling capacitors
should be placed close to the power pin, and ground vias should be added adjacent to the
ground pin for the decoupling capacitors to ensure a short return path.
Power lines should be placed on the third layer. When the power lines reach the pins of the
chipset, vias are needed so that the power lines can go through the layers and connect to
the pins of the chipset on the TOP layer. The diameter of the via holes should exceed the
width of the power lines and the diameter of the drill should be 1.5 times that of the radius
of the vias.
16/32
Submit Documentation Feedback 2024.10 Espressif


---

