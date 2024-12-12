# ruff: noqa: E731, E741
for _ in range(int(input())):
    min_x = max_x = min_y = max_y = 0
    for _ in range(int(input())):
        x, y = map(int, input().split())
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    print((max_x - min_x) + (max_y - min_y) << 1)
