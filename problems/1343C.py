# ruff: noqa: E731, E741
from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g = groupby(a, key=lambda x: x > 0)
    print(sum(max(v) for _, v in g))
