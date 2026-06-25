# ruff: noqa: E731, E741
from fractions import Fraction
from math import inf

n, x0, y0 = map(int, input().split())
slopes = set()
for _ in range(n):
    x, y = map(int, input().split())
    x, y = x - x0, y - y0
    if x == 0:
        if y != 0:
            slopes.add(inf)
    else:
        slopes.add(Fraction(y, x))
print(max(1, len(slopes)))
