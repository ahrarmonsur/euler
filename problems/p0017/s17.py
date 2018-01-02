# coding=utf-8
"""
Project Euler Problem 17
Number letter counts
Solved by Ahrar Monsur

If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers
is in compliance with British usage.
"""

tokens = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

def humanize_number(n):
    str_n = str(n)
    phrase = ""
    while str_n:
        if len(str_n) and (len(str_n) < 3) and tokens.get(int(str_n), None):
            phrase += tokens[int(str_n)]
            str_n = ''
            continue
        msd = int(str_n[0])
        if msd:
            mag = 10**(len(str_n)-1)
            token = tokens.get(msd*mag, None)
            phrase += (token + " ") if token and len(str_n) < 3 else (tokens[msd] + " " + tokens[mag] + " ")
            if len(str_n) >= 3 and int(str_n[1:]):
                phrase += "and "
        str_n = str_n[1:]
    return phrase

print sum(map(len, [humanize_number(n).replace(' ', '') for n in xrange(1, 1001)]))



