# EFM8BB3 Data Sheet - Revision History

## 13. Revision History

### 13.1 Revision 1.5 (March, 2024)
- Noted that all QSOP Package OPNs are EOL.
- Added missing 4.1.18 SPI electrical specifications.

### 13.2 Revision 1.4 (October, 2020)
- Updated ordering part numbers to revision D.
- Restored crystal oscillator in 1. Feature List, Figure 3.1 Detailed EFM8BB3 Block Diagram (page 9), and 3.4 Clocking as it is again available on revision D.
- Restored crystal frequency and current specifications to Table 4.8 External Oscillator (page 25).
- Added Input Leakage (Pullups off or Analog) current for A-grade devices and I- and G-grade devices in Table 4.16 Port I/O (page 34).
- Corrected typos and made minor edits throughout the document.

### 13.3 Revision 1.3 (December, 2018)
- Updated ordering part numbers to revision C.
- Updated 1. Feature List, Figure 3.1 Detailed EFM8BB3 Block Diagram (page 9), and 3.4 Clocking to remove external crystal oscillator as clock source.
- Updated Table 4.8 External Oscillator (page 25) for RC oscillator specifications.
- Updated 3.1 Introduction to mention all device documentation.
- Updated 4.1.1 Recommended Operating Conditions to remove the "GPIO levels are undefined whenever VIO is less than 1 V" note, added a new minimum for VIO, and added a note referencing 4.1.16 Port I/O.
- Updated 3.10 Bootloader recommendations for production programming.
- Added more information about documentation to the 3.1 Introduction section.
- Removed all references to XTAL and renamed it to EXTOSC.

### 13.4 Revision 1.2 (June, 2017)
- Added A-grade devices and additional I-grade devices.
- Added the packages for the A-grade and new I-grade devices (QFN24-AI and QFN32-AI).
- Renamed the existing QFN24 and QFN32 packages to QFN24-GI and QFN32-GI.
- Added a note to Table 4.2 Power Consumption (page 20) providing more information about the Comparator Reference specification.

---
*Page 87*