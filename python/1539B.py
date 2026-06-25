# ruff: noqa: E731, E741
from itertools import accumulate

n, q = map(int, input().split())
s = [ord(c) - 96 for c in input()]
acc = list(accumulate(s, initial=0))
for _ in range(q):
    l, r = map(int, input().split())
    print(acc[r] - acc[l - 1])
