# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(n - max(Counter(a).values()))
