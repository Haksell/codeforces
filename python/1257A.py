# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, x, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    da = min(a - 1, x)
    a -= da
    x -= da
    b += min(n - b, x)
    print(b - a)
