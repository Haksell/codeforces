# ruff: noqa: E731, E741
from bisect import bisect_left
from itertools import accumulate
import sys

read = sys.stdin.readline
mir = lambda: map(int, read().split())


def f(a, d, m, q, t):
    if t <= 0 and m < q:
        return -1
    elif q <= m:
        return bisect_left(d, q)
    z = 0 if t == 0 else max(0, (q - m) // t)
    return z * len(a) + bisect_left(d, q - t * z)


for _ in range(int(read())):
    n, m = mir()
    a = list(mir())
    d = list(accumulate(list(accumulate(a + a)), max))
    m = max(accumulate(a))
    t = sum(a)
    z = [f(a, d, m, q, t) for q in mir()]
    print(*z)
