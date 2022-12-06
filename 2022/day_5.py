import collections, string, itertools, more_itertools, re

from util import get_input
lines = get_input(2022, 5)

stacks = [
    *[list(reversed(x)) for x in [
        'GJWRFTZ', 'MWG', 'GHNJ', 'WNCRJ', 'MVQGBSFW',
        'CWVDTRS', 'VGZDCNBH', 'CGMNJS', 'LDJCWNPG'
    ]]   
]

def part_one():
    for line in lines:
        if 'move' not in line:
            continue
        a, b, c = map(int, re.findall(r'(\d+)', line))
        b -= 1
        c -= 1
        taken = [stacks[b].pop() for _ in range(min(a, len(stacks[b])))]
        stacks[c].extend(taken)

    print(''.join(stack[-1] for stack in stacks))

def part_two():
    for line in lines:
        if 'move' not in line:
            continue
        a, b, c = map(int, re.findall(r'(\d+)', line))
        b -= 1
        c -= 1
        taken = [stacks[b].pop() for _ in range(min(a, len(stacks[b])))]
        stacks[c].extend(reversed(taken))
