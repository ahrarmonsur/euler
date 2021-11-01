"""
Project Euler Problem 48
Self powers
Solved by Ahrar Monsur

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def main():
    max_digits = 1000
    sum = 0
    for i in range(1, max_digits+1):
        sum += i**i
    print str(sum)[-10:]


main()