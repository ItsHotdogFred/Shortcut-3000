---
title: "Modular Shortcut Device"
author: "ItsHotdogFred"
description: "A modular shortcut/stream deck where you snap on magnetic pogo-pin modules to build a device that fits your workflow, instead of fitting your workflow to the device."
created_at: "2026-09-26"
---

# September 26: Designed the schematic

This project is inspired by shortcut devices and stream decks. But instead of buying something premade and making your workflow fit the device, you make the device fit your workflow. Using magnetic pogo pins, you can snap on modules to build the ultimate device for your needs.

I built the schematic for the device. It uses I2C, which lets multiple devices share the same pins, so there's no worrying about running out of pins. This also means screen modules work well, since they can use the hardware I2C. I also added a multiplexer, because some I2C devices or GPIO expanders share the same address, and the multiplexer prevents those conflicts.

The module sizes are based on the size and spacing of Cherry MX switches, since that's what I think most people would use.

![schematic](https://github.com/user-attachments/assets/16150750-4495-4046-827e-190c63ad49e5)

**Total time spent: 4 hours**

# October 3: Designed the schematic

I have finished making the pcb. It doesn't have the best routing but in theory it should work. I also choose the sizes for each module. After this it's time to start creating each module

<img width="1096" height="849" alt="image" src="https://github.com/user-attachments/assets/e9245a7d-77a5-44c3-990f-565b5b9df205" />

**Total time spent: 2 hours**
