import collections, string, itertools, math, more_itertools, re, functools
import operator
from dataclasses import dataclass, field
from typing import *

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

@dataclass
class Monkey:
    items: list[int] = field(default_factory=list)
    operation: str = ''
    test: int = 0
    is_true: int = -1
    is_false: int = -1

def parse_monkey_input(line: str, monkey: Monkey):
    match line.split():
        case ['Starting', 'items:', *items]:
            monkey.items = [int(item.strip(',')) for item in items]
        case ['Operation:', 'new', '=', *op]:
            monkey.operation = ' '.join(op)
        case ['Test:', *_, n]:
            monkey.test = int(n)
        case ['If', 'true:', *_, 'monkey', n]:
            monkey.is_true = int(n)
        case ['If', 'false:', *_, 'monkey', n]:
            monkey.is_false = int(n)

def part_one(lines: list[str]):
    lines.append('')
    monkeys: list[Monkey] = []
    monkey = Monkey()
    for line in lines:
        if line == '':
            monkeys.append(monkey)
            monkey = Monkey()
            continue

        parse_monkey_input(line, monkey)

    count = collections.defaultdict(int)
    rounds = 20
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys.copy()):
            for j, item in enumerate(monkey.items.copy()):
                item = eval(monkey.operation.replace('old', str(item)))
                item //= 3
                monkey.items.pop(0)
                # breakpoint()
                if item % monkey.test == 0:
                    monkeys[monkey.is_true].items.append(item)
                else:
                    monkeys[monkey.is_false].items.append(item)
                count[i] += 1

    values = sorted(count.values(), reverse=True)
    return values[0] * values[1]

def part_two(lines: list[str]):
    lines.append('')
    monkeys: list[Monkey] = []
    monkey = Monkey()
    for line in lines:
        if line == '':
            monkeys.append(monkey)
            monkey = Monkey()
            continue

        parse_monkey_input(line, monkey)

    count = collections.defaultdict(int)
    rounds = 10000
    mod = math.lcm(*[monkey.test for monkey in monkeys])
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys.copy()):
            for item in monkey.items.copy():
                item = eval(monkey.operation.replace('old', str(item)))
                # item //= 3
                item %= mod
                monkey.items.pop(0)
                # breakpoint()
                if item % monkey.test == 0:
                    monkeys[monkey.is_true].items.append(item)
                else:
                    monkeys[monkey.is_false].items.append(item)
                count[i] += 1

    values = sorted(count.values(), reverse=True)
    return values[0] * values[1]
