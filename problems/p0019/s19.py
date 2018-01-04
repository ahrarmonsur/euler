# coding=utf-8
"""
Project Euler Problem 19
Counting Sundays
Solved by Ahrar Monsur

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def get_num_ds(y, m):
    return dpm.get(m, get_feb_ds(y))

def get_feb_ds(y):
    return 28 if (y % 4) or (not (y % 100) and (y % 400)) else 29

# Dictionary of days for each month
# 0 = Jan, 11 = Dec
dpm = {
    0: 31,
    2: 31,
    3: 30,
    4: 31,
    5: 30,
    6: 31,
    7: 31,
    8: 30,
    9: 31,
    10: 30,
    11: 31,
}

# NOTE: The days are indexed 0 to 6 where 0 = Monday and 6 = Sunday
# NOTE: To store the date information, we will use a 3 element array in the following format: [year, month, date]
# The boundaries (inclusive) of the period in which we are counting Sundays
start_t = [1901, 0, 1]
end_t = [2000, 11, 31]

# Initial conditions
cur_t = [1900, 0, 1]
cur_d = 0
count = 0

while all(map(lambda x: x[0] <= x[1], zip(cur_t, end_t))):
    count += all(map(lambda x: x[0] >= x[1] and x[0] <=x[2], zip(cur_t, start_t, end_t))) and cur_d == 6

    num_ds = get_num_ds(*cur_t[:2])
    cur_d = (cur_d + num_ds) % 7

    # increment month and year
    cur_t[1] = (cur_t[1] + 1) % 12
    cur_t[0] += 1 if not cur_t[1] else 0

print count

