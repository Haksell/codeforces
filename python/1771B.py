# ruff: noqa: E731, E741
from bisect import bisect_left
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n, m = mir()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = mir()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    g = list(map(sorted, g))
    ans = 0
    start = 0
    for i in range(n):
        prev = bisect_left(g[i], i)
        if prev > 0:
            start = max(start, g[i][prev - 1] + 1)
        ans += i - start + 1
    print(ans)
