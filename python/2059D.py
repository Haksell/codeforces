# ruff: noqa: E731, E741
from heapq import heappop, heappush
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def parse_graph(n):
    g = [[] for _ in range(n)]
    for _ in rir():
        a, b = mir()
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    return g


def solve():
    n, s1, s2 = mir()
    g1 = parse_graph(n)
    g2 = parse_graph(n)

    ends = [bool(set(g1[i]) & set(g2[i])) for i in range(n)]
    if not any(ends):
        return -1

    h = [(0, s1 - 1, s2 - 1)]
    seen = set()
    best_cost = 1 << 21
    while h:
        cost, u1, u2 = heappop(h)
        if u1 == u2 and ends[u1]:
            return cost
        if (u1, u2) in seen:
            continue
        seen.add((u1, u2))
        for v1 in g1[u1]:
            for v2 in g2[u2]:
                if (v1, v2) not in seen:
                    new_cost = cost + abs(v1 - v2)
                    if new_cost < best_cost:
                        if v1 == v2 and ends[v1]:
                            best_cost = min(best_cost, new_cost)
                        heappush(h, (new_cost, v1, v2))

    return -1


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
