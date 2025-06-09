# ESP8266EX Flash and Crystal Oscillator

## ESP8266EX Flash

The ESP8266EX module includes various GPIOs and flash interface pins as shown in the figure below.

| Pin Name     | Description       |
|--------------|-------------------|
| VDD33        | Power supply 3.3V |
| GPIO5        | General Purpose I/O|
| SDISDI       | SPI Data In       |
| SCS/ICMD     | SPI Chip Select / Command |
| SDVSD1       | SPI Data 1        |
| SD_DATA_1    | SPI Data 1        |
| SDOISDO      | SPI Data Out      |
| SD_DATA_0    | SPI Data 0        |
| RS 200R      | Resistor 200 Ohm  |
| SCKICLK      | SPI Clock         |
| SDO/SDO      | SPI Data Out      |
| SD_CLK       | SPI Clock         |
| SCS/CMD      | SPI Chip Select / Command |
| SD_CMD       | SPI Command       |
| SWPISD3      | SPI Data 3        |
| SHD/SD2      | SPI Data 2 / Hold |
| SD_DATA_2    | SPI Data 2        |
| VDDPST       | Power supply      |
| FLASH J]     | Flash Chip        |

*Figure 1-6. ESP8266EX Flash Interface*


## Crystal Oscillator

The ESP8266EX supports crystal oscillators of 40 MHz, 26 MHz, and 24 MHz. It is important to select the correct type of crystal oscillator in the ESP Flash Download Tool.

In the circuit design, capacitors C1 and C2 are connected to ground and are added to the input and output terminals of the crystal oscillator respectively. The capacitor values can range from 6 pF to 22 pF, but the exact values should be determined by testing and adjusting the overall circuit performance. The crystal precision should be within ±10 PPM.

| Pin Name   | Description       |
|------------|-------------------|
| VDDD       | Power supply      |
| XTAL_IN    | Crystal oscillator input |
| XTAL_OUT   | Crystal oscillator output|
| UOTXD      | UART TX           |
| UORXD      | UART RX           |
| XIN        | Crystal input     |
| GND        | Ground            |
| XOUT       | Crystal output    |

*Figure 1-7. ESP8266EX Crystal Oscillator*

**Notice:**

Defects in the craftsmanship of the crystal oscillators, such as high frequency deviation and unstable working temperature, may cause malfunction of the ESP8266EX and degrade overall performance.

---

*Page 14*