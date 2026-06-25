# ruff: noqa: E731, E741
from bisect import bisect

n = int(input())
x = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    print(bisect(x, int(input())))
