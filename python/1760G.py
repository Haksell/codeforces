# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def no_jump(g, a, b):
    stack = [(None, a, 0)]
    xors = []
    while stack:
        parent, node, x = stack.pop()
        xors.append(x)
        for child in g[node]:
            if child == b:
                return x == g[node][child]
            if child != parent:
                stack.append((node, child, x ^ g[node][child]))


def get_xors(g, a, avoid):
    stack = [(None, a, 0)]
    xors = []
    while stack:
        parent, node, x = stack.pop()
        if node != a:
            xors.append(x)
        for child in g[node]:
            if child != parent and child != avoid:
                stack.append((node, child, x ^ g[node][child]))
    return xors


for _ in rir():
    n, a, b = mir()
    a -= 1
    b -= 1
    g = [dict() for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = mir()
        g[u - 1][v - 1] = w
        g[v - 1][u - 1] = w
    if no_jump(g, a, b):
        print("YES")
        continue
    xa = get_xors(g, a, b)
    xb = get_xors(g, b, None)
    if 0 in xb or set(xa) & set(xb):
        print("YES")
    else:
        print("NO")
