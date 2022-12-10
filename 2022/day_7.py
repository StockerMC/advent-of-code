import collections, string, itertools, more_itertools, re
import pathlib

    # if line.startswith('$ ls'):
    #     listdirs = True
    # elif line.startswith('$ cd'):
    #     d = line[5:]
    #     listdirs = False
    #     if d == '..':
    #         current.pop()
    #     elif d == '/':
    #         current = ['/']
    #     else:
    #         current.append(current[-1] + f'{d}/')

    # if listdirs:
    #     a, b = line.split()
    #     if a.isdigit():
    #         for x in current:
    #             directories[x] += int(a)
    #             # directories[x] = tuple(dir)  # type: ignore


def part_one(lines):
    directories = collections.defaultdict(int)
    current = pathlib.Path('/')
    for line in lines:
        match line.split():
            case [size, _] if size.isdigit():
                for path in [current, *current.parents]:
                    directories[path] += int(size)
            case ['$', 'cd', new]:
                current /= new
                current = current.resolve()

    return sum(v for v in directories.values() if v <= 100_000)

def part_two(lines):
    directories = collections.defaultdict(int)
    current = pathlib.Path('/')
    for line in lines:
        match line.split():
            case [size, _] if size.isdigit():
                for path in [current, *current.parents]:
                    directories[path] += int(size)
            case ['$', 'cd', new]:
                current /= new
                current = current.resolve()

    used = directories[pathlib.Path('/').resolve()]
    return min(v for v in directories.values() if used - v <= 30_000_000)
