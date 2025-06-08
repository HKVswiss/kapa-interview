EFM8BB3 Data Sheet
Electrical Specifications

**4.1.2 Power Consumption**

**Table 4.2. Power Consumption**






|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 49 MHz (HFOSC1)2<br>SYSCLK|—|5|14.4|mA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 24.5 MHz (HFOSC0)2<br>SYSCLK|—|4.2|5|mA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 1.53 MHz (HFOSC0)2<br>SYSCLK|—|625|820|μA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 80 kHz3<br>SYSCLK|—|155|310|μA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 49 MHz (HFOSC1)2<br>SYSCLK|—|3.8|11.8|mA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 24.5 MHz (HFOSC0)2<br>SYSCLK|—|3.14|3.8|mA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 1.53 MHz (HFOSC0)2<br>SYSCLK|—|520|725|μA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 80 kHz3<br>SYSCLK|—|135|315|μA|
|Suspend Mode-Core halted and<br>high frequency clocks stopped,<br>Supply monitor off.|I<br>DD|LFO Running|—|125|320|μA|
|Suspend Mode-Core halted and<br>high frequency clocks stopped,<br>Supply monitor off.|I<br>DD|LFO Stopped|—|120|300|μA|
|Snooze Mode-Core halted and<br>high frequency clocks stopped.<br>Regulator in low-power state, Sup-<br>ply monitor off.|I<br>DD|LFO Running|—|23|190|μA|
|Snooze Mode-Core halted and<br>high frequency clocks stopped.<br>Regulator in low-power state, Sup-<br>ply monitor off.|I<br>DD|LFO Stopped|—|19|186|μA|
|Stop Mode—Core halted and all<br>clocks stopped,Internal LDO On,<br>Supply monitor off.|I<br>DD||—|120|300|μA|
|Shutdown Mode—Core halted and<br>all clocks stopped,Internal LDO<br>Off, Supply monitor off.|I<br>DD||—|0.2|0.91|μA|
|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 49 MHz (HFOSC1)2<br>SYSCLK|—|5|14.4|mA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 24.5 MHz (HFOSC0)2<br>SYSCLK|—|4.2|5.2|mA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 1.53 MHz (HFOSC0)2<br>SYSCLK|—|625|1280|μA|
|Normal Mode-Full speed with code<br>executing from flash|I<br>DD|F = 80 kHz3<br>SYSCLK|—|155|765|μA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 49 MHz (HFOSC1)2<br>SYSCLK|—|3.8|11.8|mA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 24.5 MHz (HFOSC0)2<br>SYSCLK|—|3.14|4.1|mA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 1.53 MHz (HFOSC0)2<br>SYSCLK|—|520|1175|μA|
|Idle Mode-Core halted with periph-<br>erals running|I<br>DD|F = 80 kHz3<br>SYSCLK|—|135|750|μA|
|Suspend Mode-Core halted and<br>high frequency clocks stopped,<br>Supply monitor off.|I<br>DD|LFO Running|—|125|775|μA|
|Suspend Mode-Core halted and<br>high frequency clocks stopped,<br>Supply monitor off.|I<br>DD|LFO Stopped|—|120|755|μA|


**silabs.com** | Building a more connected world. Rev. 1.5 | 20



EFM8BB3 Data Sheet

Electrical Specifications

4.1.2 Power Consumption

Table 4.2. Power Consumption

Parameter

Symbol

Test Con

ion

Typ

Max

Unit

Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)

Normal Mode-Full speed with code

'bp

14.4

Fsyscik = 49 MHz (HFOSC1)2

executing from flash

Fsysoik = 24.5 MHz (HFOSCO)2

42

Fsysoik = 1.53 MHz (HFOSCO)2

625

820

Fsyscuk = 80 kHz?

155

310

Idle Mode-Core halted with periph-

'bp

Fsysoik = 49 MHz (HFOSC1)2

3.8

11.8

:

erals running

Fsysoik = 24.5 MHz (HFOSCO)2

3.14

3.8

Fsysctk = 1.53 MHz (HFOSCO)?

520

725

pA

Fsyscik = 80 kHz?

135

315

pA

Suspend Mode-Core halted and

