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
    f = randint(1, 1 << 30)
    read()
    a = [ai + f for ai in mir()]

    seen = set()
    d = set()
    for ai in a:
        if ai not in seen:
            seen.add(ai)
        elif ai not in d:
            d.add(ai)

    lo, hi = -1, -2
    clo = 1
    for k, v in groupby(a, d.__contains__):
        v = list(v)
        if not k:
            chi = clo + len(v) - 1
            if chi - clo > hi - lo:
                lo, hi = clo, chi
        clo += len(v)

    if lo != -1:
        print(lo, hi)
    else:
        print(0)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
