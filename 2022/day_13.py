import collections, string, itertools, math, more_itertools, re, functools
import json
import functools

l = json.loads

def compare(a, b):
    # a - b instead of a < b
    # if (a - b) != 0, a != b --> check if a < b
    # also helps with sorting

    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            if ret := compare(x, y):
                return ret
        return len(a) - len(b)

    if isinstance(a, list):
        return compare(a, [b])

    if isinstance(b, list):
        return compare([a], b)

    assert False

def part_one(lines: list[str]):
    lines.append('')
    pairs = [(l(lines[i]), l(lines[i+1])) for i in range(0, len(lines), 3)]
    total = 0
    for i, (p1, p2) in enumerate(pairs, start=1):
        if compare(p1, p2) < 0:
            total += i

    return total

def part_two(lines: list[str]):
    lines.append('')
    values = [[[2]], [[6]]]
    for line in lines:
        if line == '':
            continue
        values.append(l(line))

    values.sort(key=functools.cmp_to_key(compare))
    total = 1
    for i, value in enumerate(values):
        if value in ([[2]], [[6]]):
            total *= (i + 1)
    return total
