# coding=utf-8
"""
Project Euler Problem 33
Digit cancelling fractions
Solved by Ahrar Monsur

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from __future__ import division
from functools import reduce

def get_common_digits(numerator, denominator):
    num_str = str(numerator)
    den_str = str(denominator)
    common_digits = set(num_str).intersection(den_str)
    return common_digits

def get_naive_fraction(numerator, denominator):
    common_digits = get_common_digits(numerator, denominator)
    naive_num, naive_den = map(lambda x: [y for y in str(x)], [numerator, denominator])
    for digit in common_digits:
        naive_num.remove(digit)
        naive_den.remove(digit)

    naive_num = int(''.join(naive_num)) if naive_num else 0
    naive_den = int(''.join(naive_den)) if naive_den else 0

    return naive_num, naive_den


def main():
    candidates = []
    den_range = xrange(10, 100)
    for den in den_range:
        num_range = xrange(10, den)
        for num in num_range:
            common_digits = get_common_digits(num, den)
            if common_digits not in [set('0'), set()]:
                naive_num, naive_den = get_naive_fraction(num, den)
                if (naive_num
                    and naive_den
                    and num/den == naive_num/naive_den
                ):
                    candidates.append((num, den))

    # gather all candidate numerators and denominators
    candidate_groups = zip(*candidates)
    num_prod = reduce(lambda x, y: x*y, candidate_groups[0])
    den_prod = reduce(lambda x, y: x*y, candidate_groups[1])

    print "Candidates: {}".format(candidates)
    print "Product of candidates: {}/{}".format(num_prod, den_prod)


main()

