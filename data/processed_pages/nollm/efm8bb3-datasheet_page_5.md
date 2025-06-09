# Page 6

## Text from PDF

# **Table of Contents**

**1. Feature List .** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 2**

**2. Ordering Information** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 3**

**3. System Overview .** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 9**

3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

3.2 Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .10

3.3 I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .10

3.4 Clocking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .11

3.5 Counters/Timers and PWM . . . . . . . . . . . . . . . . . . . . . . . . . .11

3.6 Communications and Other Digital Peripherals . . . . . . . . . . . . . . . . . . .12

3.7 Analog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .15

3.8 Reset Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16

3.9 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16

3.10 Bootloader . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .17

**4. Electrical Specifications** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 19**

4.1 Electrical Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . .19

4.1.1 Recommended Operating Conditions . . . . . . . . . . . . . . . . . . . . .19
4.1.2 Power Consumption. . . . . . . . . . . . . . . . . . . . . . . . . . .20
4.1.3 Reset and Supply Monitor. . . . . . . . . . . . . . . . . . . . . . . . .22
4.1.4 Flash Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . .23
4.1.5 Power Management Timing . . . . . . . . . . . . . . . . . . . . . . . .23

4.1.6 Internal Oscillators . . . . . . . . . . . . . . . . . . . . . . . . . . .24

4.1.7 External Clock Input. . . . . . . . . . . . . . . . . . . . . . . . . . .24

4.1.8 External Oscillator . . . . . . . . . . . . . . . . . . . . . . . . . . .25

4.1.9 ADC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .26

4.1.10 Voltage Reference . . . . . . . . . . . . . . . . . . . . . . . . . . .29
4.1.11 Temperature Sensor . . . . . . . . . . . . . . . . . . . . . . . . . .30
4.1.12 1.8 V Internal LDO Voltage Regulator . . . . . . . . . . . . . . . . . . . .30

4.1.13 DACs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .31

4.1.14 Comparators . . . . . . . . . . . . . . . . . . . . . . . . . . . . .32
4.1.15 Configurable Logic . . . . . . . . . . . . . . . . . . . . . . . . . . .33

4.1.16 Port I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .34

4.1.17 SMBus. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .35

4.1.18 SPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .37

4.2 Thermal Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . .39

4.3 Absolute Maximum Ratings. . . . . . . . . . . . . . . . . . . . . . . . . .40

**5. Typical Connection Diagrams** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **.** **. 41**

5.1 Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .41

5.2 Debug . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .42

5.3 Other Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . .42

**silabs.com** | Building a more connected world. Rev. 1.5 | 6



## OCR Text

Table of Contents

1. Feature List

2. Ordering Information

3. System Overview

3.1

Introduction

oo WN

3.2

Power

10

3.3

vO

10

3.4

Clocking

11

3.5

Counters/Timers and PWM

11

3.6

Communications and Other Digital Peripherals

12

3.7

Analog

15

3.8

Reset Sources

16

3.9

Debugging

16

3.10 Bootloader

17

Electrical Specifications

19

4.1 Electrical Characteristics

19

4.1.1

Recommended Operating Conditions .

19

41.2

Power Consumption

20

4.1.3

Reset and Supply Monitor

22

4.1.4

Flash Memory.

23

41.5

Power Management Timing

23

4.1.6

Internal Oscillators

24

41.7

External Clock Input

24

41.8

External Oscillator

25

41.9

ADC

26

4.1.10

29

Voltage Reference .

4.1.11

Temperature Sensor

30

4.1.12

1.8 V Internal LDO Voltage Regulator

30

4.1.13

DACs

31

4.4.14

Comparators

32

4.1.15

Configurable Logic

33

4.1.16

Port I/O

34

4.1.17

SMBus

35

4.1.18

SPI

37

4.2 Thermal Conditions

39

4.3 Absolute Maximum Ratings

40

5. Typical Connection Diagrams

4

5.1 Power

a1

5.2 Debug

42

5.3 Other Connections.

42

1m | Building a more connected world

Rev. 1.5] 6

## Tables

Table of Contents
1. Feature List
2. Ordering Information
3. System Overview
3.1 Introduction
oo
WN
3.2 Power 10
3.3 vO 10
3.4 Clocking 11
3.5 Counters/Timers and PWM 11
3.6 Communications and Other Digital Peripherals 12
3.7 Analog 15
3.8 Reset Sources 16
3.9 Debugging 16
3.10 Bootloader 17
Electrical Specifications 19
4.1 Electrical Characteristics 19
4.1.1 Recommended Operating
Conditions .
19
41.2 Power Consumption 20
4.1.3 Reset and Supply Monitor 22
4.1.4 Flash Memory. 23
41.5 Power Management
Timing
23
4.1.6 Internal Oscillators 24
41.7 External Clock Input 24
41.8 External Oscillator 25
41.9 ADC 26
4.1.10 29 Voltage Reference .
4.1.11 Temperature Sensor 30
4.1.12 1.8 V Internal LDO Voltage
Regulator
30
4.1.13 DACs 31
4.4.14 Comparators 32
4.1.15 Configurable Logic 33
4.1.16 Port I/O 34
4.1.17 SMBus 35
4.1.18 SPI 37
4.2 Thermal Conditions 39
4.3 Absolute Maximum Ratings 40
5. Typical Connection Diagrams 4
5.1 Power a1
5.2 Debug 42
5.3 Other Connections. 42
1m | Building a more connected world Rev. 1.5] 6


---

