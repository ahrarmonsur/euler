# coding=utf-8
"""
Project Euler Problem 40
Champernowne's constant
Solved by Ahrar Monsur

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

def main():
    desired_digits = [1, 10, 100, 1000, 10000, 100000, 1000000]
    count = 0
    length = 0
    product = 1
    while desired_digits:
        next_count = count + 1
        desired_digit = desired_digits[0]
        if length < desired_digit and length + len(str(next_count)) >= desired_digit:
            offset = desired_digit - length
            product = product * int(str(next_count)[offset - 1])
            desired_digits.pop(0)
        count = next_count
        length += len(str(next_count))
    print product

main()