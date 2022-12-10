import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    valid = 0
    for line in lines:
        a, b, c, d = re.match(r'(\d+)-(\d+) ([a-z]): (.+)', line).groups()  # type: ignore
        if int(a) <= d.count(c) <= int(b):
            valid += 1

    return valid

def part_two(lines: list[str]):
    valid = 0
    for line in lines:
        a, b, c, d = re.match(r'(\d+)-(\d+) ([a-z]): (.+)', line).groups()  # type: ignore
        if ((d[int(a)-1] == c) + (d[int(b)-1] == c)) == 1:
            valid += 1

    return 0
