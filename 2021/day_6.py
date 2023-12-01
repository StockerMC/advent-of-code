import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    school = list(map(int, lines[0].split(',')))
    for _ in range(80):
        for i, timer in enumerate(school.copy()):
            if timer == 0:
                school[i] = 6
                school.append(8)
            else:
                school[i] -= 1
    return len(school)

def part_two(lines: list[str]):
    school = list(map(int, lines[0].split(',')))
    counts = collections.Counter(school)
    for _ in range(256):
        counts = collections.Counter(
            {timer - 1: count for timer, count in counts.items()}
        )
        # -1 = 0
        counts[6] += counts[-1]
        counts[8] += counts[-1]
        del counts[-1]

    return sum(counts.values())
