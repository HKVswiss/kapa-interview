# 2. ESP-LAUNCHER

## Table 2-1. ESP-LAUNCHER Module Description

### Micro USB
- There are two USB interfaces. Both can be used as a 5 V power supply or for serial interface communication.
- The USB interface provides 5 V power supply which can be converted to 3.3 V through a DC-to-DC converter.
- An LED light indicates the power, and a header pin is used for testing the power current.

### Slide Switches
Three slide switches are used for:
- 5 V power supply
- GPIO0 voltage level switch
- Chip enable pin CH_EN

When the switches are toggled to the outer side, the voltage level is high; when toggled to the inner side, the voltage level is low.

**For the 5 V power switch:**
- Toggled to the inner side: the board is powered on.
- Toggled to the outer side: the board is powered off.

**For the GPIO0 control:**
- Toggle to the inner side: UART download mode is enabled; users can download firmware with ESP Flash Download Tool.
- Toggle to the outer side: Flash boot mode is enabled; UART debug tool can be used for debugging.

### Reset Key
- SW1 is connected to MTCK (GPIO13) for application reset and clearing the Wi-Fi configuration.
- SW2 is not defined.

### Indicator Lights
- Red light (D2): Wi-Fi work status.
- Blue light (D3): Communication with server.
- Green light (D1): Relay switch control.
- Blue light (D11) and red light (D10): Rx and Tx work status, respectively.
- Red light (D12): 5 V power supply.
- D4, D13, D14, D16 are not defined.

### Jumpers
- J82: Needs to be shorted by a jumper to channel the 3.3 V power supply into other circuits; can also be used to test power current.
- J3: CS of HSPI flash. HSPI flash is disabled when the two upper pins are shorted by a jumper; enabled when the two lower pins are shorted.
- J14 and J67: Short-circuit J14 to connect GPIO13 to UOCTS; short-circuit J67 to connect GPIO15 to UORTS.
- J77: Short-circuit J77 to connect GPIO16 to EXT_RSTB for Deep-sleep wake up.

### Interfaces
UART, HSPI, SDIO/SPI, I2C, ADC_IN, GPIO16, relay control, PWM, and IR TX/RX.

### Flash Memory
- 16-Mbit Flash1 (mounted on the test board): Connected to the chip via SPI interface. Used when the chip works in Wi-Fi standalone mode. RQ and R85 can be used for the CS of Flash1. By default, Flash1 is enabled.
- 32-Mbit Flash2 (mounted on the baseboard): Connected via HSPI interface. HSPI is used in SIP mode. When ESP8266EX works as a slave device, it connects to the host MCU via SPI interface defined in SDIO specifications. HSPI is connected to Flash2. J3 can be used for the CS of Flash2.

---

*Page 29*