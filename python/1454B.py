# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    unique = [k for k, v in Counter(a).items() if v == 1]
    print(a.index(min(unique)) + 1 if unique else -1)
