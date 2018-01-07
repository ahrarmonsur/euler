# coding=utf-8
"""
Project Euler Problem 21
Amicable numbers
Solved by Ahrar Monsur

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n):
    return sum(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n%i), [])).symmetric_difference([n]))

upper_bound = 10000
print sum([n for n in xrange(upper_bound) if n != d(n) and d(n) < upper_bound and d(d(n)) == n])
