# ruff: noqa: E731, E741
from itertools import count
from math import isqrt


def is_composite(n):
    return any(n % i == 0 for i in range(2, isqrt(n) + 1))


n = int(input())
for i in count(4):
    j = n - i
    if is_composite(i) and is_composite(j):
        print(i, j)
        exit()
