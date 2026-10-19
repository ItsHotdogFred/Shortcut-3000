import board
import busio

i2c_1 = busio.I2C(board.GP5, board.GP4)  # SCL, SDA
i2c_2 = busio.I2C(board.GP7, board.GP6)  # SCL, SDA
import adafruit_ssd1306
import board
import keypad
import neopixel
import usb_hid
from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)  # media keys (volume, mute)

def i2c_read(bus, addr, reg, length=1):
    buf = bytearray(length)
    with I2CDevice(bus, addr, probe=False) as dev:  # pyright: ignore  (library __exit__ type hint bug)
        dev.write_then_readinto(bytes([reg]), buf)
    return buf

def i2c_write(bus, addr, data):
    with I2CDevice(bus, addr, probe=False) as dev:  # pyright: ignore  (library __exit__ type hint bug)
        dev.write(data)

GPIO2Module = {
    board.GP10 : "J1",
    board.GP9 : "J2",
    board.GP8 : "J3",
    board.GP2 : "J4",
    board.GP12 : "J5",
    board.GP13 : "J6",
    board.GP14 : "J7",
    board.GP29 : "J8",
    board.GP27 : "J9",
    board.GP26 : "J10",
    board.GP15 : "J11",
    board.GP28 : "J12"
}

ModuleLocations = {
    "J1": {"BUS": i2c_1, "CH": 0},
    "J2": {"BUS": i2c_1, "CH": 1},
    "J3": {"BUS": i2c_1, "CH": 2},
    "J4": {"BUS": i2c_1, "CH": 3},
    "J5": {"BUS": i2c_1, "CH": 4},
    "J6": {"BUS": i2c_1, "CH": 5},
    "J7": {"BUS": i2c_2, "CH": 0},
    "J8": {"BUS": i2c_2, "CH": 1},
    "J9": {"BUS": i2c_2, "CH": 2},
    "J10": {"BUS": i2c_2, "CH": 3},
    "J11": {"BUS": i2c_2, "CH": 4},
    "J12": {"BUS": i2c_2, "CH": 5}
}

def control5MXSwitch(bus):
    pins = read_mcp_pins(bus)
    print(bin(pins))              # e.g. 0b11101 -> GP0, GP2, GP3, GP4 high, GP1 low
    key_values = read_eeprom(bus, 8, 5)
    for i in range(5):
        if (pins >> i) & 1 == 0:   # active low (pull-ups)
            kbd.press(key_values[i])
        else:
            kbd.release(key_values[i])

def controlScreen(bus):
    oled = adafruit_ssd1306.SSD1306_I2C(64, 48, bus, addr=0x3C)
    oled.fill(0)
    oled.text("Vol 42", 0, 0, 1)   # needs font5x8.bin copied to CIRCUITPY
    oled.show()


PCA9537_ADDR = 0x49  # fixed address
ENC_A_BIT = 0        # IO0
ENC_B_BIT = 1        # IO1
ENC_SW_BIT = 3       # IO3 (pushbutton)
# Quadrature step lookup, index = (prev_ab << 2) | new_ab -> +1 CW / -1 CCW / 0 none or invalid
ENC_TABLE = (0, -1, 1, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 1, -1, 0)
rotary_state = {}    # per-slot encoder state

def read_pca9537_pins(bus):
    return i2c_read(bus, PCA9537_ADDR, 0x00)[0]  # input port register (also clears INT)

def controlRotary(bus, slot):
    pins = read_pca9537_pins(bus)
    print(bin(pins))
    ab = (((pins >> ENC_A_BIT) & 1) << 1) | ((pins >> ENC_B_BIT) & 1)
    button = ((pins >> ENC_SW_BIT) & 1) == 0  # active low, S2 tied to GND

    state = rotary_state.get(slot)
    if state is None:
        # First read for this slot: just record where the encoder is resting
        rotary_state[slot] = {"ab": ab, "count": 0, "button": button}
        return

    # key_values: [CW, CCW, button] as ConsumerControlCodes; 0x00/0xFF means unassigned
    key_values = read_eeprom(bus, 8, 3)

    state["count"] += ENC_TABLE[(state["ab"] << 2) | ab]
    state["ab"] = ab
    # EC11 rests with A and B both high (pulled up) at each detent; one click
    # is 4 transitions, so accept >= 2 to tolerate missed samples over I2C
    if ab == 0b11:
        if state["count"] >= 2 and key_values[0] not in (0x00, 0xFF):
            cc.send(key_values[0])
        elif state["count"] <= -2 and key_values[1] not in (0x00, 0xFF):
            cc.send(key_values[1])
        state["count"] = 0

    if button != state["button"]:
        state["button"] = button
        if key_values[2] not in (0x00, 0xFF):
            if button:
                cc.press(key_values[2])
            else:
                cc.release()

