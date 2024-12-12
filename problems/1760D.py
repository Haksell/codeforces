# ruff: noqa: E731, E741
from itertools import groupby
from math import inf
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    a = [inf] + [k for k, _ in groupby(mir())] + [inf]
    print(
        "YES" if sum(x > y < z for x, y, z in zip(a, a[1:], a[2:])) == 1 else "NO",
    )
