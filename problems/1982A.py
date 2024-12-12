# ruff: noqa: E731, E741
for _ in range(int(input())):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print("YES" if (x1 > y1) == (x2 > y2) else "NO")
