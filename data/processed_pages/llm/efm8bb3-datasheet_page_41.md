# EFM8BB3 Data Sheet - Typical Connection Diagrams

## 5.2 Debug

The diagram below shows a typical connection diagram for the debug connection pins. The pin sharing resistors are only required if the functionality on the C2D (a GPIO pin) and the C2CK (RSTb) is routed to external circuitry. For example, if the RSTb pin is connected to an external switch with a debouncing filter or if the GPIO sharing with the C2D pin is connected to an external circuit, the pin sharing resistors and connections to the debug adapter must be placed on the hardware. Otherwise, these components and connections can be omitted.

For more information on debug connections, see the example schematics and information available in *AN124: Pin Sharing Techniques for the C2 Interface*. Application notes can be found on the Silicon Labs website ([http://www.silabs.com/8bit-appnotes](http://www.silabs.com/8bit-appnotes)) or in Simplicity Studio.

### Figure 5.2. Debug Connection Diagram

```
External EFM8BB3 Device          Debug Adapter

VDD

C2CK x --- 1k ---+                +--- 1k --- C2CK (if pin sharing)
                 |                |
C2D  x --- 1k ---+--- System ---+--- 1k --- C2D  (if pin sharing)

GND ox ------------------------- GND
```


## 5.3 Other Connections

Other components or connections may be required to meet the system-level requirements. Application Note AN203: "8-bit MCU Printed Circuit Board Design Notes" contains detailed information on these connections. Application Notes can be accessed on the Silicon Labs website ([http://www.silabs.com/8bit-appnotes](http://www.silabs.com/8bit-appnotes)).

---
*Page 42*