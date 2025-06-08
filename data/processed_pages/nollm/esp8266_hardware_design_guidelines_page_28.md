2. ESP-LAUNCHER


Table 2-1. ESP-LAUNCHER Module Description












24/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10


Espressif



2. ESP-LAUNCHER

Table 2-1. ESP-LAUNCHER Module Description

a

Micro USB

There are two USB interfaces. Both can be used as a 5 V power supply or for serial

interface

communication (2-1-4).

The USB interface provides 5 V power supply which can be converted to 3.3 V through a

Power supply

DC-to-DC converter. An LED light indicates the power, and a header pin is used for testing

the power current.

Three slide switches are used for the 5 V power supply (2-1-8), GPIOO voltage level switch

(2-1-9) and chip enable pin CH_EN (2-1-10), respectively. When the switches are toggled to

the outer side, the voltage level is high, while when the switches are toggled to the inner

side, the voltage level is low.

.

For the 5 V power switcl

Slide switch

- Toggled to the inner side, the board is powered on;

- Toggled to the outer side, the board is powered off.

For the GPIOO Control

- Toggle to the inner side, the UART download mode is enabled and users can

download firmware with ESP Flash Download Tool;

- Toggle to the outer side, the Flash boot mode is enabled and the UART debug tool

can be used for debugging.

Reset Key

SW1 is connected to MTCK (GPIO13) for application reset and clearing the Wi-Fi

configuration (2-1-2). SW2 is not defined (2-1-22).

.

Red light (D2) indicates Wi-Fi work status (2-1-3).

.

Blue (D3) indicates communication with server (2-1-3)

Green light (D1) indicates relay switch control (2-1-15)

Indicator light

Blue light (011) and red light (D10) indicate Rx and Tx work status, respectively (2-1-7)

Red light (D12) indicates a 5 V power supply (2-1-8)

D4/13/14/16 are not defined (2-1-22).

J82: It needs to be shorted by a jumper, so that the 3.3 V power supply can be

channeled into other circuits. It can also be used to test the power current (2-1-14).

J3: CS of HSPI flash. HSPI flash is disabled when the two upper pins are shorted by a

jumper. HSPI flash is enabled when the two lower pins are shorted by a jumper (2-1-12).

Jumper

J14 and J67: Short-circuit J14 to connect GPIO13 to UOCTS. Short-circuit J67 to

connect GPIO15 to UORTS (2-1-6).

J77: Short-circuit J77 to connect GPIO16 to EXT_RSTB for Deep-sleep wake up.

(2-1-26)

Interfaces

UART, HSPI, SDIO/SPI, 12C, ADC_IN, GPIO16, relay control, PWM and IR TX/RX

.

16-Mbit Flash1 (mounted on the test board): Flash1 is connected to the chip via the SPI

interface. Currently, Flash1 is used when the chip is working in the Wi-Fi standalone

mode. RQ and R85 can be used for the CS of Flash1. By default, Flash1 is enabled

(2-1-18)

Flash

32-Mbit Flash2 (mounted on the baseboard): Flash2 is connected to the chip via the

HSPI interface. HSPI is used in SIP mode. For the ESP-LAUNCHER, when ESP8266EX

works as a slave device, it connects to the host MCU via the SPI interface that is defined

in SDIO specifications. HSPI is connected to Flash2. J3 can be used for the CS of

Flash2 (2-1-11).

24/32

Espressif

Submit Documentation Feedback

2024.10

2. ESP-LAUNCHER
Table 2-1. ESP-LAUNCHER Module Description
a
Micro USB There are two USB interfaces. Both can be used as a 5 V power supply or for serial
interface communication (2-1-4).
The USB interface provides 5 V power supply which can be converted to 3.3 V through a
Power supply DC-to-DC converter. An LED light indicates the power, and a header pin is used for testing
the power current.
Three slide switches are used for the 5 V power supply (2-1-8), GPIOO voltage level switch
(2-1-9) and chip enable pin CH_EN (2-1-10), respectively. When the switches are toggled to
the outer side, the voltage level is high, while when the switches are toggled to the inner
side, the voltage level is low.
. For the 5 V power switcl
Slide switch
- Toggled to the inner side, the board is powered on;
- Toggled to the outer side, the board is powered off.
For the GPIOO Control
- Toggle to the inner side, the UART download mode is enabled and users can
download firmware with ESP Flash Download Tool;
- Toggle to the outer side, the Flash boot mode is enabled and the UART debug tool
can be used for debugging.
Reset Key
SW1 is connected to MTCK (GPIO13) for application reset and clearing the Wi-Fi
configuration (2-1-2). SW2 is not defined (2-1-22).
. Red light (D2) indicates Wi-Fi work status (2-1-3).
. Blue (D3) indicates communication with server (2-1-3)
Green light (D1) indicates relay switch control (2-1-15)
Indicator light
Blue light (011) and red light (D10) indicate Rx and Tx work status, respectively (2-1-7)
Red light (D12) indicates a 5 V power supply (2-1-8)
D4/13/14/16 are not defined (2-1-22).
J82: It needs to be shorted by a jumper, so that the 3.3 V power supply can be
channeled into other circuits. It can also be used to test the power current (2-1-14).
J3: CS of HSPI flash. HSPI flash is disabled when the two upper pins are shorted by a
jumper. HSPI flash is enabled when the two lower pins are shorted by a jumper (2-1-12).
Jumper
J14 and J67: Short-circuit J14 to connect GPIO13 to UOCTS. Short-circuit J67 to
connect GPIO15 to UORTS (2-1-6).
J77: Short-circuit J77 to connect GPIO16 to EXT_RSTB for Deep-sleep wake up.
(2-1-26)
Interfaces UART, HSPI, SDIO/SPI, 12C, ADC_IN, GPIO16, relay control, PWM and IR TX/RX
. 16-Mbit Flash1 (mounted on the test board): Flash1 is connected to the chip via the SPI
interface. Currently, Flash1 is used when the chip is working in the Wi-Fi standalone
mode. RQ and R85 can be used for the CS of Flash1. By default, Flash1 is enabled
(2-1-18)
Flash 32-Mbit Flash2 (mounted on the baseboard): Flash2 is connected to the chip via the
HSPI interface. HSPI is used in SIP mode. For the ESP-LAUNCHER, when ESP8266EX
works as a slave device, it connects to the host MCU via the SPI interface that is defined
in SDIO specifications. HSPI is connected to Flash2. J3 can be used for the CS of
Flash2 (2-1-11).
24/32
Espressif Submit Documentation Feedback 2024.10


---Page 29 

