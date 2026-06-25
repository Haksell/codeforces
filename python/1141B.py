# ruff: noqa: E731, E741
from itertools import groupby

n = int(input())
a = list(map(int, input().split()))
groups = [(k, sum(1 for _ in v)) for k, v in groupby(a)]
midnight = groups[0][1] + groups[-1][1] if groups[0][0] == groups[-1][0] == 1 else 0
print(max(midnight, max([n for k, n in groups if k == 1], default=0)))
