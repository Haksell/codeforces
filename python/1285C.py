# ruff: noqa: E731, E741
from math import isqrt, lcm
import sys

x = int(input())
for i in range(isqrt(x), 0, -1):
    j, r = divmod(x, i)
    if r == 0 and lcm(i, j) == x:
        print(i, j)
        sys.exit(0)
