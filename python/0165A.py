# ruff: noqa: E731, E741
from collections import defaultdict

l = [list(map(int, input().split())) for _ in range(int(input()))]
h, v = defaultdict(list), defaultdict(list)
for x, y in l:
    h[x].append(y)
    v[y].append(x)
h = {k: sorted(v) for k, v in h.items()}
v = {k: sorted(v) for k, v in v.items()}
print(
    sum(h[x][0] != y and h[x][-1] != y and v[y][0] != x and v[y][-1] != x for x, y in l)
)
