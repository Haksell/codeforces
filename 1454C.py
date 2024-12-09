# ruff: noqa: E731, E741
from collections import Counter
from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    a = [k for k, _ in groupby(map(int, input().split()))]
    c = Counter(a)
    c[a[0]] -= 1
    c[a[-1]] -= 1
    print(min(c.values()) + 1)
