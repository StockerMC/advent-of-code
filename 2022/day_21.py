import collections, string, itertools, math, more_itertools, re, functools
from operator import add, sub, mul, floordiv

values: dict[str, tuple[int, str, int] | tuple[str, str, str]] = {}

ops = {'+': add, '-': sub, '*': mul, '/': floordiv}

def solve(name: str):
    l, op, r = values[name]
    if isinstance(l, str):
        l = solve(l)
    if isinstance(r, str):
        r = solve(r)
    values[name] = (l, op, r)
    return ops[op](l, r)

def part_one(lines: list[str]):
    for line in lines:
        name, rest = line.split(': ')
        if rest.isdigit():
            values[name] = (int(rest), '+', 0)
        else:
            values[name] = tuple(rest.split())

    # values['humn'] = (301, '+', 0)
    root = solve('root')
    # breakpoint()
    return root


def part_two(lines: list[str]):
    ...
