# ruff: noqa: E731, E741
a, b = map(int, input().split())
print(min(a, b), abs(a - b) // 2)
