Sudoku
======

3x3 Sudoku puzzle and simple recursive solver

Input
=====
A textfile with the following format:

    0 0 6 0 3 0 0 0 0
    0 0 0 2 0 1 8 0 5
    0 0 8 7 5 4 0 2 0
    8 4 0 3 0 0 0 5 0
    0 0 9 0 0 2 1 0 0
    0 0 2 9 0 0 7 0 6
    0 9 0 0 4 0 3 6 0
    0 6 5 0 0 7 0 0 4
    7 8 4 0 0 0 0 0 9

A blank square is represented by a 0.

Output
======
Prints the unsolved puzzle, and the prints solution if it is possible. Otherwise, prints false.

    0 0 6 | 0 3 0 | 0 0 0 
    0 0 0 | 2 0 1 | 8 0 5 
    0 0 8 | 7 5 4 | 0 2 0 
    ------|-------|------
    8 4 0 | 3 0 0 | 0 5 0 
    0 0 9 | 0 0 2 | 1 0 0 
    0 0 2 | 9 0 0 | 7 0 6 
    ------|-------|------
    0 9 0 | 0 4 0 | 3 6 0 
    0 6 5 | 0 0 7 | 0 0 4 
    7 8 4 | 0 0 0 | 0 0 9 
     
    5 2 6 | 8 3 9 | 4 7 1 
    4 7 3 | 2 6 1 | 8 9 5 
    9 1 8 | 7 5 4 | 6 2 3 
    ------|-------|------
    8 4 7 | 3 1 6 | 9 5 2 
    6 5 9 | 4 7 2 | 1 3 8 
    1 3 2 | 9 8 5 | 7 4 6 
    ------|-------|------
    2 9 1 | 5 4 8 | 3 6 7 
    3 6 5 | 1 9 7 | 2 8 4 
    7 8 4 | 6 2 3 | 5 1 9 
