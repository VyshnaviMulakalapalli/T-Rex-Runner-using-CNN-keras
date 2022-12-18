# HOWTO

## Clone the project:
* Clone the project into your local machine from Github source :` https://github.com/2022-fall-comp-741-841/prasanna-vyshnavi`

## Setting-up virtual environment:
* Open the project folder in PyCharm after cloning in local machine.
* In the status bar (at the bottom of the IDE window), click Python 3.10 and select Interpreter Settings.
* Select Virtualenv Environment
* Check off New environment
* Location should be the path to your project folder
  * If the location is different, change it. 
  * Base interpreter should be Python 3.10 you have installed at the system level.
* Now you can now see the .venv folder with Lib,Scripts sub folders in it under our project in our file structure.

## Install Requirements:
* Install all the packages,modules and other dependencies using `pip install -r requirements.txt`.

## Project structure development:
* Create `docs` folder and in that create 2 markdown files : `DESIGN.md`, `PROPOSAL.md` .
* Create src folder with `trex_play.py`, `trex_train.py`, `trex_getdata.py`.
* After running the `trex_getdata.py` , play the T-rex runner by going to `https://www.trex-game.skipser.com/` while playing the game ,image screenshots are captured and stored in separate 
 data folder which will be used dataset for training the T-rex dino.
