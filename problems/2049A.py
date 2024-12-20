# ruff: noqa: E731, E741
from itertools import groupby
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    read()
    a = lmir()
    r = sum(k for k, _ in groupby(a, key=lambda x: x != 0))
    print(min(r, 2))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
