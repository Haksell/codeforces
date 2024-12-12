# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    print(sum(min(v, 2) for v in Counter(input()).values()) >> 1)
