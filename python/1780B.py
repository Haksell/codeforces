# ruff: noqa: E731, E741
from math import gcd
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
    s = sum(a)
    p = 0
    res = 1
    for ai in a[:-1]:
        p += ai
        res = max(res, gcd(p, s - p))
    return res


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
