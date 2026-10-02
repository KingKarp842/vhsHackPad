import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

UP = board.GP2
LEFT = board.GP3
DOWN = board.GP4
RIGHT = board.GP5

def setup_button(pin):
    b = digitalio.DigitalInOut(pin)
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP
    return b

up = setup_button(UP)
left = setup_button(LEFT)
down = setup_button(DOWN)
right = setup_button(RIGHT)

keyboard = Keyboard(usb_hid.devices)

shortcut_mode = False
combo_count = 0
last_combo = 0
combo_held = False

prev = {
    "up": False,
    "left": False,
    "down": False,
    "right": False
}

def is_pressed(button):
    return not button.value

def press_key(name):
    if shortcut_mode:
        if name == "up":
            keyboard.send(Keycode.COMMAND, Keycode.TAB)
        elif name == "left":
            keyboard.send(Keycode.COMMAND, Keycode.T)
        elif name == "down":
            keyboard.send(Keycode.COMMAND, Keycode.V)
        elif name == "right":
            keyboard.send(Keycode.COMMAND, Keycode.C)
    else:
        if name == "up":
            keyboard.send(Keycode.UP_ARROW)
        elif name == "left":
            keyboard.send(Keycode.LEFT_ARROW)
        elif name == "down":
            keyboard.send(Keycode.DOWN_ARROW)
        elif name == "right":
            keyboard.send(Keycode.RIGHT_ARROW)

while True:
    now = time.monotonic()

    current = {
        "up": is_pressed(up),
        "left": is_pressed(left),
        "down": is_pressed(down),
        "right": is_pressed(right)
    }

    combo = current["left"] and current["down"] and current["right"]

    if combo and not combo_held:
        combo_held = True

        if now - last_combo > 2:
            combo_count = 0

        combo_count += 1
        last_combo = now

        if combo_count == 3:
            shortcut_mode = not shortcut_mode
            combo_count = 0
            print("shortcut" if shortcut_mode else "arrows")

    if not combo:
        combo_held = False

    if not combo:
        for key in current:
            if current[key] and not prev[key]:
                press_key(key)

    prev = current.copy()
    time.sleep(0.01)