def read_mcp_pins(bus):
    return i2c_read(bus, 0x20, 0x09)[0]  # GPIO register


def controlRGB(gpio):
    pixels = neopixel.NeoPixel(gpio, 4, brightness=0.2, auto_write=False)
    pixels.fill((255, 0, 0))   # all red
    pixels[1] = (0, 0, 255)    # LED 1 blue
    pixels.show()              # send to the LEDs

def controlProboard():
    pass # Prototype board is empty so update this when you've actually added stuff on it

Modules = {
    "1": {"FUNC": controlRotary, "MCP": False},  # PCA9537: inputs + INT on by default
    "2": {"FUNC": control5MXSwitch, "MCP": True},
    "3": {"FUNC": controlProboard, "MCP": False},
    "4": {"FUNC": controlRGB, "MCP": False},
    "5": {"FUNC": controlScreen, "MCP": False}
}

ints = keypad.Keys(list(GPIO2Module.keys()), value_when_pressed=False)


def select_channel(bus, ch):
    i2c_write(bus, 0x70, bytes([1 << ch]))


def read_module_id(bus, ch):
    # Returns the module type ("1".."5"), or None for an empty slot / blank or unknown EEPROM
    try:
        select_channel(bus, ch)
        decoded = read_eeprom(bus, 0, 1).decode()
    except (OSError, UnicodeError):
        return None
    return decoded if decoded in Modules else None


def read_module(int):
    module = GPIO2Module[list(GPIO2Module)[int]]
    loc = ModuleLocations[module]
    i2c = loc["BUS"]
    decoded = read_module_id(i2c, loc["CH"])
    print(module, decoded)
    try:
        if decoded == "2":
            write_eeprom(i2c, bytes([Keycode.A, Keycode.B,Keycode.C,Keycode.D,Keycode.E]) ,8)
            control5MXSwitch(i2c)
        elif decoded == "1":
            write_eeprom(i2c, bytes([ConsumerControlCode.VOLUME_INCREMENT, ConsumerControlCode.VOLUME_DECREMENT, ConsumerControlCode.MUTE]) ,8)
            controlRotary(i2c, module)
    except OSError as e:
        print("I2C error on", module, e)

def read_eeprom(bus, start=0, length=8):
    return i2c_read(bus, 0x51, start, length)

def write_eeprom(bus, data, start=0):
    i2c_write(bus, 0x51, bytes([start]) + data)

def setup_mcp(bus):
    i2c_write(bus, 0x20, bytes([0x06, 0b00011111]))  # GPPU: pull-ups on GP0-4
    i2c_write(bus, 0x20, bytes([0x05, 0b00000100]))  # IOCON: INT open-drain
    i2c_write(bus, 0x20, bytes([0x02, 0b00011111]))  # GPINTEN: INT on change, GP0-4

def startup():
    global ints
    for module, loc in ModuleLocations.items():
        decoded = read_module_id(loc["BUS"], loc["CH"])
        print(module, decoded)
        if decoded is None:
            continue  # empty slot or blank/unknown EEPROM
        try:
            if Modules[decoded]["MCP"] == True:
                setup_mcp(loc["BUS"])
            if decoded == "5":
                controlScreen(loc["BUS"])
        except OSError as e:
            print("I2C error on", module, e)
            continue
        if decoded == "4":
            # RGB slot: free its INT pin from keypad so it can drive the LEDs
            gpio = next(pin for pin, name in GPIO2Module.items() if name == module)
            GPIO2Module.pop(gpio)
            ints.deinit()
            ints = keypad.Keys(list(GPIO2Module.keys()), value_when_pressed=False)

            controlRGB(gpio)

startup()
while True:
    event = ints.events.get()
    if event and event.pressed:
        read_module(event.key_number)  # only touch I2C for this slot
