# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, x, t = map(int, input().split())
    c = min(n, t // x)
    print(c * (2 * n - c - 1) >> 1)
