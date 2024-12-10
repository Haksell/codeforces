# ruff: noqa: E731, E741
from itertools import accumulate
import sys


def range_sum(a, size):
    acc = list(accumulate(a, initial=0))
    return [acc[i] - acc[i - size] for i in range(size, len(acc))]


for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    peaks = [int(x < y > z) for x, y, z in zip(a, a[1:], a[2:])]
    rs = range_sum(peaks, k - 2)
    m = max(rs)
    i = next(i for i, rsi in enumerate(rs) if rsi == m)
    print(m + 1, i + 1)
