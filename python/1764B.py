# ruff: noqa: E731, E741
from functools import reduce
from math import gcd
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    a = lmir()
    print(max(a) // reduce(gcd, a))
