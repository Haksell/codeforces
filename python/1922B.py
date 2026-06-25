# ruff: noqa: E731, E741
from math import comb
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def counter(a, mx):
    cnt = [0] * (mx + 1)
    for ai in a:
        cnt[ai] += 1
    return cnt


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        res = 0
        smaller = 0
        for v in counter(a, n + 1):
            res += comb(v, 3)
            res += comb(v, 2) * smaller
            smaller += v
        print(res)


if __name__ == "__main__":
    main()
