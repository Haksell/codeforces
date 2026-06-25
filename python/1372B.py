# ruff: noqa: E731, E741
from math import isqrt

for _ in range(int(input())):
    n = int(input())
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            print(n // i, n - n // i)
            break
    else:
        print(1, n - 1)
