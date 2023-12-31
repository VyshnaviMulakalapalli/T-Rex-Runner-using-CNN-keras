## Project Design
 Created: 22 Nov 2022  
 Updated: 05 Dec 2022

### Content and Organization

#### Introduction  

Author - Prasanna, Reviewer - Vyshnavi

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
* All the moves will be recorded and each move is focussed on:
  * What is the current speed of T-Rex?
  * What is the distance until the next obstacle?
  * What is the width, height and altitude of this obstacle?
  * Whether you jumped or not.

### Theoretical Background

Author - Prasanna, Reviewer - Vyshnavi

1. What areas or fields of AI provide the theoretical framework of the AI system?   

* T-Rex-Runner uses a `Convolutional Neural Network(CNN) - Keras` that takes an input of the game screen and outputs whether it should or should not jump at that specific moment.
* It can capture the screen, evaluate it, and output its calculations in real time to play the game. 

    
2. What are the key concepts and techniques that the AI system is based on?  

* T-Rex-Runner uses a `Convolutional Neural Network(CNN)` to implement the CNN model, we will do these in order:

    * Firstly, we are going to create a dataset by playing the game for a while.
    * To create a dataset, we are going to grab the screen while playing the game and record which key was pressed at that moment.
    * After the dataset is created, we are going to train a classification model which is prepared using CNN.
* We need to specify the ROI (Region of Interest) according to screen resolution. We need to change limits (width and height) for the specified ROI.
* When each press direction buttons, it saves ROI pixels by taking the screenshot using mss (multiple screenshot module). 

3. Include appropriate references that describe the field, key concepts, and techniques

* [1]. Batuhan UZUN, 2021 "Trex-CNN". https://github.com/uzunb/Trex-CNN

* [2]. Nitin Rai, 2019 "Chrome-dino-game-bot". https://github.com/imneonizer/Chrome-dino-game-bot

* [3]. Ferhat Tas, 2021 "Create an AI to Play Chrome Dino Game with CNN". https://medium.com/analytics-vidhya/create-an-ai-to-play-chrome-dino-game-with-cnn-b769e58bb14c

* [4]. Erol, 2020 "Trex Game with CNN". https://dev.to/erol/trex-game-with-cnn-3j0h

* [5]. Valeti Dilip, 2021 “Convolutional Neural Network Using Keras" . https://medium.com/@dilip.voleti/convolutional-neural-network-using-keras-e8c5f4ff8a37.

* [6]. Dabakoglu Caner, 2018 “What Is Convolutional Neural Network (CNN) ? — With Keras”. https://medium.com/@cdabakoglu/what-is-convolutional-neural-network-cnn-with-keras-cab447ad204c. 


### Development approach

Author - Vyshnavi, Reviewer - Prasanna

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

**Getting the data**

* First we should start with getting data. In order to do that, we need to import `keyboard` library to save the keyboard action. Then we need to import `mss` to record screen for the game.
* mss library helps to cut off some areas in the screen by which the model can only focus on determined area.
* We need to set the co-ordinates in order to cut off the area that we want the model to see only using mss.
* A function should be defined for recording the screen. An exit function will be defined and whenever we want to exit in recording, we will press `esc` and then exit function will be called.

**Training the CNN model**

* A CNN model will be trained based on the data we got and the model predicts keyboard actions according to images.
* We will apply `Label Encoding` and `One Hot Encoding` to get binary values for the labels UP, DOWN and RIGHT.
* Then we need to split data for training and testing and then create a `Convolutional neural network` using relu and softmax activation functions and then train it.

**Testing the model**

* Model will be tested in the game as real-time.
* Import the libraries.
* Labels will be determined again because the model predicts images, we make it choose in this list according to output of the model.
* Set up the sizes for the screen and load the model.
* Apply resize and normalization.
* `argmax()` is used to find the label maximum probability.
* If the result is 0 it means DOWN, using keyboard library, model will press DOWN.
* If the result is 2 it means UP, again using keyboard library model will press UP.

### Working Example

Author - Vyshnavi, Reviewer - Prasanna

1. What example is a technically sound illustration of the AI system?

The player controls a running dinosaur by pressing ↑ (to jump) or ↓ (to crouch) to avoid obstacles, including cacti and pterodactyls. Pressing buttons to jump for different amounts of time will result in differently heighted jumps. Pressing ↓ while in the air will cause the dinosaur to fall faster.

When the player reaches 700 points the game begins to switch between day (white background, black lines and shapes) and night (black background, white lines and shapes).Reaching a score of 900 will switch the color scheme back to day, and the switch back and forth will occur at further subsequent milestones.



### Discussion and Evaluation

Author - Vyshnavi, Reviewer - Prasanna

1. What are the considerations for developing a safe and trustworthy AI?

* AI systems should support human autonomy and decision-making.  

* AI system creators should be able to provide evidence of the effectiveness and fitness of the purpose of the system.  

* The AI system shall adhere to the knowledge and skill required for safe and effective operation. 

* The AI system shall be created and operated to provide an unambiguous rationale for all decisions made.  

* The basis of a particular AI system decision should always be discoverable. 

* Look across the AI system lifecycle and make sure that portions that interact with data, metadata and models are secured and maintain data privacy as required. 

* Examine training data sets for sources of potential bias and make sure that communities are represented in a fair and equitable way. 

2. What are the ethical considerations in determining the legitimate use of the AI system?

The legal and ethical issues that confront society due to Artificial Intelligence (AI) include 	privacy and Transparency, Technical safety and Bias in Data, Training Sets, etc. 

**Technical Safety** 

The first question for any technology is whether it works as intended. Will AI systems work as they are promised, or will they fail? When they fail, what will be the results of those failures? And if we are dependent upon them, will we be able to survive without them?

**Transparency and Privacy** 

Once we have determined that the technology functions adequately, can we understand how it works and properly gather data on its functioning? Ethical analysis always depends on getting the facts first-only then can evaluation begin. 

**Bias in Data, Training Sets, etc.** 

Algorithmic bias is one of the major concerns in AI right now and will remain so in the future unless we endeavor to make our technological products better than we are. 

**Automating Ethics** 

One strength of AI is that it can automate decision-making, thus lowering the burden on humans and speeding up - potentially greatly speeding up—some kinds of decision-making processes. However, this automation of decision-making will present huge problems for society, because if these automated decisions are good, society will benefit, but if they are bad, society will be harmed. 


