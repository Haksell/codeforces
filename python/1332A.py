# ruff: noqa: E731, E741
for _ in range(int(input())):
    l, r, d, u = map(int, input().split())
    x, y, x1, y1, x2, y2 = map(int, input().split())
    print(
        "YES"
        if (x1 != x2 or l == r == 0)
        and (y1 != y2 or d == u == 0)
        and x1 <= x + r - l <= x2
        and y1 <= y + u - d <= y2
        else "NO"
    )
