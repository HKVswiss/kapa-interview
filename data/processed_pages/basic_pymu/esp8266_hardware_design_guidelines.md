# ESP8266

#### Version 2.8
### Hardware Design Guidelines

www.espressif.com

## A bout Thi s Gu i de

This document provides product information of ESP8266EX series, including ESP8266EX
chip, ESP-LAUNCHER development board and ESP8266EX modules.

Release Notes

2015.12 V1.3 Initial release.

2016.01 V1.4 Update Section 1.5.2, Section 1.5.3 and Section 1.6.

2016.06 V1.5 Update Section 3.1.

2016.07 V1.6 Update Section 2.1.

Updated the minimum voltage of ESP8266EX to 2.5V;

2017.01 V2.0

Updated Table 1-1.

Updated the chip’s output impedance from 50Ω to 39+j6 Ω;


2017.04 V2.1


Added a note that the size of ESP-LAUNCHER’s Flash1 and Flash2 is 32
Mbit;

Updated Section 1.4.5.


2017.06 V2.2 Updated Section 1.4.2.

Updated the name of the document from “ESP8266 System Description”
to “ESP8266 Hardware Design Guidelines”;


2018.04 V2.3

2018.12 V2.4


Updated all the fifigures in the document;

Updated Section 1.4 Schematic Checklist;

Updated Chapter 3 ESP8266EX Module.

Updated description in Section 1.4.2 about reset;

Updated formatting.


2019.10 V2.5 Updated description in Section 1.6.2 about position.

2019.10 V2.6 Added UART SWAP specififications in Section 1.4.7.

Updated the flflash size in Table 2-1;

2023.02 V2.7

Added Documentation Feedback Link.

Updated the title page and disclaimer page;


2024.10 V2.8


Updated the Figure 1-3 and Figure 1-8;

Added description in Section 1.4.7 about UART GPIO confifiguration.

Documentation Change Notifification

