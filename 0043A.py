# ruff: noqa: E731, E741
from collections import Counter

print(Counter(input() for _ in range(int(input()))).most_common(1)[0][0])
