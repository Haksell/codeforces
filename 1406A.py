# ruff: noqa: E731, E741
from collections import Counter
from itertools import count


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    print(next(i for i in count() if c[i] < 2) + next(i for i in count() if c[i] == 0))