Espressif provides email notififications to keep customers updated on changes to
technical documentation. Please subscribe at *[https://www.espressif.com/en/subscribe](https://www.espressif.com/en/subscribe)* .

Certifification

Download certifificates for Espressif products from *[https://www.espressif.com/en/](https://www.espressif.com/en/certificates)*
*[certifcates](https://www.espressif.com/en/certificates)* *ifi* .

## T ab l e o f Co n te n ts

1. ESP8266EX ............................................................................................................................1

1.1. Overview ....................................................................................................................................1

1.2. Specififications .............................................................................................................................2

1.3. Pin Defifinitions ............................................................................................................................3

1.4. Schematic Checklist ..................................................................................................................5

1.4.1. Power Supply ...............................................................................................................6

1.4.2. Power-on Sequence and Power Reset .........................................................................8

1.4.3. Flash .............................................................................................................................8

1.4.4. Crystal Oscillator ..........................................................................................................9

1.4.5. RF ...............................................................................................................................10

1.4.6. External Resistor 12K .................................................................................................10

1.4.7. UART ...........................................................................................................................10

1.5. Slave SDIO/SPI ........................................................................................................................13

1.6. PCB Layout Design ..................................................................................................................14

1.6.1. General Principles of PCB Layout Design ..................................................................14

1.6.2. Positioning a ESP8266EX Module on a Base Board ..................................................15

1.6.3. Standalone ESP8266EX Module ................................................................................16

1.6.4. ESP8266EX as a Slave Device ...................................................................................19

1.6.5. Typical Layout Problems and Solutions ......................................................................20

1.7. Typical Application ...................................................................................................................21

1.7.1. UART to Wi-Fi Smart Device ......................................................................................21

1.7.2. Sensor .........................................................................................................................21

1.7.3. Smart Light .................................................................................................................22

1.7.4. Smart Plug ..................................................................................................................22

2. ESP-LAUNCHER ..................................................................................................................23

2.1. Overview ..................................................................................................................................23

2.2. Modules and Interfaces ............................................................................................................23

2.3. Schematics ..............................................................................................................................26

2.3.1. Interfaces ....................................................................................................................26

2.3.2. 5V Power Supply ........................................................................................................27

2.3.3. Test Module ................................................................................................................27

Module ................................................................................................................................29

3.1. ESP-WROOM-S2 .....................................................................................................................29

3.2. ESP-WROOM-02 .....................................................................................................................29

3.3. ESP-WROOM-02D/ESP-WROOM-02U ...................................................................................30

1. ESP8266EX
## 1. E S P 8 2 66 EX

##### 1.1. Overview


Espressif’s ESP8266EX delivers a highly integrated Wi-Fi SoC solution to meet the
continuous demand for effificient power usage, compact design and reliable performance in
the industry.

With its complete and self-contained Wi-Fi networking capabilities, ESP8266EX can
perform either as a standalone application, or as a slave to a host MCU. When ESP8266EX
hosts an application, it promptly boots up from the external flflash. The integrated highspeed cache optimizes the system's performance and memory.

Also, ESP8266EX can be applied to any micro-controller design as a Wi-Fi adaptor through
SPI/SDIO or I2C/UART interfaces.

Besides the Wi-Fi functionalities, ESP8266EX also integrates an enhanced version of
Tensilica’s L106 Diamond series 32-bit processor and on-chip SRAM. It can be interfaced
with external sensors and other devices through the GPIOs, resulting in low development
cost at early stage and minimum footprint. Software Development Kit (SDK) provides
sample codes for various applications.

ESP8266EX integrates antenna switches, RF balun, power amplififier, low-noise receive
amplififier, fifilters and power management modules. The compact design minimizes the PCB
size and the external circuitry.

ESP8266EX enables sophisticated features, such as:

         Fast switching between sleep and wake-up modes for effificient energy use;

         Adaptive radio biasing for low-power operation;

         Advanced signal processing;

         Spur cancellation;

         - Radio co-existence mechanisms for common cellular, Bluetooth, DDR, LVDS, LCD
interference mitigation.

Figure 1-1 shows the functional blocks of ESP8266EX.


Espressif


1/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX










Figure 1-1. ESP8266EX Block Diagram

##### 1.2. Specififications


Table 1-1. ESP8266EX Specififications







2/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10


Espressif

1. ESP8266EX




##### 1.3. Pin Defifinitions

The pin layout for the 32-pin QFN package is illustrated in Figure 1-2.

Figure 1-2. ESP8266EX Pin Layout

Table 1-2 lists the defifinitions and functions of each pin.


Espressif


3/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX


Table 1-2. ESP8266EX Pin Defifinitions







Espressif


4/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX

*Note:*

*GPIO2, GPIO0, and MTDO are confifigurable on PCB as the 3-bit strapping register that determines the*
*booting mode and the SDIO timing mode.*
##### 1.4. Schematic Checklist


The highly-integrated design of ESP8266EX reduces the number of components required.
Besides ESP8266EX, less than 10 resistors and capacitors, one crystal oscillator and one
SPI flflash are needed to make a complete module with wireless communication capability.

The following is a detailed description of ESP8266EX schematics, and the layout design
which ensures optimum functionality.

The complete circuit diagram of ESP8266EX is illustrated in Figure 1-3.


Espressif


5/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX















|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
|31|30|29|28|27|





























Figure 1-3. ESP8266EX Module Schematics

The ESP8266EX schematics include seven aspects:



Power supply

Power-on sequence and reset

Flash

- Crystal osci ~~l~~ lator

RF



         External resistor

         UART

1.4.1. Power Supply


1.4.1.1. Digital Power Supply

ESP8266EX has two digital pins for power supply, Pin11 and Pin17. For digital power
supply, there is no need to add additional fifilter capacitors. The operating voltage range of
digital power supply pins is 1.8 V ~ 3.3 V.


Espressif


6/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

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

1.4.2. Power-on Sequence and Power Reset

1.4.2.1. Power-on Sequence

ESP8266EX uses a 3.3 V system power supply. The chip should be activated after the
power rails have stabilized. This is achieved by delaying the activation of CH_EN (Pin7) by
time T after the 3.3 V rails have been brought up. The recommended delay time (T) is given
by the parameter of the RC circuit. For reference design, please refer to Figure ESPWROOM-02 Peripheral Schematics in the *ESP* *-* *WROOM* *-* *02 Datasheet* .

1.4.2.2. Reset

Pin32 EXT_RSTB serves as the reset pin of ESP8266EX. This pin contains an internal pullup resistor and is active low. To avoid resets caused by external interference, we
recommend that you keep the PCB trace of EXT_RSTB as short as possible, and add an
RC circuit at the EXT_RSTB pin.

Pin7 CHIP_EN serves as the enable pin of ESP8266EX. In this case, ESP8266EX powers
off when this pin is held low. Pin7 CHIP_EN also serves as the reset pin of ESP8266EX. In
this case, ESP8266EX reboots when the input level of this pin is below 0.6 V and lasts for
at least 200 μs.

We recommend that you use CHIP_EN, instead of EXT_RSTB, to reset the chip.

1.4.3. Flash

The demo flflash used on ESP8266EX is an SPI Flash with 2-MB ROM in an SOP8 (208 mil)
package. Pin21 SD_CLK is connected to the flflash CLK pin together with a 0402 resistor in
serial connection, which reduces the drive current and eliminates external interruption. The
initial resistance of the resistor is 200 Ω.


Espressif


8/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

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

1.4.5. RF


39-j6 Ω (from antenna to the c ~~hip)~~ .

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|ch|e|d|i|m|













|50 ohm Impedance Control<br>ANT1 1<br>1 RF_ANT L1 TBD LNA_IN 2<br>2 3<br>C1 C2 4<br>PCB_ANT 5<br>TBD TBD 6<br>7<br>8<br>GND<br>GND GND|Col2|1<br>2|1|VDDA<br>LNA<br>VDD3P3<br>VDD3P3<br>VDD_RTC<br>TOUT<br>CHIP_EN<br>XPD_DCDC|
|---|---|---|---|---|
|50 ohm Impedance Control<br>ANT1 1<br>1 RF_ANT L1 TBD LNA_IN 2<br>2 3<br>C1 C2 4<br>PCB_ANT 5<br>TBD TBD 6<br>7<br>8<br>GND<br>GND GND|50 ohm Impedance Control<br>ANT1 1<br>1 RF_ANT L1 TBD LNA_IN 2<br>2 3<br>C1 C2 4<br>PCB_ANT 5<br>TBD TBD 6<br>7<br>8<br>GND<br>GND GND|3|3|3|
|50 ohm Impedance Control<br>ANT1 1<br>1 RF_ANT L1 TBD LNA_IN 2<br>2 3<br>C1 C2 4<br>PCB_ANT 5<br>TBD TBD 6<br>7<br>8<br>GND<br>GND GND|50 ohm Impedance Control<br>ANT1 1<br>1 RF_ANT L1 TBD LNA_IN 2<br>2 3<br>C1 C2 4<br>PCB_ANT 5<br>TBD TBD 6<br>7<br>8<br>GND<br>GND GND|4|4|4|
|50 ohm Impedance Control<br>ANT1 1<br>1 RF_ANT L1 TBD LNA_IN 2<br>2 3<br>C1 C2 4<br>PCB_ANT 5<br>TBD TBD 6<br>7<br>8<br>GND<br>GND GND|7<br>8|7<br>8|7<br>8|7<br>8|
|50 ohm Impedance Control<br>ANT1 1<br>1 RF_ANT L1 TBD LNA_IN 2<br>2 3<br>C1 C2 4<br>PCB_ANT 5<br>TBD TBD 6<br>7<br>8<br>GND<br>GND GND|7<br>8||||


1.4.6. External Resistor 12K




|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>||||
|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>||||
|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|ESP8266EX Exte<br>tor to the U0T<br> |ESP8266EX Exte<br>tor to the U0T<br> |ESP8266EX Exte<br>tor to the U0T<br> |
|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|resistor requires high accuracy when<br>is recommended.<br><br><br><br>Figure 1-9.<br>1.4.7. UART<br>Users need to connect a 499 R resis<br>harmonics. See Figure 1-10a.<br>|||||||
|||||||||||
|||||||||||
|||||||||||


Espressif


Figure 1-10a. ESP8266EX UART

By default, UART0 will output some printed information when ESP8266EX is powered on.
For the applications that are sensitive to this feature, users can exchange the pins of UART
~~(UART~~ ~~SWAP)~~ ~~d~~ ur ~~i~~ ng system ~~i~~ n ~~i~~ t ~~i~~ a ~~li~~ zat ~~i~~ on, that is, exchange U0TXD, U0RXD with U0RTS

10/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

Espressif


1. ESP8266EX

(GPIO15), U0CTS (GPIO13). After the exchange, GPIO15 and GPIO13 will be connected
respectively to MCU_RXD and MCU_TXD as swapped U0TXD and U0RXD for serial
communication. For reference design, please refer to Figure 1-10b.

Figure 1-10b. ESP8266EX UART SWAP

GPIO15, the strapping pin of ESP8266EX, needs to be at low-voltage level when
the chip is powered on. Thus, while the system is powered on, to make sure
GPIO15 won't be pulled-up externally, which will cause the system mistakenly
entering boot mode, an isolation circuit is added. As shown in Figure 1-10b, when
the system is powered on, Q1 is switched off by default and GPIO15 is actually
disconnected from MCU_RXD. After the program starts to run, Q1 can be turned
on by GPIO5, then GPIO15 is connected to MCU_RXD, which enables power-on
isolation of GPIO15.

The IO of the ESP8266EX is a 3.3 V logic level. In the case of serial communication
with a 5 V CMOS logic system, a level switch circuit needs to be added externally.
See Figure 1-10c.

11/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

Espressif


1. ESP8266EX

Figure 1-10c. UART Voltage-level Switch circuit

When using the AT fifirmware, please note that the UART GPIO is already confifigured (refer to
*[Hardware Connection](https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp8266/Get_Started/Hardware_connection.html)* ). It is recommended to use the default confifiguration.

12/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX

##### 1.5. Slave SDIO/SPI













Espressif


Figure 1-11. Schematics of ESP8266EX as a Slave SDIO

13/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

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
##### 1.6. PCB Layout Design


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

         - The third layer is the POWER layer where only power lines can be placed. It is
acceptable to place some signal lines under unavoidable circumstances.

         - The forth layer is the BOTTOM layer. Only signal lines can be laid. Placing
components on this layer is not recommended.

Below are the suggestions for a two-layer PCB design.

         The fifirst layer is the TOP layer for signal traces and components.

         - The second layer is the BOTTOM layer, where power traces are routed. Placing any
components on this layer is not recommended. Do not route any power or signal
traces under or around the RF and crystal oscillator, and so that there is a complete
GND plane, which is connected to the Ground Pad at the bottom of the chip.

1.6.2. Positioning a ESP8266EX Module on a Base Board

If users adopt on-board design, they should pay attention to the layout of the module on
the base board. The interference of the base board on the module's antenna performance
should be reduced as much as possible.

It is recommended that the PCB antenna area of the module be placed outside the base
board while the module be put as close as possible to the edge of the base board so that
the feed point of the antenna is closest to the board.



Espressif


Figure 1-13. ESP8266EX Module Antenna Position on Base Board

15/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

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

1. ESP8266EX

The center ground pad at the bottom of the chip should be connected to ground plane
through at least 9 ground vias.

Figure 1-15. ESP8266EX PCB Layout

1.6.3.2. Crystal Oscillator Design

The crystal oscillator should be placed as close to the XTAL pins as possible (without the
traces being too long). However, the crystal cannot be placed too close to the chip to
prevent the crystal from interfering with the chip, as Figure 1-15 shows. The recommended
distance is 0.8 mm (see Figure 1-16). However, the crystal cannot be too close to the chip
to prevent the crystal from interfering with the chip. The recommended distance is 0.8mm
(see Figure 1-16). It is good practice to use via stitching around the clock trace for low
ground-plane impedance.

There should be no vias on the input and output traces, which means the traces cannot
cross layers. In addition, the input and output traces should not be routed over one
another, not even on different layers.

Place the input and output bypass capacitors on the near left or right side of the chip. Do
not place them on the traces.

Do not route high-frequency digital signal lines under the crystal oscillator. It is best not to
route any signal line under the crystal oscillator. The larger the copper area on the top layer
is, the better. As the crystal oscillator is a sensitive component, do not place any magnetic
components nearby that may cause interference, for example, power-switching converter
components or unshielded inductors.


Espressif


17/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX

Figure 1-16. ESP8266EX Crystal Oscillators

1.6.3.3. RF Design

The characteristic RF impedance is 50 Ω. The ground plane should be complete. The RF
trace should be as short as possible with dense ground via stitching around it for isolation.
The width of RF lines should be as short as possible and there should be dense vias
stitched around.

π-type matching circuitry should be reserved on the RF trace and placed close to the RF
Pin2. The components of the π-matching network should be placed in the same direction
(see Figure 1-17).

There should be no vias for the RF trace. The RF trace should be routed at a 135 ° angle,
or with circular arcs if trace bends are required.

There should be no RF routing around the high-frequency signal lines.

The RF antenna should be set away from high-frequency transmitting devices, such as
crystal oscillators, DDR, and certain high frequency clocks (SDIO_CLK, etc.). Besides, the
USB ports, USB-to-UART signal chips, UART signal lines (including traces, vias, test points,
headers, etc.) must be placed as far away from the antenna as possible. The UART signal
line is packaged and ground shielding is added.

For PCB onboard antenna design please refer to Type-B version by Espressif. If there are
power traces near the antenna, the power traces and antenna must be isolated with GND
copper.


Espressif


18/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX

Figure 1-17. ESP8266EX RF Design

1.6.4. ESP8266EX as a Slave Device

When ESP8266EX works as a slave device in a system, users need to pay more attention
to signal integrity in the PCB design. It is important to keep ESP38266EX away from the
interferences caused by the complexity of the system and an increased number of highfrequency signals. We use the mainboard of a PAD or TV Box as an example here to
provide guidelines for the PCB layout and design.

Figure 1-18. PCB/TV Box Layout

The digital signal between the CPU and the DDR is the major producer of high-frequency
noise and interferes with Wi-Fi radio from the air. Below are the key points when designing
the PCB layout:

         - As shown in Figure 1-18, ESP8266EX should be placed near the edge of the PCB
and away from the CPU and DDR, the main high-frequency noise sources. The


Espressif


19/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX

distance between the chip and the noise sources decreases the interference and
reduces the coupled noise.

         - It is suggested that a 100 Ω ~ 200 Ω series resistor is added to the six signal traces
when ESP8266EX communicates with the CPU via SDIO to decrease the drive

current and any interferences, and also to eliminate the sequencing problem caused
by the inconsistent length of the SDIO traces.

         - On-board PCB antenna is not recommended, as it receives much interference and
coupling noise, both of which impact the RF performance. We suggest that you use
an external antenna which should be directed away from the PCB board via a cable,
in order to weaken the high frequency interference with Wi-Fi.

         - The high-frequency signal traces between the CPU and associated memory should
be routed strictly ac- cording to the routing guidelines (please refer to the DDR trace
routing guidelines). CLK and data/addr lines should be laid underground.

         - The GND of the Wi-Fi circuit and that of other high-power devices should be
separated and connected through wires if there are high-power components, such as
motors, in the design.

         - The antenna should be kept away from high-frequency noise sources, such as LCD,
HDMI, Camera Sensor, USB, etc.

1.6.5. Typical Layout Problems and Solutions

1. Q: The current ripple is not large, but the Tx performance of RF is rather poor.

Analysis:

Ripple has a strong impact on the performance of RF Tx. It should be noted that ripple
must be tested when ESP8266EX is in the normal working mode. The ripple increases
when the power gets high. Generally, the ripple should be <80 mV when sending 11n
MCS7 packets, and <120 mV when sending 11b packets.

Solution:

Add a 10-μF fifilter capacitor to the branch of source circuit (ESP8266EX AVDD pin). The 10μF capacitor should be adjacent to the VDDA pin.

2. Q: The power ripple is small, but the Tx performance is poor.

Analysis:

The RF Tx performance can be affected not only by power ripples, but also by the crystal
oscillator itself. Poor quality and big frequency offsets (more than ±40 ppm) of the crystal
oscillator decrease the RF Tx performance. The crystal oscillator clock may be corrupted
by other interfering signals, such as high-speed output or input signals. Besides, sensitive
components or radiation components, such as inductors and antennas, may also decrease
the RF performance.

Solution:


Espressif


20/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX

This problem is caused by improper layout and can be solved by re-layout. See Section 1.5
for details.

3. Q: When ESP8266EX sends data packages, the power value is much higher or

lower than the target power value, and the EVM is relatively poor.

Analysis:

The disparity between the tested value and the target value may be due to signal reflflection
caused by the impedance mismatch on the transmission line connecting the RF pin and the
antenna.

Solution:

Match the antenna’s impedance with the reserved π-type circuit on the RF trace, so that
the resistance from the RF pin to the antenna approaches (39-j6)Ω.

4. Q: TX performance is not bad, but the Rx sensitivity is low.

Analysis:

Good Tx performance indicates proper RF impedance matching. External coupling to the
antenna can affect the Rx performance. For instance, the crystal oscillator signal harmonics
could couple to the antenna. If ESP8266EX serves as slave device, there will be other highfrequency interference sources on the board, which may affect the Rx performance.

Solution:

Keep the antenna away from crystal oscillators. Do not route high-frequency signal traces
close to the RF trace.
##### 1.7. Typical Application


1.7.1. UART to Wi-Fi Smart Device

The two UART interfaces are defifined in Table 1-3.

Table 1-3. Pin defifinitions of UART Interfaces

Category Pin defifinition Function

*ifi*


AT+ instruction and examples are provided here: *[http://www.espressif.com/en/support/](http://www.espressif.com/en/support/download/documents?keys=&field_type_tid%5B%5D=14)*
*[download/documents?keys=&feld_type_tid%5B%5D=14](http://www.espressif.com/en/support/download/documents?keys=&field_type_tid%5B%5D=14)* *ifi*

Application example: ESP8266EX development board (please see Chapter 2).

1.7.2. Sensor

ESP8266EX can be used for developing sensor products by using the I2C interface. The


*ifi*

Espressif


*ifi*

21/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

1. ESP8266EX

I2C works in the master mode and can connect to multiple sensors. The slave devices are
identifified through the addressing mode, as each slave device has a unique address.

The sensor products send real-time data to ESP8266EX via the I2C interface, and
ESP8266EX uploads the data to the server wirelessly. Users can acquire information from
the server through the mobile app when their mobile phones connect to the internet.

1.7.3. Smart Light

ESP8266EX can be used for developing such smart home products as smart light by using
the PWM and infrared interfaces. The three PWM interfaces control red, blue, and green
LEDs respectively. The minimal PWM duty ratio is 1/214. In addition, the infrared interface
allows specifific control on LEDs, such as reset, power on/off, color switch, etc.

1.7.4. Smart Plug

ESP8266EX can be used for developing smart plug products. The GPIOs control the power
switch through the high/low-level switch and connection/disconnection of relay. A smart
plug requires three modules: 220 V to 3.3 V power conversion module, ESP8266EX Wi-Fi
module and relay control module. **


Espressif


22/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

2. ESP-LAUNCHER
## 2. E S P-LA U N C HER

##### 2.1. Overview


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
##### 2.2. Modules and Interfaces


ESP-LAUNCHER can be confifigured and tested through USB serial or Wi-Fi connection.
The modules/interfaces integrated on the development board are described in Table 2-1.


Espressif


23/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

2. ESP-LAUNCHER


Table 2-1. ESP-LAUNCHER Module Description












24/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10


Espressif

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

2. ESP-LAUNCHER

4. Remove R58 on the PCB and disconnect GPIO14 with the infrared transmitting tube;

5. Remove the pull-down resistor R29 of MTDO/IO15 (next to J11);

6. When downloading fifirmware, pull the IO15/CS at J11 to low level and toggle the

switch of GPIO0 inwards to enable UART Download mode;

7. When downloading is completed, release IO15/CS to enable SDIO Boot mode;

8. Connect SDIO/SPI at J5 to host for communication.
##### 2.3. Schematics


2.3.1. Interfaces

























||Col2|Col3|
|---|---|---|
||||
|'<br>|'<br>|'<br>|

|Col1|Col2|Col3|� ��|
|---|---|---|---|
|||||
|||| (|
|||| |
|9|||)<br>9|













































Espressif


Figure 2-2. ESP-LAUNCHER Interface

26/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

2.3.2. 5V Power Supply




2. ESP-LAUNCHER









2.3.3. Test Module












Figure 2-3. ESP-LAUNCHER 5V Power Supply Schematics






























||Col2|
|---|---|
|||

||Col2|
|---|---|
|||













Espressif


Figure 2-4. ESP-LAUNCHER Test Module Schematics

27/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

2. ESP-LAUNCHER
##### 2.4. Test Board


A test board is embedded in ESP-LAUNCHER, as shown in Figure 2-5. The external size of
the test board is 20 mm x 31 mm. A 2-dBi SMA antenna or other testing equipment can be
connected to the test board via the SMA antenna connector. The 2.54 mm pin headers
makes test and development easy and convenient when using a breadboard.

Figure 2-5. ESP-LAUNCHER Test Board
















|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
||&|(|'|































|  ||||||
|---|---|---|---|---|---|
|  ||||||




|��|��� �|
|---|---|
|||
|||

|��|���� �|
|---|---|
|| |
|||

|���|����� �|
|---|---|
|| |
|||

|���|����� �|
|---|---|
|| |
|||

|��|���� �|
|---|---|
|| |
|||

|��|���� �|
|---|---|
|| |
|||

|���|����� �|
|---|---|
|| |
|||

|���|����� �|
|---|---|
|| |
|||

|���|�������� �|
|---|---|
||  |
|||

|��|����� �|
|---|---|
|| |
|||

|��|���� �|
|---|---|
|| |
|||

|���|����� �|
|---|---|
|| |
|||

|���|����� �|
|---|---|
|| |
|||

|��|������ �|
|---|---|
|| |
|||

|��|����� �|
|---|---|
|| |
|||

|���|������ �|
|---|---|
||  |
|||

|���|����� �|
|---|---|
|| |
|||















|��|���� �|
|---|---|
|| |
|||

|���|����� �|
|---|---|
|| |
|||

|���|������ �|
|---|---|
|| |
|||

|���|����� �|
|---|---|
|| |
|||

|���|��� �|
|---|---|
|||
|||


Espressif


Figure 2-6. ESP-LAUNCHER Test Board Schematics

28/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

3. ESP8266EX Module
## 3 . E S P 8 2 66 EX M odu l e

Espressif provides two types of modules, the SMD module (ESP-WROOM-02) and the DIP
module (ESP-WROOM-01). The modules have been improved to achieve the optimum RF
functionality. It is recommended that users use these modules for testing or further
development.
##### 3.1. ESP-WROOM-S2


The module size is 16 ± 0.2 mm x 23 ± 0.2 mm x 3 ± 0.15 mm (see Figure 1-1). The flflash
used on this module is a 2-MB SPI flflash connected to HSPI, with a package size of SOP
8-150 mil. The gain of the on-board PCB antenna is 2 dBi.

The ESP-WROOM-S2 works as the SDIO/SPI slave with the SPI speed of up to 8 Mbps.

Figure 3-1. ESP-WROOM-S2 Module

For details of ESP-WROOM-S2, please refer to *ESP* *-* *WROOM* *-* *S2 Datasheet* .
##### 3.2. ESP-WROOM-02


The module size is (18 ± 0.2) mm x (20 ± 0.2) mm x (3 ± 0.15) mm. The type of flflash used
on this module is an SPI flflash with a package size of SOP 8-150 mil. The gain of the onboard PCB antenna is 2 dBi.


Espressif


29/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

3. ESP8266EX Module

Figure 3-2. ESP-WROOM-02 Module

For details of ESP-WROOM-S2, please refer to *ESP* *-* *WROOM* *-* *02 Datasheet* .
##### 3.3. ESP-WROOM-02D/ESP-WROOM-02U


The module size of ESP-WROOM-02D is (18 ± 0.2) mm x (20 ± 0.2) mm x (3 ± 0.15) mm.
The type of flflash used on this module is an SPI flflash with a package size of SOP 8-150 mil.
The gain of the on-board PCB antenna is 3 dBi.

Figure 3-3. ESP-WROOM-02D Module

The module size of ESP-WROOM-02U is (18 ± 0.1) x (14.3 ± 0.1) x (3.2 ± 0.1) mm. The
type of flflash used on this module is an SPI flflash with a package size of SOP 8-150 mil.
ESP-WROOM-02U integrates a U.FL connector and has no onboard antenna.


Espressif


30/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

Espressif


3. ESP8266EX Module

Figure 3-4. ESP-WROOM-02U Module

For detailed information on ESP-WROOM-02D/ESP-WOOM-02U, please refer to *[ESP](https://www.espressif.com/sites/default/files/documentation/esp-wroom-02d_esp-wroom-02u_datasheet_en.pdf)* *-*
*WROOM* *-* *02D/ESP* *-* *[WROOM](https://www.espressif.com/sites/default/files/documentation/esp-wroom-02d_esp-wroom-02u_datasheet_en.pdf)* *-* *02U Datasheet* .

31/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10

Disclaimer and Copyright Notice

Information in this document, including URL references, is subject to change without notice.

ALL THIRD PARTY’S INFORMATION IN THIS DOCUMENT IS PROVIDED AS IS WITH NO WARRANTIES TO ITS
AUTHENTICITY AND ACCURACY.

NO WARRANTY IS PROVIDED TO THIS DOCUMENT FOR ITS MERCHANTABILITY, NON-INFRINGEMENT, FITNESS FOR ANY
PARTICULAR PURPOSE, NOR DOES ANY WARRANTY OTHERWISE ARISING OUT OF ANY PROPOSAL, SPECIFICATION OR
SAMPLE.

All liability, including liability for infringement of any proprietary rights, relating to use of information in this document is disclaimed.
No licenses express or implied, by estoppel or otherwise, to any intellectual property rights are granted herein.

The Wi-Fi Alliance Member logo is a trademark of the Wi-Fi Alliance. The Bluetooth logo is a registered trademark of Bluetooth SIG.

All trade names, trademarks and registered trademarks mentioned in this document are property of their respective owners, and are
hereby acknowledged.

Copyright © 2024 Espressif Systems (Shanghai) Co., Ltd. All rights reserved.

[www.espressif.com](https://www.espressif.com/)

