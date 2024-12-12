# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    g = [input() for _ in range(8)]
    print(
        *next(
            (y + 1, x + 1)
            for y in range(1, 7)
            for x in range(1, 7)
            if g[y - 1][x - 1] == g[y - 1][x + 1] == "#"
        )
    )
