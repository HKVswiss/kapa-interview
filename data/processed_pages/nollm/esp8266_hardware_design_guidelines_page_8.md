1. ESP8266EX


Table 1-2. ESP8266EX Pin Defifinitions







Espressif


4/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



1. ESP8266EX

Table 1-2. ESP8266EX Pin Definitions

a

1

VDDA

p

Analog Power 2.5 V ~ 3.6 V

RF antenna interface

LNA

vO

Chip output impedance = 39 + j6 Q. It is suggested that users

retain the mt-type matching network which matches the antenna.

VDD3P3

Amplifier Power 2.5 V ~ 3.6 V

VDD3P3

Amplifier Power 2.5 V ~ 3.6 V

VDD_RTC.

NC (1.1. V)

ADC pin. It can be used to test the power-supply voltage of

TOUT

VDD3P3 (Pin3 and Pin4) and the input power voltage of TOUT (Pin

}). However, these two functions cannot be used simultaneously.

Chip Enable

CHIP_EN

High: On, chip works properly

Low: Off, small current consumed

XPD_DCDC

vO

Deep-sleep wakeup (need to be connected to EXT_RSTB);

GPIO16

MTMS

vO

GPIO 14; HSPI_CLK

10

MTDI

vO

GPIO 12; HSPI_MISO

an]

VDDPST

Digital/iO Power Supply (1.8 V ~ 3.3 V)

12

MTCK

vO

GPIO 13; HSPI_MOSI; UARTO_CTS

13

MTDO

vO

GPIO 15; HSPI_CS; UARTO_RTS

14

GPIO2

vO

UART1_TX during flash programming; GPIO2

15

GPIOO

vO

GPIOO; SPI_CS2

16

GPIO4

vO

GPIO 4

17

VDDPST

Digital/iO Power Supply (1.8V ~ 3.3V)

18

SDIO_DATA_2

vO

Connects to SD_D2 (Series R: 200 Q); SPIHD; HSPIHD; GPIO 9

19

SDIO_DATA_3

vO

Connects to SD_D3 (Series R: 200 Q); SPIWP; HSPIWP; GPIO 10

20

SDIO_CMD

vO

Connects to SD_CMD (Series R: 200 ©); SPI_CSO; GPIO 11

a1

SDIO_CLK

vO

Connects to SD_CLK (Series R: 200 ©); SPILCLK; GPIO 6

22

SDIO_DATA_O

vO

Connects to SD_DO (Series R: 200 ©); SPI_MSIO; GPIO 7

23

SDIO_DATA_1

vO

Connects to SD_D1 (Series R: 200 ); SPI_LMOSI; GPIO 8

4/32

Espressif

Submit Documentation Feedback

2024.10

1. ESP8266EX
Table 1-2. ESP8266EX Pin Definitions
a
1 VDDA p Analog Power 2.5 V ~ 3.6 V
RF antenna interface
LNA vO Chip output impedance = 39 + j6 Q. It is suggested that users
retain the mt-type matching network which matches the antenna.
VDD3P3 Amplifier Power 2.5 V ~ 3.6 V
VDD3P3 Amplifier Power 2.5 V ~ 3.6 V
VDD_RTC. NC (1.1. V)
ADC pin. It can be used to test the power-supply voltage of
TOUT VDD3P3 (Pin3 and Pin4) and the input power voltage of TOUT (Pin
}). However, these two functions cannot be used simultaneously.
Chip Enable
CHIP_EN High: On, chip works properly
Low: Off, small current consumed
XPD_DCDC vO
Deep-sleep wakeup (need to be connected to EXT_RSTB);
GPIO16
MTMS vO GPIO 14; HSPI_CLK
10 MTDI vO GPIO 12; HSPI_MISO
an] VDDPST Digital/iO Power Supply (1.8 V ~ 3.3 V)
12 MTCK vO GPIO 13; HSPI_MOSI; UARTO_CTS
13 MTDO vO GPIO 15; HSPI_CS; UARTO_RTS
14 GPIO2 vO UART1_TX during flash programming; GPIO2
15 GPIOO vO GPIOO; SPI_CS2
16 GPIO4 vO GPIO 4
17 VDDPST Digital/iO Power Supply (1.8V ~ 3.3V)
18 SDIO_DATA_2 vO Connects to SD_D2 (Series R: 200 Q); SPIHD; HSPIHD; GPIO 9
19 SDIO_DATA_3 vO Connects to SD_D3 (Series R: 200 Q); SPIWP; HSPIWP; GPIO 10
20 SDIO_CMD vO Connects to SD_CMD (Series R: 200 ©); SPI_CSO; GPIO 11
a1 SDIO_CLK vO Connects to SD_CLK (Series R: 200 ©); SPILCLK; GPIO 6
22 SDIO_DATA_O vO Connects to SD_DO (Series R: 200 ©); SPI_MSIO; GPIO 7
23 SDIO_DATA_1 vO Connects to SD_D1 (Series R: 200 ); SPI_LMOSI; GPIO 8
4/32
Espressif Submit Documentation Feedback 2024.10


---Page 9 

