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

1.4.2. Power-on Sequence and Power Reset

1.4.2.1. Power-on Sequence

ESP8266EX uses a 3.3 V system power supply. The chip should be activated after the

power rails have stabilized. This is achieved by delaying the activation of CH_EN (Pin7) by

time T after the 3.3 V rails have been brought up. The recommended delay time (T) is given

by the parameter of the RC circuit. For reference design, please refer to Figure ESP-

WROOM-02 Peripheral Schematics in the ESP-V/ROOM-02 Datasheet.

! Notice:

If CHIP_EN is driven by a power management chip, then the power management chip controls the

ESP8266EX power state. When the power management chip turns on/off Wi-Fi through the high/low level on

GPIO, a pulse current may be generated. To avoid level instability on CHIP_EN, an RC delay (R=10 kQ,

C=100 nF) circuit is required.

1.4.2.2. Reset

Pin32 EXT_RSTB serves as the reset pin of ESP8266Ex. This pin contains an internal pull-

up resistor and is active low. To avoid resets caused by external interference, we

recommend that you keep the PCB trace of EXT_RSTB as short as possible, and add an

RC circuit at the EXT_RSTB pin.

Pin7 CHIP_EN serves as the enable pin of ESP8266EX. In this case, ESP8266EX powers

off when this pin is held low. Pin? CHIP_EN also serves as the reset pin of ESP8266EX. In

this case, ESP8266EX reboots when the input level of this pin is below 0.6 V and lasts for

at least 200 us.

We recommend that you use CHIP_EN, instead of EXT_RSTB, to reset the chip.

1! Notice:

CHIP_EN cannot be left floating.

1.4.3. Flash

The demo flash used on ESP8266ExX is an SPI Flash with 2-MB ROM in an SOP8 (208 mil)

package. Pin21 SD_CLK is connected to the flash CLK pin together with a 0402 resistor in

serial connection, which reduces the drive current and eliminates external interruption. The

initial resistance of the resistor is 200 Q.

8/32

Submit Documentation Feedback

2024.10

Espressif

1. ESP8266EX
1.4.2. Power-on Sequence and Power Reset
1.4.2.1. Power-on Sequence
ESP8266EX uses a 3.3 V system power supply. The chip should be activated after the
power rails have stabilized. This is achieved by delaying the activation of CH_EN (Pin7) by
time T after the 3.3 V rails have been brought up. The recommended delay time (T) is given
by the parameter of the RC circuit. For reference design, please refer to Figure ESP-
WROOM-02 Peripheral Schematics in the ESP-V/ROOM-02 Datasheet.
! Notice:
If CHIP_EN is driven by a power management chip, then the power management chip controls the
ESP8266EX power state. When the power management chip turns on/off Wi-Fi through the high/low level on
GPIO, a pulse current may be generated. To avoid level instability on CHIP_EN, an RC delay (R=10 kQ,
C=100 nF) circuit is required.
1.4.2.2. Reset
Pin32 EXT_RSTB serves as the reset pin of ESP8266Ex. This pin contains an internal pull-
up resistor and is active low. To avoid resets caused by external interference, we
recommend that you keep the PCB trace of EXT_RSTB as short as possible, and add an
RC circuit at the EXT_RSTB pin.
Pin7 CHIP_EN serves as the enable pin of ESP8266EX. In this case, ESP8266EX powers
off when this pin is held low. Pin? CHIP_EN also serves as the reset pin of ESP8266EX. In
this case, ESP8266EX reboots when the input level of this pin is below 0.6 V and lasts for
at least 200 us.
We recommend that you use CHIP_EN, instead of EXT_RSTB, to reset the chip.
1! Notice:
CHIP_EN cannot be left floating.
1.4.3. Flash
The demo flash used on ESP8266ExX is an SPI Flash with 2-MB ROM in an SOP8 (208 mil)
package. Pin21 SD_CLK is connected to the flash CLK pin together with a 0402 resistor in
serial connection, which reduces the drive current and eliminates external interruption. The
initial resistance of the resistor is 200 Q.
8/32
Submit Documentation Feedback 2024.10 Espressif


---Page 13 

