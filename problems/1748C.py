# ruff: noqa: E731, E741
from collections import defaultdict
from itertools import accumulate
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
    acc = list(accumulate(a))
    d = defaultdict(int)
    res = 0
    for s, n in reversed(list(zip(acc, a))):
        d[s] += 1
        if n == 0:
            res += max(d.values())
            d.clear()
    res += d[0]
    print(res)
