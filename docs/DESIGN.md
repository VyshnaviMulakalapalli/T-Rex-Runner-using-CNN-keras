
## Project Design
 Created: 22 Nov 2022  
 Updated: 28 Nov 2022

### Content and Organization
#### Introduction  

1. What AI system are you interested in investigating further?  

   * **`T-REX DINO CHROME AI BOT`** , In this AI system we teach T-Rex Dino to dodge obstacles in 3 stages. 

    **Stages** :  
          1- Collect dataset when playing.  
          2- Train dataset.  
          3- Start and watch it.   


2. Why is it of interest to you?   

* Chrome users find themselves without Internet connection occasionally,
  and when this happens, they enjoy playing the popular T-Rex, Run! Game.  


3. What specifically you'll focus on? What's the overall guiding question your study will pursue?
* In this game, the player controls a dinosaur and accumulates points by jumping over obstacles.
* The controls are simple – press the space bar or the up arrow to jump up or press the down arrow to duck. 

### Theoretical Background

1. What areas or fields of AI provide the theoretical framework of the AI system?   

* T-Rex-Runner uses a `Convolutional Neural Network(CNN)` that takes an input of the game screen and outputs whether it should or should not jump at that specific moment.
* It can capture the screen, evaluate it, and output its calculations in real time to play the game. 


2. What are the key concepts and techniques that the AI system is based on?  

* It collects the dataset when playing, trains with the obtained dataset and then it plays the game.
* We need to specify the ROI (Region of Interest) according to screen resolution. We need to change limits (width and height) for the specified ROI.
* When each press direction buttons, it saves ROI pixels by taking the screenshot using mss (multiple screenshot module). 

3. Include appropriate references that describe the field, key concepts, and techniques

* [1]. Batuhan UZUN, 2021 "Trex-CNN". https://github.com/uzunb/Trex-CNN

* [2]. Nitin Rai, 2019 "Chrome-dino-game-bot". https://github.com/imneonizer/Chrome-dino-game-bot

#### Development approach

1. What tools, platforms, APIs, libraries, datasets are available and needed to develop the AI system?

* A dataset should be created by playing the game manually. The dataset contains pixels of **`Region of Interest`** which will be specified by user according to their screen resolution.
* The below python libraries should be imported to run the T-Rex dino bot.
  * Image from PIL - The Image module provides a class with the same name which is used to represent a PIL image. The module also provides a number of factory functions, including functions to load images from files, and to create new images.
  * MSS(Multiple Screenshots) - An ultra-fast cross-platform multiple screenshots module in pure python using ctypes.
  * Keyboard - Python provides a library named keyboard which is used to get full control of the keyboard. It can hook global events, register hotkeys and simulate key presses.
  * uuid - helps in generating random objects of 128 bits as ids. It provides the uniqueness as it generates ids on the basis of time, Computer hardware.
  * os - The OS module in Python provides functions for creating and removing a directory, fetching its contents, changing and identifying the current directory.
  * glob - In Python, the glob module is used to retrieve files/pathname matching a specified pattern. 
  * Numpy - It is a Python library that provides a multidimensional array object, various derived objects, and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, basic linear algebra and basic statistical operations.
  * Keras - Keras is a high-level, deep learning API developed by Google for implementing neural networks. It is written in Python and is used to make the implementation of neural networks easy. It also supports multiple backend neural network computation.  
  * Sklearn - It provides a selection of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction via a consistence interface in Python.
  * Seaborn - Seaborn is a library for making statistical graphics in Python. It builds on top of matplotlib and integrates closely with pandas data structures. Seaborn helps you explore and understand your data.


 
