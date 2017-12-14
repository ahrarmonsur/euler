# coding=utf-8
"""
Project Euler Problem 4
Largest palindrome product
Solved by Ahrar Monsur

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools as its

def is_palindrome(n):
    strn = str(n)
    return all(strn[i] == strn[-(i+1)] for i in range(len(strn)/2 + 1))

def is_palindrome_factors(a, b):
    return is_palindrome(a*b)

print max(i[0]*i[1] for i in its.product(xrange(100, 1000), repeat=2) if is_palindrome_factors(*i))



