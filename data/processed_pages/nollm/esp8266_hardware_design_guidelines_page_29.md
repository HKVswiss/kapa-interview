# Page 30

## Text from PDF

2. ESP-LAUNCHER





Table 2-2 lists the function description of ESP-LAUNCHER.

Table 2-2: ESP-LAUNCHER interfaces









Espressif


To use the SDIO/SPI interfaces on ESP-LAUNCHER, please follow the steps below:

1. Move the 0R at R85 to R9, and then disable the flflash on the ESP_Test Board;

2. Short-circuit the two lower pins on J3 with a jumper to enable HSPI flflash;

3. Remove C8 (next to the Reset key on the left of the PCB);

25/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



## OCR Text

2. ESP-LAUNCHER

a

There are multiple modules that can be connected to the ESP-LAUNCHER for testing and

development, through the 1.27mm double-row pin headers (2-1-23) and 2.00 mm double-

Test modules

row pin headers (2-1-24).

Please note that module pins should be connected to their corresponding pins on the

board. Besides, only one module at a time can be used.

Table 2-2 lists the function description of ESP-LAUNCHER.

Table 2-2: ESP-LAUNCHER interfaces

—S——_as

HSPI

It can interface SPI flash (Flash2), display screen, MCU, etc (2-1-13).

SDIO/SPI

It can interface flash, host MCU, display screen, etc (2-1-19).

Currently the PWM interface has four channels, and users can extend the channels as

PWM

needed. The PWM interface can be used to control LED lights, buzzers, relays, motors, etc

(2-1-20).

The functionality of the infrared remote control interface can be implemented via software

IR

programming. NEC coding, modulation and demodulation are used by this interface. The

frequency of the modulated carrier signal is 38 KHz (2-1-24).

ADC

The interface is used to test the power supply voltage of VDD3P3 (pin3 and pin4), as well

as the input voltage of TOUT (pin6). It can also be used in sensors (2-1-25).

12C

It can interface sensors and display screens with 2.54 mm or 1.27 mm pin headers

(2-1-21).

UARTO: UOTXD, UORXD, MTDO (UORTS), MTCK (UOCTS)

UART1: GPIO2 (U1TXD)

It can interface other UARTdevices (2-1-5).

« For firmware downloading: UOTXD + UORXD or GPIO2 + UORXD

* For communication: UARTO: UOTXD, UORXD, MTDO(UORTS), MTCK(UOCTS)

UART

« For debugging: UART1_TXD (GPIO2) can be used to print debugging information.

By default, UARTO will output some printed information when the device is powered on. For

the applications that are sensitive to this feature, users can exchange the pins of UART

during system initialization, that is, exchange UOTXD, UORXD with UORTS, UOCTS.

R1/3/5/7 should not be mounted with other components, while R2/4/6/8 can be mounted

with other components. J14 and J67 should be shorted.

Relay control

It is used to control, with an indicator light, the on-and-off switch of the relay in a smart plug

terminal

application ( 2-1-15).

To use the SDIO/SPI interfaces on ESP-LAUNCHER, please follow the steps below:

1. Move the OR at R85 to R9, and then disable the flash on the ESP_Test Board;

2. Short-circuit the two lower pins on J3 with a jumper to enable HSPI flash;

3. Remove C8 (next to the Reset key on the left of the PCB);

25/32

Espressif

Submit Documentation Feedback

2024.10

## Tables

2. ESP-LAUNCHER
a
There are multiple modules that can be connected to the ESP-LAUNCHER for testing and
development, through the 1.27mm double-row pin headers (2-1-23) and 2.00 mm double-
Test modules row pin headers (2-1-24).
Please note that module pins should be connected to their corresponding pins on the
board. Besides, only one module at a time can be used.
Table 2-2 lists the function description of ESP-LAUNCHER.
Table 2-2: ESP-LAUNCHER interfaces
—S——_as
HSPI It can interface SPI flash (Flash2), display screen, MCU, etc (2-1-13).
SDIO/SPI It can interface flash, host MCU, display screen, etc (2-1-19).
Currently the PWM interface has four channels, and users can extend the channels as
PWM needed. The PWM interface can be used to control LED lights, buzzers, relays, motors, etc
(2-1-20).
The functionality of the infrared remote control interface can be implemented via software
IR programming. NEC coding, modulation and demodulation are used by this interface. The
frequency of the modulated carrier signal is 38 KHz (2-1-24).
ADC The interface is used to test the power supply voltage of VDD3P3 (pin3 and pin4), as well
as the input voltage of TOUT (pin6). It can also be used in sensors (2-1-25).
12C
It can interface sensors and display screens with 2.54 mm or 1.27 mm pin headers
(2-1-21).
UARTO: UOTXD, UORXD, MTDO (UORTS), MTCK (UOCTS)
UART1: GPIO2 (U1TXD)
It can interface other UARTdevices (2-1-5).
« For firmware downloading: UOTXD + UORXD or GPIO2 + UORXD
* For communication: UARTO: UOTXD, UORXD, MTDO(UORTS), MTCK(UOCTS)
UART « For debugging: UART1_TXD (GPIO2) can be used to print debugging information.
By default, UARTO will output some printed information when the device is powered on. For
the applications that are sensitive to this feature, users can exchange the pins of UART
during system initialization, that is, exchange UOTXD, UORXD with UORTS, UOCTS.
R1/3/5/7 should not be mounted with other components, while R2/4/6/8 can be mounted
with other components. J14 and J67 should be shorted.
Relay control It is used to control, with an indicator light, the on-and-off switch of the relay in a smart plug
terminal application ( 2-1-15).
To use the SDIO/SPI interfaces on ESP-LAUNCHER, please follow the steps below:
1. Move the OR at R85 to R9, and then disable the flash on the ESP_Test Board;
2. Short-circuit the two lower pins on J3 with a jumper to enable HSPI flash;
3. Remove C8 (next to the Reset key on the left of the PCB);
25/32
Espressif Submit Documentation Feedback 2024.10


---

