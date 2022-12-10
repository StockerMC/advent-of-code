import collections, string, itertools, math, more_itertools, re

def part_one(lines: list[str]):
    for x in itertools.combinations(map(int, lines), 2):
        if sum(x) == 2020:
            return math.prod(x)

def part_two(lines: list[str]):
    for x in itertools.combinations(map(int, lines), 3):
        if sum(x) == 2020:
            return math.prod(x)
