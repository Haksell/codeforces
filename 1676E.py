# ruff: noqa: E731, E741
from bisect import bisect_left
from itertools import accumulate

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
    acc = list(accumulate(a))
    for _ in range(q):
        x = int(input())
        print(-1 if x > acc[-1] else bisect_left(acc, x) + 1)
