# coding=utf-8
"""
Project Euler Problem 32
Pandigital products
Solved by Ahrar Monsur

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum."""

import itertools as itt

def is_pandigital(product, multiplicand, multiplier):
    total_str = str(product) + str(multiplier) + str(multiplicand)
    if total_str.count('0') != 0:
        return False
    return all(map(lambda n: total_str.count(str(n)) == 1, range(1, 10)))

def proper_divisors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n%i), [])).symmetric_difference([n])

candidates = []
for product in range(1, 100000):
    divisisors = proper_divisors(product)
    for multiplier in divisisors:
        multiplicand = product/multiplier
        if is_pandigital(product, multiplier, multiplicand):
            candidates.append(product)

print sum(set(candidates))


