# EFM8BB3 Data Sheet - Electrical Specifications

| Parameter | Symbol | Test Condition | Min | Typ | Max | Unit |
|-----------|--------|----------------|-----|-----|-----|------|
| *Notes:* |
| 1. Conversion Time does not include Tracking Time. Total Conversion Time is:
  Total Conversion Time = [RPT x (ADTK + NUMBITS + 1) x T(SARCLK)] + (T(ADCCLK) x 4)
  where RPT is the number of conversions represented by the ADRPT field and ADCCLK is the clock selected for the ADC.
| 2. Absolute input pin voltage is limited by the V supply.
| 3. The offset is determined using curve fitting since the specification is measured using linear search where the intercept is always positive.
| 4. Production test uses a 2.4 V external reference and external ground.

---

*Source: silabs.com | Building a more connected world. Rev. 1.5 | Page 28*