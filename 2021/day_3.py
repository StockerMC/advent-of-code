import collections

from util import get_input
lines = get_input(2021, 3)

def part_one():
    a = collections.defaultdict(list)
    g = ''
    e = ''

    for line in lines:
        for i, x in enumerate(line):
            a[i].append(x)

    for i, x in a.items():
        m = collections.Counter(x).most_common()[0][0]
        l = collections.Counter(x).most_common()[-1][0]
        g += m
        e += l

    return int(g, 2) * int(e, 2)

# def part_two():
