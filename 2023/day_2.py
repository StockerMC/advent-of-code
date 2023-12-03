import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    sum = 0
    for i, line in enumerate(lines, start=1):
        good = True
        for sub in line.split(';'):
            a = {'red': 0, 'blue': 0, 'green': 0}
            for b in a.keys():
                for m in re.findall(rf'(\d+) ({b})', sub):
                    a[m[1]] += int(m[0])
            if a['red'] > 12 or a['green'] > 13 or a['blue'] > 14:
                good = False
                break
        if good:
            sum += i
    return sum

def part_two(lines: list[str]):
    sum = 0
    for i, line in enumerate(lines, start=1):
        mina = minb = minc = 1
        for sub in line.split(';'):
            a = {'red': 0, 'blue': 0, 'green': 0}
            for b in a.keys():
                for m in re.findall(rf'(\d+) ({b})', sub):
                    a[m[1]] += int(m[0])
            mina = max(mina, a['red'])
            minb = max(minb, a['blue'])
            minc = max(minc, a['green'])
        sum += mina * minb * minc
    return sum