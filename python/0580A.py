# ruff: noqa: E731, E741
from math import inf

input()
a = list(map(int, input().split()))
res = cur = 0
last = -inf
for i, n in enumerate(a):
    cur = 1 if n < last else cur + 1
    res = max(res, cur)
    last = n
print(res)
