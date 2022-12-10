import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    grid: list[str] = []
    rowlen = collen = 0
    for line in lines:
        grid.append(line)
        rowlen = len(line)
        collen += 1

    total = rowlen * 2 + collen * 2 - 4
    for y in range(1, collen - 1):
        for x in range(1, rowlen - 1):
            val = grid[y][x]
            left = grid[y][:x]
            right = grid[y][x+1:]
            up = grid[:y]
            down = grid[y+1:]
            if any(
                all(a < val for a in b)
                for b in (left, right)
            ) or any(
                all(a[x] < val for a in b)
                for b in (up, down)
            ):
                total += 1

    return total

def part_two(lines: list[str]):
    grid: list[str] = []
    rowlen = collen = 0
    for line in lines:
        row = line
        grid.append(line)
        rowlen = len(line)
        collen += 1

    score = 1
    for y in range(1, collen - 1):
        for x in range(1, rowlen - 1):
            val = grid[y][x]
            left = grid[y][:x]
            right = grid[y][x+1:]
            up = grid[:y]
            down = grid[y+1:]
            s = 1
            for a in (list(reversed(left)), right):
                dist = 0
                for i, b in enumerate(a, start=1):
                    dist += 1
                    if b >= val or i == len(a):
                        s *= dist
                        break

            for a in (list(reversed(up)), down):
                dist = 0
                for i, b in enumerate(a, start=1):
                    dist += 1
                    if b[x] >= val or i == len(a):
                        s *= dist
                        break

            score = max(score, s)
    return score
