1. ESP8266EX

The center ground pad at the bottom of the chip should be connected to ground plane
through at least 9 ground vias.

Figure 1-15. ESP8266EX PCB Layout

1.6.3.2. Crystal Oscillator Design

The crystal oscillator should be placed as close to the XTAL pins as possible (without the
traces being too long). However, the crystal cannot be placed too close to the chip to
prevent the crystal from interfering with the chip, as Figure 1-15 shows. The recommended
distance is 0.8 mm (see Figure 1-16). However, the crystal cannot be too close to the chip
to prevent the crystal from interfering with the chip. The recommended distance is 0.8mm
(see Figure 1-16). It is good practice to use via stitching around the clock trace for low
ground-plane impedance.

There should be no vias on the input and output traces, which means the traces cannot
cross layers. In addition, the input and output traces should not be routed over one
another, not even on different layers.

Place the input and output bypass capacitors on the near left or right side of the chip. Do
not place them on the traces.

Do not route high-frequency digital signal lines under the crystal oscillator. It is best not to
route any signal line under the crystal oscillator. The larger the copper area on the top layer
is, the better. As the crystal oscillator is a sensitive component, do not place any magnetic
components nearby that may cause interference, for example, power-switching converter
components or unshielded inductors.


Espressif


17/32
*[Submit Documentation Feedback](https://www.espressif.com/en/company/documents/documentation_feedback?docId=2667&sections=&version=2.8)* 2024.10



1. ESP8266EX

The center ground pad at the bottom of the chip should be connected to ground plane

through at least 9 ground vias.

Cl

f+ EAN

Nag

mm

1S

|

x]

2c6,

_—

tt

aim

~ dlp

1 ea

=|

F

=

=

—=— = =aa=

mis

n

Lie)

a

Laer

|k

RS

Figure 1-15. ESP8266EX PCB Layout

1.6.3.2. Crystal Oscillator Design

The crystal oscillator should be placed as close to the XTAL pins as possible (without the

traces being too long). However, the crystal cannot be placed too close to the chip to

prevent the crystal from interfering with the chip, as Figure 1-15 shows. The recommended

distance is 0.8 mm (see Figure 1-16). However, the crystal cannot be too close to the chip

to prevent the crystal from interfering with the chip. The recommended distance is 0.8mm

(see Figure 1-16). It is good practice to use via stitching around the clock trace for low

ground-plane impedance.

There should be no vias on the input and output traces, which means the traces cannot

cross layers. In addition, the input and output traces should not be routed over one

another, not even on different layers.

Place the input and output bypass capacitors on the near left or right side of the chip. Do

not place them on the traces.

Do not route high-frequency digital signal lines under the crystal oscillator. It is best not to

route any signal line under the crystal oscillator. The larger the copper area on the top layer

is, the better. As the crystal oscillator is a sensitive component, do not place any magnetic

components nearby that may cause interference, for example, power-switching converter

components or unshielded inductors.

17/32

2024.10

Espressif

1. ESP8266EX
The center ground pad at the bottom of the chip should be connected to ground plane
through at least 9 ground vias.
Cl
f+
EAN
Nag
mm 1S
|
x] 2c6,
_—
tt
aim
~ dlp
1 ea =|
F
= =
—=— = =aa=
mis
n
Lie) a
Laer
|k
RS
Figure 1-15. ESP8266EX PCB Layout
1.6.3.2. Crystal Oscillator Design
The crystal oscillator should be placed as close to the XTAL pins as possible (without the
traces being too long). However, the crystal cannot be placed too close to the chip to
prevent the crystal from interfering with the chip, as Figure 1-15 shows. The recommended
distance is 0.8 mm (see Figure 1-16). However, the crystal cannot be too close to the chip
to prevent the crystal from interfering with the chip. The recommended distance is 0.8mm
(see Figure 1-16). It is good practice to use via stitching around the clock trace for low
ground-plane impedance.
There should be no vias on the input and output traces, which means the traces cannot
cross layers. In addition, the input and output traces should not be routed over one
another, not even on different layers.
Place the input and output bypass capacitors on the near left or right side of the chip. Do
not place them on the traces.
Do not route high-frequency digital signal lines under the crystal oscillator. It is best not to
route any signal line under the crystal oscillator. The larger the copper area on the top layer
is, the better. As the crystal oscillator is a sensitive component, do not place any magnetic
components nearby that may cause interference, for example, power-switching converter
components or unshielded inductors.
17/32
2024.10 Espressif


---Page 22 

