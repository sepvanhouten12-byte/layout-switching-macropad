import time
import board
import analogio
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
 
ROW_PINS = [board.GP2, board.GP3, board.GP4, board.GP5, board.GP6]
COL_PINS = [board.GP7, board.GP8, board.GP9]
FADER_PINS = [board.GP26, board.GP27, board.GP28]
COLUMNS_TO_ANODES = True
 
KEY_ACTIONS = [
    (Keycode.CONTROL, Keycode.C),
    (Keycode.CONTROL, Keycode.V),
    (Keycode.CONTROL, Keycode.X),
    (Keycode.CONTROL, Keycode.Z),
    (Keycode.CONTROL, Keycode.Y),
    (Keycode.CONTROL, Keycode.S),
    (Keycode.CONTROL, Keycode.A),
    (Keycode.CONTROL, Keycode.F),
    (Keycode.CONTROL, Keycode.P),
    (Keycode.ENTER,),
    (Keycode.ESCAPE,),
    (Keycode.TAB,),
    (Keycode.BACKSPACE,),
    (Keycode.DELETE,),
    (Keycode.SPACE,),
]
 
keyboard = Keyboard(usb_hid.devices)
media = ConsumerControl(usb_hid.devices)
 
keys = keypad.KeyMatrix(
    row_pins=ROW_PINS,
    column_pins=COL_PINS,
    columns_to_anodes=COLUMNS_TO_ANODES,
)
 
faders = [analogio.AnalogIn(pin) for pin in FADER_PINS]
 
 
def read_fader(adc):
    total = 0
    for _ in range(8):
        total += adc.value
    return total // 8
 
 
def to_percent(raw):
    return raw * 100 // 65535
 
 
print("OpenPad Firmware v1")
 
last_percent = [to_percent(read_fader(f)) for f in faders]
 
while True:
    event = keys.events.get()
    if event:
        if event.pressed:
            keyboard.press(*KEY_ACTIONS[event.key_number])
        else:
            keyboard.release_all()
 
    for i, fader in enumerate(faders):
        percent = to_percent(read_fader(fader))
        change = percent - last_percent[i]
 
        if abs(change) >= 2:
            if i == 0:
                code = (ConsumerControlCode.VOLUME_INCREMENT if change > 0
                        else ConsumerControlCode.VOLUME_DECREMENT)
                for _ in range(abs(change) // 2):
                    media.send(code)
            else:
                print("Fader", i, "=", percent, "%")
 
            last_percent[i] = percent
 
    time.sleep(0.01)
