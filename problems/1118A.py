# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    print((n >> 1) * min(a << 1, b) + (n & 1) * a)
