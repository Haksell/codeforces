# ruff: noqa: E731, E741
import math
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    a = lmir()
    full = math.gcd(*a)
    a = [ai // full for ai in a]
    res = g = mini = min(a)
    a.remove(mini)
    while a and g > 1:
        (g, val) = min((math.gcd(g, val), val) for val in a)
        res += g
        a.remove(val)
    res += len(a)
    print(full * res)
