# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())

for _ in rir():
    n, k = mir()
    l = list(range(k + 1, n + 1))
    half = (k + 1) >> 1
    l.extend(list(range(half, k)))
    print(len(l))
    print(*l)
