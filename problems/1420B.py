# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [ai.bit_length() for ai in a]
    c = Counter(b)
    print(sum(v * (v - 1) >> 1 for v in c.values()))
