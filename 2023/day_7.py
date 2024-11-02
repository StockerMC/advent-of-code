import collections, string, itertools, math, more_itertools, re, functools

def get_rankings(line: str, p2: bool = False):
    hand = line.split()[0]

    result = (0,)

    allcards = 'AKQT98765432J' if p2 else 'AKQJT98765432'
    for card in (allcards if p2 else 'J'):
        temphand = hand.replace('J', card)
        unique = list(set(temphand))

        pairs = sum(temphand.count(x) == 2 for x in unique)

        five = temphand.count(temphand[0]) == 5
        four = not five and 4 in (temphand.count(temphand[0]), temphand.count(temphand[1]))  
        full = not four and len(unique) == 2
        three = len(unique) == 3 and any(temphand.count(x) == 3 for x in unique)
        twopair = len(unique) == 3 and pairs == 2
        onepair = len(unique) == 4 and pairs == 1
        high = len(unique) == len(temphand)

        result = max(result, (five, four, full, three, twopair, onepair, high, *(len(allcards) - allcards.index(hand[i]) for i in range(len(temphand)))))
    return result

def part_one(lines: list[str]):
    total = 0
    lines.sort(key=get_rankings)
    for i, line in enumerate(lines, start=1):
        bid = int(line.split()[1])
        total += bid * i
    return total

def part_two(lines: list[str]):
    total = 0
    lines.sort(key=lambda x: get_rankings(x, True))
    for i, line in enumerate(lines, start=1):
        bid = int(line.split()[1])
        total += bid * i
    breakpoint()
    return total
