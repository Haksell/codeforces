# ruff: noqa: E731, E741
from itertools import groupby
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    read()
    fuzz = randint(1, 1 << 30)
    a = sorted({ai + fuzz for ai in mir()})
    g = groupby(ai - i for i, ai in enumerate(a))
    print(sum((sum(1 for _ in v) + 1) // 2 for _, v in g))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
