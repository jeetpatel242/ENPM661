# Project 3 Phase 3
## Part-1
# Implementation of A* algorithm on a differential drive (non-holonomic) TurtleBot robot


## Introduction 
This file includes python program solution for Project 3 for
UMD ENPM 661 Spring 2021 batch. The folders consists of python
program along with generated outputs as .mp4 files.
  
    This project will solve given path planning puzzel with A* algorithm using non-holonomic constraints.
	
#### These files are executable:
  * main.py
  * algo.py
  * map.py
  * utils.py
       
### To run this code following libraries are required

* Python3
* NumPy
* math
* matplotlib

### Installation (For ubuntu 18.04)
* Matplotlib
  ````
  sudo apt install python3-matplotlib
  ````
* NumPy
  ````
  pip install numpy
  ````
	
### Running code in ubuntu
After installing dependencies, 
Make sure that current working derectory is same as the directory of program,
You can change the working derectory by using **cd** command.

* Run the following command in this directory, which will START the program
````
python3 main.py
````
* THe program will ask for the clearance (in meters) from the obstacles, provide input in 'float' format. For eg: 0.2.
* Choose the initial position, provide input in [x,y,theta] format. For eg: [1, 1, 0]
* Choose the goal position, provide input in [x,y] format. For eg. [9, 9]
* Enter the two RPM's for the wheels, provide input in [rpm1,rpm2] format, For eg: [6,4]

* The blue circle is the start point, and the yellow circle is the goal with threshold radius of 0.25 meters. The green color is for the explored nodes, while the black color signifies the final path. 

It is important to note that if both python files are in different directory
we have to change to the correct directory again.



### Troubleshooting ###
	Most of the cases the issue will be incorrect working derectory.
	Double check the path by typing **pwd** command in console
  This will output the current working directory.
  Check if it is same as the python file location.

	For issues that you may encounter create an issue on GitHub.
  
## Maintainers ##
### Group-10
Jeet Patel (jeetpatel242@gmail.com)

Mrugesh Shah (mrugesh.shah92@gmail.com)



