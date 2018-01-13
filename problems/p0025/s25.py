# coding=utf-8
"""
Project Euler Problem 25
1000-digit Fibonacci number
Solved by Ahrar Monsur

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_(n−1) + F_(n−2), where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
The 12th term, F_12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

prev2 = prev1 = 1
idx = 2
while len(str(prev1)) < 1000:
    idx += 1
    prev1, prev2 = prev2 + prev1, prev1

print "Index: {}\nValue: {}".format(idx, prev1)
