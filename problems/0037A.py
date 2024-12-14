# ruff: noqa: E731, E741
from collections import Counter

n = int(input())
l = list(map(int, input().split()))
counter = Counter(l)
print(counter.most_common(1)[0][1], len(counter))
