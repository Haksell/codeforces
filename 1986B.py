# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, w = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(h)]
    for val, y, x in sorted([(-m[y][x], y, x) for y in range(h) for x in range(w)]):
        max_neighbor = max(
            m[y + dy][x + dx]
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]
            if (dx or dy) and 0 <= x + dx < w and 0 <= y + dy < h
        )
        if max_neighbor < m[y][x]:
            m[y][x] = max_neighbor
    for row in m:
        print(*row)
