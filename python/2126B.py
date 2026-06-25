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
    n, k = mir()
    a = lmir()
    res = 0
    for w, v in groupby(a):
        if w == 1:
            continue
        v = sum(1 for _ in v)
        res += (v + 1) // (k + 1)
    print(res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
