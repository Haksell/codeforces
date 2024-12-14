# ruff: noqa: E731, E741
n, a, b = map(int, input().split())
print(max(0, min(n - a, b + 1)))
