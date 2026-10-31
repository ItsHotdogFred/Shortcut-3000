# Shortcut 3000

Shortcut 3000 is a shortcut device which solves a big problem when buying a shortcut device. If you have already brought one before you may notice that some stuff on it go unused or aren't fit for your purpose. This leads to wasted space and wasted potential. 
To avoid this happening, Shortcut 3000 contains 12 magnetic pogo pads called modules which allow you to swap stuff on it. For example: Got a key you're not using and would much rather have a rotary encoder for managing sound? Well you can do that by swapping the key module with a rotary encoder!

The secret is using i2c for communication which allows it to hold 12 modules without running out of gpio pins and also easy in code. Each module has a eeprom which is used to identify what a module is. This allows the firmware to know how to use the module. modules can also choose if they want to turn the int line into a I/O pin which is required for things like rgb strips.

<img width="3239" height="1756" alt="image" src="https://github.com/user-attachments/assets/040bf21e-2b77-46b6-a197-d372eb80d324" />

<img width="1415" height="966" alt="image" src="https://github.com/user-attachments/assets/c9191d4e-ede5-42b4-b958-7b8bb4e6770e" />

<img width="1406" height="1066" alt="image" src="https://github.com/user-attachments/assets/994c8bde-4f21-493b-9bcd-650dee2391b8" />

<img width="2189" height="1186" alt="image" src="https://github.com/user-attachments/assets/ec7d7678-bf6d-4cdc-8c43-b70a159a1876" />
