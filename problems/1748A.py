# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    a = n // 2
    b = (n + 1) // 2
    t = a * (a + 1) // 2 + b * (b + 1) // 2
    print(isqrt(t))
