# ruff: noqa: E731, E741
def f(g, m):
    for y in range(3):
        for x in range(3):
            if y != x and g[y][x] == g[x][y]:
                return [y + 1 if i & 1 else x + 1 for i in range(m + 1)]


for _ in range(int(input())):
    n, m = map(int, input().split())
    g = [input()[:3] for _ in range(n)][:3]
    if m & 1:
        print("YES")
        print(*[1 if i & 1 else 2 for i in range(m + 1)])
    elif g == ["*a", "b*"] or g == ["*b", "a*"]:
        print("NO")
    elif len(g) == 2:
        print("YES")
        print(*[1 if i & 1 else 2 for i in range(m + 1)])
    elif res := f(g, m):
        print("YES")
        print(*res)
    elif g[0][1] == g[1][2] == g[2][0]:
        print("YES")
        print(*[i % 3 + 1 for i in range(m + 1)])
    else:
        x = 1 if g[0][1] != g[0][2] else 2 if g[1][0] != g[1][2] else 3
        y, z = {1, 2, 3} - {x}
        print("YES")
        r = range(1, m + 2) if m & 2 else range(m + 1)
        print(*[x if i & 1 == 0 else y if i & 2 == 0 else z for i in r])
