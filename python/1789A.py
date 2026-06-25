# ruff: noqa: E731, E741
from itertools import combinations
from math import gcd
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
        a = lmir()
        print("YES" if any(gcd(x, y) <= 2 for x, y in combinations(a, 2)) else "NO")


if __name__ == "__main__":
    main()
