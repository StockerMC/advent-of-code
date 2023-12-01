import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    sum = 0
    # can be combined to one line lol
    for line in lines:
        num = ''
        for char in line:
            if char.isdigit():
                num += char
                break
        for char in line[::-1]:
            if char.isdigit():
                num += char
                break
        # breakpoint()
        sum += int(num)
    return sum

def part_two(lines: list[str]):
    mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    lines = lines.copy()
    sum = 0
    for i in range(len(lines)):
        line = lines[i]
        indices: list[tuple[int, str]] = []
        for x in (list(mapping.keys()) + list(mapping.values())):
            for match in re.finditer(x, line):
                indices.append((match.end(), match.group(0)))

        indices.sort(key=lambda x: x[0])
        lines[i] = re.sub('|'.join(list(mapping.keys()) + list(mapping.values())), lambda m: mapping.get(m.group(0), m.group(0)), ''.join(map(lambda x: x[1], indices)))
        # breakpoint()

    return part_one(lines)
