# coding=utf-8
"""
Project Euler Problem 9
Special Pythagorean triplet
Solved by Ahrar Monsur

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_pythagorean_triplet():
    for c in xrange(3, 1001):
        for b in xrange(2, c):
            for a in xrange(1, b):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a, b, c, a*b*c

    return "No triplets found"

print find_pythagorean_triplet()


