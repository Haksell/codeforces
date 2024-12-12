# ruff: noqa: E731, E741
from collections import deque

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    d = deque()
    for i, pi in enumerate(p):
        (d.appendleft if i == 0 or pi < d[0] else d.append)(pi)
    print(*d)
