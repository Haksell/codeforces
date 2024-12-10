# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    counter = Counter(c for _ in range(n) for c in input())
    print("YES" if all(v % n == 0 for v in counter.values()) else "NO")
