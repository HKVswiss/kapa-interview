# EFM8BB3 Data Sheet

## System Overview

### 3.10 Bootloader

All devices come pre-programmed with a UART0 bootloader. This bootloader resides in the code security page, which is the last page of code flash; it can be erased if it is not needed.

The byte before the Lock Byte is the Bootloader Signature Byte. Setting this byte to a value of 0xA5 indicates the presence of the bootloader in the system. Any other value in this location indicates that the bootloader is not present in flash.

When a bootloader is present, the device will jump to the bootloader vector after any reset, allowing the bootloader to run. The bootloader then determines if the device should stay in bootload mode or jump to the reset vector located at 0x0000. When the bootloader is not present, the device will jump to the reset vector of 0x0000 after any reset.

Silicon Labs recommends the bootloader be disabled and the flash memory locked after the production programming step in applications where code security is a concern. More information about the factory bootloader protocol, usage, customization, and best practices can be found in *AN945: EFM8 Factory Bootloader User Guide*. Application notes can be found on the Silicon Labs website (www.silabs.com/8bit-appnotes) or within Simplicity Studio by using the **Application Notes** tile.

---

### Figure 3.2. Flash Memory Map with Bootloader — 62.5 KB Devices

```
0xFFFF  Read-Only 64 Bytes
0xFFC0
0xFFBF  Reserved
0xFC00
0xFBFF  Lock Byte
0xFBFE  Bootloader Signature Byte
0xFBFD  Code Security Page
Bootloader
0xFA00  (1 x 512 Byte pages)
<— Bootloader Vector
0xF0FF  62 KB Code (124 x 512 Byte pages)
0x0000  <— Reset Vector
```

---

### Table 3.2. Summary of Pins for Bootloader Communication

| Bootloader | Pins for Bootload Communication |
|------------|--------------------------------|
| UART       | TX – P0.4                      |
| UART       | RX – P0.5                      |

---

*Page 17*