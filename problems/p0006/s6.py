# coding=utf-8
"""
Project Euler Problem 6
Sum square difference
Solved by Ahrar Monsur

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_square_diff(n):
    gen = xrange(n+1)
    return sum(gen)**2 - sum(map(lambda x: x**2, gen))

print sum_square_diff(100)
