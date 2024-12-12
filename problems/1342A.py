# ruff: noqa: E731, E741
for _ in range(int(input())):
    x, y = map(abs, map(int, input().split()))
    a, b = map(int, input().split())
    if 2 * a <= b:
        print(a * (x + y))
    else:
        diag = min(x, y)
        remaining = max(x, y) - diag
        print(b * diag + a * remaining)
