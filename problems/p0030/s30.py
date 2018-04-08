# coding=utf-8
"""
Project Euler Problem 30
Digit fifth powers
Solved by Ahrar Monsur

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
candidates = []
n = 2

# A cursory check for an upper-bound for this problem is done by checking which order of magnitude has a number which
# is larger than the sum of the fifth power of the digits. We can roughly determine that 999999 is a number that fits
# this check. Any iteration less than a million steps is reasonable to attempt a brute-force solution; and so it shall be.
upper_n = 999999

def fifth_power_sum(n):
    return sum(map(lambda x: int(x)**5, str(n)))

for n in range(2, upper_n+1):
    if n == fifth_power_sum(n):
        candidates.append(n)

print sum(candidates)




