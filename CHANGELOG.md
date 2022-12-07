# CHANGELOG

### ADDED

* Created an empty markdown file `README.md`.
* Created a directory named `docs`.
* Created a markdown file `PROPOSAL.md` in `docs` directory for writing project proposal.
* Update `PROPOSAL.md` with project proposal.
* Created a markdown file `DESIGN.md` in `docs` directory for writing project design.
* Added introduction and theoretical background for project in design.
* Added the approach for developing the project in design.
* Added the working example and ethical considerations for the project in design.
* Created a directory called `src` for code development.
* Created a file `trex_getdata.py` in `src` directory for developing the code for collecting the data.
* Created a directory called `data` to store the images got when run the file `trex_getdata.py`.
* Created a file `trex_train.py` in `src` directory for developing code to train the CNN model using keras.
* Created a file `trex_play.py` in `src` directory for developing code to make the trex play the game.
* 

### FIXED

* Fixed pylint errors in `trex_getdata.py`.
* Fixed pylint errors in `trex_train.py`.
* Updated the path to the images generated in `trex_train.py` to fix FileNotFound error.
* Changed the entropy type to 'sparse_categorical_crossentropy' from 'categorical_crossentropy' in `trex_train.py` to fix the value error.
* Fixed pylint errors in `trex_play.py`.


### REMOVED

* Removed .idea folder from remote repository
