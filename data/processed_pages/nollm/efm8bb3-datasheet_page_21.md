# Page 22

## Text from PDF

EFM8BB3 Data Sheet
Electrical Specifications

|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|Note:<br>1. Currents are additive. For example, where I is specified and the mode is not mutually exclusive, enabling the functions increa-<br>DD<br>ses supply current by the specified amount.<br>2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.<br>3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.<br>4. ADC0 power excludes internal reference supply current.<br>5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will<br>depend on sampling rate.<br>6. DAC supply current for each enabled DA and not including external load on pin.<br>7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.|



**4.1.3 Reset and Supply Monitor**

**Table 4.3. Reset and Supply Monitor**







|Parameter|Symbol|Test Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDD Supply Monitor Threshold|V<br>VDDM||1.95|2.05|2.15|V|
|Power-On Reset (POR) Threshold|V<br>POR|Rising Voltage on VDD|—|1.4|—|V|
|Power-On Reset (POR) Threshold|V<br>POR|Falling Voltage on VDD|0.75|—|1.36|V|
|VDD Ramp Time|t<br>RMP|Time to V > 2.2 V<br>DD|10|—|—|μs|
|Reset Delay from POR|t<br>POR|Relative to V > V<br>DD POR|3|10|31|ms|
|Reset Delay from non-POR source|t<br>RST|Time between release of reset<br>source and code execution|—|50|—|μs|
|RST Low Time to Generate Reset|t<br>RSTL||15|—|—|μs|
|Missing Clock Detector Response<br>Time (final rising edge to reset)|t<br>MCD|F >1 MHz<br>SYSCLK|—|0.625|1.2|ms|
|Missing Clock Detector Trigger<br>Frequency|F<br>MCD||—|7.5|13.5|kHz|
|VDD Supply Monitor Turn-On Time|t<br>MON||—|2|—|μs|


**silabs.com** | Building a more connected world. Rev. 1.5 | 22



## OCR Text

EFM8BB3 Data Sheet

Electrical Specifications

Parameter

Test Condition

Min

Max

Unit

Symbol

Typ

Note:

1. Currents are additive. For example, where Ipp is specified and the mode is not mutually exclusive, enabling the functions increa-

ses supply current by the specified amount.

2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.

3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.

4. ADCO power excludes internal reference supply current.

5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will

depend on sampling rate.

6. DAC supply current for each enabled DA and not including external load on pin.

7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.

4.1.3 Reset and Supply Monitor

Table 4.3. Reset and Supply Monitor

Parameter

Test Condition

Min

Max

Uni

Sy

Typ

VDD Supply Monitor Threshold

Vvopm

1.95

2.05

2.15

Power-On Reset (POR) Threshold | Vpor

Rising Voltage on VDD

1.4

Falling Voltage on VDD

0.75

1.36

VDD Ramp Time

trmp

Time to Vpp > 2.2 V.

10

us

10

31

ms

Reset Delay from POR

tpor

Relative to Vpp > Vpor

Reset Delay from non-POR source | trast

Time between release of reset

50

us

source and code execution

RST Low Time to Generate Reset

tRsTL

15

us

Missing Clock Detector Response

tmcp

Fsyscik >1 MHz

0.625

1.2

ms

Time (final rising edge to reset)

Missing Clock Detector Trigger

Fico

7.5

13.5

kHz

Frequency

VDD Supply Monitor Turn-On Time | tyion

us

silabs.com | Building a more connected world.

Rev. 1.5 | 22

## Tables

EFM8BB3 Data Sheet
Electrical Specifications
Parameter Test Condition Min Max Unit Symbol Typ
Note:
1. Currents are additive. For example, where Ipp is specified and the mode is not mutually exclusive, enabling the functions increa-
ses supply current by the specified amount.
2. Includes supply current from internal LDO regulator, supply monitor, and High Frequency Oscillator.
3. Includes supply current from internal LDO regulator, supply monitor, and Low Frequency Oscillator.
4. ADCO power excludes internal reference supply current.
5. The internal reference is enabled as-needed when operating the ADC in low power mode. Total ADC + Reference current will
depend on sampling rate.
6. DAC supply current for each enabled DA and not including external load on pin.
7. This value is the current sourced from the pin or supply selected as the full-scale reference to the comparator DAC.
4.1.3 Reset and Supply Monitor
Table 4.3. Reset and Supply Monitor
Parameter Test Condition Min Max Uni Sy Typ
VDD Supply Monitor Threshold Vvopm 1.95 2.05 2.15
Power-On Reset (POR) Threshold | Vpor Rising Voltage on VDD 1.4
Falling Voltage on VDD 0.75 1.36
VDD Ramp Time trmp Time to Vpp > 2.2 V. 10 us
10 31 ms Reset Delay from POR tpor Relative to Vpp > Vpor
Reset Delay from non-POR source | trast Time between release of reset 50 us
source and code execution
RST Low Time to Generate Reset tRsTL 15 us
Missing Clock Detector Response tmcp Fsyscik >1 MHz 0.625 1.2 ms
Time (final rising edge to reset)
Missing Clock Detector Trigger Fico 7.5 13.5 kHz
Frequency
VDD Supply Monitor Turn-On Time | tyion us
silabs.com | Building a more connected world. Rev. 1.5 | 22


---

