# coding=utf-8
"""
Project Euler Problem 27
Quacratic primes
Solved by Ahrar Monsur

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39. However, when
n = 40, 40^2 + 40 + 41 = 40 (40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41n = 41
is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values
0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
"""

# Since we need to produce prime numbers from the quadratic expression with consecutive values of n starting from n =0,
# we can begin formulating some systems of equations.
# For n = 0, b must be prime
# For n = 1, 1 + a + b much be prime
# Further, since we are asked to find a b value where |b| <= 1000, we have a limited solution space to work with

def sieve_of_eratosthenes(n):
    import math as m
    not_primes = { j for i in xrange(2, int(m.ceil(n**0.5)+1)) for j in xrange(i**2, n, i) }
    return [p for p in xrange(2, n) if p not in not_primes]

def is_prime(n):
    return n > 1 and not bool(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n%i), [])).symmetric_difference([n, 1]))

def q_exp(a, b, n):
    return n**2 + a*n + b


def find_quadratic_primes(max_val):
    max_qp = {}
    prime_set = sieve_of_eratosthenes(max_val + 1)
    for b in prime_set:
        for a in xrange(-1 * max_val + 1, max_val):
            n = 0
            prime = True
            while prime:
                n += 1
                prime = is_prime(q_exp(a, b, n))
            cur_max_count = max_qp.get('count', None)
            if (not cur_max_count) or n >= cur_max_count:
                max_qp['a'] = a
                max_qp['b'] = b
                max_qp['count'] = n

    return max_qp, max_qp['a'] * max_qp['b']


print find_quadratic_primes(1000)





