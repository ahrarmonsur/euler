# coding=utf-8
"""
Project Euler Problem 10
Summation of primes
Solved by Ahrar Monsur

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def sieve_of_eratosthenes(n):
    import math as m
    not_primes = { j for i in xrange(2, int(m.ceil(n**0.5)+1)) for j in xrange(i**2, n, i) }
    return [p for p in xrange(2, n) if p not in not_primes]

print sum(sieve_of_eratosthenes(2000000))

# So, this problem taught me that it is actually pretty easy to do nested loops in a list comprehension.
# For the following form:
#   for i in iter1:
#       for j in iter2:
#           for k in iter3:
#               ...
#               arr.append(i*j*k*...)
#
# The list comprehension is the following: [i*j*k*... for i in iter1 for j in iter2 for k in iter3 ...]
# As you can seem it is just a matter of chaining the for statements. How cool is that?!
