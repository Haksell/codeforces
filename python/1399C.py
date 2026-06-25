# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    res = 0
    for s in range(2, 2 * n + 1):
        d = Counter(w)
        tot = (d[s / 2] >> 1) + sum(min(d[i], d[s - i]) for i in range(1, (s + 1) >> 1))
        res = max(res, tot)
    print(res)
