# ESP8266EX UART Voltage-level Switch Circuit

Below is the UART voltage-level switch circuit for the ESP8266EX:

```
5V0   3V3   3V3
Rt    R2    R3
10K   10K   40K

MCU_TXD ---- GPIO13_RX
MCU_RXD ---- GPIO15_TX

Ra    Rs    Rb    Rt
10K   100K  10K   10K

GND
```

**Figure 1-10c. UART Voltage-level Switch circuit**

> **Notice:**
> - When using GPIO13 and GPIO15 as serial communication pins, please pay attention to the direction of sending and receiving information. They need to be connected correctly to the MCU UART pins.
> - When using the AT firmware, the UART GPIO is already configured (refer to [Hardware Connection](https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp8266/Get_Started/Hardware_connection.html)). It is recommended to use the default configuration.

---

*Page 17*