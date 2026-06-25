# ruff: noqa: E731, E741
from collections import Counter


for _ in range(int(input())):
    n = int(input())
    c = Counter(map(int, input().split()))
    print("YES" if any(v & 1 for v in c.values()) else "NO")