lop

LFO Running

125

320

pA

high frequency clocks stopped,

LFO Stopped

120

300

pA

Supply monitor off.

Snooze Mode-Core halted and

lop

LFO Running

23

190

pA

high frequency clocks stopped.

LFO Stopped

19

186

pA

Regulator in low-power state, Sup-

ply monitor off.

Stop Mode—Core halted and all

lop

120

300

pA

clocks stopped,|nternal LDO On,

Supply monitor off.

Shutdown Mode—Core halted and

0.2

0.91

lop

pA

all clocks stopped,Internal LDO

Off, Supply monitor off.

Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)

14.4

3

Normal Mode-Full speed with code

'bp

Fsysoik = 49 MHz (HFOSC1)2

executing from flash

Fsysoik = 24.5 MHz (HFOSCO)2

42

5.2

3

625

1280

Fsysctk = 1.53 MHz (HFOSCO)?

Fsyscuk = 80 kHz?

155

765

3.8

11.8

2 BS

Idle Mode-Core halted with periph-

'bp

Fsysoik = 49 MHz (HFOSC1)2

erals running

Fsyscik = 24.5 MHz (HFOSCO)?

3.14

41

3

520

1175

Fsysctk = 1.53 MHz (HFOSCO)?

pA

Fsyscik = 80 kHz?

135

750

pA

lop

125

775

Suspend Mode-Core halted and

LFO Running

pA

high frequency clocks stopped,

120

755

Supply monitor off.

LFO Stopped

pA

silabs.com | Building a more connected world.

Rev. 1.5 | 20

EFM8BB3 Data Sheet
Electrical Specifications
4.1.2 Power Consumption
Table 4.2. Power Consumption
Parameter Symbol Test Con ion Typ Max Unit
Digital Core Supply Current (G-grade devices, -40 °C to +85 °C)
Normal Mode-Full speed with code 'bp 14.4 Fsyscik = 49 MHz (HFOSC1)2
executing from flash
Fsysoik = 24.5 MHz (HFOSCO)2 42
Fsysoik = 1.53 MHz (HFOSCO)2 625 820
Fsyscuk = 80 kHz? 155 310
Idle Mode-Core halted with periph- 'bp Fsysoik = 49 MHz (HFOSC1)2 3.8 11.8
:
erals running
Fsysoik = 24.5 MHz (HFOSCO)2 3.14 3.8
Fsysctk = 1.53 MHz (HFOSCO)? 520 725 pA
Fsyscik = 80 kHz? 135 315 pA
Suspend Mode-Core halted and lop LFO Running 125 320 pA
high frequency clocks stopped,
LFO Stopped 120 300 pA Supply monitor off.
Snooze Mode-Core halted and lop LFO Running 23 190 pA
high frequency clocks stopped.
LFO Stopped 19 186 pA Regulator in low-power state, Sup-
ply monitor off.
Stop Mode—Core halted and all lop 120 300 pA
clocks stopped,|nternal LDO On,
Supply monitor off.
Shutdown Mode—Core halted and 0.2 0.91 lop pA
all clocks stopped,Internal LDO
Off, Supply monitor off.
Digital Core Supply Current (I-grade or A-grade devices, -40 °C to +125 °C)
14.4 3 Normal Mode-Full speed with code 'bp Fsysoik = 49 MHz (HFOSC1)2
executing from flash
Fsysoik = 24.5 MHz (HFOSCO)2 42 5.2 3
625 1280 Fsysctk = 1.53 MHz (HFOSCO)?
Fsyscuk = 80 kHz? 155 765
3.8 11.8 2
BS
Idle Mode-Core halted with periph- 'bp Fsysoik = 49 MHz (HFOSC1)2
erals running
Fsyscik = 24.5 MHz (HFOSCO)? 3.14 41 3
520 1175 Fsysctk = 1.53 MHz (HFOSCO)? pA
Fsyscik = 80 kHz? 135 750 pA
lop 125 775 Suspend Mode-Core halted and LFO Running pA
high frequency clocks stopped,
120 755 Supply monitor off. LFO Stopped pA
silabs.com | Building a more connected world. Rev. 1.5 | 20


---Page 20 

