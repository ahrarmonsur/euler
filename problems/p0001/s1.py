# coding=utf-8
"""
Project Euler Problem 1
Multiples of 3 and 5
Solved by Ahrar Monsur

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

print sum([i for i in range(1000) if not (i % 3 and i % 5)])
