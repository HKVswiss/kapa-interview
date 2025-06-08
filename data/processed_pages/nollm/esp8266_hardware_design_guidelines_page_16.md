1. ESP8266EX


Figure 1-10c. UART Voltage-level Switch circuit



Espressif


When using the AT fifirmware, please note that the UART GPIO is already confifigured (refer to
*[Hardware Connection](https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp8266/Get_Started/Hardware_connection.html)* ). It is recommended to use the default confifiguration.

12/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



1. ESP8266EX

5v0

3v3

3v3

Rt

R2

R3

10K

10K

40K

MCU_TXD

ngs

GPIO13_RX

MCU_RXD

GPIO1S_TX

at

GPIOS

Ra

RS

Ré

RT

10K

100K

10K

10K

33

GND

Figure 1-10c. UART Voltage-level Switch circuit

!

Notice:

When using GPIO13 and GPIO15 as serial communications, please pay attention to the direction of sending

and receiving information, and they need to be connected correctively to MCU UART pins.

When using the AT firmware, please note that the UART GPIO is already configured (refer to

Hardware Connection). It is recommended to use the default configuration.

12/32

Espressif

Submit Documentation Feedback

2024.10

1. ESP8266EX
5v0 3v3 3v3
Rt R2 R3
10K 10K 40K
MCU_TXD ngs GPIO13_RX
MCU_RXD GPIO1S_TX
at
GPIOS
Ra RS Ré RT
10K 100K 10K 10K
33
GND
Figure 1-10c. UART Voltage-level Switch circuit
! Notice:
When using GPIO13 and GPIO15 as serial communications, please pay attention to the direction of sending
and receiving information, and they need to be connected correctively to MCU UART pins.
When using the AT firmware, please note that the UART GPIO is already configured (refer to
Hardware Connection). It is recommended to use the default configuration.
12/32
Espressif Submit Documentation Feedback 2024.10


---Page 17 

