# ruff: noqa: E731, E741
from math import sqrt
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: list(map(int, read().split()))
lmir = lambda: list(map(int, read().split()))


def it(n, eps=1e-9):
    return int(sqrt((n << 1) + 0.25) - 0.5 + eps)


def tr(n):
    return n * (n + 1) >> 1


for _ in rir():
    m, s = mir()
    b = lmir()
    if len(set(b)) != len(b):
        print("NO")
    else:
        mb = max(b)
        sb = sum(b)
        t = sb + s
        u = it(t)
        if tr(u) == t and u >= mb:
            print("YES")
        else:
            print("NO")
