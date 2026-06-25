# ruff: noqa: E731, E741
from math import isqrt


def is_square(n):
    i = isqrt(n)
    return i * i == n


for _ in range(int(input())):
    n = int(input())
    print(
        "YES"
        if (n & 1 == 0 and is_square(n >> 1) or (n & 3 == 0 and is_square(n >> 2)))
        else "NO"
    )
