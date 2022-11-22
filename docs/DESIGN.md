## Project Design
 Created: 22 Nov 2022  
 Updated: 22 Nov 2022

### Content and Organization
#### Introduction  

1. What AI system are you interested in investigating further?
**`T-REX DINO CHROME AI BOT`**
* In this AI system, we teach T-Rex to dodge obstacles in 3 stages. 

**Stages** :  
 1- Collect dataset when playing.  
 2- Train dataset.  
 3- Start and watch it.  

2. Why is it of interest to you?  
Chrome users find themselves without Internet connection occasionally, and when this happens, they enjoy playing the popular T-Rex, Run! Game.  

3. What specifically you'll focus on? What's the overall guiding question your study will pursue?  
In this game, the player controls a dinosaur and accumulates points by jumping over obstacles.
 The controls are simple – press the space bar or the up arrow to jump up or press the down arrow to duck. 

### Theoretical Background

1. What areas or fields of AI provide the theoretical framework of the AI system?   
T-Rex-Runner uses a convolutional neural network that takes an input of the game screen and outputs whether it should or should not jump at that specific moment. It can capture the screen, evaluate it, and output its calculations in real time to play the game. 


2. What are the key concepts and techniques that the AI system is based on?  
* It collects the dataset when playing, trains with the obtained dataset and then it plays the game.
* We need to specify the ROI (Region of Interest) according to screen resolution. We need to change limits (width and height) for the specified ROI.
* When each press direction buttons, it saves ROI pixels by taking the screenshot using mss (multiple screenshot module). 

3. Include appropriate references that describe the field, key concepts, and techniques

 **References**
 
 [1]. Batuhan UZUN, 2021 "Trex-CNN". https://github.com/uzunb/Trex-CNN
 
 [2]. Nitin Rai, 2019 "Chrome-dino-game-bot". https://github.com/imneonizer/Chrome-dino-game-bot