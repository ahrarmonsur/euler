# coding=utf-8
"""
Project Euler Problem 18
Maximum path sum I
Solved by Ahrar Monsur

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)


COMMENTARY:
So, this problem has a naive, brute force solution of a depth-first search through the triangle. This is understandably
not scalable, as the complexity grows exponentially with addition of a new row.

The key to my solution was not in going downwards, but upwards instead. If you traverse downwards, the option pool
increases with each row. By contrast, going from any number on the bottom row towards the top, the path narrows, indicating
fewer and fewer combinations with each row. The next step in the logic of this solution is to note that only two numbers
in the ith row has a path of any one number on the (i-1)th row. With these two pieces of knowledge, we can formulate
the algorithm of creating a running list of sums, going from the last row upwards.

In the ith row, for the kth element, look at sum of that number and the kth or the (k+1)th elements of the (i+1)th row.
Choose the greater sum, and send the resulting array upwards for evaluation with the (i-1)th row. With this approach,
each successive step is a smaller version of the same model, thus making the solution sequential rather than combinatorial.

This solution would also be an appropriate solution for Problem 67, which is a much larger version of this one.
"""

num_triangle = [map(int, line.split()) for line in """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".strip().split("\n")]


def recursive_promotion(triangle, sum_arr=None):
    if not triangle:
        return sum(sum_arr) if sum_arr else 0

    sum_arr = sum_arr or [0]*(len(triangle[-1])+1)
    sum_arr = [max(triangle[-1][i] + sum_arr[i], triangle[-1][i] + sum_arr[i+1]) for i in xrange(len(triangle[-1]))]
    return recursive_promotion(triangle[:-1], sum_arr)

print recursive_promotion(num_triangle)






