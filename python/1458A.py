# ruff: noqa: E731, E741
from math import gcd
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive(a, b):
    g = gcd(*[x - y for x, y in zip(a, a[1:])])
    if g == 0:
        return [bj + a[0] for bj in b]
    r = a[0] % g
    return [gcd(g, bj + r) for bj in b]


def main():
    read()
    a = lmir()
    b = lmir()
    print(*naive(a, b))


if __name__ == "__main__":
    main()
