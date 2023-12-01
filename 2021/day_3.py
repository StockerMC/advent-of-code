import collections

def part_one(lines: list[str]):
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

def part_two(lines: list[str]):
    a = collections.defaultdict(list)
    oxygen = lines.copy()
    scrubber = lines.copy()

    i = 0
    while len(oxygen) > 1:
        a = [line[i] for line in oxygen]
        c = collections.Counter(a).most_common()
        m = c[0][0]
        if c[0][1] == c[1][1]:
            m = '1'
        oxygen = [x for x in oxygen if x[i] == m]
        i += 1

    i = 0
    while len(scrubber) > 1:
        a = [line[i] for line in scrubber]
        c = collections.Counter(a).most_common()
        l = c[1][0]
        if c[0][1] == c[1][1]:
            l = '0'
        scrubber = [x for x in scrubber if x[i] == l]
        i += 1

    
    return int(scrubber[0], 2) * int(oxygen[0], 2)
