import collections, string, itertools, math, more_itertools, re, functools

def falseyaccess(list, i):
    try:
        return list[i]
    except:
        return None

def part_one(lines: list[str]):
    total = 0
    for i, line in enumerate(lines):
        j = 0
        while j < len(line):
            # print(j)
            num = ''
            ispart = False
            if j >= len(line):
                break
            while line[j].isdigit():
                if j >= len(line):
                    break
                num += line[j]
                # print(any(falseyaccess(falseyaccess(lines, i+1), j-1+x) not in list('1234567890.') for x in range(3)))
                # breakpoint()
                # 592 FLASE
                # 664 FALSE
                # if num == '592':
                #     breakpoint()
                if any(falseyaccess(falseyaccess(lines, i-1), j-1+x) not in list('1234567890.') + [None] for x in range(3)):
                    ispart = True
                elif any(falseyaccess(falseyaccess(lines, i+1), j-1+x) not in list('1234567890.') + [None] for x in range(3)):
                    ispart = True
                elif falseyaccess(line, j-1) not in list('1234567890.') + [None] or falseyaccess(line, j+1) not in list('1234567890.') + [None]:
                    ispart = True
                j += 1
                if j >= len(line):
                    break
            # if num:
                # print(num, ispart)
                # breakpoint()
            if ispart:
                total += int(num)
            j += 1
            if j >= len(line):
                break
    # breakpoint()
    return total

def part_two(lines: list[str]):
    total = 0
    mapping: dict[tuple[int, int], list[tuple[int, int]]] = collections.defaultdict(list)
    for i, line in enumerate(lines):
        j = 0
        while j < len(line):
            # print(j)
            num = ''
            ispart = False
            if j >= len(line):
                break
            gears: list[tuple[int, int]] = []
            while line[j].isdigit():
                if j >= len(line):
                    break
                num += line[j]
                # print(any(falseyaccess(falseyaccess(lines, i+1), j-1+x) not in list('1234567890.') for x in range(3)))
                # breakpoint()
                # 592 FLASE
                # 664 FALSE
                # if num == '592':
                #     breakpoint()
                if any(falseyaccess(falseyaccess(lines, i-1), j-1+x) == '*' for x in range(3)):
                    ispart = True
                    for x in range(3):
                        if falseyaccess(falseyaccess(lines, i-1), j-1+x) == '*':
                            gears.append((i-1, j-1+x))
                elif any(falseyaccess(falseyaccess(lines, i+1), j-1+x) == '*' for x in range(3)):
                    ispart = True
                    for x in range(3):
                        if falseyaccess(falseyaccess(lines, i+1), j-1+x) == '*':
                            gears.append((i+1, j-1+x))
                elif falseyaccess(line, j-1) == '*' or falseyaccess(line, j+1) == '*':
                    ispart = True
                    for x in range(3):
                        if falseyaccess(line, j-1) == '*':
                            gears.append((i, j-1))
                        elif falseyaccess(line, j+1) == '*':
                            gears.append((i, j+1))
                j += 1
                if j >= len(line):
                    break
            # if num:
                # print(num, ispart)
                # breakpoint()
            if ispart:
                for gear in gears:
                    if (j, int(num)) not in mapping[gear]:
                        mapping[gear].append((j, int(num)))
                total += int(num)
            j += 1
            if j >= len(line):
                break
    # breakpoint()
    total = 0
    for gear, nums in mapping.items():
        # breakpoint()
        if len(nums) == 2:
            total += nums[0][1] * nums[1][1]
    return total