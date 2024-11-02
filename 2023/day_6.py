import collections, string, itertools, math, more_itertools, re, functools

def part_one(lines: list[str]):
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]

    total = 1
    for time, dist in zip(times, distances):
        ways = 0
        for speed in range(1, time):
            remaining = time - speed
            if speed * remaining > dist:
                ways += 1
        total *= ways
    return total

def part_two(lines: list[str]):
    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))

    # could have just done this and waited ~10 seconds
    # return part_one(['_ ' + str(time), '_ ' + str(distance)])

    # for part 2, find the range where this would be true for {speed}
    # s * (t - s) > dist
    # -s^2 + st - d = 0
    # -(s^2 - st + d) = 0

    s1 = (time + math.sqrt(time ** 2 - 4 * distance)) / 2
    s2 = (time - math.sqrt(time ** 2 - 4 * distance)) / 2

    if s1 < s2:
        s1 = math.ceil(s1)
        s2 = math.floor(s2)
    else:
        s1 = math.floor(s1)
        s2 = math.ceil(s2)

    return abs(s2 - s1) + 1
