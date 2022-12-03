from util import get_input
lines = get_input(2022, 1)

def part_one():
    # print(max(sum(map(int, group.split())) for group in lines.split('\n\n')))
    maxv = 0
    v = 0
    for line in lines:
        if not line:
            maxv = max(maxv, v)
            v = 0
            continue
        v += int(line)

    print(maxv)

def part_two():
    maxv = []
    v = 0
    for line in lines:
        if not line:
            maxv.append(v)
            v = 0
            continue

        v += int(line)

    maxv.sort()
    print(sum(maxv[-3:]))
