values = []

def part_one(lines):
    cur = 0
    for line in lines:
        if not line:
            values.append(cur)
            cur = 0
        else:
            cur += int(line)
    return max(values)
    # print(max(sum(map(int, group.split())) for group in lines.split('\n\n')))

def part_two(lines):
    values.sort()
    return sum(values[-3:])
