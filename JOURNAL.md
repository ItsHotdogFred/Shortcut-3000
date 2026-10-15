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

# October 3: Designed the pcb

I have finished making the pcb. It doesn't have the best routing but in theory it should work. I also choose the sizes for each module. After this it's time to start creating each module

<img width="1096" height="849" alt="image" src="https://github.com/user-attachments/assets/e9245a7d-77a5-44c3-990f-565b5b9df205" />

**Total time spent: 2 hours**

# October 15: Designed the modules
I have created 6 modules each one being unique and having their own purpose. Each module has a EEPROM for storing an UUID. This helps store specific settings for each module so moving it around the board doesn't cause any issues. I also made each module have its own int line as there were lots of spare gpio pins so it didn't make sense to not use them. This should result in less unnecessary reads and the ability to convert the int line into a direct line to the MCU (very helpful for RGB daisy chaining) Here is some info about each module:  

## 5 MX Switch Module

This module holds 5 Cherry MX switches, which makes it the main module for shortcuts and macros. Its pretty generic but very important for a device designed about being a shortcut to common things.

<img width="1568" height="1176" alt="image" src="https://github.com/user-attachments/assets/11654fa1-bf3e-4747-97c0-906aaf374078" />

## Rotary Encoder Module

This module has a rotary encoder with a push button, which works well for volume, scrolling, or scrubbing through a timeline. I also prevented debouncing from happening which is more reliable then doing it on the software side.

<img width="1568" height="1176" alt="image" src="https://github.com/user-attachments/assets/83724b58-4ae5-4300-835f-6a6ca0c5bf6c" />

## Screen Module

This module has a small 0.66" 64x48 OLED display that runs straight off the I2C bus. You can use it to show your current layer, what each key does, or stats like volume and time. It’s one of the simplest modules since the screen only needs power and the two I2C lines from the pogo connector.

<img width="1568" height="1176" alt="image" src="https://github.com/user-attachments/assets/f070fa7d-2a1f-4b75-a251-e7f991cdaed9" />

## RGB Daisy Chain Module

This module has 20 tiny WS2812B-2020 addressable LEDs chained together, so each one can be set to its own color. It adds lighting effects to the device, and it can also show status, like flashing when a shortcut runs. The LEDs are daisy chained, so a single data line controls all of them (replaces the int line)

<img width="1568" height="1176" alt="image" src="https://github.com/user-attachments/assets/a397cc07-e004-4417-90a6-d4b0c015cf37" />

## Protoboard Module

This module is basically a blank protoboard with 54 holes, made so if I get any ideas after this I am able to prototype them without having to wait for shipping.

<img width="1568" height="1176" alt="image" src="https://github.com/user-attachments/assets/78d6d539-9fce-47fb-8201-9b56538fcb7e" />


**Total time spent 5 hours **
