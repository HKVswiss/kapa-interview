# ESP-LAUNCHER Power Supply and Test Module Schematics

## 2.3.2. 5V Power Supply

### ESP-LAUNCHER 5V Power Supply Schematics

- Components include:
  - SY8088 voltage regulator
  - 22µH inductor
  - Various resistors (e.g., 2kΩ, 680kΩ, 150kΩ)
  - Capacitors (e.g., 22µF)
  - Toggle switch
  - 5V Power LED indicator
  - Connections for RST, GND, and 5V output

```plaintext
Figure 2-3. ESP-LAUNCHER 5V Power Supply Schematics
```

## 2.3.3. Test Module

### ESP-LAUNCHER Test Module Schematics

- Includes ESP_Test board with connections:
  - GPIO pins (GPIO0, GPIO1, GPIO2, GPIO5, GPIO12, GPIO15, etc.)
  - UART pins (UOTXD, UORXD)
  - SPI pins (SPI0)
  - Power supply pins (VDD33, VOP33, VPPA3)
  - Ground (GND) connections
- Compatible with ESP_WROOM-01/02 2.0 and ESP8266EX Module 1.27

```plaintext
Figure 2-4. ESP-LAUNCHER Test Module Schematics
```

---

*Page 32*