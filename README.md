# T-Rex-Runner using CNN-keras


This project is about teaching the T-Rex to dodge obstacles in 3 stages. It is a CNN model that predicts objects and keyboard actions.

* Getting the data
* Training the CNN model
* Testing the trained CNN model

### Getting the data

We need below libraries to collect the data.
```angular2html
import keyboard
import uuid
import time
from PIL import Image
from mss import mss
```

* **keyboard** library is used to save our action like "up", "down" and "right".
* Game screen can be recorded using **mss** library. 
* When all the lines are executed, we will switch the game screen and the model that is trained with the data we got, will predict action according to images. Also, this library helps to cut off some areas in the screen.
* A function will be created which will be used for recording the screen.
* An exit function will be defined and whenever we want to stop collecting data, then we can press `esc` which calls exit function and stops collecting the data.

### Training a CNN model

A CNN model will be trained with the data we got. For that we need below libraries.

```angular2html
import glob
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from PIL import Image
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
```

* The model will predict keyboard actions according to images. 
* If the model recognizes a cactus, the action will be "UP", or if the model recognizes a bird, the action will be "DOWN" or "UP".
* Labels(UP, DOWN, RIGHT) will be determined and before training, recorded images will be resized and normalized.
* Data will be split into training and testing data.
* Firstly Label Encoding and then One Hot Encoding will be applied on labels by which a binary value will be generated for each label.
* A CNN will be created in the next step which we will train and test.


### Testing the trained CNN model

* We will test our model in the game as real-time.
* We will import below libraries.

```angular2html
from keras.models import model_from_json
import numpy as np
from PIL import Image
import keyboard
import time
import os
from mss import mss
```

* We will upload our Trained CNN Model and make it choose in the list according to output of the model.
* Resize and normalization will be done and turned into array and reshaped it. Because the input is known for model. 
* The np.argmax() returns the indices of the maximum values along an axis. We will use it due to find the label maximum probability.
* If the result is 0 it means DOWN, using keyboard library, model will press DOWN. 
* If the result is 2 it means UP, again using keyboard library model will press UP.



