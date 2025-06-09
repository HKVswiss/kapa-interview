# ESP8266EX

I2C works in the master mode and can connect to multiple sensors. The slave devices are identified through the addressing mode, as each slave device has a unique address.

The sensor products send real-time data to ESP8266EX via the I2C interface, and ESP8266EX uploads the data to the server wirelessly. Users can acquire information from the server through the mobile app when their mobile phones connect to the internet.

## 1.7.3. Smart Light

ESP8266EX can be used for developing smart home products such as smart lights by using the PWM and infrared interfaces. The three PWM interfaces control red, blue, and green LEDs respectively. The minimal PWM duty ratio is 1/214. In addition, the infrared interface allows specific control on LEDs, such as reset, power on/off, color switch, etc.

## 1.7.4. Smart Plug

ESP8266EX can be used for developing smart plug products. The GPIOs control the power switch through the high/low-level switch and connection/disconnection of relay. A smart plug requires three modules:

- 220 V to 3.3 V power conversion module
- ESP8266EX Wi-Fi module
- Relay control module

---

*Page 27*