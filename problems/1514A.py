# ruff: noqa: E731, E741
from math import isqrt


def is_square(n):
    i = isqrt(n)
    return i * i == n


for _ in range(int(input())):
    input()
    print("NO" if all(map(is_square, map(int, input().split()))) else "YES")
