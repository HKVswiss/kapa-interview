# Page 16

## Text from PDF

Espressif


1. ESP8266EX

(GPIO15), U0CTS (GPIO13). After the exchange, GPIO15 and GPIO13 will be connected
respectively to MCU_RXD and MCU_TXD as swapped U0TXD and U0RXD for serial
communication. For reference design, please refer to Figure 1-10b.

Figure 1-10b. ESP8266EX UART SWAP

GPIO15, the strapping pin of ESP8266EX, needs to be at low-voltage level when
the chip is powered on. Thus, while the system is powered on, to make sure
GPIO15 won't be pulled-up externally, which will cause the system mistakenly
entering boot mode, an isolation circuit is added. As shown in Figure 1-10b, when
the system is powered on, Q1 is switched off by default and GPIO15 is actually
disconnected from MCU_RXD. After the program starts to run, Q1 can be turned
on by GPIO5, then GPIO15 is connected to MCU_RXD, which enables power-on
isolation of GPIO15.

The IO of the ESP8266EX is a 3.3 V logic level. In the case of serial communication
with a 5 V CMOS logic system, a level switch circuit needs to be added externally.
See Figure 1-10c.

11/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



## OCR Text

1. ESP8266EX

(GPIO15), UOCTS (GPIO13). After the exchange, GPIO15 and GPIO13 will be connected

respectively to MCU_RXD and MCU_TXD as swapped UOTXD and UORXD for serial

communication. For reference design, please refer to Figure 1-10b.

3Vv3

R1

10K

MCU_TXD

GPIO13_RX

GPIO15_TX

MCU_RXD ait

GPIO5

R2

R3

R4

100K

10K

10K

3Vv3

GND

GND

Figure 1-10b. ESP8266EX UART SWAP

GPIO15, the strapping pin of ESP8266EX, needs to be at low-voltage level when

the chip is powered on. Thus, while the system is powered on, to make sure

GPIO15 won't be pulled-up externally, which will cause the system mistakenly

entering boot mode, an isolation circuit is added. As shown in Figure 1-10b, when

the system is powered on, Q1 is switched off by default and GPIO15 is actually

disconnected from MCU_RXD. After the program starts to run, Q1 can be turned

on by GPIO5, then GPIO15 is connected to MCU_RXD, which enables power-on

isolation of GPIO15.

The IO of the ESP8266EX is a 3.3 V logic level. In the case of serial communication

with a 5 V CMOS logic system, a level switch circuit needs to be added externally.

See Figure 1-10c.

11/32

Submit Documentation Feedback

2024.10

Espressif

## Tables

1. ESP8266EX
(GPIO15), UOCTS (GPIO13). After the exchange, GPIO15 and GPIO13 will be connected
respectively to MCU_RXD and MCU_TXD as swapped UOTXD and UORXD for serial
communication. For reference design, please refer to Figure 1-10b.
3Vv3
R1
10K
MCU_TXD GPIO13_RX
GPIO15_TX MCU_RXD ait
GPIO5
R2 R3 R4
100K 10K 10K
3Vv3 GND GND
Figure 1-10b. ESP8266EX UART SWAP
GPIO15, the strapping pin of ESP8266EX, needs to be at low-voltage level when
the chip is powered on. Thus, while the system is powered on, to make sure
GPIO15 won't be pulled-up externally, which will cause the system mistakenly
entering boot mode, an isolation circuit is added. As shown in Figure 1-10b, when
the system is powered on, Q1 is switched off by default and GPIO15 is actually
disconnected from MCU_RXD. After the program starts to run, Q1 can be turned
on by GPIO5, then GPIO15 is connected to MCU_RXD, which enables power-on
isolation of GPIO15.
The IO of the ESP8266EX is a 3.3 V logic level. In the case of serial communication
with a 5 V CMOS logic system, a level switch circuit needs to be added externally.
See Figure 1-10c.
11/32
Submit Documentation Feedback 2024.10 Espressif


---

