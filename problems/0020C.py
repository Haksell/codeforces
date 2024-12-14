# ruff: noqa: E731, E741
from heapq import heappop, heappush
from math import inf
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
g = [dict() for _ in range(v)]
for _ in range(e):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = min(g[a].get(b, inf), w)
    g[b][a] = min(g[b].get(a, inf), w)

distances = [inf] * v
heap = [(0, 0)]
while heap:
    d, a = heappop(heap)
    if distances[a] == inf:
        distances[a] = d
        for b, w in g[a].items():
            if distances[b] == inf:
                heappush(heap, (d + w, b))

if distances[-1] == inf:
    print(-1)
else:
    path = [v]
    i = v - 1
    while i != 0:
        i = next(j for j, w in g[i].items() if distances[j] + w == distances[i])
        path.append(i + 1)
    print(*reversed(path))
