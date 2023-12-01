import collections, string, itertools, math, more_itertools, re, functools
import bisect

def part_one(lines: list[str]):
    total = 0
    for line in lines:
        value = 0
        for i, char in zip(range(len(line)-1, -1, -1), line):
            multiply = 5 ** i
            value += ({'-': -1, '=': -2}.get(char) or int(char)) * multiply

        total += value

    snafu = ''
    while total > 0:
        total, r = divmod(total, 5)
        if r > 2:
            total += 1
        snafu = '012=-'[r] + snafu

    return snafu

def part_two(lines: list[str]):
    ...
