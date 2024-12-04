# ruff: noqa: E731, E741
from heapq import heappop, heappush
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

UNREACHED = 1 << 62


def dijkstra(graph, horses, start):
    with_horse = [UNREACHED] * len(graph)
    without_horse = [UNREACHED] * len(graph)
    heap = [(0, horses[start], start)]
    while heap:
        d, horse, node = heappop(heap)
        if (horse and d >= with_horse[node]) or (
            not horse and d >= without_horse[node]
        ):
            continue
        (with_horse if horse else without_horse)[node] = d
        for neighbor, w in graph[node].items():
            if horse or horses[node]:
                new_dist = d + (w >> 1)
                if new_dist < with_horse[neighbor]:
                    heappush(heap, (new_dist, True, neighbor))
            else:
                new_dist = d + w
                if new_dist < without_horse[neighbor]:
                    heappush(heap, (new_dist, False, neighbor))
    return list(map(min, with_horse, without_horse))


def main():
    for _ in rir():
        nodes, edges, _ = mir()
        horses = [False] * nodes
        for i in mir():
            horses[i - 1] = True
        graph = [dict() for _ in range(nodes)]
        for _ in range(edges):
            u, v, w = mir()
            graph[u - 1][v - 1] = graph[v - 1][u - 1] = w
        distances_start = dijkstra(graph, horses, 0)
        distances_end = dijkstra(graph, horses, nodes - 1)
        res = min(map(max, distances_start, distances_end))
        print(res if res < UNREACHED else -1)


if __name__ == "__main__":
    main()