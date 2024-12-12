# ruff: noqa: E731, E741
for _ in range(int(input())):
    grid = [list(map(int, input())) for _ in range(9)]
    for y, x in [
        (0, 0),
        (3, 1),
        (6, 2),
        (1, 3),
        (4, 4),
        (7, 5),
        (2, 6),
        (5, 7),
        (8, 8),
    ]:
        grid[y][x] = (grid[y][x] + 1) % 9 or 9
    for row in grid:
        print("".join(map(str, row)))
