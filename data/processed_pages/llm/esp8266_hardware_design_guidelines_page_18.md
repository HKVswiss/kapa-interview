# 1. ESP8266EX

**Note:**

- Please refer to the design of ESP-WROOM-S2 for further details.
- UART Download Mode: Jumper J1 short circuit.
- SDIO Boot Mode: Jumper J1 open circuit.
- If the external host CPU's SDIO or SPI interface has been pulled up, the optional pull-up resistor can be omitted.

## 1.6. PCB Layout Design

This chapter introduces the ESP8266EX PCB layout design by using the ESP8266EX as an example. The PCB layout design guidelines are applicable to cases when:

- The ESP8266EX module functions as a standalone device.
- The ESP8266EX functions as a slave device.

### Figure 1-12. ESP8266EX PCB Layout

### 1.6.1. General Principles of PCB Layout Design

The PCB has four layers:

- The first layer is the TOP layer for signal lines and components.
- The second layer is the GND layer, where no signal lines are laid to ensure a complete GND plane.

---
*Page 19*