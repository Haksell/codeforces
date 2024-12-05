# ruff: noqa: E731, E741
a = list(map(int, input().split()))
print(max(a) - min(a))
