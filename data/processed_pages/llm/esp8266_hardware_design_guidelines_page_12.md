# ESP8266EX

## 1.4.2. Power-on Sequence and Power Reset

### 1.4.2.1. Power-on Sequence

ESP8266EX uses a 3.3 V system power supply. The chip should be activated after the power rails have stabilized. This is achieved by delaying the activation of CH_EN (Pin 7) by time T after the 3.3 V rails have been brought up. The recommended delay time (T) is given by the parameter of the RC circuit. For reference design, please refer to Figure ESP-WROOM-02 Peripheral Schematics in the *ESP-WROOM-02 Datasheet*.

> **Notice:**
> If CHIP_EN is driven by a power management chip, then the power management chip controls the ESP8266EX power state. When the power management chip turns on/off Wi-Fi through the high/low level on GPIO, a pulse current may be generated. To avoid level instability on CHIP_EN, an RC delay (R=10 kΩ, C=100 nF) circuit is required.

### 1.4.2.2. Reset

Pin 32 EXT_RSTB serves as the reset pin of ESP8266EX. This pin contains an internal pull-up resistor and is active low. To avoid resets caused by external interference, it is recommended to keep the PCB trace of EXT_RSTB as short as possible and add an RC circuit at the EXT_RSTB pin.

Pin 7 CHIP_EN serves as the enable pin of ESP8266EX. When this pin is held low, ESP8266EX powers off. CHIP_EN also serves as the reset pin of ESP8266EX; the chip reboots when the input level of this pin is below 0.6 V and lasts for at least 200 µs.

> **Notice:**
> CHIP_EN cannot be left floating.
>
> It is recommended to use CHIP_EN, instead of EXT_RSTB, to reset the chip.

## 1.4.3. Flash

The demo flash used on ESP8266EX is an SPI Flash with 2-MB ROM in an SOP8 (208 mil) package. Pin 21 SD_CLK is connected to the flash CLK pin together with a 0402 resistor in series connection, which reduces the drive current and eliminates external interference. The initial resistance of the resistor is 200 Ω.

---

*Page 13*