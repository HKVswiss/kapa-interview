# 3. ESP8266EX Module

Espressif provides two types of modules, the SMD module (ESP-WROOM-02) and the DIP module (ESP-WROOM-01). The modules have been improved to achieve optimum RF functionality. It is recommended that users use these modules for testing or further development.

## 3.1. ESP-WROOM-S2

- Module size: 16 ± 0.2 mm x 23 ± 0.2 mm x 3 ± 0.15 mm (see Figure 1-1).
- Flash: 2-MB SPI flash connected to HSPI, package size SOP 8-150 mil.
- On-board PCB antenna gain: 2 dBi.
- Functionality: Works as the SDIO/SPI slave with SPI speed up to 8 Mbps.

### Figure 3-1. ESP-WROOM-S2 Module

```
+-------+-------+-------+-------+-------+-------+-------+-------+
| ANTI  | SYN   | eco   | sa    | €N    | GND   | (Gna) | YGRY  |
| wee   | «     | ral   | ADC_IN| v3    | U2    | RST   | 1016  |
| z     | 105   | 10    | TXD   | 10:   |       | RXD   | 100   |
| ee    | os    | (ee 2 | Tui\rd2| 104   | we    | a8    | S00/MISO|
| /109  | .?    | ie    | ee    | SCLK  | /c    | Ge    | U3    |
| GND   | CMD/  | wos:  |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
```

For details of ESP-WROOM-S2, please refer to the *ESP-WROOM-S2 Datasheet*.

## 3.2. ESP-WROOM-02

- Module size: 18 ± 0.2 mm x 20 ± 0.2 mm x 3 ± 0.15 mm.
- Flash: SPI flash with package size SOP 8-150 mil.
- On-board PCB antenna gain: 2 dBi.

---

*Page 34*