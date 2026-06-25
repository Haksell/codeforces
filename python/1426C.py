# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        i = isqrt(n)
        if i * i == n:
            print(i + i - 2)
        elif i * (i + 1) >= n:
            print(i + i - 1)
        else:
            print(i + i)


if __name__ == "__main__":
    main()
