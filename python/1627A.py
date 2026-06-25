# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, w, r, c = map(int, input().split())
    r -= 1
    c -= 1
    g = [input() for _ in range(h)]
    if all("B" not in r for r in g):
        print(-1)
    elif g[r][c] == "B":
        print(0)
    elif "B" in g[r] or any(g[y][c] == "B" for y in range(h)):
        print(1)
    else:
        print(2)
