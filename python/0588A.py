# ruff: noqa: E731, E741
from math import inf

min_p = inf
ans = 0
for _ in range(int(input())):
    ai, pi = map(int, input().split())
    min_p = min(min_p, pi)
    ans += ai * min_p
print(ans)
