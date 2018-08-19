# coding=utf-8
"""
Project Euler Problem 31
Coin sums
Solved by Ahrar Monsur

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

import itertools as itt
# The value, in pence, of the coins of the English currency
coins = [200, 100, 50, 20, 10, 5, 2, 1]

def reducing_fn(total, coins, counter):
    if total == 0: return counter + 1
    elif total < 0 or not coins: return counter
    return reducing_fn(total - coins[-1], coins, counter) + reducing_fn(total, coins[:-1], counter)

def change_combos(total):
    return reducing_fn(total, coins, 0)


print change_combos(200)





