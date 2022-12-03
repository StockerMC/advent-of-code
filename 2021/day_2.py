from util import get_input
values: list[tuple[str, int]] = get_input(2021, 2, func=lambda k: (k.split()[0], int(k.split()[1])))

def part_one() -> int:
    horizontal_position = depth = 0
    for direction, value in values:
        if direction == 'forward':
            horizontal_position += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value

    return horizontal_position * depth

def part_two() -> int:
    horizontal_position = depth = aim = 0
    for direction, value in values:
        if direction == 'forward':
            horizontal_position += value
            depth += aim * value
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value

    return horizontal_position * depth
