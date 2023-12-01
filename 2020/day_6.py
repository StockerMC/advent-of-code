import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    lines.append('')
    a = set()
    total = 0
    for line in lines:
        if line == '':
            total += len(a)
            a = set()
            continue
        a.update(line)

    return total

def part_two(lines: list[str]):
    lines.append('')
    a: list[set[str]] = []
    total = 0
    for line in lines:
        # breakpoint()
        if line == '':
            total += len(a[0].intersection(*a[1:]))
            a = []
            continue
        a.append(set(line))

    return total
    
