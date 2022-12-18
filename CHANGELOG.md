# CHANGELOG

### ADDED

* Created an empty markdown file `README.md`.
* Created a directory named `docs`.
* Created a markdown file `PROPOSAL.md` in `docs` directory for writing project proposal.
* Created a markdown file `DESIGN.md` in `docs` directory for writing project design.
* Created a directory called `src` for code development.
* Created a file `trex_getdata.py` in `src` directory for developing the code for collecting the data.
* Created a directory called `data` to store the images got when run the file `trex_getdata.py`.
* Created a file `trex_train.py` in `src` directory for developing code to train the CNN model using keras.
* Created a file `trex_play.py` in `src` directory for developing code to make the trex play the game.
* Generated `requirements.txt` file using the command: `pip freeze > requirements.txt`.
* Created a markdown file `HOWTO.md` to write how to clone and run the project.
* Created a markdown file `CHANGELOG.md` to keep note of all changes made to project.

### UPDATED

* Updated `PROPOSAL.md` with project proposal.
* Updated introduction and theoretical background for project in `DESIGN.md`.
* Updated the approach for developing the project in `DESIGN.md`.
* Updated the working example and ethical considerations for the project in `DESIGN.md`.
* Updated code in `trex_getdata.py`.
* Updated code in `trex_train.py`.
* Updated code in `trex_play.py`.
* Updated project description in `README.md`.
* Updated `HOWTO.md`.
* Updated `CHANGELOG.md`.

### FIXED

* Fixed pylint errors in `trex_getdata.py`.
* Fixed pylint errors in `trex_train.py`.
* Updated the path to the images generated in `trex_train.py` to fix FileNotFound error.
* Changed the entropy type to 'sparse_categorical_crossentropy' from 'categorical_crossentropy' in `trex_train.py` to fix the value error.
* Fixed pylint errors in `trex_play.py`.


### REMOVED

* Removed .idea folder from remote repository
