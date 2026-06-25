# ruff: noqa: E731, E741
from math import inf

input()
l = list(map(int, input().split()))
res = cur = 0
last = -inf
for i, n in enumerate(l):
    if n > last:
        cur += 1
        res = max(res, cur)
    else:
        cur = 1
    last = n
print(res)
