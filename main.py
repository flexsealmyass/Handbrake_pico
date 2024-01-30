import board
from digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard

switch = DigitalInOut(board.GP15)
switch.switch_to_input(pull=digitalio.Pull.UP)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

while True:
    if (switch.value):
        kbd.send(keycode.P)
    else:
        kbd.release_all()
