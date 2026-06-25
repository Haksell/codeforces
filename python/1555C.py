# ruff: noqa: E731, E741
from itertools import accumulate

for _ in range(int(input())):
    m = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    acc1 = list(accumulate(a1[:0:-1], initial=0))[::-1]
    acc2 = list(accumulate(a2[:-1], initial=0))
    print(min(map(max, acc1, acc2)))
