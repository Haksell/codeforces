# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    m = c.most_common(1)[0][1]
    l = len(c)
    res = min(m, l)
    print(res - 1 if l == m else res)
