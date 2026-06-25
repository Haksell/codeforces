# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    x, k = mir()
    if x == 1:
        x = int("1" * k)
        k = 1
    return k == 1 and x >= 2 and all(x % i for i in range(2, isqrt(x) + 1))


def main():
    for _ in rir():
        print("YES" if solve() else "NO")


if __name__ == "__main__":
    main()
