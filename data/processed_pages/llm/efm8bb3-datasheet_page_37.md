# EFM8BB3 Data Sheet - Electrical Specifications

## SPI Timing Diagrams

- SCK is shown for CKPOL = 0. SCK is the opposite polarity for CKPOL = 1.

### Figure 4.3. SPI Master Timing (CKPHA = 1)

```
Signals:
- SCK*
- MISO
- MOSI
- NSS
```

### Figure 4.4. SPI Slave Timing (CKPHA = 0)

```
Signals:
- NSS
- SCK*
- MOSI
- MISO
```

---

*Source: silabs.com | Building a more connected world. Rev. 1.5 | Page 38*