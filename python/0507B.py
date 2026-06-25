# ruff: noqa: E731, E741
from math import ceil, hypot

r, x0, y0, x1, y1 = map(int, input().split())
print(ceil(hypot(x0 - x1, y0 - y1) / (2 * r)))
