import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    X = 1
    cycles = 0
    signal = 0
    for line in lines:
        if line == 'noop':
            cycles += 1
            if (cycles - 20) % 40 == 0:
                signal += cycles * X
        else:
            _, V = line.split()
            cycles += 1
            if (cycles - 20) % 40 == 0:
                signal += cycles * X
            cycles += 1
            if (cycles - 20) % 40 == 0:
                signal += cycles * X
            V = int(V)
            X += V

    return signal

def part_two(lines: list[str]):
    X = 1
    cycles = 0
    signal = 0
    rows = [['.' for _ in range(40)] for _ in range(6)]
    sprite = (X - 1, X, X + 1)
    left = 0
    for line in lines:
        if line == 'noop':
            cycles += 1
            rows[left // 40][left % 40] = '#' if left % 40 in sprite else '.'
            left += 1
        else:
            _, V = line.split()
            cycles += 1
            rows[left // 40][left % 40] = '#' if left % 40 in sprite else '.'
            left += 1
            cycles += 1
            rows[left // 40][left % 40] = '#' if left % 40 in sprite else '.'
            left += 1
            V = int(V)
            X += V
            sprite = (X - 1, X, X + 1)

    for row in rows:
        for x in row:
            print(x, end='')
        print()
    print()