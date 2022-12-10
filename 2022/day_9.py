import collections, string, itertools, math, more_itertools, re, functools

from util import convert

converter = lambda x: (x.split()[0], int(x.split()[1]))

def x_y_tail_diff(tx: int, ty: int, hx: int, hy: int):
    x = hx - tx
    y = hy - ty
    # the x/y needs to be increased/decreased by this much to be touching the head
    dx = min(1, max((-1, x)))
    dy = min(1, max((-1, y)))
    if (dx, dy) == (x, y):
        # the tail is already touching the head
        return 0, 0
    return dx, dy 

@convert(converter)
def part_one(lines: list[tuple[str, int]]):
    visited = set()
    hx = hy = tx = ty = 0
    for direction, n in lines:
        n = int(n)
        for _ in range(n):
            match direction:
                case 'R':
                    hx += 1
                case 'L':
                    hx -= 1
                case 'U':
                    hy += 1
                case 'D':
                    hy -= 1

            diff = x_y_tail_diff(tx, ty, hx, hy)
            tx += diff[0]
            ty += diff[1]
            visited.add((tx, ty))
    return len(visited)

@convert(converter)
def part_two(lines: list[tuple[str, int]]):
    visited = set()
    rope = [[0, 0] for _ in range(10)]
    for direction, n in lines:
        n = int(n)
        for _ in range(n):
            match direction:
                case 'R':
                    rope[0][0] += 1
                case 'L':
                    rope[0][0] -= 1
                case 'U':
                    rope[0][1] += 1
                case 'D':
                    rope[0][1] -= 1

            for i, head in enumerate(rope[:9]):
                # adjust the next knot to be touching the one ahead of it
                tail = rope[i+1]
                diff = x_y_tail_diff(*tail, *head)
                rope[i+1][0] += diff[0]
                rope[i+1][1] += diff[1]
            visited.add(tuple(rope[-1]))
    return len(visited)
