import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    sum = 0
    # can be combined to one line probably
    for line in lines:
        digits = re.findall(r'\d', line)
        sum += int(digits[0] + digits[-1])
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
    all_numbers = list(mapping.keys()) + list(mapping.values())

    lines = lines.copy()
    for i in range(len(lines)):
        line = lines[i]
        indices: list[tuple[int, str]] = []
        # eightwo -> [eight, two]
        for num in all_numbers:
            for m in re.finditer(num, line):
                indices.append((m.end(), m.group(0)))

        indices.sort(key=lambda x: x[0])
        lines[i] = re.sub('|'.join(all_numbers), lambda m: mapping.get(m.group(0), m.group(0)), ''.join(map(lambda x: x[1], indices)))

    return part_one(lines)
