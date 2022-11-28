## Project design

Created: 22 November 2022  
Updated: 22 November 2022

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
