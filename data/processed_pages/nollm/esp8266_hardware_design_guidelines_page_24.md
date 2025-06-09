# Page 25

## Text from PDF

1. ESP8266EX

distance between the chip and the noise sources decreases the interference and
reduces the coupled noise.

         - It is suggested that a 100 Ω ~ 200 Ω series resistor is added to the six signal traces
when ESP8266EX communicates with the CPU via SDIO to decrease the drive

current and any interferences, and also to eliminate the sequencing problem caused
by the inconsistent length of the SDIO traces.

         - On-board PCB antenna is not recommended, as it receives much interference and
coupling noise, both of which impact the RF performance. We suggest that you use
an external antenna which should be directed away from the PCB board via a cable,
in order to weaken the high frequency interference with Wi-Fi.

         - The high-frequency signal traces between the CPU and associated memory should
be routed strictly ac- cording to the routing guidelines (please refer to the DDR trace
routing guidelines). CLK and data/addr lines should be laid underground.

         - The GND of the Wi-Fi circuit and that of other high-power devices should be
separated and connected through wires if there are high-power components, such as
motors, in the design.

         - The antenna should be kept away from high-frequency noise sources, such as LCD,
HDMI, Camera Sensor, USB, etc.

1.6.5. Typical Layout Problems and Solutions

1. Q: The current ripple is not large, but the Tx performance of RF is rather poor.

Analysis:

Ripple has a strong impact on the performance of RF Tx. It should be noted that ripple
must be tested when ESP8266EX is in the normal working mode. The ripple increases
when the power gets high. Generally, the ripple should be <80 mV when sending 11n
MCS7 packets, and <120 mV when sending 11b packets.

Solution:

Add a 10-μF fifilter capacitor to the branch of source circuit (ESP8266EX AVDD pin). The 10μF capacitor should be adjacent to the VDDA pin.

2. Q: The power ripple is small, but the Tx performance is poor.

Analysis:

The RF Tx performance can be affected not only by power ripples, but also by the crystal
oscillator itself. Poor quality and big frequency offsets (more than ±40 ppm) of the crystal
oscillator decrease the RF Tx performance. The crystal oscillator clock may be corrupted
by other interfering signals, such as high-speed output or input signals. Besides, sensitive
components or radiation components, such as inductors and antennas, may also decrease
the RF performance.

Solution:


Espressif


20/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



## OCR Text

1. ESP8266EX

distance between the chip and the noise sources decreases the interference and

reduces the coupled noise.

It is suggested that a 100 O ~ 200 O series resistor is added to the six signal traces

when ESP8266EX communicates with the CPU via SDIO to decrease the drive

current and any interferences, and also to eliminate the sequencing problem caused

by the inconsistent length of the SDIO traces.

On-board PCB antenna is not recommended, as it receives much interference and

coupling noise, both of which impact the RF performance. We suggest that you use

an external antenna which should be directed away from the PCB board via a cable

:

in order to weaken the high frequency interference with Wi-Fi.

The high-frequency signal traces between the CPU and associated memory should

be routed strictly ac- cording to the routing guidelines (please refer to the DDR trace

routing guidelines). CLK and data/addr lines should be laid underground.

The GND of the Wi-Fi circuit and that of other high-power devices should be

separated and connected through wires if there are high-power components, such as

motors, in the design.

The antenna should be kept away from high-frequency noise sources, such as LCD,

HDMI, Camera Sensor, USB, etc.

1.6.5. Typical Layout Problems and Solutions

1. Q: The current ripple is not large, but the Tx performance of RF is rather poor.

Analysis:

Ripple has a strong impact on the performance of RF Tx. It should be noted that ripple

must be tested when ESP8266EX is in the normal working mode. The ripple increases

when the power gets high. Generally, the ripple should be <80 mV when sending 11n

MCS7 packets, and <120 mV when sending 11b packets.

Solution:

Add a 10-uF filter capacitor to the branch of source circuit (ESP8266EX AVDD pin). The 10-

UF capacitor should be adjacent to the VDDA pin.

2. Q: The power ripple is small, but the Tx performance is poor.

Analysis:

The RF Tx performance can be affected not only by power ripples, but also by the crystal

oscillator itself. Poor quality and big frequency offsets (more than +40 ppm) of the crystal

oscillator decrease the RF Tx performance. The crystal oscillator clock may be corrupted

by other interfering signals, such as high-speed output or input signals. Besides, sensitive

components or radiation components, such as inductors and antennas, may also decrease

the RF performance.

Solution:

20/32

Submit Documentation Feedback

2024.10

Espressif

## Tables

1. ESP8266EX
distance between the chip and the noise sources decreases the interference and
reduces the coupled noise.
It is suggested that a 100 O ~ 200 O series resistor is added to the six signal traces
when ESP8266EX communicates with the CPU via SDIO to decrease the drive
current and any interferences, and also to eliminate the sequencing problem caused
by the inconsistent length of the SDIO traces.
On-board PCB antenna is not recommended, as it receives much interference and
coupling noise, both of which impact the RF performance. We suggest that you use
an external antenna which should be directed away from the PCB board via a cable
:
in order to weaken the high frequency interference with Wi-Fi.
The high-frequency signal traces between the CPU and associated memory should
be routed strictly ac- cording to the routing guidelines (please refer to the DDR trace
routing guidelines). CLK and data/addr lines should be laid underground.
The GND of the Wi-Fi circuit and that of other high-power devices should be
separated and connected through wires if there are high-power components, such as
motors, in the design.
The antenna should be kept away from high-frequency noise sources, such as LCD,
HDMI, Camera Sensor, USB, etc.
1.6.5. Typical Layout Problems and Solutions
1. Q: The current ripple is not large, but the Tx performance of RF is rather poor.
Analysis:
Ripple has a strong impact on the performance of RF Tx. It should be noted that ripple
must be tested when ESP8266EX is in the normal working mode. The ripple increases
when the power gets high. Generally, the ripple should be <80 mV when sending 11n
MCS7 packets, and <120 mV when sending 11b packets.
Solution:
Add a 10-uF filter capacitor to the branch of source circuit (ESP8266EX AVDD pin). The 10-
UF capacitor should be adjacent to the VDDA pin.
2. Q: The power ripple is small, but the Tx performance is poor.
Analysis:
The RF Tx performance can be affected not only by power ripples, but also by the crystal
oscillator itself. Poor quality and big frequency offsets (more than +40 ppm) of the crystal
oscillator decrease the RF Tx performance. The crystal oscillator clock may be corrupted
by other interfering signals, such as high-speed output or input signals. Besides, sensitive
components or radiation components, such as inductors and antennas, may also decrease
the RF performance.
Solution:
20/32
Submit Documentation Feedback 2024.10 Espressif


---

