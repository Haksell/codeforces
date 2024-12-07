# ruff: noqa: E731, E741
from math import isqrt


def is_square(n):
    i = isqrt(n)
    return i * i == n


for _ in range(int(input())):
    x, y = map(int, input().split())
    print(0 if x == y == 0 else 1 if is_square(x * x + y * y) else 2)
