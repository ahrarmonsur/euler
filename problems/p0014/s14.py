# coding=utf-8
"""
Project Euler Problem 14
Longest Collatz sequence
Solved by Ahrar Monsur

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import operator
memo = {}

def collatz(n, original=None, count=0):
    original = original or n
    count += 1
    if n == 1:
        memo[original] = count
        return 1
    else:
        n = 3*n + 1 if n % 2 else n/2
        return 1 + memo.get(n, collatz(n, original, count))


map(collatz, xrange(1, 1000000))

# This was a clever way of iterating through the memo and getting the key of the maximum chain length
print max(memo.iteritems(), key=operator.itemgetter(1))[0]
