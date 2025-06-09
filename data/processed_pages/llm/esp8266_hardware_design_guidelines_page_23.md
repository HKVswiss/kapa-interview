# ESP8266EX

## 1.6.4. ESP8266EX as a Slave Device

When ESP8266EX works as a slave device in a system, users need to pay more attention to signal integrity in the PCB design. It is important to keep ESP8266EX away from the interferences caused by the complexity of the system and an increased number of high-frequency signals. The mainboard of a PAD or TV Box is used as an example to provide guidelines for the PCB layout and design.

### PCB/TV Box Layout

The digital signal between the CPU and the DDR is the major producer of high-frequency noise and interferes with Wi-Fi radio from the air. Below are the key points when designing the PCB layout:

- As shown in Figure 1-18, ESP8266EX should be placed near the edge of the PCB and away from the CPU and DDR, the main high-frequency noise sources.


---

**Figures:**

- Figure 1-17. ESP8266EX RF Design
- Figure 1-18. PCB/TV Box Layout


*Page 24*