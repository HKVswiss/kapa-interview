# Page 28

## Text from PDF

2. ESP-LAUNCHER
# 2. E S P-LA U N C HER

## 2.1. Overview


Espressif provides ESP8266EX development board—ESP-LAUNCHER for quick
confifiguration and further development. The size of the board is 46 mm x 78.5 mm (see
Figure 2-1).































|GND Pin Pin Pin Pin Pin Pin Pin<br>26 25 14 12 13 15 7<br>IO IO IO IO IO IO<br>1 3 2 13 15 0<br>TX0 RX0 TX1 CTS0 RTS0 Mode Chip_En<br>select<br>UART<br>5<br>1<br>Pin 12 IO 13 Reset key 2 9 10<br>6<br>3<br>USB UART Micro USB 11 12<br>4<br>Pin 9 IO 14 CLK 7|Col2|Pin Pin Pin Pin Pin<br>14 12 13 15 7<br>IO IO IO IO<br>2 13 15 0<br>TX1 CTS0 RTS0 Mode Chip_En<br>select<br>UART|GND 3V3|Pin Pin<br>14 9<br>IO IO<br>2 14<br>SDA SCL<br>I2C<br>1<br>22<br>24<br>25|
|---|---|---|---|---|
|GND Pin Pin Pin Pin Pin Pin Pin<br>26 25 14 12 13 15 7<br>IO IO IO IO IO IO<br>1 3 2 13 15 0<br>TX0 RX0 TX1 CTS0 RTS0 Mode Chip_En<br>select<br>UART<br>5<br>1<br>Pin 12 IO 13 Reset key 2 9 10<br>6<br>3<br>USB UART Micro USB 11 12<br>4<br>Pin 9 IO 14 CLK 7|5<br>1<br>2 9 10<br>6<br>3<br>11 12<br>7|5<br>1<br>2 9 10<br>6<br>3<br>11 12<br>7|16 21<br>17<br>23<br>18|16 21<br>17<br>23<br>18|
|Pin 10 IO 12 MISO HSPI 13<br>Pin 12 IO 13 MOSI<br>Pin 13 IO 15 CS<br>4<br>5 V power Micro USB 19<br>14<br>1 8 15 20 24<br>SDIO / SPI PWM IR remote control Relay<br>SD_D1 SD_D0 SD_CLK SD_CMD SD_D3 SD_D2 control Transmittor Detector<br>R G B W<br>7 IO 8 IO 6 IO 11 IO 10 IO 9 IO 15 IO 12 IO 15 IO 14 IO 4 IO 14 IO 5 IO<br>GND 23 Pin 22 Pin 21 Pin 20 Pin 19 Pin 18 Pin 13 Pin V 5 10 Pin 13 Pin 9 Pin 16 Pin GND 9 Pin 24 Pin|Pin 10 IO 12 MISO HSPI 13<br>Pin 12 IO 13 MOSI<br>Pin 13 IO 15 CS<br>4<br>5 V power Micro USB 19<br>14<br>1 8 15 20 24<br>SDIO / SPI PWM IR remote control Relay<br>SD_D1 SD_D0 SD_CLK SD_CMD SD_D3 SD_D2 control Transmittor Detector<br>R G B W<br>7 IO 8 IO 6 IO 11 IO 10 IO 9 IO 15 IO 12 IO 15 IO 14 IO 4 IO 14 IO 5 IO<br>GND 23 Pin 22 Pin 21 Pin 20 Pin 19 Pin 18 Pin 13 Pin V 5 10 Pin 13 Pin 9 Pin 16 Pin GND 9 Pin 24 Pin|Pin 10 IO 12 MISO HSPI 13<br>Pin 12 IO 13 MOSI<br>Pin 13 IO 15 CS<br>4<br>5 V power Micro USB 19<br>14<br>1 8 15 20 24<br>SDIO / SPI PWM IR remote control Relay<br>SD_D1 SD_D0 SD_CLK SD_CMD SD_D3 SD_D2 control Transmittor Detector<br>R G B W<br>7 IO 8 IO 6 IO 11 IO 10 IO 9 IO 15 IO 12 IO 15 IO 14 IO 4 IO 14 IO 5 IO<br>GND 23 Pin 22 Pin 21 Pin 20 Pin 19 Pin 18 Pin 13 Pin V 5 10 Pin 13 Pin 9 Pin 16 Pin GND 9 Pin 24 Pin|Pin 10 IO 12 MISO HSPI 13<br>Pin 12 IO 13 MOSI<br>Pin 13 IO 15 CS<br>4<br>5 V power Micro USB 19<br>14<br>1 8 15 20 24<br>SDIO / SPI PWM IR remote control Relay<br>SD_D1 SD_D0 SD_CLK SD_CMD SD_D3 SD_D2 control Transmittor Detector<br>R G B W<br>7 IO 8 IO 6 IO 11 IO 10 IO 9 IO 15 IO 12 IO 15 IO 14 IO 4 IO 14 IO 5 IO<br>GND 23 Pin 22 Pin 21 Pin 20 Pin 19 Pin 18 Pin 13 Pin V 5 10 Pin 13 Pin 9 Pin 16 Pin GND 9 Pin 24 Pin|ADC_IN TOUT Pin 6<br>26<br>Deep sleep XPD-DCDC IO 16 Pin 8<br>wake up EXT_RSTB Pin 32<br>1|


