import collections, string, itertools, more_itertools, re

from util import get_input
lines = get_input(2022, 6)

def part_one():
    for i, a in enumerate(more_itertools.windowed(lines[0], 4)):
        if len(set(a)) == len(a):
            return i + 4

def part_two():
    for i, a in enumerate(more_itertools.windowed(lines[0], 14)):
        if len(set(a)) == len(a):
            return i + 14
