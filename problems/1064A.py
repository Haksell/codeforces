# ruff: noqa: E731, E741
a, b, c = sorted(map(int, input().split()))
print(max(0, c - a - b + 1))
