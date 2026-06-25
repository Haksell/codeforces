# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c, x, y = map(int, input().split())
    dx = max(0, x - a)
    dy = max(0, y - b)
    print("YES" if c >= dx + dy else "NO")
