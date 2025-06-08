1. ESP8266EX

Note:

*•*
*Please refer to the design of ESP-WROOM-S2 for further details.*

*•*
*UART Download Mode: Jumper J1 short circuit.*

*•*
*SDIO Boot Mode: Jumper J1 open circuit.*

*•* *If the external host CPU's SDIO or SPI interface has been pulled up, the optional pull-up resistor can*

*be omitted.*
# 1.6. PCB Layout Design


The chapter introduces the ESP8266EX PCB layout design by using the ESP8266EX as an
example. The PCB layout design guidelines are applicable to cases when

         the ESP8266EX module functions as a standalone device, and when

         the ESP8266EX functions as a salve device.

Figure 1-12. ESP8266EX PCB Layout

1.6.1. General Principles of PCB Layout Design

The PCB has four layers:

         The fifirst layer is the TOP layer for signal lines and components.

         - The second layer is the GND layer, where no signal lines are laid to ensure a complete
GND plane.


Espressif


14/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



1. ESP8266EX

LU Note:

Please refer to the design of ESP-WWROOM-S2 for further details.

UART Download Mode: Jumper J1 short circuit.

SDIO Boot Mode: Jumper J1 open circuit.

If the external host CPU's SDIO or SPI interface has been pulled up, the optional pull-up resistor can

be omitted.

1.6. PCB Layout Design

The chapter introduces the ESP8266EX PCB layout design by using the ESP8266EX as an

example. The PCB layout design guidelines are applicable to cases when

.

the ESP8266EX module functions as a standalone device, and when

.

the ESP8266EX functions as a salve device

ad ry

ss HAANTA a

pay

ei

a

a Lécgg

——

R

f

cr

=

(3

C1

c

Ss

|

— =

a)

|

&»

E]

pi]Les

*e

Canes

:

Figure 1-12. ESP8266EX PCB Layout

1.6.1

General Principles of PCB Layout Design

The PCB has four layers:

.

The first layer is the TOP layer for signal lines and components.

.

The second layer is the GND layer, where no signal lines are laid to ensure a complete

GND plane.

14,

2024.10

Espressif

1. ESP8266EX
LU Note:
Please refer to the design of ESP-WWROOM-S2 for further details.
UART Download Mode: Jumper J1 short circuit.
SDIO Boot Mode: Jumper J1 open circuit.
If the external host CPU's SDIO or SPI interface has been pulled up, the optional pull-up resistor can
be omitted.
1.6. PCB Layout Design
The chapter introduces the ESP8266EX PCB layout design by using the ESP8266EX as an
example. The PCB layout design guidelines are applicable to cases when
. the ESP8266EX module functions as a standalone device, and when
. the ESP8266EX functions as a salve device
ad ry
ss HAANTA a
pay
ei a
a Lécgg
——
R f
cr
=
(3
C1
c Ss |
— =
a)
|
&» E] pi]Les
*e
Canes
:
Figure 1-12. ESP8266EX PCB Layout
1.6.1 General Principles of PCB Layout Design
The PCB has four layers:
. The first layer is the TOP layer for signal lines and components.
. The second layer is the GND layer, where no signal lines are laid to ensure a complete
GND plane.
14,
2024.10 Espressif


---Page 19 

