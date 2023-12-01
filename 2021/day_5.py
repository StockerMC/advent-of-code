import collections, string, itertools, math, more_itertools, re, functools

# def r(a, b):
#     if a > b:
#         return range(a, b - 1, -1)
#     else:
#         return range(a, b + 1)

def part_one(lines: list[str]):
    count = collections.defaultdict(int)
    for line in lines:
        a, b = line.split(' -> ')
        ax, ay = map(int, a.split(','))
        bx, by = map(int, b.split(','))

        if ax == bx:
            for y in range(min(ay, by), max(ay, by) + 1):
                count[ax, y] += 1
        elif ay == by:
            for x in range(min(ax, bx), max(ax, bx) + 1):
                count[x, ay] += 1

    return sum(1 for x in count.values() if x > 1)

def part_two(lines: list[str]):
    ...
