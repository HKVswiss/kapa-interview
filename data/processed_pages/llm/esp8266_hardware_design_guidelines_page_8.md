# ESP8266EX Pin Definitions

| Pin Number | Pin Name       | Type       | Description                                                                                      |
|------------|----------------|------------|--------------------------------------------------------------------------------------------------|
| 1          | VDDA           | Analog     | Power 2.5 V ~ 3.6 V                                                                              |
| -          | RF antenna     | Interface  | LNA vO Chip output impedance = 39 + j6 Ω. Suggested to retain the mt-type matching network.      |
| -          | VDD3P3         | Power      | Amplifier Power 2.5 V ~ 3.6 V                                                                   |
| -          | VDD_RTC        | NC         | (1.1 V) ADC pin. Can test power-supply voltage of TOUT and input power voltage of TOUT.          |
| -          | TOUT           | ADC        | VDD3P3 (Pin3 and Pin4) and input power voltage test pin. Cannot be used simultaneously with ADC. |
| -          | CHIP_EN        | Control    | Chip Enable: High = On (chip works properly), Low = Off (small current consumed)                   |
| -          | XPD_DCDC       | Control    | Deep-sleep wakeup (needs connection to EXT_RSTB)                                                |
| -          | GPIO16         | GPIO       | Deep-sleep wakeup pin                                                                            |
| 10         | MTMS           | GPIO 14    | HSPI_CLK                                                                                        |
| 11         | MTDI           | GPIO 12    | HSPI_MISO                                                                                       |
| 12         | VDDPST         | Power      | Digital I/O Power Supply (1.8 V ~ 3.3 V)                                                        |
| 13         | MTCK           | GPIO 13    | HSPI_MOSI; UART0_CTS                                                                            |
| 14         | MTDO           | GPIO 15    | HSPI_CS; UART0_RTS                                                                             |
| 15         | GPIO2          | GPIO       | UART1_TX during flash programming; GPIO2                                                       |
| 16         | GPIO0          | GPIO       | GPIO0; SPI_CS2                                                                                  |
| 17         | GPIO4          | GPIO       | GPIO 4                                                                                        |
| 18         | VDDPST         | Power      | Digital I/O Power Supply (1.8 V ~ 3.3 V)                                                        |
| 19         | SDIO_DATA_2    | GPIO 9     | Connects to SD_D2 (Series R: 200 Ω); SPIHD; HSPIHD                                            |
| 20         | SDIO_DATA_3    | GPIO 10    | Connects to SD_D3 (Series R: 200 Ω); SPIWP; HSPIWP                                            |
| 21         | SDIO_CMD       | GPIO 11    | Connects to SD_CMD (Series R: 200 Ω); SPI_CS0                                                  |
| 22         | SDIO_CLK       | GPIO 6     | Connects to SD_CLK (Series R: 200 Ω); SPI_CLK                                                  |
| 23         | SDIO_DATA_0    | GPIO 7     | Connects to SD_DO (Series R: 200 Ω); SPI_MISO                                                 |
| 24         | SDIO_DATA_1    | GPIO 8     | Connects to SD_D1 (Series R: 200 Ω); SPI_MOSI                                                 |

---

*Page 9*