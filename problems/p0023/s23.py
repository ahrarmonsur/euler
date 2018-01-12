# coding=utf-8
"""
Project Euler Problem 23
Non-abundant sums
Solved by Ahrar Monsur

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import itertools as its
max_n = 28124

# Helper function which accepts a number n and returns the sum of the proper divisors of that number
def d(n):
    return sum(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n%i), [])).symmetric_difference([n]))

abundants = [n for n in xrange(max_n) if d(n) > n]
abundant_sums = set(sum(i) for i in its.combinations_with_replacement(abundants, 2))

print sum(set(range(max_n)).difference(abundant_sums))
