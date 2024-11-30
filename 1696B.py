# ruff: noqa: E731, E741
from itertools import groupby
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        read()
        groups = sum(k for k, _ in groupby(mir(), key=(0).__ne__))
        print(min(groups, 2))


if __name__ == "__main__":
    main()
