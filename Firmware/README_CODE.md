# Firmware

The macropad runs on CircuitPython and uses the adafruit_hid library to act like a USB keyboard.
The four switches are connected directly to GPIO pins on the RP2040:
- GPIO2 = Up
- GPIO3 = Left
- GPIO4 = Down
- GPIO5 = Right
By default, the macropad works as a normal arrow-key pad.
It also has a second shortcut mode. To switch modes, press all three bottom keys at the same time, release them, and repeat that 3 times within about 2 seconds.
Arrow Mode
- Top = Up Arrow
- Bottom Left = Left Arrow
- Bottom Middle = Down Arrow
- Bottom Right = Right Arrow
Shortcut Mode
- Top = Command + Tab
- Bottom Left = Command + T
- Bottom Middle = Command + V
- Bottom Right = Command + C
Pressing the bottom three keys together 3 times again switches back to arrow mode.
How the Code Works
Each switch is set up as a digital input with the RP2040's internal pull-up resistor enabled.
Because each switch connects the GPIO pin to ground when pressed, the code treats a LOW signal as a key press.
The program constantly checks the state of all four switches. When a key changes from released to pressed, it sends the matching keyboard command over USB using adafruit_hid.
The code also watches for the three bottom keys being pressed at the same time. Each completed three-key press counts toward the mode-change sequence. After three of these presses, the firmware switches between arrow mode and shortcut mode.

Setting Up the Board
The RP2040 first needs CircuitPython installed.
Hold the BOOTSEL button while plugging the board into a computer. The board should appear as a drive called:
RPI-RP2
Download the correct CircuitPython .uf2 file for the RP2040 and copy it onto RPI-RP2.
After the board restarts, it should appear as:
CIRCUITPY

Installing the HID Library
The firmware uses Adafruit's HID library.
Download the CircuitPython Library Bundle that matches the major version of CircuitPython installed on the board.
From the bundle, copy:
adafruit_hid
into the lib folder on the board.

Installing the Firmware
Copy the macropad firmware into the root of the CIRCUITPY drive and name it:
code.py

CircuitPython automatically runs code.py whenever the board powers on or the file is saved.
No separate compiler or flashing software is needed after CircuitPython is installed.
Requirements
- RP2040
- CircuitPython
- adafruit_hid
- 4 switches connected between GPIO2–GPIO5 and GND
- USB connection to the computer
The current shortcut layout is made for macOS because it uses the Command key for copy, paste, new tab, and application switching.
