import collections, string, itertools

from util import get_input
lines = get_input(2022, 4)

def part_one():
    # could've used set.issubset to check for full subsets
    count = 0
    for line in lines:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if all(x in range(a1, a2 + 1) for x in range(b1, b2 + 1)):
            count += 1
        elif all(x in range(b1, b2 + 1) for x in range(a1, a2 + 1)):
            count += 1

    return count

def part_two():
    # could've used set.intersection to check for any overlaps
    count = 0
    for line in lines:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if any(x in range(a1, a2 + 1) for x in range(b1, b2 + 1)):
            count += 1
        elif any(x in range(b1, b2 + 1) for x in range(a1, a2 + 1)):
            count += 1

    return count
