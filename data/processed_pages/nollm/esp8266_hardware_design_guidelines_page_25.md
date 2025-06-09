# Page 26

## Text from PDF

1. ESP8266EX

This problem is caused by improper layout and can be solved by re-layout. See Section 1.5
for details.

3. Q: When ESP8266EX sends data packages, the power value is much higher or

lower than the target power value, and the EVM is relatively poor.

Analysis:

The disparity between the tested value and the target value may be due to signal reflflection
caused by the impedance mismatch on the transmission line connecting the RF pin and the
antenna.

Solution:

Match the antenna’s impedance with the reserved π-type circuit on the RF trace, so that
the resistance from the RF pin to the antenna approaches (39-j6)Ω.

4. Q: TX performance is not bad, but the Rx sensitivity is low.

Analysis:

Good Tx performance indicates proper RF impedance matching. External coupling to the
antenna can affect the Rx performance. For instance, the crystal oscillator signal harmonics
could couple to the antenna. If ESP8266EX serves as slave device, there will be other highfrequency interference sources on the board, which may affect the Rx performance.

Solution:

Keep the antenna away from crystal oscillators. Do not route high-frequency signal traces
close to the RF trace.
# 1.7. Typical Application


1.7.1. UART to Wi-Fi Smart Device

The two UART interfaces are defifined in Table 1-3.

Table 1-3. Pin defifinitions of UART Interfaces

Category Pin defifinition Function

*ifi*


AT+ instruction and examples are provided here: *[http://www.espressif.com/en/support/](http://www.espressif.com/en/support/download/documents?keys=&field_type_tid%5B%5D=14)*
*[download/documents?keys=&feld_type_tid%5B%5D=14](http://www.espressif.com/en/support/download/documents?keys=&field_type_tid%5B%5D=14)* *ifi*

Application example: ESP8266EX development board (please see Chapter 2).

1.7.2. Sensor

ESP8266EX can be used for developing sensor products by using the I2C interface. The


*ifi*

Espressif


*ifi*

21/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



## OCR Text

1. ESP8266EX

This problem is caused by improper layout and can be solved by re-layout. See Section 1.5

for details.

3. Q: When ESP8266EX sends data packages, the power value is much higher or

lower than the target power value, and the EVM is relatively poor.

Analysis:

The disparity between the tested value and the target value may be due to signal reflection

caused by the impedance mismatch on the transmission line connecting the RF pin and the

antenna.

Solution:

Match the antenna’s impedance with the reserved r1-type circuit on the RF trace, so that

the resistance from the RF pin to the antenna approaches (39-j6)Q.

4. Q: TX performance is not bad, but the Rx sensitivity is low.

Analysis:

Good Tx performance indicates proper RF impedance matching. External coupling to the

antenna can affect the Rx performance. For instance, the crystal oscillator signal harmonics

could couple to the antenna. If ESP8266EX serves as slave device, there will be other high-

frequency interference sources on the board, which may affect the Rx performance.

Solution:

Keep the antenna away from crystal oscillators. Do not route high-frequency signal traces

close to the RF trace.

1.7. Typical Application

1.7.41

UART to Wi-Fi Smart Device

The two UART interfaces are defined in Table 1-3.

Table 1-3. Pin definitions of UART Interfaces

Category

Pin definition

Function

UARTO.

(Pin 25) UORXD+ (Pin 26) UOTXD

Receive and transmit user's data packages.

UART1

Print information.

(Pin 14) GPIO2 (U1TXD)

AT+ instruction and examples are provided here: htto:/Avww.espressif.com/en/support/

download/documents ?keys=&field_type tid%5B%5D=14

Application example: ESP8266EX development board (please see Chapter 2).

1.7.2. Sensor

ESP8266EX can be used for developing sensor products by using the I2C interface. The

21/32

Submit Documentation Feedback

2024.10

Espressif

## Tables

1. ESP8266EX
This problem is caused by improper layout and can be solved by re-layout. See Section 1.5
for details.
3. Q: When ESP8266EX sends data packages, the power value is much higher or
lower than the target power value, and the EVM is relatively poor.
Analysis:
The disparity between the tested value and the target value may be due to signal reflection
caused by the impedance mismatch on the transmission line connecting the RF pin and the
antenna.
Solution:
Match the antenna’s impedance with the reserved r1-type circuit on the RF trace, so that
the resistance from the RF pin to the antenna approaches (39-j6)Q.
4. Q: TX performance is not bad, but the Rx sensitivity is low.
Analysis:
Good Tx performance indicates proper RF impedance matching. External coupling to the
antenna can affect the Rx performance. For instance, the crystal oscillator signal harmonics
could couple to the antenna. If ESP8266EX serves as slave device, there will be other high-
frequency interference sources on the board, which may affect the Rx performance.
Solution:
Keep the antenna away from crystal oscillators. Do not route high-frequency signal traces
close to the RF trace.
1.7. Typical Application
1.7.41 UART to Wi-Fi Smart Device
The two UART interfaces are defined in Table 1-3.
Table 1-3. Pin definitions of UART Interfaces
Category Pin definition Function
UARTO. (Pin 25) UORXD+ (Pin 26) UOTXD Receive and transmit user's data packages.
UART1 Print information. (Pin 14) GPIO2 (U1TXD)
AT+ instruction and examples are provided here: htto:/Avww.espressif.com/en/support/
download/documents ?keys=&field_type tid%5B%5D=14
Application example: ESP8266EX development board (please see Chapter 2).
1.7.2. Sensor
ESP8266EX can be used for developing sensor products by using the I2C interface. The
21/32
Submit Documentation Feedback 2024.10 Espressif


---

