# ruff: noqa: E731, E741
from collections import defaultdict

for _ in range(int(input())):
    h, w = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(h)]
    d1, d2 = defaultdict(int), defaultdict(int)
    for y in range(h):
        for x in range(w):
            d1[x - y] += g[y][x]
            d2[w - 1 - x - y] += g[y][x]
    print(
        max(d1[x - y] + d2[w - 1 - x - y] - g[y][x] for y in range(h) for x in range(w))
    )
