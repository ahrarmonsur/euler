# coding=utf-8
"""
Project Euler Problem 15
Lattice paths
Solved by Ahrar Monsur

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


# My initial thought was to model a recursive solution which makes accept a lattice size
# (assuming you alwyas start at top left corner) and makes a move either down or right. Then, the new lattice
# modelled just as the initial problem, but with a smaller lattice (potential path). Continue this problem till
# you model a latttice which is of 0 side length, meaning you have reached the bottom right side. The recursive function
# is written below.
#
# def num_paths(xmax, ymax):
#     if xmax == ymax == 0:
#         return 1
#     return (num_paths(xmax - 1, ymax) if xmax else 0) + (num_paths(xmax, ymax - 1) if ymax else 0)
#
# The problem is that the recursive function uses a stack that has a large time/space overhead, meaning as the lattice
# size increases, the time the program takes to reach completion increases exponentially. (Note, that this solution
# essentially creates a depth-first decision tree)
#
# An alternative way to think about the issue is that given a lattice which requires x number of rights and y number
# of downs to go from top-left to bottom right, it is essentially a combination problem of arranging x Rs and y Ds into
# x + y moves. This is a simple nCr problem.

def nCr(n, r):
   from math import factorial as f
   return f(n) // (f(n-r)*f(r))

xmax = ymax = 20
print nCr(xmax + ymax, xmax)



