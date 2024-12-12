# ruff: noqa: E731, E741

from math import gcd
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n, a, b = mir()
    g = gcd(a, b)
    c = lmir()
    c = sorted({ci % g for ci in c})
    print(g, c)
    res = c[-1] - c[0]
    for i, ci in enumerate(c):
        res = min(res, c[i] + g - c[(i + 1) % len(c)])
    print(res)
