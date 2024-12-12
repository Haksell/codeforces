# ruff: noqa: E731, E741
from itertools import accumulate
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
p = sorted(map(int, input().split()), reverse=True)
a = list(accumulate(p, initial=0))
for _ in range(q):
    x, y = map(int, input().split())
    print(a[x] - a[x - y])
