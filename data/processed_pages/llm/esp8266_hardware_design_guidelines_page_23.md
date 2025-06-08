# ESP8266EX RF Design and PCB Layout Guidelines

## 1. ESP8266EX

### Figure 1-17. ESP8266EX RF Design

## 1.6.4. ESP8266EX as a Slave Device

When ESP8266EX works as a slave device in a system, users need to pay more attention to signal integrity in the PCB design. It is important to keep ESP8266EX away from the interferences caused by the complexity of the system and an increased number of high-frequency signals. We use the mainboard of a PAD or TV Box as an example here to provide guidelines for the PCB layout and design.

### Figure 1-18. PCB/TV Box Layout

The digital signal between the CPU and the DDR is the major producer of high-frequency noise and interferes with Wi-Fi radio from the air. Below are the key points when designing the PCB layout:

- As shown in Figure 1-18, ESP8266EX should be placed near the edge of the PCB and away from the CPU and DDR, the main high-frequency noise sources.

---

*Page 24*