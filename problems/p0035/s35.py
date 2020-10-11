"""
Project Euler Problem 35
Circular primes
Solved by Ahrar Monsur

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def sieve_of_eratosthenes(n):
    import math as m
    not_primes = {j for i in xrange(2, int(m.ceil(n**0.5)+1)) for j in xrange(i**2, n, i)}
    return [p for p in xrange(2, n) if p not in not_primes]

def get_rotations(n):
    rotations = [n]
    str_n = str(n)
    for i in range(1, len(str_n)):
        rotations.append(int(str_n[-i:]+str_n[len(str_n)-1]))

    return rotations

def main():
    prime_set = sieve_of_eratosthenes(1000000)
    circular_primes = set()
    for p in prime_set:
        rotations = get_rotations(p)
        if all(map(lambda rot: rot in prime_set, rotations)):
            circular_primes.update(rotations)
    print "Number of circular primes below 1000000: {}".format(len(circular_primes))


main()