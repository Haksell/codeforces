# ruff: noqa: E731, E741
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ra = {ai: i for i, ai in enumerate(a)}
rb = {bi: i for i, bi in enumerate(b)}
d = [(ra[i] - rb[i]) % n for i in range(1, n + 1)]
print(max(Counter(d).values()))
