# ESP8266EX

## Table 1-2. ESP8266EX Pin Definitions

| Pin Number | Pin Name       | Type | Description                                                                                  |
|------------|----------------|------|----------------------------------------------------------------------------------------------|
| 1          | VDDA           | p    | Analog Power 2.5 V ~ 3.6 V                                                                 |
| -          | RF antenna interface LNA | vO   | Chip output impedance = 39 + j6 Ω. It is suggested that users retain the mt-type matching network which matches the antenna. |
| -          | VDD3P3         |      | Amplifier Power 2.5 V ~ 3.6 V                                                               |
| -          | VDD_RTC        |      | NC (1.1 V)                                                                                   |
| -          | ADC pin (TOUT) |      | Can be used to test the power-supply voltage of VDD3P3 (Pin 3 and Pin 4) and the input power voltage of TOUT (Pin ?). These two functions cannot be used simultaneously. |
| -          | CHIP_EN        |      | Chip Enable: High = On, chip works properly; Low = Off, small current consumed                |
| -          | XPD_DCDC       | vO   | Deep-sleep wakeup (need to be connected to EXT_RSTB)                                        |
| 16         | GPIO16 (MTMS)  | vO   | GPIO 14; HSPI_CLK                                                                           |
| 10         | MTDI           | vO   | GPIO 12; HSPI_MISO                                                                          |
| -          | VDDPST         |      | Digital I/O Power Supply (1.8 V ~ 3.3 V)                                                    |
| 12         | MTCK           | vO   | GPIO 13; HSPI_MOSI; UART0_CTS                                                              |
| 13         | MTDO           | vO   | GPIO 15; HSPI_CS; UART0_RTS                                                                 |
| 14         | GPIO2          | vO   | UART1_TX during flash programming; GPIO2                                                   |
| 15         | GPIO0          | vO   | GPIO0; SPI_CS2                                                                             |
| 16         | GPIO4          | vO   | GPIO 4                                                                                      |
| 17         | VDDPST         |      | Digital I/O Power Supply (1.8 V ~ 3.3 V)                                                    |
| 18         | SDIO_DATA_2    | vO   | Connects to SD_D2 (Series R: 200 Ω); SPIHD; HSPIHD; GPIO 9                                  |
| 19         | SDIO_DATA_3    | vO   | Connects to SD_D3 (Series R: 200 Ω); SPIWP; HSPIWP; GPIO 10                                 |
| 20         | SDIO_CMD       | vO   | Connects to SD_CMD (Series R: 200 Ω); SPI_CS0; GPIO 11                                      |
| 21         | SDIO_CLK       | vO   | Connects to SD_CLK (Series R: 200 Ω); SPI_CLK; GPIO 6                                       |
| 22         | SDIO_DATA_0    | vO   | Connects to SD_DO (Series R: 200 Ω); SPI_MISO; GPIO 7                                       |
| 23         | SDIO_DATA_1    | vO   | Connects to SD_D1 (Series R: 200 Ω); SPI_MOSI; GPIO 8                                       |

---

*Page 9*