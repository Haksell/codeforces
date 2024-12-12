# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, m = map(int, input().split())
    h = m * (m + 1) >> 1
    v = m * n * (n + 1) >> 1
    print(h + v - m)
