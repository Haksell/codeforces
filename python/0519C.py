# ruff: noqa: E731, E741
n, m = map(int, input().split())
print(min(n, m, (n + m) // 3))
