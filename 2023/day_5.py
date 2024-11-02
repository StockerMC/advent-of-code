import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    seeds = [int(x) for x in lines[0].split()[1:]]
    maps: dict[int, list[tuple[int, int, int]]] = collections.defaultdict(list)
    i = 3
    for _ in range(7):
        while i < len(lines) and lines[i] not in ('', '\n'):
            line = lines[i]
            a, b, c = list(map(int, line.split()))
            maps[_].append((a, b, c))
            i += 1
        i += 2

    result = 1e10
    for seed in seeds:
        prev = seed
        for m in range(7):
            ranges = maps[m]
            for a, b, c in ranges:
                if b <= prev <= b + c:
                    prev += a - b
                    break

        result = min(result, prev)
    return result

def part_two(lines: list[str]):
    seeds = [(int(x), int(x) + int(y)) for x, y in more_itertools.grouper(lines[0].split()[1:], 2)]
    maps: dict[int, list[tuple[int, int, int]]] = collections.defaultdict(list)
    i = 3
    for _ in range(7):
        while i < len(lines) and lines[i] not in ('', '\n'):
            line = lines[i]
            a, b, c = list(map(int, line.split()))
            maps[_].append((a, b, c))
            i += 1
        i += 2

    result = int(1e10)
    for seed in seeds:
        prev = seed
        for m in range(7):
            ranges = maps[m]
            for a, b, c in ranges:
                lower = max(prev[0], b)
                upper = min(prev[1], b + c)
                if lower < upper and (lower, upper) < prev:
                    prev = (lower, upper)
                    print(prev)
                # instead find all of the values of prev that would satisfy this and check if it's in range
                # possible = range(b, b + c + 1)
                # if b <= prev <= b + c:
                #     prev += a - b
                #     break

        print(prev)
        result = min(result, prev[0])
    return result
