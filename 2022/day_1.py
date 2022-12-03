from util import get_input
lines = get_input(2022, 1)

values = []
cur = 0
for line in lines:
    if not line:
        values.append(cur)
        cur = 0
    else:
        cur += int(line)

def part_one():
    print(max(values))
    # print(max(sum(map(int, group.split())) for group in lines.split('\n\n')))

def part_two():
    values.sort()
    print(sum(values[-3:]))
