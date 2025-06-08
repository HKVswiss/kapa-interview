# EFM8BB3x-QFP32 Pin Definitions

## Figure 6.2. EFM8BB3x-QFP32 Pinout

```
Pin 32: P0.1    Pin 31: P0.2    Pin 30: P0.3    Pin 29: P0.4    Pin 28: P0.5    Pin 27: P0.6    Pin 26: P0.7    Pin 25: P1.0
Pin 24: P0.0    Pin 23: GND     Pin 22: VIO     Pin 21: VDD     Pin 20: RSTb / C2CK  Pin 19: P3.7 / C2D  Pin 18: P3.3  Pin 17: P3.2
Pin 16: P2.1    Pin 15: P2.2    Pin 14: P2.3    Pin 13: P2.4    Pin 12: P2.5    Pin 11: P2.6    Pin 10: P3.0    Pin 9: P3.1
Pin 8: P2.0     Pin 7: P1.7     Pin 6: P1.6     Pin 5: P1.5     Pin 4: P1.4     Pin 3: P1.3     Pin 2: P1.2     Pin 1: P1.1
```

## Table 6.2. Pin Definitions for EFM8BB3x-QFP32

| Pin Number | Pin Name     | Description               | Crossbar Capability | Additional Digital Functions           | Analog Functions |
|------------|--------------|---------------------------|---------------------|--------------------------------------|------------------|
| 1          | P0.0         | Multifunction I/O         | Yes                 | P0MAT.0, INT0.0, INT1.0, CLU0A.8, CLU2A.8, CLU3B.8 | VREF             |
| 2          | GND          | Ground                    |                     |                                      |                  |
| 3          | VIO          | I/O Supply Power Input    |                     |                                      |                  |
| 4          | VDD          | Supply Power Input        |                     |                                      |                  |
| 5          | RSTb / C2CK  | Active-low Reset / C2 Debug Clock |             |                                      |                  |

---
*Page 48*