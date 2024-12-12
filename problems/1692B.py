# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    print(n - (1 + sum(v - 1 for v in c.values()) & ~1))
