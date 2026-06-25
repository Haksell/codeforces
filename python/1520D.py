# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    input()
    a = [int(n) - i for i, n in enumerate(input().split())]
    c = Counter(a)
    print(sum(v * (v - 1) >> 1 for v in c.values()))
