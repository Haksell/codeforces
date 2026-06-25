# ruff: noqa: E731, E741
from itertools import groupby
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        s = input()
        r = {k for k, v in groupby(s) if len(list(v)) & 1}
        print("".join(sorted(r)))


if __name__ == "__main__":
    main()
