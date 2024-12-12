# ruff: noqa: E731, E741
from collections import Counter

n = int(input())
s = input()
counter = Counter(s[i : i + 2] for i in range(n - 1))
print(counter.most_common(1)[0][0])
