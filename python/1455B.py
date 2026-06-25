# ruff: noqa: E731, E741
from math import ceil, sqrt

EPSILON = 1e-9
for _ in range(int(input())):
    x = int(input())
    y = ceil(sqrt(2 * x + 1 / 4) - 1 / 2 - EPSILON)
    t = y * (y + 1) >> 1
    print(y + (t - x == 1))
