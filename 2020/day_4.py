import collections, string, itertools, math, more_itertools, re, functools

mandatory = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def part_one(lines: list[str]):
    lines.append('')
    passports = []
    passport = {}
    for line in lines:
        if line == '':
            passports.append(passport)
            passport = {}
        else:
            for field in line.split():
                a, b = field.split(':')
                passport[a] = b

    return sum(
        1 for passport in passports
        if all(v in passport for v in mandatory)
    )

def part_two(lines: list[str]):
    lines.append('')
    passports: list[dict[str, str]] = []
    passport = {}
    for line in lines:
        if line == '':
            passports.append(passport)
            passport = {}
        else:
            for field in line.split():
                a, b = field.split(':')
                passport[a] = b

    count = 0
    for passport in passports:
        if not all(field in passport for field in mandatory):
            continue
        byr = int(passport['byr'])
        iyr = int(passport['iyr'])
        eyr = int(passport['eyr'])
        hgt = passport['hgt']
        hcl = passport['hcl']
        ecl = passport['ecl']
        pid = passport['pid']
        if (
            1920 <= byr <= 2002 and
            2010 <= iyr <= 2020 and
            2020 <= eyr <= 2030 and
            hgt.endswith(('cm', 'in')) and
            (150 <= int(hgt[:-2]) <= 193 if hgt.endswith('cm') else 59 <= int(hgt[:-2]) <= 76) and
            hcl[0] == '#' and all(x.isdigit() or 'a' <= x <= 'f' for x in hcl[1:]) and
            ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and
            len(pid) == 9 and all(x.isdigit() for x in pid)
        ):
            # breakpoint()
            count += 1
        
    return count
