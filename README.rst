==================================
Semi Connected Graph Status Check
==================================

Contents:


Introduction
------------

Purpose of this program is to to determine if 
a directed graph is semi connected or not.

Defeniton:
A directed graph is semi connected if for all pairs of vertices i,j 
there is  either a path from i to j or a path from j to i.

Algorithm
---------

We want to detremine if our directed graph is semi connected or not.
Therefore, first we create a n*n matrix which its initial values on the 
main diagonal are 'True' and the rest are 'False'.
Then we perform Breadth-first search on each of vertices to detremine the
path distance of each vertex from another and if no path have found, then 
we set the distance '-1'.


Instruction
-----------

Step 1.
~~~~~~~
Install Virtual Envitoment (venv):

:: pip install virtualenv

Step 2.
~~~~~~~
Create a Virtual Envitoment:

:: virtualenv venv

Step 3.
~~~~~~~
Activate your Virtual Envitoment:

    For Linux:

        :: source venv/bin/activate

    For Windows;

        :: venv\Scripts\activate.bat

Step 4.
~~~~~~~
Install required packages from requirements.txt:

:: pip install -r requirements.txt

Step 5.
~~~~~~~
Run the program:

:: python run.py


Examples
--------