# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    g = [list(input()) for _ in range(n)]
    (y1, x1), (y2, x2) = [(y, x) for y in range(n) for x in range(n) if g[y][x] == "*"]
    if y1 == y2:
        d = abs(x1 - x2)
        newy = y1 - 1 if y1 > 0 else y1 + 1
        g[newy][x1] = "*"
        g[newy][x2] = "*"
    elif x1 == x2:
        d = abs(y1 - y2)
        newx = x1 - 1 if x1 > 0 else x1 + 1
        g[y1][newx] = "*"
        g[y2][newx] = "*"
    else:
        g[y1][x2] = "*"
        g[y2][x1] = "*"
    print("\n".join("".join(r) for r in g))
