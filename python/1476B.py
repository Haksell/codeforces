# ruff: noqa: E731, E741
from itertools import accumulate
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def int_ceil(num, den):
    return (num + den - 1) // den


def main():
    for _ in rir():
        n, k = mir()
        p = lmir()
        a = list(accumulate(p))
        r = 0
        for i in range(1, n):
            x = int_ceil(100 * p[i] - k * a[i - 1], k)
            r = max(r, x)
        print(r)


if __name__ == "__main__":
    main()
