# ruff: noqa: E731, E741
from collections import Counter

counter = Counter(input())
odds = sum(v & 1 for v in counter.values())
print("First" if odds == 0 or odds & 1 else "Second")
