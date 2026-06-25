# ruff: noqa: E731, E741
from functools import reduce
from operator import and_
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    read()
    p = lmir()
    misplaced = [i for i, pi in enumerate(p) if i != pi]
    print(reduce(and_, misplaced))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
