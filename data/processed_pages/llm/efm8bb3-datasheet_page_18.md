# EFM8BB3 Data Sheet

## 4. Electrical Specifications

### 4.1 Electrical Characteristics

All electrical parameters in all tables are specified under the conditions listed in Table 4.1 Recommended Operating Conditions on page 19, unless stated otherwise.

### 4.1.1 Recommended Operating Conditions

| Parameter                          | Symbol | Test Condition       | Min  | Typ | Max  | Unit |
|----------------------------------|--------|---------------------|------|-----|------|------|
| Operating Supply Voltage on VDD  | VDD    |                     | 2.2  | —   | 3.6  | V    |
| Operating Supply Voltage on VIO2 | VIO    |                     | 2.2  | —   | VDD  | V    |
| System Clock Frequency            | fSYSCLK|                     | 0    | —   | 50   | MHz  |
| Operating Ambient Temperature     | TA     | G-grade devices      | -40  | —   | 85   | °C   |
| Operating Ambient Temperature     | TA     | I-grade or A-grade devices | -40  | —   | 125  | °C   |

**Notes:**
1. All voltages are with respect to GND.
2. In certain package configurations, the VIO and VDD supplies are bonded to the same pin.
3. I/O have reduced current drive/sink capabilities at lower VIO levels. See section 4.1.16 Port I/O for additional information.

---
*Page 19*