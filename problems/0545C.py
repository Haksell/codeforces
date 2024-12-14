# ruff: noqa: E731, E741
from math import inf

xs = []
hs = []
n = int(input())
for _ in range(n):
    x, h = map(int, input().split())
    xs.append(x)
    hs.append(h)

ans = 0
last = -inf
for i, (x, h) in enumerate(zip(xs, hs)):
    if x - h > last:
        last = x
        ans += 1
    elif i == n - 1 or x + h < xs[i + 1]:
        ans += 1
        last = x + h
    else:
        last = x
print(ans)
