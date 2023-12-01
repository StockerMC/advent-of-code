import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    positions = list(map(int, lines[0].split(',')))
    minimum = 1e9
    for i, pos in enumerate(positions):
        temp = 0
        for j, pos2 in enumerate(positions):
            if j == i: continue
            temp += abs(pos - pos2) 
        minimum = min(minimum, temp)

    return minimum

def part_two(lines: list[str]):
    positions = list(map(int, lines[0].split(',')))
    minimum = 1e9
    for pos in range(min(positions), max(positions) + 1):
        temp = 0
        for pos2 in positions:
            if pos == pos2: continue
            diff = abs(pos - pos2)
            temp += (diff * (diff + 1)) // 2
        minimum = min(minimum, temp)

    return minimum
