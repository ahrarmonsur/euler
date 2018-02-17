# coding=utf-8
"""
Project Euler Problem 28
Number spiral diagonals
Solved by Ahrar Monsur

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

# Instead of developing a solution which constructs the spiral, noting when the direction changes, and using that to
# run a tally, we can look at the problem differently, and potentially come up with a more elegant solution.
# We should begin by noting that the nth layer of the spiral has a maximum number, which is (2*n-1)^2, occuring at the
# top left corner. In other words, the square of the nth odd number.
# Further, each layer, save the first one, has four numbers (each corner) we want to add to the tally of the previous layer.
# For the layer of a particular odd number base =, k, with the max number in that layer being k^2, the sum of the four numbers are:
# \sum_{i=0}^{3} k^2 - i(k-1) = 4*k^2 - 6*k + 6

# With the above analysis, lets develop the solution


def layer_sum(odd_base):
    return 4 * (odd_base**2) - 6 * odd_base + 6

def sum_spiral_diagonals(dim):
    # dim: side length of the largest square formed by the spiral
    if dim%2 == 0:
        raise ValueError("Malformed spiral. The side length of a spiral must be an odd number")
    if dim == 1: return 1
    return layer_sum(dim) + sum_spiral_diagonals(dim - 2)

print sum_spiral_diagonals(1001)






