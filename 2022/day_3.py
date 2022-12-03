import collections, string, itertools

from util import get_input
lines = get_input(2022, 3)

priorities = {
    **{letter: ord(letter) - 96 for letter in string.ascii_lowercase},
    **{letter: ord(letter) - 38 for letter in string.ascii_uppercase}
}

def part_one():
    score = 0
    for line in lines:
        half = len(line) // 2
        a, b = line[:half], line[half:]
        same = set(a).intersection(set(b)).pop()
        score += priorities[same]

    print(score)

def part_two():
    score = 0
    sets = []
    for i, line in enumerate(lines, start=1):
        line = line.rstrip()
        sets.append(set(line))
        if i % 3 == 0:
            same = sets[0].intersection(sets[1]).intersection(sets[2]).pop()
            score += priorities[same]
            sets = []

    print(score)
