"""
File: trex_getdata.py
Purpose: Collects data for team project
Author: Vyshnavi Mulakalapalli
Created: Dec 05, 2022
Updated: Dec 05, 2022
"""

import keyboard
import os
import uuid
from mss import mss
from PIL import Image
import time
import sys

mon = {'top': 350, 'left': 625, 'width': 650, 'height': 130}
sct = mss()

counter = 0


def record_screen(record_id1, key):
    """Records screen in the game."""
    global counter
    counter += 1
    print("{}: {}".format(key, counter))
    data = sct.grab(mon)
    im = Image.frombytes('RGB', data.size, data.rgb)
    im.save("../data/{}_{}_{}.png".format(key, record_id1, counter))


is_exit = False


def exit1():
    """Stops collection of data."""
    global is_exit
    is_exit = True


keyboard.add_hotkey("esc", exit1)

record_id = uuid.uuid4()
while True:

    if is_exit:
        break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            record_screen(record_id, "up")
            time.sleep(0.1)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            record_screen(record_id, "down")
            time.sleep(0.1)
        elif keyboard.is_pressed("right"):
            record_screen(record_id, "right")
            time.sleep(0.2)
    except RuntimeError:
        continue
