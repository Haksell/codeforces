# ruff: noqa: E731, E741
from math import inf

n, k = map(int, input().split())
res = -inf
for _ in range(n):
    f, t = map(int, input().split())
    x = f - max(0, t - k)
    res = max(res, x)
print(res)
