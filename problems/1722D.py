# ruff: noqa: E731, E741
from itertools import accumulate
import sys

sys.setrecursionlimit(25000)
read = sys.stdin.readline
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    s = input()
    l = sorted([i if c == "L" else n - i - 1 for i, c in enumerate(s)])
    acc = list(accumulate(l, initial=0))
    z = sum(l)
    mi = sum(x + x < n - 1 for x in l) - 1
    res = [z + (n - 1) * (min(i, mi) + 1) - 2 * acc[min(i, mi) + 1] for i in range(n)]
    # print(z, mi)
    # print(l)
    # print(acc)
    print(*res)
    # print()
