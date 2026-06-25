# ruff: noqa: E731, E741
from itertools import groupby
from operator import itemgetter
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        read()
        groups = sum(map(itemgetter(0), groupby(mir(), key=bool)))
        print(min(groups, 2))


if __name__ == "__main__":
    main()
