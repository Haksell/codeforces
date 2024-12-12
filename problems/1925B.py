# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def valid(x, n, d):
    return n * d <= x


def main():
    for _ in rir():
        x, n = mir()
        r = 0
        for i in range(1, isqrt(x) + 1):
            if x % i == 0:
                j = x // i
                if j > r and valid(x, n, j):
                    r = j
                if i > r and valid(x, n, i):
                    r = i
        print(r)


if __name__ == "__main__":
    main()
