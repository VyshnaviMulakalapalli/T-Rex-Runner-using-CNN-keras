"""
File: trex_getdata.py
Purpose: Collects data for team project
Author: Vyshnavi Mulakalapalli
Created: Dec 05, 2022
Updated: Dec 13, 2022
"""
import uuid
import time
import keyboard
# import os
from mss import mss
from PIL import Image
# import sys

mon = {'top': 350, 'left': 625, 'width': 650, 'height': 130}
sct = mss()

COUNTER = 0


def record_screen(record_id1, key):
    """
    Records screens in the game and saves images into data folder.

    record_id1: uuid generated when a key is pressed.
    key: the keyboard action, for example UP, RIGHT or DOWN.
    """
    global COUNTER
    COUNTER += 1
    print(f"{key}: {COUNTER}")
    data = sct.grab(mon)
    im_dt = Image.frombytes('RGB', data.size, data.rgb)
    im_dt.save(f"../data/{key}_{record_id1}_{COUNTER}.png")


IS_EXIT = False


def exit1():
    """Stops collection of data."""
    global IS_EXIT
    IS_EXIT = True


keyboard.add_hotkey("esc", exit1)

record_id = uuid.uuid4()
while True:

    if IS_EXIT:
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
