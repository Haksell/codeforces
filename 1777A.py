# ruff: noqa: E731, E741
from itertools import groupby


for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print(sum(sum(1 for _ in v) - 1 for _, v in groupby(a, lambda ai: ai & 1)))
