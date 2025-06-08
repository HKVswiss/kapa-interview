# ESP-LAUNCHER

## Module Description

- **Micro USB:** There are two USB interfaces. Both can be used as a 5 V power supply or for serial interface communication.
  - The USB interface provides 5 V power supply which can be converted to 3.3 V through a DC-to-DC converter.
  - An LED indicates the power status.
  - A header pin is used for testing the power current.

- **Slide Switches:** Three slide switches control different functions:
  - **5 V Power Supply Switch:**
    - Toggled to the inner side: board is powered on.
    - Toggled to the outer side: board is powered off.
  - **GPIO0 Voltage Level Switch:**
    - Toggled to the inner side: UART download mode enabled (firmware download with ESP Flash Download Tool).
    - Toggled to the outer side: Flash boot mode enabled (UART debug tool for debugging).
  - **Chip Enable Pin (CH_EN) Switch:** Controls chip enable.

- **Reset Keys:**
  - SW1 connected to MTCK (GPIO13) for application reset and clearing Wi-Fi configuration.
  - SW2 is not defined.

- **Indicator Lights:**
  - Red light (D2): Wi-Fi work status.
  - Blue light (D3): Communication with server.
  - Green light (D1): Relay switch control.
  - Blue light (D11) and Red light (D10): Rx and Tx work status respectively.
  - Red light (D12): 5 V power supply indicator.

- **Undefined Pins:** D4, D13, D14, D16 are not defined.

- **Jumpers:**
  - J82: Shorted by jumper to channel 3.3 V power supply to other circuits or test power current.
  - J3: CS of HSPI flash. Upper pins shorted disables HSPI flash; lower pins shorted enables HSPI flash.
  - J14 and J67: Short-circuit J14 to connect GPIO13 to U0CTS; short-circuit J67 to connect GPIO15 to U0RTS.
  - J77: Short-circuit to connect GPIO16 to EXT_RSTB for Deep-sleep wake up.

- **Interfaces:** UART, HSPI, SDIO/SPI, I2C, ADC_IN, GPIO16, relay control, PWM, and IR TX/RX.

- **Flash Memory:**
  - 16-Mbit Flash1 (on test board): Connected via SPI interface, used in Wi-Fi standalone mode. RQ and R85 can be used for CS of Flash1. Enabled by default.
  - 32-Mbit Flash2 (on baseboard): Connected via HSPI interface, used in SIP mode. When ESP8266EX works as a slave device, it connects to host MCU via SPI defined in SDIO specifications. J3 used for CS of Flash2.

---

*Page 29*