# ruff: noqa: E731, E741
from math import inf

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mini = inf
    ans = 0
    for p in reversed(a):
        if p <= mini:
            mini = p
        else:
            ans += 1
    print(ans)
