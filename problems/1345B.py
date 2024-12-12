# ruff: noqa: E731, E741
from math import sqrt


def f_inv(n, epsilon=1e-8):
    return int(sqrt(2 / 3 * n + 1 / 36) - 1 / 6 + epsilon)


def f(n):
    return n * (3 * n + 1) >> 1


for _ in range(int(input())):
    n = int(input())
    res = 0
    while n >= 2:
        n -= f(f_inv(n))
        res += 1
    print(res)
