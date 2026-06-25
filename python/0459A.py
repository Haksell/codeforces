# ruff: noqa: E731, E741
x1, y1, x2, y2 = map(int, input().split())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 0:
    print(x1 + dy, y1, x2 + dy, y2)
elif dy == 0:
    print(x1, y1 + dx, x2, y2 + dx)
elif dx == dy:
    print(x1, y2, x2, y1)
else:
    print(-1)
