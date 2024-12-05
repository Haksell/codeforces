# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(m * min(n - 1, 2))
