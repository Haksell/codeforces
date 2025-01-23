# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, m = mir()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = mir()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    seen = [False] * n
    res = 0
    for i in range(n):
        if seen[i]:
            continue
        seen[i] = True
        component = [i]
        stack = [i]
        while stack:
            u = stack.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
                    component.append(v)
        nodes = len(component)
        edges = sum(len(g[u]) for u in component) >> 1
        is_tree = nodes == edges + 1
        res += is_tree
    print(res)


if __name__ == "__main__":
    main()
