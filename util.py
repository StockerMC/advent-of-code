from __future__ import annotations

import pathlib
from typing import Any, Callable, Generic, Literal, TypeVar, overload

T = TypeVar('T')
PT = TypeVar('PT', int, str)
Point = tuple[int, int]

@overload
def get_input(year: int, day: int, *, raw: Literal[True], func: None = ...) -> str:
    ...

@overload
def get_input(year: int, day: int, *, raw: bool = ..., func: Callable[[str], T]) -> list[T]:
    ...

@overload
def get_input(year: int, day: int, *, raw: bool = ..., func: None = ...) -> list[str]:
    ...

def get_input(year: int, day: int, *, raw: bool = False, func: Callable[[str], Any] | None = None) -> list[Any] | str:
    with open(pathlib.Path(__file__).parent / f'{year}/inputs/day_{day}.txt') as f:
        text = f.read()
        if raw:
            return text
        values = [func(value) if func else value for value in text.splitlines()]
        return values

def convert(converter: Callable[[str], T]) -> Callable[[Callable[[list[T]], PT]], Callable[[list[T]], PT]]:
    def decorator(func: Callable[[list[T]], PT]) -> Callable[[list[T]], PT]:
        func.converter = converter
        return func
    return decorator

# class Grid(Generic[T]):
#     def __init__(self, data: list[list[T]]) -> None:
#         self.data = data

#     def diagonals_from(self, point: Point):
#         # for i in range