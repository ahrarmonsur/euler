"""
Project Euler Problem 43
Sub-string divisibility
Solved by Ahrar Monsur

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools

def check_substring_divisibility(str_num):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for idx, divisor in enumerate(divisors):
        substring_num = int(str_num[idx+1: idx+4])
        if substring_num % divisor:
            return False

    return True




def main():
    digits = "0123456789"
    candidates = []
    permutations = itertools.permutations(digits, 10)
    for permutation in permutations:
        str_permutation = "".join(permutation)
        is_valid = check_substring_divisibility(str_permutation)
        if is_valid:
            candidates.append(int(str_permutation))
            print permutation

    print sum(candidates)

main()