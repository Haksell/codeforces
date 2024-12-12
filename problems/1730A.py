# ruff: noqa: E731, E741
from collections import Counter


for _ in range(int(input())):
    _, c = map(int, input().split())
    print(sum(min(v, c) for v in Counter(map(int, input().split())).values()))
