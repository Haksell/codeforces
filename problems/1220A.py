# ruff: noqa: E731, E741
from collections import Counter

input()
c = Counter(input())
print(*([1] * c["n"] + [0] * c["z"]))
