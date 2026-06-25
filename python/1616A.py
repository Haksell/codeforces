# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    input()
    a = [abs(int(x)) for x in input().split()]
    print(sum(1 if k == 0 else min(v, 2) for k, v in Counter(a).items()))
