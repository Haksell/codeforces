# ruff: noqa: E731, E741
from bisect import bisect
from itertools import accumulate


def int_ceil(numer, denom):
    return (numer + denom - 1) // denom


for _ in range(int(input())):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    d = [0] + sorted(y - x for x, y in zip(a, a[1:]))
    acc = list(accumulate(d))
    tot = [acc[i] + (n - i) * di for i, di in enumerate(d)]
    if h > tot[-1]:
        print(d[-1] + h - tot[-1])
    else:
        idx = bisect(tot, h) - 1
        print(d[idx] + int_ceil(h - tot[idx], n - idx))
