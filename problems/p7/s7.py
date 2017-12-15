# coding=utf-8
"""
Project Euler Problem 7
10001st prime
Solved by Ahrar Monsur

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def nth_prime(n):
    i = 2           # The first prime
    primes = [i]
    while len(primes) < n:
        if (i % 2) and all(map(lambda x: i % x,  primes)):
           primes.append(i)
        i += 1

    return primes[-1]

print nth_prime(10001)

# This is the first challenge which took a significantly long amount of time to run.
# I believe this probelm would have easier if asked for a largest prime under the value of n. Then, I could have
# have implemented a Sieve of Eratosthenes, and memoized the process for efficiency. Instead, having an open bound
# on the iteration (who knows how large the 10001st prime is), the easy solution was to keep iterating.
