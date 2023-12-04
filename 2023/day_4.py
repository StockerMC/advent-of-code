import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    total = 0
    for line in lines:
        _ = line.split(': ')[1:]
        _ = ''.join(_).split('|')
        winning = list(map(int, _[0].split()))
        yours = list(map(int, _[1].split()))
        matches = set(winning) & set(yours)
        points = int(pow(2, (len(matches) - 1)))
        total += points
    return total

def part_two(lines: list[str]):
    counts = collections.defaultdict()
    for i in range(len(lines)):
        counts[i] = 1

    for i, line in enumerate(lines):
        _ = line.split(': ')[1:]
        _ = ''.join(_).split('|')
        winning = list(map(int, _[0].split()))
        yours = list(map(int, _[1].split()))
        matches = set(winning) & set(yours)
        
        for j in range(i + 1, i + len(matches) + 1):
            counts[j] += counts[i]

    return sum(counts.values())
