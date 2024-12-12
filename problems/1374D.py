# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mods = [-ai % k for ai in a if ai % k != 0]
    if not mods:
        print(0)
        continue
    x, y = max(Counter(mods).items(), key=lambda t: t[::-1])
    print(k * (y - 1) + x + 1)
