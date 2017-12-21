# coding=utf-8
"""
Project Euler Problem 3
Largest prime factor
Solved by Ahrar Monsur

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def generate_prime_factors(n):
    i = 2
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            yield i
            n /= i
    if n > 1:
        yield n

print max(generate_prime_factors(600851475143))
