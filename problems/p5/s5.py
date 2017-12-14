# coding=utf-8
"""
Project Euler Problem 5
Smallest multiple
Solved by Ahrar Monsur

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from operator import mul

def smallest_multiple(n):
    result = []
    for i in xrange(1, n+1):
        # This solution starts from the smallest number and adds each as a candidate until the product of
        # all the previous candidates cannot be divided evently by the current number. At that point, all previous
        # candidates which are factors of the current number is ejected from the list and the current number is added
        # to the candidate list. The solution is the product of the final candidate list.
        #
        # The reason we cannot start from the larger numbers and work our way to the smaller ones is because it produces
        # an unnecessarily large product, which could have been smaller by incorporating some smaller candidates
        # (and would still qualify for being a multiple of all numbers)
        product = reduce(mul, result, 1)
        if product % i:
            result = filter(lambda x: i % x, result)
            result.append(i)
    return reduce(mul, result, 1)

print smallest_multiple(20)

