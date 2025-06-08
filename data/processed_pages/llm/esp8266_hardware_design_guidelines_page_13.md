# ESP8266EX Flash and Crystal Oscillator

## ESP8266EX Flash Interface

| Pin Name       | Description           |
|----------------|-----------------------|
| VDD33          | Power supply 3.3V     |
| GPIO5          | General Purpose I/O 5  |
| SDI/SDI        | SPI Data Input        |
| SCS/ICMD       | SPI Chip Select / Command |
| SDVSD1         | SPI Data 1            |
| SD_DATA_1      | SPI Data 1            |
| SDO/SDO        | SPI Data Output       |
| SCKICLK        | SPI Clock             |
| SD_CLK         | SPI Clock             |
| SCS/CMD        | SPI Chip Select / Command |
| SD_CMD         | SPI Command           |
| SWPISD3        | SPI Data 3            |
| SHD/SD2        | SPI Data 2 / Hold     |
| WP             | Write Protect         |
| VDDPST         | Power Supply          |
| FLASH          | Flash Memory Interface|

*Figure 1-6. ESP8266EX Flash Interface*


## Crystal Oscillator

ESP8266EX supports 40 MHz, 26 MHz, and 24 MHz crystal oscillators. It is important to select the correct type of crystal oscillator in the ESP Flash Download Tool.

In the circuit design, capacitors C1 and C2 are connected to ground and added to the input and output terminals of the crystal oscillator respectively. The values of these capacitors can range from 6 pF to 22 pF, but the exact values depend on testing and adjustment for optimal circuit performance. The crystal precision should be ±10 PPM.

| Pin Name  | Description       |
|-----------|-------------------|
| VDDD (28) | Power supply      |
| XTAL_IN (27)  | Crystal oscillator input |
| XTAL_OUT (26) | Crystal oscillator output|
| UOTXD (25) | UART TX           |
| UORXD      | UART RX           |
| GND        | Ground            |

*Figure 1-7. ESP8266EX Crystal Oscillator*

> **Notice:**
> Defects in the craftsmanship of the crystal oscillators (e.g., high frequency deviation and unstable working temperature) may cause malfunction of the ESP8266EX, resulting in decreased overall performance.

---

*Page 14*