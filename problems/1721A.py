# ruff: noqa: E731, E741
from collections import Counter
import sys

sys.setrecursionlimit(25000)
read = sys.stdin.readline
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    a, b, *_ = map(ord, read())
    c, d, *_ = map(ord, read())
    l = sorted(Counter([a, b, c, d]).values())
    print(len(l) - 1)
