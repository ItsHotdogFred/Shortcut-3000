# Shortcut 3000

Shortcut 3000 is a shortcut device which solves a big problem when buying a shortcut device. If you have already brought one before you may notice that some stuff on it go unused or aren't fit for your purpose. This leads to wasted space and wasted potential. 
To avoid this happening, Shortcut 3000 contains 12 magnetic pogo pads called modules which allow you to swap stuff on it. For example: Got a key you're not using and would much rather have a rotary encoder for managing sound? Well you can do that by swapping the key module with a rotary encoder!

The secret is using i2c for communication which allows it to hold 12 modules without running out of gpio pins and also easy in code. Each module has a eeprom which is used to identify what a module is. This allows the firmware to know how to use the module. modules can also choose if they want to turn the int line into a I/O pin which is required for things like rgb strips.

<img width="3239" height="1756" alt="image" src="https://github.com/user-attachments/assets/040bf21e-2b77-46b6-a197-d372eb80d324" />

<img width="1415" height="966" alt="image" src="https://github.com/user-attachments/assets/c9191d4e-ede5-42b4-b958-7b8bb4e6770e" />

<img width="1406" height="1066" alt="image" src="https://github.com/user-attachments/assets/994c8bde-4f21-493b-9bcd-650dee2391b8" />

<img width="2189" height="1186" alt="image" src="https://github.com/user-attachments/assets/ec7d7678-bf6d-4cdc-8c43-b70a159a1876" />

| BOM Item | Footprint | Qty Needed | Source | Part / Listing | Part # / Link | Buy Qty | Unit Price | Line Total (NZD) | Shipping |
|---|---|---|---|---|---|---:|---|---:|---|
| 4.7k resistor | 0805 | 28 | LCSC | UNI-ROYAL 0805W8F4701T5E (C17673) | [Link](https://www.lcsc.com/product-detail/C17673.html) | 100 | US$0.0051 | 0.90 | Combined w/ JLC order |
| 10k resistor | 0805 | 19 | LCSC | UNI-ROYAL 0805W8F1002T5E (C17414) | [Link](https://www.lcsc.com/product-detail/C17414.html) | 100 | US$0.0034 | 0.60 | Combined w/ JLC order |
| WS2812B-2020 LED | 2.0x2.0mm | 20 | LCSC | Worldsemi WS2812B-2020-V6 (C52917434) | [Link](https://www.lcsc.com/product-detail/C52917434.html) | 20 | US$0.0921 | 3.25 | Combined w/ JLC order |
| MagneticPogo 1x05 M+F | 2.54mm | 12M+12F | Alibaba | Shenzhen Lixiang magnetic pogo 5P 2.54mm - '5p with positioning holes' | [Link](https://www.alibaba.com/product-detail/_1601788916589.html) | 12 | NZ$1.65 | 19.80 | FREE (new-buyer promo, capped NZ$36.09; normally NZ$25.59) |
| MX hotswap socket | Kailh CPG151101S11 | 5 | Owned | - | | 0 | | 0.00 | |
| 100nF cap | 0805 | 4 | LCSC | YAGEO CC0805KRX7R9BB104 (C49678) | [Link](https://www.lcsc.com/product-detail/C49678.html) | 20 | US$0.0206 | 0.73 | Combined w/ JLC order |
| 10nF cap | 0805 | 3 | LCSC | Samsung CL21B103KBANNNC (C1710) | [Link](https://www.lcsc.com/product-detail/C1710.html) | 50 | US$0.0116 | 1.02 | Combined w/ JLC order |
| 1uF cap | 0805 | 2 | LCSC | Samsung 1uF 0805 25V X7R (C116352) | [Link](https://www.lcsc.com/product-detail/C116352.html) | 10 | US$0.0409 | 0.72 | Combined w/ JLC order |
| 24LC02 EEPROM | SOIC-8 narrow | 3 | LCSC | Microchip 24LC02BT-I/SN (C5453) | [Link](https://www.lcsc.com/product-detail/C5453.html) | 5 | US$0.2957 | 2.61 | Combined w/ JLC order |
| TCA9548APWR mux | TSSOP-24 | 2 | LCSC | TI TCA9548APWR (C130026) | [Link](https://www.lcsc.com/product-detail/C130026.html) | 2 | US$0.8192 | 2.89 | Combined w/ JLC order |
| MCP23008 | DIP-18 | 1 | LCSC | Microchip MCP23008-E/P (C646745) | [Link](https://www.lcsc.com/product-detail/C646745.html) | 1 | US$2.9512 | 5.21 | Combined w/ JLC order |
| 0.66in OLED | 64x48 I2C | 1 | AliExpress | 0.66in OLED SSD1306 (Wemos shield) | [Link](https://www.aliexpress.com/item/1005010695971596.html) | 1 | NZ$5.29 | 5.29 | Choice |
| PCA9537 | TSSOP-10 | 1 | LCSC (backorder) | NXP PCA9537DP,118 (C2652305) | [Link](https://www.lcsc.com/product-detail/C2652305.html) | 1 | US$1.5903 | 2.81 | Combined w/ JLC order |
| RP2040-Zero | Castellated | 1 | AliExpress | RP2040-Zero 1PCS | [Link](https://www.aliexpress.com/item/1005010706978212.html) | 1 | NZ$5.49 | 5.49 | Choice |
| EC11E encoder | Vertical H20mm | 1 | LCSC | ALPS EC11E18244A5 (C255515) | [Link](https://www.lcsc.com/product-detail/C255515.html) | 1 | US$2.4355 | 4.30 | Combined w/ JLC order |
| Shortcut-3000 main PCB | PCB, black, 1.6mm, LeadFree HASL | 1 | JLCPCB | Shortcut-3000-Gerbers_Y11 | Y11-13394057A | 5 | US$9.50 (per 5) | 16.78 | JLC est. (shared) |
| Screen module PCB | PCB, black, 1.6mm, LeadFree HASL | 1 | JLCPCB | screen-module-Gerbers_Y10 | Y10-13394057A | 5 | US$5.20 (per 5) | 9.18 | JLC est. (shared) |
| Rotary encoder module PCB | PCB, black, 1.6mm, LeadFree HASL | 1 | JLCPCB | Rotary-encoder-module-Gerbers_Y9 | Y9-13394057A | 5 | US$5.20 (per 5) | 9.18 | JLC est. (shared) |
| RGB daisy-chain module PCB | PCB, black, 1.6mm, LeadFree HASL | 1 | JLCPCB | rgb-daisy-chain-module-Gerbers_Y8 | Y8-13394057A | 5 | US$5.20 (per 5) | 9.18 | JLC est. (shared) |
| Protoboard module PCB | PCB, black, 1.6mm, LeadFree HASL | 1 | JLCPCB | proboard-module-Gerbers_Y7 | Y7-13394057A | 5 | US$5.20 (per 5) | 9.18 | JLC est. (shared) |
| 5x MX switch module PCB | PCB, black, 1.6mm, LeadFree HASL | 1 | JLCPCB | 5-MX-Switch-Module-Gerbers_Y6 | Y6-13394057A | 5 | US$3.30 (per 5) | 5.83 | JLC est. (shared) |
| **TOTAL** | | | | | | | | **114.95** | |
