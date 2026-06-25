# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = sorted([list(map(int, input().split())) for _ in range(n)])
    if any(y1 < y0 for (_, y0), (_, y1) in zip(a, a[1:])):
        print("NO")
    else:
        print("YES")
        x = y = 0
        for nx, ny in a:
            print(end="R" * (nx - x) + "U" * (ny - y))
            x, y = nx, ny
        print()
