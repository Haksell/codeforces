# ruff: noqa: E731, E741
from itertools import accumulate

input()
v = list(map(int, input().split()))
u = sorted(v)
av = list(accumulate(v, initial=0))
au = list(accumulate(u, initial=0))
for _ in range(int(input())):
    t, l, r = map(int, input().split())
    a = av if t == 1 else au
    print(a[r] - a[l - 1])
