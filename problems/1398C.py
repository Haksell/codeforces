# ruff: noqa: E731, E741
from collections import Counter
from itertools import accumulate

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))
    acc = [x - i for i, x in enumerate(accumulate(a, initial=0))]
    print(sum(v * (v - 1) >> 1 for v in Counter(acc).values()))
