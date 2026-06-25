# ruff: noqa: E731, E741
from itertools import groupby

for _ in range(int(input())):
    _, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    groups = [sum(1 for _ in v) for k, v in groupby(a, lambda x: x <= q) if k]
    big_groups = [g - k + 1 for g in groups if g >= k]
    print(sum(n * (n + 1) >> 1 for n in big_groups))
