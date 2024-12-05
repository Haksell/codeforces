# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x = c - a
    y = d - b
    print(-1 if y < 0 or y < x else 2 * y - x)
