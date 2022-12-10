import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    grid = []
    rowlength = collength = 0
    for line in lines:
        rowlength = len(line)
        collength += 1
        row = []
        for char in line:
            row.append(char == '#')
        grid.append(row)
    trees = 0
    x, y = 0, 0
    i = 0
    while y != collength - 1:
        x = i * 3
        y = i
        trees += grid[(y)%(collength)][(x)%(rowlength)]
        i += 1
    return trees

def part_two(lines: list[str]):
    grid = []
    rowlength = collength = 0
    for line in lines:
        rowlength = len(line)
        collength += 1
        row = []
        for char in line:
            row.append(char == '#')
        grid.append(row)

    trees = 1
    for ix, jx in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        x, y = 0, 0
        temp = 0
        while y != collength - 1:
            x += ix
            y += jx
            temp += grid[(y)%(collength)][(x)%(rowlength)]

        trees *= temp

    return trees
