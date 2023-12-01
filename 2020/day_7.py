import collections, string, itertools, math, more_itertools, re, functools

parents = collections.defaultdict(list)
def part_one(lines: list[str]):
    for line in lines:
        colour, contains = line.split('bags contain')
        if contains == ' no other bags.':
            continue

        colour = colour.strip()
        # breakpoint()
        contains = re.findall(r'\d+ ([a-z]+ [a-z]+) bag', contains)
        # breakpoint()
        for bag in contains:
            # _, *bag 
            parents[bag].extend([colour, *parents[colour]])

    # print(parents)
    return len(set(parents['shiny gold']))

def part_two(lines: list[str]):
    ...
