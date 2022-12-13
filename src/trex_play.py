"""
File: trex_play.py
Purpose: Trex played by AI for team project
Author: Vyshnavi Mulakalapalli
Created: Dec 05, 2022
Updated: Dec 05, 2022
"""

import os
import time
from keras.models import model_from_json
# import glob
import numpy as np
from PIL import Image
import keyboard
from mss import mss


mon = {'top': 350, 'left': 625, 'width': 650, 'height': 130}
sct = mss()

# Force to use only CPU
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""

WIDTH = 200
HEIGHT = 40

# Load Model
# model = model_from_json(open("model.json", "r", encoding="utf-8").read())
with open("model.json", "r", encoding="utf-8") as model1:
    model = model_from_json(model1.read())
model.load_weights("trex_weight.h5")
print(model.summary())

# Down = 0, Right = 1, UP = 2
labels = ["Down", "Right", "Up"]


framerate_time = time.time()
COUNTER = 0
i = 0
CURRENT_FRAMERATE = 0
DELAY = 0.04
COUNT_TIME = 0
LAST_RESULT = 1

while True:

    time_start = time.time()
    img = sct.grab(mon)
    im = Image.frombytes('RGB', img.size, img.rgb)
    im = np.array(im.convert("L").resize((WIDTH, HEIGHT)))
    im = im / 255

    time_grab = time.time() - time_start
    time_start = time.time()

    X = np.array([im])
    X = X.reshape(X.shape[0], WIDTH, HEIGHT, 1)
    r = model.predict(X)
    result = np.argmax(r)

    time_predict = time.time() - time_start

    if (result == 0) and (LAST_RESULT != 0):
        # Hold down button
        keyboard.press(keyboard.KEY_DOWN)
    elif result == 2:
        if LAST_RESULT == 0:
            # Release down button
            keyboard.release(keyboard.KEY_DOWN)
        keyboard.press_and_release(keyboard.KEY_UP)

    last_result = result

    COUNTER += 1
    if (time.time() - framerate_time) > 1:
        CURRENT_FRAMERATE = COUNTER / (time.time() - framerate_time)
        COUNTER = 0
        framerate_time = time.time()
        DELAY -= 0.0001
        DELAY = max(DELAY, 0)

    os.system('clear')
    print(f"Down: {r[0][0]:3.2%} \nRight: {r[0][1]:3.2%} \n"
          f"Up: {r[0][2]:3.2%} \n", end="\r")
    print("=========================")
    print(f"Frame Count: {i}\nCurrent Frame Rate: {CURRENT_FRAMERATE:.2f}\n"
          f"Grab Screen: {time_grab:.5f}\nPredict: {time_predict:.5f}")
    print("=========================")
    print(f"Delay: {DELAY:.5f}")
    i += 1
    time.sleep(DELAY)
