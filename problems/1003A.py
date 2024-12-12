# ruff: noqa: E731, E741
from collections import Counter

input()
print(Counter(input().split()).most_common(1)[0][1])
