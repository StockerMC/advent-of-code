import collections, string, itertools, math, more_itertools, re, functools
from queue import Queue

def part_one(lines: list[str]):
    directions = itertools.cycle(lines[0])

    adj: dict[str, list[str]] = collections.defaultdict(list)
    for line in lines[2:]:
        a, b, c = re.findall('[A-Z]{3}', line)
        adj[a].extend([b, c])


    next_node = 'AAA'
    total = 0
    for direction in directions:
        next_node = adj[next_node][{'L':0,'R':1}[direction]]
        total += 1
        if next_node == 'ZZZ':
            return total

def part_two(lines: list[str]):
    directions = itertools.cycle(lines[0])

    adj: dict[str, list[str]] = collections.defaultdict(list)
    next_nodes: list[str] = []
    for line in lines[2:]:
        a, b, c = re.findall('(?:[1-9]{2})|(?:XX)[A-Z]', line)
        adj[a].extend([b, c])
        if a.endswith('A'):
            next_nodes.append(a)


    total = 0
    for direction in directions:
        next_node = adj[next_node][{'L':0,'R':1}[direction]]
        total += 1
        if next_node == 'ZZZ':
            return total
