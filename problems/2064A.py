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
    s = input()
    print(sum(1 for _ in groupby(s)) - 1 + (s[0] == "1"))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
