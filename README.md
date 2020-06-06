## Google Hashcode 2019

### About

* This includes the solutions my team and I came up with for the [Google Hashcode 2019](https://codingcompetitions.withgoogle.com/hashcode/) challenge as well as the Practise Problem for 2019.
* Hashcode is a team programming competition, organized by Google, for students and professionals around the world where the premise is focused around solving engineering problems as part of a team.

### Challenge

#### Practice Problem 
* The pizza is represented as a rectangular, 2-dimensional grid of R rows and C columns. The cells within the grid are referenced using a pair of 0-based coordinates ```[r, c]```, denoting respectively the row and the column of the cell.
    * Each cell of the pizza contains either:
        * mushroom, represented in the input file as M ; or
        * tomato, represented in the input file as T
* A slice of pizza is a rectangular section of the pizza delimited by two rows and two columns, without holes.
* The slices we want to cut out must contain at least L cells of each ingredient (that is, at least L cells of mushroom and at least L cells of tomato) and at most H cells of any kind in total – surprising as it is, there is such a thing as too much pizza in one slice.
* The slices being cut out cannot overlap. The slices being cut do not need to cover the entire pizza.
* The goal is to cut correct slices out of the pizza maximizing the total number of cells in all slices.
* For more information on the Practise problem look [pizzapracticeproblem.pdf](practice/pizzapracticeproblem.pdf).

#### Google Hashcode 2019 Problem
* Given a list of photos and the tags associated with each photo, arrange the photos into a slideshow that is as interesting as possible.
* A slideshow is an ordered list of slides. Each slide contains either:
    * a single horizontal photo, or
    * two vertical photos side-by-side
* If the slide contains a single horizontal photo, the tags of the slide are the same as the tags of the single photo it contains.
* If the slide contains two ve ical photos, the tags of the slide are all the tags present in any or both of the two photos it contains.
* Each photo can be used either once or not at all. The slideshow must have at least one slide.
* For more information on the Hashcode 2019 problem look [Hashcodeproblem.pdf](hashcode2019/Hashcodeproblem.pdf).




### Pre-requisites
* You need to have ***Python 3*** installed on your machine, follow this [guide](https://realpython.com/installing-python/) to install Python.

### How to Run

#### Practise Problem
* First go into the directory ```practise``` and run the command ```python pizza.py input_size```.
* To change the output the solution will save results to change the line ```f = open("outputC.txt","w+")``` to one of :
    * outputA.txt
    * outputB.txt
    * outputC.txt
    * outputD.txt
* To change the input the solution will take in run change the ```input_size``` variable to one of:
    * a_example.in
    * b_small.in
    * c_medium.in
    * d_big.in
* To test the quality of the solution submit the output test file [here](https://codingcompetitions.withgoogle.com/hashcode/archive/2019).

#### Google Hashcode 2019 Problem
* First go into the directory ```hashcode2019``` and run the command ```python slideshow.py input_size```.
* To change the output the solution will save results to change the line ```f = open("outputC.txt","w+")``` to one of :
    * outputA.txt
    * outputB.txt
    * outputC.txt
    * outputD.txt
    * outputE.txt
* To change the input the solution will take in run change the ```input_size``` variable to one of:
    * a_example.in
    * b_lovely_landscapes.in
    * c_memorable_moments.in
    * d_pet_pictures.in
    * e_shiny_selfies.in
* To test the quality of the solution submit the output test file [here](https://codingcompetitions.withgoogle.com/hashcode/archive/2019).




