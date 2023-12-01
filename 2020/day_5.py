import collections, string, itertools, math, more_itertools, re, functools
import bisect

def part_one(lines: list[str]):
    highest = 0
    for line in lines:
        lower = 0
        upper = 127
        for char in line[:7]:
            mid = (lower + upper) / 2
            if char == 'F':
                upper = math.floor(mid)
            else:
                lower = math.ceil(mid)

        row = lower

        lower = 0
        upper = 7
        for char in line[7:]:
            mid = (lower + upper) / 2
            if char == 'L':
                upper = math.floor(mid)
            else:
                lower = math.ceil(mid)

        col = lower
        highest = max(highest, row * 8 + col)

    return highest

def part_two(lines: list[str]):
    seats = set()
    for line in lines:
        lower = 0
        upper = 127
        for char in line[:7]:
            mid = (lower + upper) / 2
            if char == 'F':
                upper = math.floor(mid)
            else:
                lower = math.ceil(mid)

        row = lower

        lower = 0
        upper = 7
        for char in line[7:]:
            mid = (lower + upper) / 2
            if char == 'L':
                upper = math.floor(mid)
            else:
                lower = math.ceil(mid)

        col = lower
        seatid = row * 8 + col
        seats.add(seatid)

    for i in range(min(seats) + 1, max(seats)):
        if i not in seats:
            return i
