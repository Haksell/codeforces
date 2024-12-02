# ruff: noqa: E731, E741
from math import gcd, isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    g = gcd(*mir())
    i = isqrt(g)
    r = -1 if i * i == g else 0
    for i in range(1, i + 1):
        if g % i == 0:
            r += 2
    print(r)


if __name__ == "__main__":
    main()
