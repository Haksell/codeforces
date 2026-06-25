# ruff: noqa: E731, E741
from itertools import groupby
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 998244353


def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i % MOD
    return res


def solve():
    s = input()
    a = 0
    b = 1
    for _, v in groupby(s):
        n = sum(1 for _ in v)
        a += n - 1
        b = b * n % MOD
    print(a, b * factorial(a) % MOD)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
