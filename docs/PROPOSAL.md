## Project Proposal 

### T-REX DINO CHROME AI BOT 

### Team members – Prasanna & Vyshnavi 

### Platform - GitHub

### Author- Batuhan UZUN 

**1. What AI system are you interested in investigating further and why?** 

Chrome users find themselves without Internet connection occasionally, and when this happens, they enjoy playing the popular T-Rex, Run! Game. In this game, the player controls a dinosaur and accumulates points by jumping over obstacles. The controls are simple – press the space bar or the up arrow to jump up or press the down arrow to duck. 

In this AI system, we teach T-Rex to dodge obstacles in 3 stages. 

1- Collect dataset when playing.  
2- Train dataset.  
3- Start and watch it. 

Lead author – Vyshnavi    Reviewer – Prasanna 

**2. What content knowledge (theories and concepts) does the AI system use?**

T-Rex-Runner uses a convolutional neural network that takes an input of the game screen and outputs whether it should or should not jump at that specific moment. It can capture the screen, evaluate it, and output its calculations in real time to play the game. 

It collects the dataset when playing, trains with the obtained dataset and then it plays the game. We need to specify the ROI (Region of Interest) according to screen resolution. We need to change limits for the specified ROI. When each press direction buttons, it saves ROI pixels by taking the screenshot using mss (multiple screenshot module).          

Lead author – Prasanna    Reviewer – Vyshnavi 

**3. What tools, platforms, and APIs are needed to develop the AI system?**

* Pillow - PIL (python imaging library for images), 

* PyAutoGUI-to automate mouse and keyboard interactions with other applications. And, for taking screenshots, locate application’s window, maximize, minimize, resize, move and close it. Display alert and message boxes. 

* OS X 

* python 2.6 or 2.7 

* Numpy (pip install numpy) - NumPy is a Python library used for working with arrays. 

* Sklearn - It provides a selection of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction via a consistence interface in Python.

* Seaborn (pip install seaborn) - Seaborn is a Python visualization library based on matplotlib. 

* keyboard (pip install keyboard) - It helps to enter keys, record the keyboard activities and block the keys until a specified key is entered and simulate the keys.

* uuid (pip install uuid) - UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids.

* time  

* glob - In Python, the glob module is used to retrieve files/pathname matching a specified pattern.

* keras (pip install keras) - It is used to make the implementation of neural networks easy. It also supports multiple backend neural network computation.

* sequential 

* mss (python -m pip install -U --user mss) 

Lead author – Vyshnavi    Reviewer – Prasanna 

**4. What example illustrates the basic "ingredients" of the AI system?** 

Pressing the space bar too soon or too late might prevent the player from jumping again if another obstacle is quickly approaching. Therefore, T-Rex, Run! is a good candidate for a project whose focus is decision making under uncertainty as some obstacles are not yet visible. 

Import the mss module and cut Region of Interest (ROI) frame by setting the pixel limits (height, top, width, left). This is used to create dataset to train the T-rex.  Keyboard operations such as key down, key up, right are labelled and assigned to values as down = 0, right = 1, up = 2. For all key operations record the screen after each operation. Change the image width, height pixel values and train the system using CNN model. 

Lead author – Prasanna    Reviewer – Vyshnavi 

**5. What are the considerations for developing a safe and trustworthy AI system?**

* AI systems should support human autonomy and decision-making.  

* AI system creators should be able to provide evidence of the effectiveness and fitness of the purpose of the system.  

* The AI system shall adhere to the knowledge and skill required for safe and effective operation. 

* The AI system shall be created and operated to provide an unambiguous rationale for all decisions made.  

* The basis of a particular AI system decision should always be discoverable. 

* Look across the AI system lifecycle and make sure that portions that interact with data, metadata and models are secured and maintain data privacy as required. 

* Examine training data sets for sources of potential bias and make sure that communities are represented in a fair and equitable way. 

Lead author – Vyshnavi    Reviewer – Prasanna 

**6. What are the ethical considerations in determining the legitimate use of the AI system?**

The legal and ethical issues that confront society due to Artificial Intelligence (AI) include 	privacy and Transparency, Technical safety and Bias in Data, Training Sets, etc. 

**Technical Safety** 

The first question for any technology is whether it works as intended. Will AI systems work as they are promised, or will they fail? When they fail, what will be the results of those failures? And if we are dependent upon them, will we be able to survive without them?

**Transparency and Privacy** 

Once we have determined that the technology functions adequately, can we understand how it works and properly gather data on its functioning? Ethical analysis always depends on getting the facts first-only then can evaluation begin. 

**Bias in Data, Training Sets, etc.** 

Algorithmic bias is one of the major concerns in AI right now and will remain so in the future unless we endeavor to make our technological products better than we are. 

**Automating Ethics** 

One strength of AI is that it can automate decision-making, thus lowering the burden on humans and speeding up - potentially greatly speeding up—some kinds of decision-making processes. However, this automation of decision-making will present huge problems for society, because if these automated decisions are good, society will benefit, but if they are bad, society will be harmed. 

Lead author – Prasanna    Reviewer – Vyshnavi 


**References**

[1]. Batuhan UZUN, 2021 "Trex-CNN". https://github.com/uzunb/Trex-CNN

[2]. Nitin Rai, 2019 "Chrome-dino-game-bot". https://github.com/imneonizer/Chrome-dino-game-bot



