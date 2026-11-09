import sys

read = sys.stdin.readline


def build_graph(n, jumps):
    graph = [[] for _ in range(n)]
    for i, jump in enumerate(jumps):
        if i != 0:
            graph[i].append(i - 1)
        if i != n - 1:
            graph[i].append(i + 1)
        if jump > i + 1:
            graph[i].append(jump)
    return graph


def bfs(n, graph):
    distances = [-1] * n
    distances[0] = 0
    level = [0]
    distance = 0
    while level:
        distance += 1
        next_level = []
        for node in level:
            for neighbor in graph[node]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distance
                    next_level.append(neighbor)
        level = next_level
    return distances


def main():
    n = int(read())
    jumps = [int(j) - 1 for j in read().split()]
    graph = build_graph(n, jumps)
    distances = bfs(n, graph)
    print(*distances)


if __name__ == "__main__":
    main()
