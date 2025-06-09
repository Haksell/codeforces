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
    n = ir()
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            print(n // i, n - n // i)
            return
    print(1, n - 1)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
