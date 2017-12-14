"""
Problem 2
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


# Generator function which yields each successive element in the fibonacci sequence which is still less than n
def fib_to_n(n):
    prev2 = 1
    prev1 = 2
    while prev2 < n:
        yield prev2
        prev1, prev2 = prev2 + prev1, prev1

print sum(n for n in fib_to_n(4000000) if not n % 2)
