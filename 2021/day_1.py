import more_itertools

from util import get_input
values = get_input(2021, 1, func=int)

def part_one():
    previous_value: int | None = None
    increased_measurements = 0

    for value in values:
        if previous_value is not None and value > previous_value:
            increased_measurements += 1

        previous_value = value

    print(increased_measurements)

def part_two():
    increased_sums = previous_sum = 0
    groups = list(more_itertools.triplewise(values))
    for group in groups[1:]:
        group_sum = sum(group)
        if group_sum > previous_sum:
            increased_sums += 1
        
        previous_sum = group_sum

    print(increased_sums)
