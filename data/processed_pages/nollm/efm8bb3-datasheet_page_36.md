# Page 37

## Text from PDF

EFM8BB3 Data Sheet
Electrical Specifications

**4.1.18 SPI**

**Table 4.19. SPI Timing Parameters**

|Parameter|Description|Min|Max|Units|
|---|---|---|---|---|
|Master Mode Timing|Master Mode Timing|Master Mode Timing|Master Mode Timing|Master Mode Timing|
|T<br>MCKH|SCK High Time|1 x T<br>SYSCLK|—|ns|
|T<br>MCKL|SCK Low Time|1 x T<br>SYSCLK|—|ns|
|T<br>MIS|MISO Valid to SCK Sample Edge|20|—|ns|
|T<br>MIH|SCK Sample Edge to MISO Change|5|—|ns|
|Slave Mode Timing|Slave Mode Timing|Slave Mode Timing|Slave Mode Timing|Slave Mode Timing|
|T<br>SE|NSS Falling to First SCK Edge|5|—|ns|
|T<br>SD|Last SCK Edge to NSS Rising|5|—|ns|
|T<br>SEZ|NSS Falling to MISO Valid|—|20|ns|
|T<br>SDZ|NSS Rising to MISO High-Z|—|20|ns|
|T<br>CKH|SCK High Time|40|—|ns|
|T<br>CKL|SCK Low Time|40|—|ns|
|T<br>SIS|MOSI Valid to SCK Sample Edge|20|—|ns|
|T<br>SIH|SCK Sample Edge to MOSI Change|5|—|ns|
|T<br>SOH|SCK Shift Edge to MISO Change|—|20|ns|
|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|Note:<br>1. T is equal to one period of the device system clock (SYSCLK).<br>SYSCLK|



SCK*




MISO

MOSI

      - SCK is shown for CKPOL = 0. SCK is the opposite polarity for CKPOL = 1.

**Figure 4.2. SPI Master Timing (CKPHA = 0)**

**silabs.com** | Building a more connected world. Rev. 1.5 | 37



## OCR Text

EFM8BB3 Data Sheet

Electrical Specifications

4.1.18 SPI

Table 4.19. SPI Timing Parameters

Parameter

Desc

ion

Max

Uni

its

Master Mode Timing

ns

TwckH

SCK High Time

1x Tsyscik

TmckL

SCK Low Time

1x Tsyscik

ns

20

ns

Tus

MISO Valid to SCK Sample Edge

TH

SCK Sample Edge to MISO Change

5

ns

Slave Mode Timing

Tse

NSS Falling to First SCK Edge

ns

Tsp

Last SCK Edge to NSS Rising

ns

20

ns

Tsez

NSS Falling to MISO Valid

Tspz

NSS Rising to MISO High-Z

20

ns

40

ns

ToKH

SCK High Time

Tok.

SCK Low Time

40

ns

20

ns

Tsis

MOS! Valid to SCK Sample Edge

TsiH

SCK Sample Edge to MOS! Change

ns

20

ns

Tsou

SCK Shift Edge to MISO Change

Note:

1. Tsyscik is equal to one period of the device system clock (SYSCLK).

{ |

SCK*

I]

te

MI

[ MIs

{ |

MISO. X

ii

ia

{ L

MOSI

X

fi

Tl

* SCK is shown for CKPOL = 0. SCK is the opposite polarity for CKPOL = 1.

Figure 4.2. SPI Master Timing (CKPHA = 0)

silabs.com | Building a more connected world.

Rev. 1.5 | 37

## Tables

EFM8BB3 Data Sheet
Electrical Specifications
4.1.18 SPI
Table 4.19. SPI Timing Parameters
Parameter Desc ion Max Uni its
Master Mode Timing
ns TwckH SCK High Time 1x Tsyscik
TmckL SCK Low Time 1x Tsyscik ns
20 ns Tus MISO Valid to SCK Sample Edge
TH SCK Sample Edge to MISO Change 5 ns
Slave Mode Timing
Tse NSS Falling to First SCK Edge ns
Tsp Last SCK Edge to NSS Rising ns
20 ns Tsez NSS Falling to MISO Valid
Tspz NSS Rising to MISO High-Z 20 ns
40 ns ToKH SCK High Time
Tok. SCK Low Time 40 ns
20 ns Tsis MOS! Valid to SCK Sample Edge
TsiH SCK Sample Edge to MOS! Change ns
20 ns Tsou SCK Shift Edge to MISO Change
Note:
1. Tsyscik is equal to one period of the device system clock (SYSCLK).
{ |
SCK*
I]
te
MI [ MIs
{ |
MISO.
X ii
ia
{ L
MOSI
X fi
Tl
* SCK is shown for CKPOL = 0. SCK is the opposite polarity for CKPOL = 1.
Figure 4.2. SPI Master Timing (CKPHA = 0)
silabs.com | Building a more connected world. Rev. 1.5 | 37


---

