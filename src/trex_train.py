"""
File: trex_train.py
Purpose: train the T-rex dino AI system using CNN
Author: Prasanna
Created: Dec 05,200
Updated: Dec 05,2022.
"""
import glob
import os
import random
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split


def onehot_labels(values):
    """
    Label Encoding -> One Hot Encoding

    convert labels to binary values
    firstly labels will be numeric for example;
    UP --> 0
    DOWN --> 1
    RIGHT --> 2
    After Label Encoding will apply One Hot Encoding
    Thus, labels will be Binary Value, for example,
    0 --> 000
    1 --> 010
    2 -->001
    """
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    return onehot_encoded


imgs = glob.glob("../data/*.png")

width = 200
height = 40

X = []
Y = []
for data in imgs:
    filename = os.path.basename(data)
    label = filename.split("_")[0]
    im = np.array(Image.open(data).convert("L").resize((width, height)))
    im = im / 255
    X.append(im)
    Y.append(label)

X = np.array(X)
X = X.reshape(X.shape[0], width, height, 1)
Y = onehot_labels(Y)

train_X, test_X, train_y, test_y = train_test_split(X, Y, test_size=0.25,
                                                    random_state=random.randint
                                                    (112, 1112))

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(width, height, 1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(3, activation='softmax'))

if os.path.exists("./trex_weight.h5"):
    model.load_weights('trex_weight.h5')
    print("Load weight file")

print(model.summary())

model.compile(loss='sparse_categorical_crossentropy', optimizer='SGD',
              metrics=['accuracy'])

model.fit(train_X, train_y, epochs=20, batch_size=64)

scores = model.evaluate(train_X, train_y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

scores = model.evaluate(test_X, test_y)
print("\nTEST %s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

print(model.evaluate(X, Y))
open("model.json", "w").write(model.to_json())
model.save_weights('trex_weight.h5')
