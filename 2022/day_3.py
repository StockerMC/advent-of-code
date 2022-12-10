import more_itertools

from util import get_input
lines = get_input(2022, 3)

def priority(letter: str):
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38

def part_one():
    score = 0
    for line in lines:
        half = len(line) // 2
        a, b = line[:half], line[half:]
        same = set(a) & set(b)
        score += priority(same.pop())

    return score

def part_two():
    score = 0
    for group in more_itertools.chunked(lines, 3):
        sets = [set(line) for line in group]
        same = sets[0] & sets[1] & sets[2]
        score += priority(same.pop())

    return score
