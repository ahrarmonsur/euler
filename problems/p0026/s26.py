# coding=utf-8
"""
Project Euler Problem 26
Reciprocal cycles
Solved by Ahrar Monsur

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
with denominators 2 to 10 are given:

1/2	 = 	0.5
1/3	 = 	0.(3)
1/4	 = 	0.25
1/5	 = 	0.2
1/6	 = 	0.1(6)
1/7	 = 	0.(142857)
1/8	 = 	0.125
1/9	 = 	0.(1)
1/10 = 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

# First rendition of the cycle length; does not account for numbers which yield a reciprocal cycle that starts
# later than the ones decimal position
# from __future__ impoort division
# def cycle_length(den):
#     rest = 10
#     i = 0
#     while (rest != 10 and i < 19) or i < 1:
#         temprest = rest
#         rest = (rest % den) * 10
#         print i, temprest, temprest/den, rest
#         i += 1
#     return i


def generate_reciprocal(divisor):
    dividend = remainder = 10
    count = 0
    while remainder:
        count += 1
        quotient = dividend / divisor
        remainder = dividend % divisor
        dividend = remainder * 10
        yield (count, quotient, remainder)
    yield (count, quotient, remainder)

def cycle_length(num):
    memo = {}
    gen = generate_reciprocal(num)
    cur = next(gen)
    while cur[2] not in memo or cur[1] != memo[cur[2]]["quotient"]:
        memo[cur[2]] = {"quotient": cur[1], "position": cur[0]}
        cur = next(gen)

    return cur[0] - memo[cur[2]]["position"]



longest_num = longest_length = 0
for i in xrange(2, 1000):
    l = cycle_length(i)
    if l >= longest_length:
        longest_num, longest_length = i, l

print longest_num, longest_length

# Interesting that the number with with the longest repicocal cycle, 983, has a cycle length of 982
