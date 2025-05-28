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
    i = isqrt(n)
    if i * i != n:
        print(-1)
    else:
        print(0, i)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
