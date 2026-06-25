# ruff: noqa: E731, E741
from itertools import accumulate

s = input()
l = [c1 == c2 for c1, c2 in zip(s, s[1:])]
acc = [0] + list(accumulate(l))
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(acc[r - 1] - acc[l - 1])