Figure 2-1. ESP-LAUNCHER development board layout

1 Chip positioning hole 8 5V power switch 15 Relay control 22 Undefifined LED and buttons

2 Reset Button 9 IO0 control 16 SMA ANT 23 1.27 mm pin header

3 Wi-Fi LED, Link LED 10 CH_EN switch 17 Test board 24 2.0 mm pin header

Micro USB: USB-UART, 5V
4 11 Flash2: HSPI 18 Flash1: SPI 25 ADC_IN
power

5 UART 12 CS of Flash2 19 SDIO/SPI 26 Deep-sleep wakeup

6 UART SWAP 13 HSPI 20 IR_T, IR_R

7 USB-UART chip 14 3.3 V power 21 I2C
## 2.2. Modules and Interfaces


ESP-LAUNCHER can be confifigured and tested through USB serial or Wi-Fi connection.
The modules/interfaces integrated on the development board are described in Table 2-1.


Espressif


23/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



## OCR Text

2. ESP-LAUNCHER

2.

ESP-LAUNCHER

2.1.

Overview

Espressif provides ESP8266EX development board —ESP-LAUNCHER for quick

configuration and further development. The size of the board is 46 mm x 78.5 mm (see

Figure 2-1).

HE:

3

—

iL

f

iI

(o)

YQ

3

re)

of RET

©

Pan

oa

A

2

olexe

Sp

ole »

(0)

(su |

Ls

Es

oles &

va

Sl

Bio

ow) KE

1012 EMSS

5

:

Pa

Pan

101 -SMOsL

IBBRH GAG,

:

=

mas

0%) Sm

= ant

SSOOOSOOS0OD

mene (1016

om

[s¥eoe

cB,

CELEEEE »

PAT

©

sk

:

© GEEEEE"

:

TT

UL

a

g

a

j “ i

—

5

Figure 2-1. ESP-LAUNCHER development board layout

Chip positioning hole

8 5V power switch

15 Relay control

22 Undefined LED and buttons

Reset Button

9 100 control

16 SMA ANT

23 1.27 mm pin header

Wi-Fi LED, Link LED

40 CH_EN switch

17 Test board

24 2.0 mm pin header

Micro USB: USB-UART, 5V

41. Flash2: HSPI

18 Flasht: SPI

power

25 ADC_IN

UART

42 CS of Flash2

19 SDIO/SPI

26 Deep-sleep wakeup

UART SWAP

43 HSPI

20 IRT,IR_R

USB-UART chip

14 3.3 V power

21 2c

2.2. Modules and Interfaces

ESP-LAUNCHER can be configured and tested through USB serial or Wi-Fi connection.

The modules/interfaces integrated on the development board are described in Table 2-1.

23/32

Espressif

Submit Documentation Feedback

2024.10

## Tables

2. ESP-LAUNCHER
2. ESP-LAUNCHER
2.1. Overview
Espressif provides ESP8266EX development board —ESP-LAUNCHER for quick
configuration and further development. The size of the board is 46 mm x 78.5 mm (see
Figure 2-1).
HE:
3
—
iL
f iI
(o)
YQ
3
re)
of RET ©
Pan oa
A
2 olexe
Sp ole »
(0)
(su |
Ls
Es
oles &
va Sl
Bio
ow) KE
1012 EMSS
5
:
Pa
Pan
101 -SMOsL IBBRH GAG,
:
= mas
0%) Sm = ant
SSOOOSOOS0OD
mene (1016 om
[s¥eoe
cB,
CELEEEE » PAT
© sk
:
© GEEEEE"
:
TT UL
a g a
j “
i
—
5
Figure 2-1. ESP-LAUNCHER development board layout
Chip positioning hole 8 5V power switch 15 Relay control 22 Undefined LED and buttons
Reset Button 9 100 control 16 SMA ANT 23 1.27 mm pin header
Wi-Fi LED, Link LED 40 CH_EN switch 17 Test board 24 2.0 mm pin header
Micro USB: USB-UART, 5V 41. Flash2: HSPI 18 Flasht: SPI power 25 ADC_IN
UART 42 CS of Flash2 19 SDIO/SPI 26 Deep-sleep wakeup
UART SWAP 43 HSPI 20 IRT,IR_R
USB-UART chip 14 3.3 V power 21 2c
2.2. Modules and Interfaces
ESP-LAUNCHER can be configured and tested through USB serial or Wi-Fi connection.
The modules/interfaces integrated on the development board are described in Table 2-1.
23/32
Espressif Submit Documentation Feedback 2024.10


---

