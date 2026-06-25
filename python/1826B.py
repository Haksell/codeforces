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
    n = ir()
    a = lmir()
    d = [abs(a[i] - a[~i]) for i in range(n // 2)]
    print(gcd(*d))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
