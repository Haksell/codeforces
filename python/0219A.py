# ruff: noqa: E731, E741
from collections import Counter

k = int(input())
s = input()
counter = Counter(s)
if any(count % k != 0 for count in counter.values()):
    print(-1)
else:
    print(k * "".join(count // k * c for c, count in counter.items()))
