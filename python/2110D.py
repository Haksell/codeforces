# ruff: noqa: E731, E741
import math
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def attempt(nodes, batteries, graph, allowed):
    mx = [-math.inf] * nodes
    mx[0] = 0
    for e in range(1, nodes):
        for s, w in graph[e]:
            if mx[s] + batteries[s] >= w and allowed >= w:
                mx[e] = max(mx[e], min(mx[s] + batteries[s], allowed))
    return math.isfinite(mx[-1])


def solve():
    nodes, edges = mir()
    batteries = lmir()
    graph = [[] for _ in range(nodes)]
    for _ in range(edges):
        s, e, w = mir()
        graph[e - 1].append((s - 1, w))
    if not attempt(nodes, batteries, graph, math.inf):
        return -1
    bits = 55
    lo = 0
    hi = 1 << bits
    res = -1
    while lo <= hi:
        mi = lo + hi >> 1
        if attempt(nodes, batteries, graph, mi):
            hi = mi - 1
            res = mi
        else:
            lo = mi + 1
    return res


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
