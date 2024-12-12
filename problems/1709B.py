# ruff: noqa: E731, E741
from itertools import accumulate

n, m = map(int, input().split())
a = list(map(int, input().split()))
ltr = [max(0, x - y) for x, y in zip(a, a[1:])]
rtl = [max(0, y - x) for x, y in zip(a, a[1:])]
acc_ltr = list(accumulate(ltr, initial=0))
acc_rtl = list(accumulate(rtl[::-1], initial=0))[::-1]
for _ in range(m):
    s, t = map(int, input().split())
    dir = acc_ltr if s < t else acc_rtl
    print(dir[t - 1] - dir[s - 1])
