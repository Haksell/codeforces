# ruff: noqa: E731, E741
from itertools import groupby

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()
    g = sum(1 for _ in groupby(s))
    x = g // 2 + 1 if b < 0 else n
    print(n * a + b * x)
