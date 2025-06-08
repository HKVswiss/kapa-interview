1. ESP8266EX



| <br>   <br>   <br> <br>  <br>   <br>   <br> |  |
|---|---|
| <br>   <br>   <br> <br>  <br>   <br>   <br> | |
| <br>   <br>   <br> <br>  <br>   <br>   <br> | |
| <br>   <br>   <br> <br>  <br>   <br>   <br> |    <br> |
| <br>   <br>   <br> <br>  <br>   <br>   <br> |  |
| <br>   <br>   <br> <br>  <br>   <br>   <br> | |


1.4.4. Crystal Oscillator









Figure 1-6. ESP8266EX Flash


ESP8266EX can support 40 MHz, 26 MHz and 24 MHz crystal oscillators.Please select the
right type of crystal oscillator that is used in the ESP Flash Download Tool. In circuit design,






Espressif


9/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



1. ESP8266EX

VDD33

o

GPIO5

23

24

GPIOS

‘SDISDI

SCS/ICMD

1

5

SDVSD1

SD_DATA_1

22

‘SDOISDO

Ics

8

ol

SD_DATA_0

21

RS

200R

‘SCKICLK

SCKICLK.

6

2

SDO/SDO

‘SD_CLK

20

‘SCS/CMD

cLK

Do

sD_CMD

19

‘SWPISD3

SHD/SD2

z

3

SWPISD3

SD_DATA 3

18

‘SHDISD2

/HOLD 9 WP.

6

SD_DATA_2

VDDPST

17

FLASH J]

U3

aL

—

end

U2

Figure 1-6. ESP8266EX Flash

1.4.4. Crystal Oscillator

ESP8266EX can support 40 MHz, 26 MHz and 24 MHz crystal oscillators.Please select the

right type of crystal oscillator that is used in the ESP Flash Download Tool. In circuit design,

capacitors C1 and C2, which are connected to the ground are added to the input and

output terminals of the crystal oscillator respectively. The values of the two capacitors can

be flexible, ranging from 6 pF to 22 pF. However, the specific capacitive values of C1 and

C2 depend on further testing of and adjustment to the overall performance of the whole

circuit. The crystal precision should be +10 PPM.

VDDD

28

XTAL_IN

27

+

XTAL_OUT

26

{eH Ir

g

UOTXD

25

UORXD

XIN

GND

iS

GND XOUT

WOXLN

é

2

F4

Figure 1-7. ESP8266EX Crystal Oscillator

!

Notice:

Defects in the craftsmanship of the crystal oscillators (for example, high frequency deviation and unstable

working temperature) may lead to the malfunction of ESP8266ExX, resulting in the decrease of overall

performance.

9/32

Espressif

Submit Documentation Feedback

2024.10

1. ESP8266EX
VDD33
o
GPIO5 23
24 GPIOS
‘SDISDI SCS/ICMD 1 5 SDVSD1 SD_DATA_1 22 ‘SDOISDO Ics
8
ol
SD_DATA_0 21 RS 200R ‘SCKICLK SCKICLK. 6 2 SDO/SDO ‘SD_CLK 20 ‘SCS/CMD cLK Do
sD_CMD 19 ‘SWPISD3 SHD/SD2 z 3 SWPISD3 SD_DATA 3
18 ‘SHDISD2 /HOLD 9 WP.
6 SD_DATA_2
VDDPST 17
FLASH J] U3
aL — end
U2
Figure 1-6. ESP8266EX Flash
1.4.4. Crystal Oscillator
ESP8266EX can support 40 MHz, 26 MHz and 24 MHz crystal oscillators.Please select the
right type of crystal oscillator that is used in the ESP Flash Download Tool. In circuit design,
capacitors C1 and C2, which are connected to the ground are added to the input and
output terminals of the crystal oscillator respectively. The values of the two capacitors can
be flexible, ranging from 6 pF to 22 pF. However, the specific capacitive values of C1 and
C2 depend on further testing of and adjustment to the overall performance of the whole
circuit. The crystal precision should be +10 PPM.
VDDD 28
XTAL_IN 27 +
XTAL_OUT 26
{eH Ir g
UOTXD 25
UORXD XIN GND
iS
GND XOUT
WOXLN
é
2 F4
Figure 1-7. ESP8266EX Crystal Oscillator
! Notice:
Defects in the craftsmanship of the crystal oscillators (for example, high frequency deviation and unstable
working temperature) may lead to the malfunction of ESP8266ExX, resulting in the decrease of overall
performance.
9/32
Espressif Submit Documentation Feedback 2024.10


---Page 14 

