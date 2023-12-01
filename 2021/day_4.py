import collections, string, itertools, math, more_itertools, re, functools
from dataclasses import dataclass

@dataclass
class Square:
    number: int
    called: bool = False

def is_bingo(board: list[list[Square]]):
    # check rows/columns
    for row in board:
        if all(square.called for square in row):
            # breakpoint()
            return True

    for col in zip(*board):
        if all(square.called for square in col):
            # breakpoint()
            return True

    return False
    # # check diagonals
    # d1 = [board[x][x] for x in range(5)]
    # d2 = [board[4-x][x] for x in range(5)]
    # return all(square.called for square in d1) or all(square.called for square in d2)

def call_num(board: list[list[Square]], num: int):
    for row in board:
        for cell in row:
            if cell.number == num:
                cell.called = True

def get_unmarked(board: list[list[Square]]):
    for row in board:
        for cell in row:
            if not cell.called:
                yield cell.number

def part_one(lines: list[str]):
    lines.append('')
    numbers = map(int, lines[0].split(','))
    boards: list[list[list[Square]]] = []
    rows = []
    for line in lines[2:]:
        if line == '':
            boards.append(rows)
            rows = []
            continue
        rows.append([Square(int(x)) for x in line.split()])

    for num in numbers:        
        for board in boards:
            call_num(board, num)
            if is_bingo(board):
                return sum(get_unmarked(board)) * num

def part_two(lines: list[str]):
    lines.append('')
    numbers = map(int, lines[0].split(','))
    boards: list[list[list[Square]]] = []
    rows = []
    for line in lines[2:]:
        if line == '':
            boards.append(rows)
            rows = []
            continue
        rows.append([Square(int(x)) for x in line.split()])

    seen = set()
    score = 0
    for num in numbers:        
        for i, board in enumerate(boards):
            call_num(board, num)
            if is_bingo(board):
                if i not in seen:
                    score = sum(get_unmarked(board)) * num
                seen.add(i)

    return score
