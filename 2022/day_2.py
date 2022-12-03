from util import get_input
lines = get_input(2022, 2)

def part_one():
    score = 0
    for line in lines:
        o, m = line.split()
        v = ord(m) - 87
        score += v
        if (
            o == 'A' and m == 'Y' or
            o == 'B' and m == 'Z' or
            o == 'C' and m == 'X'
        ):
            score += 6
        elif ord(o) - 65 == ord(m) - 88:
            score += 3

    print(score)

def part_two():
    loss = {
        'A': 3,
        'B': 1,
        'C': 2,
    }
    win = {
        'A': 2,
        'B': 3,
        'C': 1,
    }
    draw = {
        'A': 1,
        'B': 2,
        'C': 3,
    }
    score = 0
    for line in lines:
        o, e = line.split()
        if e == 'X':
            score += loss[o]
        elif e == 'Y':
            score += draw[o] + 3
        else:
            score += win[o] + 6

    print(score)
