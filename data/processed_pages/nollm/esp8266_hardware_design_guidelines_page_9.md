# Page 10

## Text from PDF

1. ESP8266EX

*Note:*

*GPIO2, GPIO0, and MTDO are confifigurable on PCB as the 3-bit strapping register that determines the*
*booting mode and the SDIO timing mode.*
# 1.4. Schematic Checklist


The highly-integrated design of ESP8266EX reduces the number of components required.
Besides ESP8266EX, less than 10 resistors and capacitors, one crystal oscillator and one
SPI flflash are needed to make a complete module with wireless communication capability.

The following is a detailed description of ESP8266EX schematics, and the layout design
which ensures optimum functionality.

The complete circuit diagram of ESP8266EX is illustrated in Figure 1-3.


Espressif


5/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



## OCR Text

1. ESP8266EX

AP

24

GPIOS

vO

GPIO5

25

UORXD

vO

UART Rx during flash programming; GPIO 3

26

UOTXD

vO

UART Tx during flash progamming; GPIO 1; SPILCS1

27

vO

Connects to crystal oscillator output, can be used to provide BT

XTAL_OUT

clock input

28

XTAL_IN

vO

Connects to crystal oscillator input

29

VDDD

Analog Power 2.5 V ~ 3.6 V

30

VDDA

Analog Power 2.5 V ~ 3.6 V

31

RES12K

Serial connection with a 12 kQ resistor and connect to the ground

32

EXT_RSTB

External reset signal (Low voltage level: Active)

LU Note:

GPIO2, GPIOO, and MTDO are configurable on PCB as the 3-bit strapping register that determines the

booting mode and the SDIO timing mode.

1.4. Schematic Checklist

The highly-integrated design of ESP8266EX reduces the number of components required.

Besides ESP8266Ex, less than 10 resistors and capacitors, one crystal oscillator and one

SPI flash are needed to make a complete module with wireless communication capability.

The following is a detailed description of ESP8266EX schematics, and the layout design

which ensures optimum functionality.

The complete circuit diagram of ESP8266EX is illustrated in Figure 1-3.

5/32

Espressif

Submit Documentation Feedback

2024.10

## Tables

1. ESP8266EX
AP
24 GPIOS vO GPIO5
25 UORXD vO UART Rx during flash programming; GPIO 3
26 UOTXD vO UART Tx during flash progamming; GPIO 1; SPILCS1
27 vO
Connects to crystal oscillator output, can be used to provide BT
XTAL_OUT
clock input
28 XTAL_IN vO Connects to crystal oscillator input
29 VDDD Analog Power 2.5 V ~ 3.6 V
30 VDDA Analog Power 2.5 V ~ 3.6 V
31 RES12K Serial connection with a 12 kQ resistor and connect to the ground
32 EXT_RSTB External reset signal (Low voltage level: Active)
LU Note:
GPIO2, GPIOO, and MTDO are configurable on PCB as the 3-bit strapping register that determines the
booting mode and the SDIO timing mode.
1.4. Schematic Checklist
The highly-integrated design of ESP8266EX reduces the number of components required.
Besides ESP8266Ex, less than 10 resistors and capacitors, one crystal oscillator and one
SPI flash are needed to make a complete module with wireless communication capability.
The following is a detailed description of ESP8266EX schematics, and the layout design
which ensures optimum functionality.
The complete circuit diagram of ESP8266EX is illustrated in Figure 1-3.
5/32
Espressif Submit Documentation Feedback 2024.10


---

