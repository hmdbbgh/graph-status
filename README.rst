==================================
Semi Connected Graph Status Check
==================================

**Contents:**

.. contents:: :local:

Introduction
------------

Purpose of this program is to to determine if 
a directed graph is semi connected or not.

*Definition:*

A directed graph is semi connected if for all pairs of vertices i, j 
there is  either a path from i to j or a path from j to i.

Algorithm
---------

We want to detremine if our directed graph is semi connected or not.

Therefore, first we create a n*n matrix which its initial values on 
the main diagonal are 'True' and the rest are 'False'.

Then we perform Breadth-first search on each of vertices to detremine the
path distance of each vertex from another and if no path have been found,
then we set the distance '-1'. Thus if the distance between two vertices
isn't '-1' then matrix elements of the two vertices will be set 'True'.

Finally when Breadth-first search is performed, if none of the
matrix elements wouldn't be 'False' then we can conclude that our graph is
semi connected.

Instruction
-----------

Step 1.
~~~~~~~
**Install Virtual Environment (venv):**

.. code-block:: bash

   pip install virtualenv

Step 2.
~~~~~~~
**Create a Virtual Environment:**

.. code-block:: bash

   virtualenv venv

Step 3.
~~~~~~~
**Activate your Virtual Environment:**

    For Linux:
        
        .. code-block:: bash

            source venv/bin/activate

    For Windows:
    
        .. code-block:: bash

            venv\Scripts\activate.bat

Step 4.
~~~~~~~
**Install required packages from requirements.txt:**

.. code-block:: bash

    pip install -r requirements.txt

Step 5.
~~~~~~~
**Run the program:**

.. code-block:: bash

    python run.py

Examples
--------

.. image:: https://github.com/hmdbbgh/graph-status/blob/master/Media/Examples/01.png

.. image:: https://github.com/hmdbbgh/graph-status/blob/master/Media/Examples/01_graph.png

.. image:: https://github.com/hmdbbgh/graph-status/blob/master/Media/Examples/02.png

.. image:: https://github.com/hmdbbgh/graph-status/blob/master/Media/Examples/02_graph.png
